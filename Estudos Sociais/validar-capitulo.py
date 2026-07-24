#!/usr/bin/env python3
"""
validar-capitulo.py — verificação mecânica de um capítulo, em UMA passada.

Arquivo ÚNICO, na raiz de ~/Autores-de-Material/ (antes havia 13 cópias).

USO:
    python3 validar-capitulo.py <capitulo.md> --disciplina <nome>

DISCIPLINAS: portugues · ciencias · biologia · fisica · quimica · estudos-sociais
             geografia · historia · operacoes · geometria · financeira
             sociologia · filosofia · matematica-ef1

O QUE ELE FAZ — só o que a máquina decide melhor que a leitura:
  [1] estrutura do capítulo      [4] boxes (família, consecutivos)
  [2] extensão por aula          [5] emoji fora de box
  [3] seções de fechamento       [6] ortografia pré-Acordo
  [2b] LaTeX que quebra render   [7] regras da família/disciplina

O QUE ELE NÃO FAZ (fica para a leitura humana / do autor):
  - julgar se o recorte do blueprint foi cumprido ou se algum item do
    NÃO ANTECIPAR apareceu;
  - avaliar qualidade, clareza, adequação de nível ou mistura prosa/marcadores.

Rodar DEPOIS de entregar o capítulo, nunca durante a produção.
Código de saída: 0 se nada falhou; 1 se há falhas (⚠️ são avisos, não falham).
"""
import re, argparse

# ── Configuração por disciplina ───────────────────────────────────────────────
# boxes: emojis permitidos em linha de box (blockquote)
# fora_box: emojis permitidos FORA de box (ex.: rótulo 📝 Exemplo da Física)
DISC = {
    "portugues":       dict(boxes="💡⚠️📌🔎👤", fora_box="",  familia="humanas"),
    "estudos-sociais": dict(boxes="🔎💭👤",       fora_box="",  familia="humanas"),
    "geografia":       dict(boxes="🔎💭",         fora_box="",  familia="humanas"),
    "historia":        dict(boxes="🔎💭",         fora_box="",  familia="humanas"),
    "sociologia":      dict(boxes="💭⏸️💡🔍",     fora_box="",  familia="humanas"),
    "filosofia":       dict(boxes="💭⏸️💡🔍",     fora_box="",  familia="humanas"),
    "ciencias":        dict(boxes="💭⏸️💡📏🔬",   fora_box="",  familia="empiricas"),
    "biologia":        dict(boxes="💭⏸️💡📏🔬",   fora_box="",  familia="empiricas"),
    "fisica":          dict(boxes="💭⏸️💡📏⚡📐", fora_box="📝", familia="empiricas"),
    "quimica":         dict(boxes="💡🔎🌍💭⏸️⚠️", fora_box="",  familia="empiricas"),
    "operacoes":       dict(boxes="🔢⚠️",         fora_box="",  familia="matematicas"),
    "geometria":       dict(boxes="🔢⚠️",         fora_box="",  familia="matematicas"),
    "financeira":      dict(boxes="🔢⚠️",         fora_box="",  familia="matematicas"),
    "matematica-ef1":  dict(boxes="🔢⚠️",         fora_box="",  familia="matematicas"),
}

# Extensão por aula: (piso, teto). O piso só avisa; o teto reprova acima de +10%.
# Disciplinas fórmula-driven entregam o mesmo conteúdo em menos texto — fórmula,
# tabela e figura carregam o que em Humanas precisa de frase.
# ⚠️ Os limites foram calibrados com o método de contagem de contar_conteudo().
# Mudar o método sem recalibrar faz o validador reprovar o padrão-ouro.
MIN_PAL, MAX_PAL = 180, 300
PAL_POR_DISC = {
    "fisica":         (110, 190),
    "geografia":      (140, 190),
    "historia":       (140, 190),
    "geometria":      (150, 240),
    "matematica-ef1": (150, 260),   # provisório — calibrar após o piloto
}

TETO_DURO_POR_DISC = {
    "geografia": 200,
    "historia":  200,
}

# Títulos de fechamento proibidos (o formato novo dissolveu tudo nas aulas).
# AMBIGUOS  → só reprova se for o título INTEIRO ("## Síntese" sim;
#             "Síntese proteica" não). INEQUIVOCOS → reprova com complemento.
FECH_AMBIGUOS = ["introdução", "síntese", "na vida real"]
FECH_INEQUIVOCOS = [
    "fórmulas do capítulo", "para não esquecer", "simplificando",
    "e a bíblia nisso", "o que a bíblia diz", "sua parte",
    "aplicações práticas", "fechamento", "a língua no dia a dia",
    "explorando os conceitos", "ampliando o olhar", "no fio da história",
    "o que a fé diz", "pensador em destaque", "você já pensou nisso",
]

