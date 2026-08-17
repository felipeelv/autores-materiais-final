import importlib.util
import json
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
CAMINHO = RAIZ / "Fisica" / "auditar-fisica.py"
SPEC = importlib.util.spec_from_file_location("auditar_fisica", CAMINHO)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def gravar(tmp_path, texto):
    arquivo = tmp_path / "capitulo.md"
    arquivo.write_text(texto, encoding="utf-8")
    return arquivo


def test_detecta_resultado_antes_da_ferramenta(tmp_path):
    arquivo = gravar(
        tmp_path,
        """# Capítulo 1 — Teste

> Pergunta?

## 1. Primeiro

### 1.1 Uso antecipado

$$x=2$$

## 2. Segundo

### 2.1 Ferramenta
""",
    )
    contrato = {
        "conceitos": [
            {
                "id": "x",
                "introduzido_em": "2.1",
                "depende_de": [],
                "padroes": [r"x\s*="],
            }
        ]
    }
    achados = MOD.auditar(arquivo, contrato)
    assert any(a.regra == "resultado_antes_da_ferramenta" for a in achados)


def test_detecta_box_e_prosa_que_repetem(tmp_path):
    arquivo = gravar(
        tmp_path,
        """# Capítulo 1 — Teste

> Pergunta?

## 1. Aula

### 1.1 Conceito

O atrito máximo fornece a resultante centrípeta necessária para manter o carro na curva.

> ⚡ **Física no Dia a Dia:**  
> O atrito máximo fornece a resultante centrípeta necessária para manter o carro na curva.

| Material | Estado | Efeito |
|---|---|---|
| Gelo | liso | reduz o atrito |
| Asfalto | rugoso | aumenta o atrito |

O gelo liso reduz o atrito, enquanto o asfalto rugoso aumenta o atrito.
""",
    )
    achados = MOD.auditar(arquivo, {})
    regras = {a.regra for a in achados}
    assert "box_repetitivo" in regras
    assert "prosa_repete_tabela" in regras


def test_distingue_historia_essencial_de_acessoria(tmp_path):
    arquivo = gravar(
        tmp_path,
        """# Capítulo 1 — Teste

> Pergunta?

## 1. Aula

### 1.1 Conceito

Faraday mostrou que a variação do fluxo induz corrente.

## 2. Aula final

### 2.1 Aplicação

Faraday recebeu um prêmio por essa contribuição.
""",
    )
    contrato = {
        "historia": {
            "pessoas": [
                {
                    "id": "faraday",
                    "padroes_nome": ["Faraday"],
                    "secoes_inline_essenciais": ["1.1"],
                    "padroes_acessorios": ["prêmio"],
                }
            ]
        }
    }
    achados = MOD.auditar(arquivo, contrato)
    acessorios = [a for a in achados if a.regra == "biografia_acessoria_no_fluxo"]
    assert len(acessorios) == 1
    assert acessorios[0].linha == 15


def test_contrato_piloto_e_json_validos():
    contrato = RAIZ / "Fisica" / "contratos-semanticos" / "1serie-3bim-cap3.json"
    dados = json.loads(contrato.read_text(encoding="utf-8"))
    assert dados["conceitos"]
    assert dados["historia"]["pessoas"]
