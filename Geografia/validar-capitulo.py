#!/usr/bin/env python3
"""Executa o validador comum com a configuração própria de Geografia."""

from pathlib import Path
import runpy


VALIDADOR = Path(__file__).resolve().parents[1] / "Estudos Sociais" / "validar-capitulo.py"


if __name__ == "__main__":
    runpy.run_path(str(VALIDADOR), run_name="__main__")