PRE_ACORDO = ["idéia", "assembléia", "heróico", "jibóia", "vôo", "enjôo",
              "crêem", "vêem", "feiúra", "baiúca", "pára ", "pêra ", "pólo ", "péla "]

# Emoji PICTOGRÁFICO (o que a regra proíbe fora de box). Setas, ✅/❌ e sinais
# matemáticos NÃO entram: são tipografia legítima de tabela e lista.
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000026FF\U000023E9-\U000023FA]")
TIPOGRAFIA_OK = set("→←↔⇒⇐✅❌✓✗±≈≥≤≠∴")
# ️ é o seletor de variação que acompanha ⚠️ e ⏸️ — sem ele esses boxes
# passavam invisíveis pelo validador.
BOX_TITULO = re.compile(r"^\s*>\s*(" + EMOJI.pattern + r")️?\s*\*\*")


def falha(msg): print(f"  ✗ {msg}"); return 1
def aviso(msg): print(f"  ⚠️  {msg}"); return 0
def ok(msg):    print(f"  ✓ {msg}"); return 0


def contar_conteudo(corpo: str) -> int:
    """Palavras que o aluno lê na aula.

    Exclui blocos de código/ASCII, LaTeX e separadores de tabela.
    Inclui prosa, exemplos, versículos, texto de box e de tabela.
    """
    t = re.sub(r"```.*?```", " ", corpo, flags=re.S)
    t = re.sub(r"\$\$.*?\$\$", " ", t, flags=re.S)
    manter = [l for l in t.split("\n")
              if l.strip() and l.strip() != "---"
              and not re.match(r"^\|[\s:\-|]+\|$", l.strip())]
    txt = re.sub(r"[>#*|_`]", " ", "\n".join(manter))
    return len(re.findall(r"[A-Za-zÀ-ÿ0-9]+(?:[-'][A-Za-zÀ-ÿ0-9]+)*", txt))


def separar_aulas(texto: str):
    """Retorna [(numero, titulo, corpo)] para cada '## N. ...'."""
    aulas = []
    for m in re.finditer(r"(?m)^##\s+(\d+)\.\s*(.*)$", texto):
        aulas.append([m.group(1), m.group(2).strip(), m.start()])
    for i, a in enumerate(aulas):
        fim = aulas[i + 1][2] if i + 1 < len(aulas) else len(texto)
        a.append(texto[a[2]:fim])
    return [(a[0], a[1], a[3]) for a in aulas]


def subsecoes_com_prosa_corrida(texto: str):
    """Localiza subseções com 3+ parágrafos de prosa sem quebra visual."""
    achados = []
    partes = re.split(r"(?m)^(?=###\s+)", texto)
    for parte in partes:
        cabecalho = re.match(r"###\s+([^\n]+)", parte)
        if not cabecalho:
            continue
        corpo = parte[cabecalho.end():]
        corpo = re.split(r"(?m)^(?:##\s+|---\s*$)", corpo, maxsplit=1)[0]
        blocos = re.split(r"\n\s*\n", corpo.strip())
        corrida = 0
        maior = 0
        for bloco in blocos:
            inicio = bloco.lstrip()
            visual = re.match(r"(?:>|[-*+]\s|\d+[.)]\s|\||```)", inicio)
            if visual:
                corrida = 0
            elif inicio:
                corrida += 1
                maior = max(maior, corrida)
        if maior >= 3:
            achados.append((cabecalho.group(1).strip(), maior))
    return achados


