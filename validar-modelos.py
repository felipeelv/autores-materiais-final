#!/usr/bin/env python3
"""Valida todos os capítulos-modelo existentes nas pastas dos autores."""

from pathlib import Path
import subprocess
import sys


BASE = Path(__file__).resolve().parent
REORGANIZACAO = BASE.parent / "Reorganizacao-2026-2Semestre"
DISCIPLINAS = {
    "Biologia": "biologia",
    "Ciencias": "ciencias",
    "Estudos Sociais": "estudos-sociais",
    "Fisica": "fisica",
    "Financeira": "financeira",
}


def main():
    modelos = []
    for pasta, slug in DISCIPLINAS.items():
        for arquivo in sorted((BASE / pasta / "modelos").glob("*-modelo.md")):
            modelos.append((pasta, slug, arquivo))

    if not modelos:
        print("Nenhum capítulo-modelo encontrado.")
        return 1

    falhas = []
    for pasta, slug, arquivo in modelos:
        print(f"\n{'═' * 72}\nMODELO: {arquivo.relative_to(BASE)}", flush=True)
        comando = [
            sys.executable,
            str(BASE / pasta / "validar-capitulo.py"),
            str(arquivo),
            "--disciplina",
            slug,
        ]
        if pasta == "Biologia":
            serie = arquivo.stem.removeprefix("biologia-").removesuffix("-modelo")
            blueprint = (
                REORGANIZACAO
                / "disciplinas"
                / "Biologia"
                / "blueprints"
                / serie
                / "3bim-bloco1.md"
            )
            if blueprint.exists():
                comando.extend(["--blueprint", str(blueprint)])
        resultado = subprocess.run(comando)
        if resultado.returncode:
            falhas.append(str(arquivo.relative_to(BASE)))

    print(f"\n{'═' * 72}")
    if falhas:
        print("Modelos com falha:")
        for arquivo in falhas:
            print(f"  · {arquivo}")
        return 1

    print(f"✓ {len(modelos)} modelo(s) validado(s) com sucesso")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
