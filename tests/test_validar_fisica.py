import importlib.util
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
CAMINHO = RAIZ / "Fisica" / "validar-capitulo.py"
SPEC = importlib.util.spec_from_file_location("validar_fisica", CAMINHO)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def test_inventario_de_unidades_e_definicao_unica():
    inventario = (
        "Nessas expressões, $$v$$ é medida em metro por segundo (m/s) "
        "e $$R$$ em metro (m)."
    )
    definicao = "Aqui, $$\\omega$$ é a velocidade angular, em rad/s."
    assert MOD.parece_inventario_unidades(inventario)
    assert not MOD.parece_inventario_unidades(definicao)


def test_numeros_latex_nao_se_fragmentam():
    valores = MOD.numeros_fisicos(r"P_x=100\cdot0{,}50")
    assert valores == {"100", "0.5"}


def test_formula_de_calculo_precisa_ocupar_linha_propria():
    texto = (
        "📝 **Exemplo:**\n"
        "Dados: $$m=10\\,\\mathrm{kg}$$\n\n"
        "$$P=mg=100\\,\\mathrm{N}$$\n"
    )
    exemplos = MOD.separar_exemplos(texto)
    assert len(exemplos) == 1
    formulas = list(MOD.FORMULA_LINHA.finditer(exemplos[0][1]))
    assert len(formulas) == 1
    assert formulas[0].group(1).count("=") == 2