def pares_subsecoes_sem_marcadores(aulas):
    """Localiza pares de subtópicos consecutivos sem lista com marcadores."""
    achados = []
    for numero, _, corpo_aula in aulas:
        encontrados = list(re.finditer(r"(?m)^###\s+([^\n]+)", corpo_aula))
        subsecoes = []
        for indice, encontrado in enumerate(encontrados):
            fim = encontrados[indice + 1].start() if indice + 1 < len(encontrados) else len(corpo_aula)
            corpo = corpo_aula[encontrado.end():fim]
            tem_marcadores = bool(
                re.search(r"(?m)^\s*(?:>\s*)?[-*+]\s+\S", corpo)
            )
            subsecoes.append((encontrado.group(1).strip(), tem_marcadores))
        for anterior, atual in zip(subsecoes, subsecoes[1:]):
            if not anterior[1] and not atual[1]:
                achados.append((numero, anterior[0], atual[0]))
    return achados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("capitulo")
    ap.add_argument("--disciplina", required=True, choices=DISC.keys())
    args = ap.parse_args()

    cfg = DISC[args.disciplina]
    min_pal, max_pal = PAL_POR_DISC.get(args.disciplina, (MIN_PAL, MAX_PAL))
    texto = open(args.capitulo, encoding="utf-8").read()
    linhas = texto.split("\n")
    rc = 0

    print(f"\n═══ VALIDAÇÃO · {args.disciplina} · {args.capitulo} ═══")

    # 1. Estrutura ------------------------------------------------------------
    print("\n[1] Estrutura")
    if not re.match(r"^#\s+Capítulo\s+\d+\s+—\s+.+", texto.strip()):
        rc |= falha("título não é `# Capítulo N — Tema`")
    else:
        ok("título no formato `# Capítulo N — Tema`")

    aulas = separar_aulas(texto)
    if not aulas:
        rc |= falha("nenhuma aula `## N.` encontrada")
    else:
        nums = [int(n) for n, _, _ in aulas]
        if nums != list(range(1, len(nums) + 1)):
            rc |= falha(f"numeração das aulas fora de ordem: {nums}")
        else:
            ok(f"{len(aulas)} aulas numeradas em ordem")

    cabeca = texto.split("\n## ", 1)[0]
    if not re.search(r"(?m)^>\s*\S", cabeca):
        rc |= falha("pergunta-problema ausente (blockquote após o título)")
    elif re.search(r"(?i)pergunta-problema\s*:", cabeca):
        rc |= falha("pergunta-problema com rótulo — deve ser só a pergunta")
    else:
        ok("pergunta-problema em blockquote, sem rótulo")

    # 2. Extensão por aula ----------------------------------------------------
    teto_duro = TETO_DURO_POR_DISC.get(args.disciplina, max_pal * 1.1)
    complemento = (
        f" · teto de segurança {teto_duro}"
        if args.disciplina in TETO_DURO_POR_DISC
        else ""
    )
    print(f"\n[2] Extensão por aula (faixa até {max_pal} · piso de referência {min_pal}{complemento})")
    for num, tit, corpo in aulas:
        n = contar_conteudo(corpo)
        if n > teto_duro:
            rc |= falha(f"Aula {num} — {tit}: {n} palavras")
        elif n > max_pal:
            aviso(f"Aula {num} — {tit}: {n} palavras (pouco acima do teto)")
        elif n < min_pal:
            aviso(f"Aula {num} — {tit}: {n} palavras (abaixo do piso — só confira se ficou truncada)")
        else:
            ok(f"Aula {num} — {tit}: {n} palavras")

    if args.disciplina in {"estudos-sociais", "geografia", "historia"}:
        print("\n[2a] Ritmo visual da prosa")
        corridas = subsecoes_com_prosa_corrida(texto)
        for titulo, quantidade in corridas:
            rc |= falha(
                f"{titulo}: {quantidade} parágrafos consecutivos sem quebra visual"
            )
        if not corridas:
            ok("nenhuma sequência de 3+ parágrafos sem lista, tabela ou blockquote")

        print("\n[2b] Alternância de subtópicos")
        pares = pares_subsecoes_sem_marcadores(aulas)
        for numero, anterior, atual in pares:
            rc |= falha(
                f"Aula {numero}: `{anterior}` e `{atual}` estão seguidos e sem marcadores"
            )
        if not pares:
            ok("nenhum par de subtópicos consecutivos sem lista de marcadores")

    # 2c. LaTeX que quebra a renderização -------------------------------------
    # Dois bugs reais do material do 3º bimestre: `\text{}` não aceita acento
    # (o renderizador lê como comando e imprime erro na tela) e `%` sem escape
    # inicia COMENTÁRIO em LaTeX — tudo depois some em silêncio.
    formulas = re.findall(r"\$\$(.+?)\$\$", texto, flags=re.S)
    if formulas:
        print("\n[2c] LaTeX seguro no renderizador")
        acento = [f.strip()[:60] for f in formulas
                  if re.search(r"\\text\{[^}]*[À-ÿ][^}]*\}", f)]
        pct = [f.strip()[:60] for f in formulas if re.search(r"(?<!\\)%", f)]
        for f in acento:
            rc |= falha(f"acento dentro de \\text{{}} — não renderiza: {f}")
        for f in pct:
            rc |= falha(f"`%` sem escape (vira comentário e some): {f}")
        if not acento and not pct:
            ok("nenhum acento em \\text{} e todo `%` escapado")

    # 3. Seções de fechamento proibidas ---------------------------------------
    print("\n[3] Seções de fechamento (devem estar ausentes)")
    achou = []
    for i, l in enumerate(linhas, 1):
        s = l.strip()
        if not s.startswith("#"):
            continue
        titulo = re.sub(r"^#+\s*(?:\d+[\.\)]\s*)?", "", s).strip(" *_?!.").lower()
        if (titulo in FECH_AMBIGUOS or
                any(re.match(rf"^{re.escape(f)}\b", titulo) for f in FECH_INEQUIVOCOS)):
            achou.append(f"linha {i}: {s[:50]}")
    for a in achou:
        rc |= falha(a)
    if not achou:
        ok("nenhuma seção de fechamento")

    # 4. Boxes ----------------------------------------------------------------
    print("\n[4] Boxes")
    box_emojis = set(cfg["boxes"])
    titulos_box = [(i, m.group(1)) for i, l in enumerate(linhas) if (m := BOX_TITULO.match(l))]

    fora = [f"linha {i+1}: {e}" for i, e in titulos_box if e not in box_emojis]
    for f in fora:
        rc |= falha(f"box fora da família permitida — {f}")
    if not fora:
        ok(f"boxes usam só a família permitida ({cfg['boxes']})")

    consec = []
    for a in range(len(titulos_box) - 1):
        i1, i2 = titulos_box[a][0], titulos_box[a + 1][0]
        prosa = any(linhas[k].strip() and not linhas[k].strip().startswith((">", "#", "---", "|"))
                    for k in range(i1 + 1, i2))
        if not prosa:
            consec.append(f"linhas {i1+1} e {i2+1}")
    for c in consec:
        rc |= falha(f"boxes consecutivos sem prosa entre eles — {c}")
    if not consec:
        ok("nenhum par de boxes consecutivos")

    # 5. Emoji fora de box ----------------------------------------------------
    print("\n[5] Emoji fora de box")
    permit = set(cfg["fora_box"])
    fugitivos = []
    for i, l in enumerate(linhas, 1):
        if l.strip().startswith(">"):
            continue
        for m in EMOJI.finditer(l):
            if m.group() in permit or m.group() in TIPOGRAFIA_OK:
                continue
            fugitivos.append(f"linha {i}: {m.group()}  ({l.strip()[:40]})")
    for f in fugitivos:
        rc |= falha(f)
    if not fugitivos:
        ok("nenhum emoji fora de box" + (f" (exceto {cfg['fora_box']})" if permit else ""))

    # 6. Ortografia -----------------------------------------------------------
    print("\n[6] Ortografia (pré-Acordo e trema)")
    baixo = texto.lower()
    achou_pa = [p.strip() for p in PRE_ACORDO if p in baixo]
    if achou_pa:
        rc |= falha("formas pré-Acordo: " + ", ".join(achou_pa))
    else:
        ok("nenhuma forma pré-Acordo")
    trema = {t for t in re.findall(r"[a-zà-ÿ]*ü[a-zà-ÿ]*", baixo)
             if t not in ("müller", "mülleriano")}
    if trema:
        aviso("trema (só permitido em nome próprio estrangeiro): " + ", ".join(trema))
    else:
        ok("nenhum trema indevido")

    # 7. Regras da família / disciplina ---------------------------------------
    print("\n[7] Regras da família / disciplina")
    if cfg["familia"] == "humanas":
        v = re.findall(r"\bos? brasileiros?\b", baixo)
        if v:
            rc |= falha(f"voz em 3ª pessoa ('o brasileiro/os brasileiros'): {len(v)}×")
        else:
            ok("voz inclusiva (sem 'o brasileiro')")
    if cfg["familia"] == "matematicas":
        ast = [i + 1 for i, l in enumerate(linhas) if re.match(r"^\s*\*\s+\S", l)]
        if ast:
            rc |= falha(f"marcadores de lista com '*' (use '-') nas linhas {ast[:8]}")
        else:
            ok("marcadores de lista com '-'")
        prep = [i + 1 for i, l in enumerate(linhas)
                if re.search(r"como veremos adiante|mais à frente estudaremos", l.lower())]
        if prep:
            rc |= falha(f"antecipação proibida ('como veremos adiante') nas linhas {prep}")
        else:
            ok("sem antecipações ('como veremos adiante')")
    if args.disciplina == "geometria":
        fig = [i + 1 for i, l in enumerate(linhas)
               if re.search(r"figura ao lado|veja a figura|conforme o desenho|imagem ao lado", l.lower())]
        if fig:
            rc |= falha(f"referência a imagem inexistente nas linhas {fig}")
        else:
            ok("nenhuma referência a 'figura ao lado'")

    print("\n" + ("═══ ✗ HÁ FALHAS — revisar antes de publicar ═══"
                  if rc else "═══ ✓ TUDO CERTO ═══") + "\n")
    print("Lembrete: recorte do blueprint, itens do NÃO ANTECIPAR, dados e cálculos")
    print("são conferência de LEITURA — este script não julga conteúdo.\n")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
