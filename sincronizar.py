#!/usr/bin/env python3
"""
sincronizar.py — replica os anexos comuns nas 12 pastas de disciplina.

Cada pasta de disciplina é AUTOSSUFICIENTE: o `AUTOR.md` traz, na Parte 3, a
referência completa (nível × faixa, ortografia, LaTeX) e a pasta tem sua cópia
do validador. Isso permite usar/mover uma disciplina sozinha — mas significa que
o material comum existe em 12 lugares.

Este script é o que mantém as 12 cópias iguais. A fonte oficial de escrita fica
visível na raiz; `_fontes/` conserva um espelho para compatibilidade:

    PADRAO-GERAL-DE-ESCRITA.md      →  Anexo A
    _fontes/_PADROES-DE-ESCRITA.md  →  espelho automático
    _fontes/_CONVENCOES.md          →  Anexo B (ortografia) + Anexo C (LaTeX)

Os validadores não são alterados por este script: cada disciplina é revisada
separadamente, sem apagar ajustes locais já aprovados.

USO:
    python3 sincronizar.py            # aplica
    python3 sincronizar.py --check    # só relata o que está fora de sincronia

⚠️ A Parte 3 de um AUTOR.md é SEMPRE reescrita. Nunca edite os anexos direto na
disciplina. Padrão geral de escrita se edita na raiz; ortografia e LaTeX, em
`_fontes/_CONVENCOES.md`. Regra de uma disciplina vai na Parte 2, que este
script nunca toca.
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
PADRAO_GERAL = f"{BASE}/PADRAO-GERAL-DE-ESCRITA.md"
PADRAO_ESPELHO = f"{BASE}/_fontes/_PADROES-DE-ESCRITA.md"
COM_FORMULA = {"Operacoes", "Geometria", "Financeira", "Matematica EF1",
               "Fisica", "Quimica", "Biologia"}
MARCA = "\n---\n\n# PARTE 3 — REFERÊNCIA\n"


def blocos():
    """Monta os textos dos anexos a partir das fontes oficiais."""
    pad = open(PADRAO_GERAL).read()
    pad = pad.split("\n", 1)[1]
    pad = re.sub(r"^>.*$", "", pad, flags=re.M)
    pad = re.sub(r"\n## ", "\n### ", pad)
    pad = re.sub(r"\n#### ", "\n##### ", pad)
    pad = re.sub(r"\n{3,}", "\n\n", pad).strip()

    conv = open(f"{BASE}/_fontes/_CONVENCOES.md").read()
    i = conv.index("## PARTE II")
    orto = conv[:i].split("## PARTE I — ORTOGRAFIA", 1)[1].strip()
    latex = re.sub(r"^>.*$", "", conv[i:].split("\n", 1)[1], flags=re.M).strip()
    return pad, orto, latex


def parte3(disc, pad, orto, latex):
    p = [MARCA,
         "> Material de consulta, igual em todas as disciplinas. Está embutido aqui para que **esta pasta funcione sozinha**. Fonte oficial: `PADRAO-GERAL-DE-ESCRITA.md`, na raiz do conjunto — não edite o anexo por aqui (ver `sincronizar.py`).\n",
         "\n## Anexo A — Nível de profundidade × nível do aluno\n\n" + pad,
         "\n\n## Anexo B — Ortografia (Acordo de 1990 + escolhas da casa)\n\n" + orto]
    if disc in COM_FORMULA:
        p.append("\n\n## Anexo C — LaTeX / MathJax (base comum)\n\n"
                 "> A notação **específica desta disciplina** está na seção 7 do manual, acima.\n\n" + latex)
    return "".join(p) + "\n"


def main():
    check = "--check" in sys.argv
    pad, orto, latex = blocos()
    discs = sorted(d for d in os.listdir(BASE)
                   if os.path.isdir(f"{BASE}/{d}")
                   and not d.startswith("_")
                   and os.path.exists(f"{BASE}/{d}/AUTOR.md"))
    mudou = []

    # Mantém o caminho antigo como espelho, sem criar duas fontes de verdade.
    padrao_fonte = open(PADRAO_GERAL).read()
    if not os.path.exists(PADRAO_ESPELHO) or open(PADRAO_ESPELHO).read() != padrao_fonte:
        mudou.append("_fontes/_PADROES-DE-ESCRITA.md")
        if not check:
            open(PADRAO_ESPELHO, "w").write(padrao_fonte)

    for disc in discs:
        p = f"{BASE}/{disc}/AUTOR.md"
        if not os.path.exists(p):
            print(f"  ⚠️  {disc}: sem AUTOR.md — pulado")
            continue
        t = open(p).read()
        if MARCA not in t:
            print(f"  ⚠️  {disc}: sem a marca da Parte 3 — pulado (verifique o arquivo)")
            continue
        novo = t.split(MARCA)[0].rstrip() + parte3(disc, pad, orto, latex)
        if novo != t:
            mudou.append(f"{disc}/AUTOR.md")
            if not check:
                open(p, "w").write(novo)

    if not mudou:
        print("✓ tudo em sincronia")
    elif check:
        print("Fora de sincronia (rode sem --check para aplicar):")
        for m in mudou:
            print("  ·", m)
    else:
        print(f"✓ {len(mudou)} arquivo(s) atualizado(s):")
        for m in mudou:
            print("  ·", m)
        print("\nLembre de subir de novo os AUTOR.md alterados nos Claude Projects.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
