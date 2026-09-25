#!/usr/bin/env python3
"""Testes do contrato Markdown → manifesto/fonte privados → PNG público."""

import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


BASE = Path(__file__).resolve().parents[1]
VALIDADOR = BASE / "Geometria" / "validar-capitulo.py"
ALT = "Triângulo ABC retângulo em A, com os três vértices identificados"
URL_BASE = (
    "https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/"
    "geometria/6ano/triangulos/fig-01-triangulo-retangulo.png"
)


def capitulo(corpo: str) -> str:
    return (
        "# Capítulo 1 — Figuras\n\n"
        "> Como interpretar uma configuração geométrica?\n\n"
        "## 1. Configuração\n\n"
        f"{corpo}\n"
    )


class ValidarImagensGeometriaTest(unittest.TestCase):
    def executar(self, pasta: Path, corpo: str):
        arquivo = pasta / "capitulo.md"
        arquivo.write_text(capitulo(corpo), encoding="utf-8")
        return subprocess.run(
            [
                sys.executable,
                str(VALIDADOR),
                str(arquivo),
                "--disciplina",
                "geometria",
                "--raiz-tikz",
                str(pasta / "_tikz"),
            ],
            capture_output=True,
            text=True,
        )

    def criar_contrato(self, pasta: Path, *, publicado: bool = True):
        raiz = pasta / "_tikz"
        raiz.mkdir()
        (raiz / "config.json").write_text(
            json.dumps(
                {
                    "versao": 1,
                    "repositorio_publico": "felipeelv/imagens-tikz",
                    "branch_publicacao": "main",
                }
            ),
            encoding="utf-8",
        )
        documento = raiz / "geometria" / "6ano" / "triangulos"
        documento.mkdir(parents=True)
        (documento / "figuras.tex").write_text(
            "\\begin{tikzpicture}\n\\draw (0,0) -- (1,0);\n"
            "\\end{tikzpicture}\n",
            encoding="utf-8",
        )
        resumo = "a" * 64
        figura = {
            "id": "fig-01-triangulo-retangulo",
            "pagina": 1,
            "arquivo": "fig-01-triangulo-retangulo.png",
            "alt": ALT,
            "sha256": resumo,
        }
        if publicado:
            figura["publicado_sha256"] = resumo
        (documento / "manifesto.json").write_text(
            json.dumps(
                {
                    "versao": 1,
                    "disciplina": "geometria",
                    "ano_serie": "6ano",
                    "titulo_documento": "Triângulos",
                    "slug_documento": "triangulos",
                    "arquivo_markdown": "capitulo.md",
                    "fonte": "figuras.tex",
                    "figuras": [figura],
                }
            ),
            encoding="utf-8",
        )

    def test_figura_publica_indexada_e_valida(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            self.criar_contrato(pasta)
            resultado = self.executar(pasta, f"![{ALT}]({URL_BASE})")
            self.assertEqual(resultado.returncode, 0, resultado.stdout)
            self.assertIn("1 figura(s) com URL pública", resultado.stdout)

    def test_capitulo_sem_imagem_continua_valido(self):
        with tempfile.TemporaryDirectory() as tmp:
            resultado = self.executar(Path(tmp), "O texto não exige uma figura.")
            self.assertEqual(resultado.returncode, 0, resultado.stdout)
            self.assertIn("nenhuma figura no capítulo", resultado.stdout)

    def test_imagem_fora_do_repositorio_autorizado_falha(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            self.criar_contrato(pasta)
            url = URL_BASE.replace("felipeelv/imagens-tikz", "outro/repositorio")
            resultado = self.executar(pasta, f"![{ALT}]({url})")
            self.assertEqual(resultado.returncode, 1, resultado.stdout)
            self.assertIn("aponta fora de felipeelv/imagens-tikz/main", resultado.stdout)

    def test_texto_alternativo_divergente_falha(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            self.criar_contrato(pasta)
            resultado = self.executar(
                pasta, f"![Descrição diferente da figura]({URL_BASE})"
            )
            self.assertEqual(resultado.returncode, 1, resultado.stdout)
            self.assertIn("diverge do manifesto TikZ", resultado.stdout)

    def test_versao_nao_publicada_falha(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            self.criar_contrato(pasta, publicado=False)
            resultado = self.executar(pasta, f"![{ALT}]({URL_BASE})")
            self.assertEqual(resultado.returncode, 1, resultado.stdout)
            self.assertIn("ainda não foi publicada nesta versão", resultado.stdout)

    def test_marcadores_tikz_nao_entram_na_contagem(self):
        with tempfile.TemporaryDirectory() as tmp:
            pasta = Path(tmp)
            self.criar_contrato(pasta)
            imagem = f"![{ALT}]({URL_BASE})"
            sem_marcadores = self.executar(pasta, imagem)
            com_marcadores = self.executar(
                pasta,
                "<!-- tikz:inicio fig-01-triangulo-retangulo -->\n"
                f"{imagem}\n"
                "<!-- tikz:fim fig-01-triangulo-retangulo -->",
            )
            padrao = r"Aula 1 — Configuração: (\d+) palavras"
            contagem_sem = re.search(padrao, sem_marcadores.stdout)
            contagem_com = re.search(padrao, com_marcadores.stdout)
            self.assertIsNotNone(contagem_sem, sem_marcadores.stdout)
            self.assertIsNotNone(contagem_com, com_marcadores.stdout)
            self.assertEqual(contagem_sem.group(1), contagem_com.group(1))

    def test_referencia_vaga_falha(self):
        with tempfile.TemporaryDirectory() as tmp:
            resultado = self.executar(Path(tmp), "Veja a figura ao lado para comparar.")
            self.assertEqual(resultado.returncode, 1, resultado.stdout)
            self.assertIn("referência vaga a figura/imagem", resultado.stdout)


if __name__ == "__main__":
    unittest.main()
