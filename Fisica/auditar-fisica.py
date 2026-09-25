#!/usr/bin/env python3
"""Auditoria semântica assistida para capítulos de Física.

O validador mecânico reprova o que é objetivamente demonstrável. Este auditor
reduz a leitura humana nos quatro pontos que exigem contexto:

1. dependência conceitual e sequenciamento;
2. novidade real de boxes;
3. repetição semântica entre tabela e prosa;
4. história essencial versus biografia acessória.

Um contrato JSON torna explícitas as dependências e as exceções do blueprint.
Achados de confiança alta reprovam; média e baixa são enviados para decisão do
autor/agente. O relatório pode ser impresso ou salvo como JSON.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import asdict, dataclass
from difflib import SequenceMatcher
from pathlib import Path


STOPWORDS = {
    "a", "ao", "aos", "as", "com", "como", "da", "das", "de", "do", "dos",
    "e", "em", "essa", "esse", "esta", "este", "isso", "na", "nas", "no",
    "nos", "o", "os", "ou", "para", "pela", "pelas", "pelo", "pelos", "por",
    "que", "se", "sem", "ser", "sua", "suas", "um", "uma",
}
BOX_TITULO = re.compile(
    r"^\s*>\s*(?P<emoji>[\U0001F300-\U0001FAFF\u2600-\u26FF])️?\s*\*\*(?P<titulo>[^*]+)\*\*"
)
SECAO = re.compile(r"^###\s+(\d+\.\d+)\b|^##\s+(\d+)\.")
TABELA = re.compile(r"^\s*\|.*\|\s*$")
SEPARADOR_TABELA = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
FORMULA = re.compile(r"\$\$(.+?)\$\$", flags=re.S)
ANO = re.compile(r"\b(?:1[5-9]\d{2}|20\d{2})\b")


@dataclass
class Achado:
    arquivo: str
    linha: int
    regra: str
    confianca: float
    nivel: str
    evidencia: str
    correcao_sugerida: str


def nivel_confianca(valor: float) -> str:
    if valor >= 0.90:
        return "alta"
    if valor >= 0.65:
        return "media"
    return "baixa"


def criar_achado(
    arquivo: Path,
    linha: int,
    regra: str,
    confianca: float,
    evidencia: str,
    correcao: str,
) -> Achado:
    return Achado(
        arquivo=str(arquivo),
        linha=linha,
        regra=regra,
        confianca=round(confianca, 2),
        nivel=nivel_confianca(confianca),
        evidencia=evidencia.strip()[:280],
        correcao_sugerida=correcao,
    )


def normalizar(texto: str) -> str:
    texto = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", texto)
    texto = re.sub(r"<!--.*?-->", " ", texto, flags=re.S)
    texto = re.sub(r"\\[A-Za-z]+", " ", texto)
    texto = re.sub(r"[$#>*_`|{}\[\]()=+\-–—/:;,.!?]", " ", texto)
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c)).lower()
    palavras = re.findall(r"[a-z0-9]+", texto)
    return " ".join(p for p in palavras if p not in STOPWORDS and len(p) > 1)


def tokens(texto: str) -> set[str]:
    return set(normalizar(texto).split())


def secao_em_linhas(linhas: list[str]) -> tuple[list[str], list[int]]:
    atual = "0"
    secoes: list[str] = []
    inicios: list[int] = []
    inicio = 0
    for i, linha in enumerate(linhas):
        m = SECAO.match(linha)
        if m:
            atual = m.group(1) or m.group(2)
            inicio = i
        secoes.append(atual)
        inicios.append(inicio)
    return secoes, inicios


def ordem_secao(secao: str) -> tuple[int, ...]:
    try:
        return tuple(int(p) for p in secao.split("."))
    except ValueError:
        return (0,)


def intervalos_boxes(linhas: list[str]) -> list[dict]:
    boxes = []
    i = 0
    while i < len(linhas):
        m = BOX_TITULO.match(linhas[i])
        if not m:
            i += 1
            continue
        fim = i + 1
        while fim < len(linhas) and (
            linhas[fim].lstrip().startswith(">") or not linhas[fim].strip()
        ):
            fim += 1
        conteudo = "\n".join(
            re.sub(r"^\s*>\s?", "", linha)
            for linha in linhas[i + 1:fim]
            if linha.lstrip().startswith(">")
        ).strip()
        boxes.append(
            {
                "inicio": i,
                "fim": fim,
                "emoji": m.group("emoji"),
                "titulo": m.group("titulo").strip(),
                "conteudo": conteudo,
            }
        )
        i = fim
    return boxes


def dentro_de_box(indice: int, boxes: list[dict], emoji: str | None = None) -> bool:
    return any(
        box["inicio"] <= indice < box["fim"]
        and (emoji is None or box["emoji"] == emoji)
        for box in boxes
    )


def auditar_sequenciamento(
    arquivo: Path,
    linhas: list[str],
    secoes: list[str],
    contrato: dict,
) -> list[Achado]:
    achados: list[Achado] = []
    conceitos = {c["id"]: c for c in contrato.get("conceitos", [])}
    for conceito in conceitos.values():
        introduzido = conceito.get("introduzido_em", "0")
        dependencias = conceito.get("depende_de", [])
        secao_minima = ordem_secao(introduzido)
        for padrao in conceito.get("padroes", []):
            regex = re.compile(padrao, flags=re.I)
            for i, linha in enumerate(linhas):
                if not regex.search(linha):
                    continue
                atual = ordem_secao(secoes[i])
                if atual < secao_minima:
                    achados.append(
                        criar_achado(
                            arquivo,
                            i + 1,
                            "resultado_antes_da_ferramenta",
                            0.98,
                            linha,
                            f"Mover para a seção {introduzido} ou introduzir antes os pré-requisitos.",
                        )
                    )
                    continue
                faltantes = [
                    dep for dep in dependencias
                    if dep in conceitos
                    and atual < ordem_secao(conceitos[dep].get("introduzido_em", "0"))
                ]
                if faltantes:
                    achados.append(
                        criar_achado(
                            arquivo,
                            i + 1,
                            "dependencia_conceitual_ausente",
                            0.96,
                            linha,
                            "Introduzir antes: " + ", ".join(faltantes) + ".",
                        )
                    )
    return achados


def auditar_boxes(
    arquivo: Path,
    linhas: list[str],
    secoes: list[str],
    inicios_secao: list[int],
    boxes: list[dict],
) -> list[Achado]:
    achados: list[Achado] = []
    for box in boxes:
        if box["emoji"] == "👤":
            ultima_aula = max((ordem_secao(s)[0] for s in secoes), default=0)
            aula_box = ordem_secao(secoes[box["inicio"]])[0]
            if aula_box != ultima_aula:
                achados.append(
                    criar_achado(
                        arquivo,
                        box["inicio"] + 1,
                        "historia_box_fora_da_ultima_aula",
                        0.99,
                        linhas[box["inicio"]],
                        "Mover o box 👤 para a última aula.",
                    )
                )
            continue

        conteudo = box["conteudo"]
        box_tokens = tokens(conteudo)
        if len(box_tokens) < 4:
            continue
        inicio = inicios_secao[box["inicio"]]
        contexto = "\n".join(
            linha for i, linha in enumerate(linhas[inicio:box["inicio"]], inicio)
            if not dentro_de_box(i, boxes)
        )
        contexto_tokens = tokens(contexto)
        cobertura = len(box_tokens & contexto_tokens) / len(box_tokens)
        sequencia = SequenceMatcher(None, normalizar(conteudo), normalizar(contexto)).ratio()

        confianca = 0.0
        if cobertura >= 0.88 and sequencia >= 0.35:
            confianca = 0.94
        elif cobertura >= 0.72 and sequencia >= 0.25:
            confianca = 0.76
        if confianca:
            achados.append(
                criar_achado(
                    arquivo,
                    box["inicio"] + 1,
                    "box_repetitivo",
                    confianca,
                    conteudo,
                    "Substituir por aplicação concreta, consequência, erro comum, "
                    "pergunta ainda não respondida ou dado realmente novo.",
                )
            )
    return achados


def blocos_tabela(linhas: list[str]) -> list[tuple[int, int]]:
    blocos = []
    i = 0
    while i < len(linhas):
        if not TABELA.match(linhas[i]):
            i += 1
            continue
        inicio = i
        while i < len(linhas) and TABELA.match(linhas[i]):
            i += 1
        if i - inicio >= 2 and any(SEPARADOR_TABELA.match(l) for l in linhas[inicio:i]):
            blocos.append((inicio, i))
    return blocos


def proximo_paragrafo(linhas: list[str], inicio: int) -> tuple[int, str] | None:
    i = inicio
    while i < len(linhas) and not linhas[i].strip():
        i += 1
    if i >= len(linhas):
        return None
    if linhas[i].lstrip().startswith(("#", "|", ">", "$$", "![", "<!--", "---")):
        return None
    paragrafo = []
    linha_inicial = i
    while i < len(linhas) and linhas[i].strip():
        if linhas[i].lstrip().startswith(("#", "|", ">", "$$", "![", "<!--", "---")):
            break
        paragrafo.append(linhas[i])
        i += 1
    return (linha_inicial, " ".join(paragrafo)) if paragrafo else None


def auditar_tabelas(arquivo: Path, linhas: list[str]) -> list[Achado]:
    achados: list[Achado] = []
    for inicio, fim in blocos_tabela(linhas):
        seguinte = proximo_paragrafo(linhas, fim)
        if not seguinte:
            continue
        linha_p, prosa = seguinte
        prosa_tokens = tokens(prosa)
        if len(prosa_tokens) < 5:
            continue
        tabela = "\n".join(l for l in linhas[inicio:fim] if not SEPARADOR_TABELA.match(l))
        tabela_tokens = tokens(tabela)
        cobertura = len(prosa_tokens & tabela_tokens) / len(prosa_tokens)
        if cobertura >= 0.90:
            confianca = 0.94
        elif cobertura >= 0.70:
            confianca = 0.76
        else:
            continue
        achados.append(
            criar_achado(
                arquivo,
                linha_p + 1,
                "prosa_repete_tabela",
                confianca,
                prosa,
                "Cortar a repetição ou reescrever a prosa como interpretação, causa, "
                "consequência, exceção, limite ou erro comum.",
            )
        )
    return achados


def auditar_historia(
    arquivo: Path,
    linhas: list[str],
    secoes: list[str],
    boxes: list[dict],
    contrato: dict,
) -> list[Achado]:
    achados: list[Achado] = []
    linhas_classificadas: set[int] = set()
    historia = contrato.get("historia", {})

    for pessoa in historia.get("pessoas", []):
        nomes = [re.compile(p, flags=re.I) for p in pessoa.get("padroes_nome", [])]
        acessorios = [
            re.compile(p, flags=re.I) for p in pessoa.get("padroes_acessorios", [])
        ]
        permitidas = set(pessoa.get("secoes_inline_essenciais", []))
        for i, linha in enumerate(linhas):
            if not any(p.search(linha) for p in nomes):
                continue
            linhas_classificadas.add(i)
            if dentro_de_box(i, boxes, "👤"):
                continue
            if any(p.search(linha) for p in acessorios):
                achados.append(
                    criar_achado(
                        arquivo,
                        i + 1,
                        "biografia_acessoria_no_fluxo",
                        0.96,
                        linha,
                        "Mover a informação útil para o único box 👤 final ou cortá-la.",
                    )
                )
            elif permitidas and secoes[i] not in permitidas:
                achados.append(
                    criar_achado(
                        arquivo,
                        i + 1,
                        "historia_fora_do_conceito_pertinente",
                        0.78,
                        linha,
                        "Levar a contribuição para a seção conceitual indicada no contrato.",
                    )
                )

    for i, linha in enumerate(linhas):
        if i in linhas_classificadas or dentro_de_box(i, boxes, "👤"):
            continue
        if ANO.search(linha) and re.search(r"\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+", linha):
            achados.append(
                criar_achado(
                    arquivo,
                    i + 1,
                    "historia_nao_classificada",
                    0.55,
                    linha,
                    "Classificar no contrato como contribuição essencial ou biografia acessória.",
                )
            )
    return achados


def auditar(arquivo: Path, contrato: dict) -> list[Achado]:
    texto = arquivo.read_text(encoding="utf-8")
    linhas = texto.splitlines()
    secoes, inicios_secao = secao_em_linhas(linhas)
    boxes = intervalos_boxes(linhas)
    achados = []
    achados.extend(auditar_sequenciamento(arquivo, linhas, secoes, contrato))
    achados.extend(auditar_boxes(arquivo, linhas, secoes, inicios_secao, boxes))
    achados.extend(auditar_tabelas(arquivo, linhas))
    achados.extend(auditar_historia(arquivo, linhas, secoes, boxes, contrato))
    unicos = {}
    for achado in achados:
        chave = (achado.linha, achado.regra, achado.evidencia)
        unicos[chave] = achado
    return sorted(unicos.values(), key=lambda a: (a.linha, a.regra))


def carregar_contrato(caminho: Path | None) -> dict:
    if caminho is None:
        return {}
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    if not isinstance(dados, dict):
        raise ValueError("o contrato precisa ser um objeto JSON")
    return dados


def imprimir_relatorio(achados: list[Achado], arquivo: Path) -> None:
    print(f"\n═══ AUDITORIA SEMÂNTICA · {arquivo} ═══\n")
    if not achados:
        print("  ✓ Nenhum achado pelos critérios contratados.\n")
        return
    for achado in achados:
        simbolo = "✗" if achado.nivel == "alta" else "⚠️"
        print(
            f"  {simbolo} linha {achado.linha} · {achado.regra} · "
            f"{achado.nivel} ({achado.confianca:.2f})"
        )
        print(f"    Evidência: {achado.evidencia}")
        print(f"    Sugestão: {achado.correcao_sugerida}")
    totais = {
        nivel: sum(a.nivel == nivel for a in achados)
        for nivel in ("alta", "media", "baixa")
    }
    print(
        "\n  Resumo: "
        f"{totais['alta']} alta · {totais['media']} média · {totais['baixa']} baixa\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("capitulo", type=Path)
    ap.add_argument("--contrato", type=Path)
    ap.add_argument("--json", action="store_true", help="imprime somente JSON")
    ap.add_argument("--saida", type=Path, help="salva o relatório JSON neste caminho")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="também reprova achados de confiança média",
    )
    args = ap.parse_args()

    try:
        contrato = carregar_contrato(args.contrato)
        achados = auditar(args.capitulo, contrato)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, re.error) as exc:
        print(f"erro: {exc}", file=sys.stderr)
        return 2

    dados = {
        "arquivo": str(args.capitulo),
        "contrato": str(args.contrato) if args.contrato else None,
        "achados": [asdict(a) for a in achados],
        "resumo": {
            nivel: sum(a.nivel == nivel for a in achados)
            for nivel in ("alta", "media", "baixa")
        },
    }
    if args.saida:
        args.saida.parent.mkdir(parents=True, exist_ok=True)
        args.saida.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if args.json:
        print(json.dumps(dados, ensure_ascii=False, indent=2))
    else:
        imprimir_relatorio(achados, args.capitulo)

    limite = 0.65 if args.strict else 0.90
    return 1 if any(a.confianca >= limite for a in achados) else 0


if __name__ == "__main__":
    raise SystemExit(main())
