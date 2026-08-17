#!/usr/bin/env python3
"""Validação local do piloto genérico de figuras em Asymptote."""

from __future__ import annotations

import hashlib
import json
import re
import struct
import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree


PASTA = Path(__file__).resolve().parent
RAIZ_REPOSITORIO = PASTA.parents[3]
MANIFESTO = PASTA / "manifesto.json"
ASSINATURA_PNG = b"\x89PNG\r\n\x1a\n"


def png_info(caminho: Path) -> tuple[int, int, int]:
    with caminho.open("rb") as arquivo:
        if arquivo.read(8) != ASSINATURA_PNG:
            raise ValueError("assinatura PNG inválida")
        tamanho = struct.unpack(">I", arquivo.read(4))[0]
        if arquivo.read(4) != b"IHDR" or tamanho != 13:
            raise ValueError("bloco IHDR ausente")
        largura, altura, _, tipo_cor, _, _, _ = struct.unpack(
            ">IIBBBBB", arquivo.read(13)
        )
    return largura, altura, tipo_cor


def largura_sips(caminho: Path) -> int:
    resultado = subprocess.run(
        ["sips", "-g", "pixelWidth", str(caminho)],
        check=True,
        capture_output=True,
        text=True,
    )
    correspondencia = re.search(r"pixelWidth:\s*(\d+)", resultado.stdout)
    if not correspondencia:
        raise ValueError("largura não identificada pelo sips")
    return int(correspondencia.group(1))


def main() -> int:
    erros: list[str] = []
    manifesto = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    markdown = RAIZ_REPOSITORIO / manifesto["arquivo_markdown"]
    texto = markdown.read_text(encoding="utf-8")
    figuras_markdown = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", texto)
    figuras = manifesto.get("figuras", [])

    if manifesto.get("politica", {}).get("renderizador") != "asymptote":
        erros.append("o orquestrador não selecionou Asymptote")
    tipografia = manifesto.get("politica", {}).get("tipografia", {})
    if tipografia.get("rotulos") != "Roboto Regular":
        erros.append("a tipografia dos rótulos não está definida como Roboto Regular")
    for campo in ("arquivo_rotulos", "licenca_rotulos"):
        caminho_tipografico = PASTA / tipografia.get(campo, "")
        if not caminho_tipografico.is_file() or caminho_tipografico.stat().st_size == 0:
            erros.append(f"arquivo tipográfico ausente: {campo}")
    if len(figuras) != 8:
        erros.append(f"manifesto possui {len(figuras)} figuras; esperado: 8")
    if len(figuras_markdown) != len(figuras):
        erros.append(
            f"Markdown possui {len(figuras_markdown)} imagens; manifesto possui {len(figuras)}"
        )

    ids = [figura.get("id") for figura in figuras]
    if len(ids) != len(set(ids)):
        erros.append("há IDs de figura repetidos")

    mapa_markdown = {alt: destino for alt, destino in figuras_markdown}
    hashes: list[str] = []

    for figura in figuras:
        figura_id = figura["id"]
        fonte = PASTA / figura["fonte"]
        inicio = f"<!-- figura:inicio {figura_id} -->"
        fim = f"<!-- figura:fim {figura_id} -->"

        if texto.count(inicio) != 1 or texto.count(fim) != 1:
            erros.append(f"{figura_id}: marcadores ausentes ou repetidos no Markdown")

        campos_autor = [
            figura.get("finalidade_pedagogica", ""),
            figura.get("descricao", ""),
            *figura.get("dados", []),
            *figura.get("relacoes", []),
            *figura.get("incognitas", []),
            figura.get("alt", ""),
            figura.get("insercao_markdown", ""),
        ]
        if re.search(r"\b(?:asymptote|tikz|svg|png|pdf)\b", " ".join(campos_autor), re.I):
            erros.append(f"{figura_id}: especificação do Autor escolhe tecnologia")

        if not fonte.is_file() or fonte.suffix != ".asy":
            erros.append(f"{figura_id}: fonte Asymptote ausente")

        destino_markdown = mapa_markdown.get(figura["alt"])
        if destino_markdown is None:
            erros.append(f"{figura_id}: texto alternativo diverge do Markdown")
        else:
            destino_resolvido = (markdown.parent / destino_markdown).resolve()
            svg_esperado = (PASTA / figura["saidas"]["svg"]).resolve()
            if destino_resolvido != svg_esperado:
                erros.append(f"{figura_id}: Markdown não aponta para o SVG do manifesto")

        for formato in ("svg", "pdf", "png"):
            saida = PASTA / figura["saidas"][formato]
            if not saida.is_file() or saida.stat().st_size == 0:
                erros.append(f"{figura_id}: saída {formato.upper()} ausente")

        svg = PASTA / figura["saidas"]["svg"]
        png = PASTA / figura["saidas"]["png"]
        pdf = PASTA / figura["saidas"]["pdf"]
        preview = PASTA / figura["saidas"]["preview_300"]

        try:
            if not ElementTree.parse(svg).getroot().tag.endswith("svg"):
                raise ValueError("elemento raiz não é SVG")
        except Exception as exc:  # noqa: BLE001
            erros.append(f"{figura_id}: SVG inválido ({exc})")

        try:
            largura, altura, tipo_cor = png_info(png)
            if largura < 1000 or altura < 300:
                erros.append(f"{figura_id}: PNG mestre pequeno ({largura}x{altura})")
            if tipo_cor not in (4, 6):
                erros.append(f"{figura_id}: PNG sem canal alfa (tipo de cor {tipo_cor})")
        except Exception as exc:  # noqa: BLE001
            erros.append(f"{figura_id}: PNG inválido ({exc})")

        try:
            if pdf.read_bytes()[:4] != b"%PDF":
                raise ValueError("assinatura PDF inválida")
        except Exception as exc:  # noqa: BLE001
            erros.append(f"{figura_id}: PDF inválido ({exc})")

        try:
            if largura_sips(preview) != 300:
                erros.append(f"{figura_id}: prévia não possui 300 px de largura")
        except Exception as exc:  # noqa: BLE001
            erros.append(f"{figura_id}: prévia inválida ({exc})")

        if png.is_file():
            resumo_completo = hashlib.sha256(png.read_bytes()).hexdigest()
            if figura.get("sha256_png") != resumo_completo:
                erros.append(f"{figura_id}: hash PNG diverge do manifesto")
            hashes.append(f"{figura_id}: {resumo_completo[:12]}")

    if erros:
        print("PILOTO INVÁLIDO")
        for erro in erros:
            print(f"- {erro}")
        return 1

    print("PILOTO VÁLIDO")
    print(f"- {len(figuras)} especificações independentes da tecnologia")
    print("- SVG, PDF e PNG presentes para todas as figuras")
    print("- PNGs mestres transparentes e prévias com 300 px")
    print("- marcadores, textos alternativos e caminhos sincronizados")
    print("- hashes PNG:")
    for resumo in hashes:
        print(f"  - {resumo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
