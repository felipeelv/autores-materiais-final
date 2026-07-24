#!/usr/bin/env python3
"""Atalho local para o validador compartilhado da área de Humanas."""

from pathlib import Path
import runpy

VALIDADOR = Path(__file__).resolve().parent.parent / "Estudos Sociais" / "validar-capitulo.py"
runpy.run_path(str(VALIDADOR), run_name="__main__")
