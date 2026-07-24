#!/usr/bin/env python3
"""Teste integrado local do criador TikZ, sem acesso ao GitHub."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


BASE = Path(__file__).resolve().parents[1]
CRIADOR = BASE / "_tikz" / "ferramentas" / "criar.py"
ESTILO = BASE / "_tikz" / "estilos" / "eleve-geometria.sty"
ESTILO_FISICA = BASE / "_tikz" / "estilos" / "eleve-fisica.sty"
ESTILO_MATEMATICA_EF1 = (
    BASE / "_tikz" / "estilos" / "eleve-matematica-ef1.sty"
)
ESTILO_QUIMICA = BASE / "_tikz" / "estilos" / "eleve-quimica.sty"
PNG_ASSINATURA = b"\x89PNG\r\n\x1a\n"


@unittest.skipUnless(
    shutil.which("pdflatex") and shutil.which("pdftocairo"),
    "pdflatex e pdftocairo são necessários para o teste integrado",
)
class PipelineTikzTest(unittest.TestCase):
    def executar(self, raiz: Path, *args: str):
        return subprocess.run(
            [sys.executable, str(CRIADOR), "--raiz", str(raiz), *args],
            capture_output=True,
            text=True,
        )

    def preparar_raiz(self, raiz: Path):
        (raiz / "_tikz" / "estilos").mkdir(parents=True)
        shutil.copyfile(ESTILO, raiz / "_tikz" / "estilos" / ESTILO.name)
        shutil.copyfile(
            ESTILO_FISICA,
            raiz / "_tikz" / "estilos" / ESTILO_FISICA.name,
        )
        shutil.copyfile(
            ESTILO_MATEMATICA_EF1,
            raiz / "_tikz" / "estilos" / ESTILO_MATEMATICA_EF1.name,
        )
        shutil.copyfile(
            ESTILO_QUIMICA,
            raiz / "_tikz" / "estilos" / ESTILO_QUIMICA.name,
        )
        (raiz / "_tikz" / "config.json").write_text(
            json.dumps(
                {
                    "versao": 1,
                    "repositorio_publico": "felipeelv/imagens-tikz",
                    "branch_publicacao": "main",
                    "dpi": 300,
                    "disciplinas_ativas": [
                        "geometria",
                        "fisica",
                        "matematica-ef1",
                        "quimica",
                    ],
                }
            ),
            encoding="utf-8",
        )
        (raiz / "Geometria").mkdir()
        (raiz / "Geometria" / "capitulo.md").write_text(
            "# Capítulo 1 — Triângulos\n\n"
            "> Como os elementos do triângulo se relacionam?\n\n"
            "## 1. Elementos\n\n"
            "<!-- tikz:fig-01-elementos-do-triangulo -->\n",
            encoding="utf-8",
        )

    def test_fluxo_local_completo(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            self.preparar_raiz(raiz)
            novo = self.executar(
                raiz,
                "novo",
                "--ano-serie",
                "6ano",
                "--titulo",
                "Triângulos",
                "--markdown",
                "Geometria/capitulo.md",
                "--id",
                "fig-01-elementos-do-triangulo",
                "--alt",
                "Triângulo ABC com seus três vértices e lados identificados",
            )
            self.assertEqual(novo.returncode, 0, novo.stderr)
            manifesto = (
                raiz
                / "_tikz"
                / "geometria"
                / "6ano"
                / "triangulos"
                / "manifesto.json"
            )

            renderizar = self.executar(raiz, "renderizar", str(manifesto))
            self.assertEqual(renderizar.returncode, 0, renderizar.stderr)
            dados = json.loads(manifesto.read_text(encoding="utf-8"))
            figura = dados["figuras"][0]
            png = manifesto.parent / "build" / figura["arquivo"]
            self.assertTrue(png.is_file())
            self.assertEqual(png.read_bytes()[:8], PNG_ASSINATURA)
            self.assertIn(png.read_bytes()[25], {4, 6})
            self.assertEqual(len(figura["sha256"]), 64)
            self.assertFalse(figura["aprovada"])

            aprovar = self.executar(raiz, "aprovar", str(manifesto), "--todas")
            self.assertEqual(aprovar.returncode, 0, aprovar.stderr)
            validar = self.executar(raiz, "validar", str(manifesto), "--aprovada")
            self.assertEqual(validar.returncode, 0, validar.stderr)

            bloqueado = self.executar(raiz, "indexar", str(manifesto))
            self.assertEqual(bloqueado.returncode, 1)
            self.assertIn("ainda não foi publicada", bloqueado.stderr)

            indexar = self.executar(raiz, "indexar", str(manifesto), "--rascunho")
            self.assertEqual(indexar.returncode, 0, indexar.stderr)
            markdown = (raiz / "Geometria" / "capitulo.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("raw.githubusercontent.com/felipeelv/imagens-tikz", markdown)
            self.assertIn("<!-- tikz:inicio fig-01-elementos-do-triangulo -->", markdown)

            simulacao = self.executar(raiz, "publicar", str(manifesto))
            self.assertEqual(simulacao.returncode, 0, simulacao.stderr)
            self.assertIn("Simulação concluída", simulacao.stdout)

    def test_markdown_em_raiz_privada_configurada(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            raiz = base / "autores"
            raiz.mkdir()
            self.preparar_raiz(raiz)
            privada = base / "conteudos-prontos"
            privada.mkdir()
            capitulo = privada / "capitulo.md"
            capitulo.write_text(
                "# Capítulo 1 — Triângulos\n\n"
                "> Como os elementos do triângulo se relacionam?\n\n"
                "## 1. Elementos\n\n"
                "<!-- tikz:fig-01-elementos-do-triangulo -->\n",
                encoding="utf-8",
            )
            config = raiz / "_tikz" / "config.json"
            dados = json.loads(config.read_text(encoding="utf-8"))
            dados["raizes_markdown_permitidas"] = [".", "../conteudos-prontos"]
            config.write_text(json.dumps(dados), encoding="utf-8")

            novo = self.executar(
                raiz,
                "novo",
                "--ano-serie",
                "6ano",
                "--titulo",
                "Triângulos externos",
                "--markdown",
                "../conteudos-prontos/capitulo.md",
                "--id",
                "fig-01-elementos-do-triangulo",
                "--alt",
                "Triângulo ABC com seus três vértices e lados identificados",
            )
            self.assertEqual(novo.returncode, 0, novo.stderr)

    def test_novo_documento_usa_estilo_da_disciplina(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            self.preparar_raiz(raiz)
            (raiz / "Fisica").mkdir()
            (raiz / "Fisica" / "capitulo.md").write_text(
                "# Capítulo 1 — Dinâmica\n\n"
                "<!-- tikz:fig-01-diagrama-de-corpo-livre -->\n",
                encoding="utf-8",
            )

            novo = self.executar(
                raiz,
                "novo",
                "--disciplina",
                "fisica",
                "--ano-serie",
                "1serie",
                "--titulo",
                "Dinâmica",
                "--markdown",
                "Fisica/capitulo.md",
                "--id",
                "fig-01-diagrama-de-corpo-livre",
                "--alt",
                "Bloco apoiado com as forças peso e normal em sentidos opostos",
            )
            self.assertEqual(novo.returncode, 0, novo.stderr)
            fonte = (
                raiz
                / "_tikz"
                / "fisica"
                / "1serie"
                / "dinamica"
                / "figuras.tex"
            ).read_text(encoding="utf-8")
            self.assertIn(r"\usepackage{eleve-fisica}", fonte)
            self.assertIn(r"\begin{tikzpicture}[fisica figura", fonte)

    def test_novo_documento_de_matematica_ef1_usa_estilo_proprio(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            self.preparar_raiz(raiz)
            (raiz / "Matematica EF1").mkdir()
            (raiz / "Matematica EF1" / "capitulo.md").write_text(
                "# Capítulo 1 — Frações\n\n"
                "<!-- tikz:fig-01-fracoes-equivalentes -->\n",
                encoding="utf-8",
            )

            novo = self.executar(
                raiz,
                "novo",
                "--disciplina",
                "matematica-ef1",
                "--ano-serie",
                "4ano",
                "--titulo",
                "Frações",
                "--markdown",
                "Matematica EF1/capitulo.md",
                "--id",
                "fig-01-fracoes-equivalentes",
                "--alt",
                "Uma metade e dois quartos ocupam a mesma parte do inteiro",
            )
            self.assertEqual(novo.returncode, 0, novo.stderr)
            fonte = (
                raiz
                / "_tikz"
                / "matematica-ef1"
                / "4ano"
                / "fracoes"
                / "figuras.tex"
            ).read_text(encoding="utf-8")
            self.assertIn(r"\usepackage{eleve-matematica-ef1}", fonte)
            self.assertIn(r"\begin{tikzpicture}[matematica figura", fonte)

    def test_novo_documento_de_quimica_usa_estilo_proprio(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            self.preparar_raiz(raiz)
            (raiz / "Quimica").mkdir()
            (raiz / "Quimica" / "capitulo.md").write_text(
                "# Capítulo 1 — Equilíbrio químico\n\n"
                "<!-- tikz:fig-01-equilibrio-dinamico -->\n",
                encoding="utf-8",
            )

            novo = self.executar(
                raiz,
                "novo",
                "--disciplina",
                "quimica",
                "--ano-serie",
                "2serie",
                "--titulo",
                "Equilíbrio químico",
                "--markdown",
                "Quimica/capitulo.md",
                "--id",
                "fig-01-equilibrio-dinamico",
                "--alt",
                "Velocidades direta e inversa convergem para o mesmo valor",
            )
            self.assertEqual(novo.returncode, 0, novo.stderr)
            fonte = (
                raiz
                / "_tikz"
                / "quimica"
                / "2serie"
                / "equilibrio-quimico"
                / "figuras.tex"
            ).read_text(encoding="utf-8")
            self.assertIn(r"\usepackage{eleve-quimica}", fonte)
            self.assertIn(r"\begin{tikzpicture}[quimica figura", fonte)


if __name__ == "__main__":
    unittest.main()
