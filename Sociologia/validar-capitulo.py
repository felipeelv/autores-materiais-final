#!/usr/bin/env python3
"""
validar-capitulo.py — verificação mecânica de um capítulo, em UMA passada.

Arquivo ÚNICO, na raiz de ~/Autores-de-Material/ (antes havia 13 cópias).

USO:
    python3 validar-capitulo.py <capitulo.md> --disciplina <nome>

DISCIPLINAS: portugues · ciencias · biologia · fisica · quimica · estudos-sociais
             operacoes · geometria · financeira · sociologia · filosofia · matematica-ef1

O QUE ELE FAZ — só o que a máquina decide melhor que a leitura:
  [1] estrutura do capítulo      [4] boxes (família, consecutivos)
  [2] extensão por aula          [5] emoji fora de box
  [3] seções de fechamento       [6] ortografia pré-Acordo
  [2b] prosa × marcadores        [7] regras da família/disciplina
  [2c] LaTeX que quebra render

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
    "estudos-sociais": dict(boxes="🔎💭👤",       fora_box="",  familia="humanas",
                            prefixo_bloco=True),
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
    "sociologia":     (170, 195),
    "fisica":         (110, 190),
    "geometria":      (150, 240),
    "matematica-ef1": (150, 260),   # provisório — calibrar após o piloto
}

# Prosa corrida como fração do conteúdo da aula. É diagnóstico, nunca portão:
# a regra operacional continua sendo estruturar o que é enumerável sem forçar
# marcadores em raciocínios encadeados.
PROSA_REF, PROSA_ALERTA = 0.45, 0.70

TETO_DURO_POR_DISC = {
    "sociologia": 200,
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


def perfil_forma(corpo: str):
    """Retorna palavras em (prosa, lista, box, tabela).

    Fórmulas contam como conteúdo estruturado com peso fixo. Isso evita que
    aulas de cálculo pareçam compostas apenas de prosa explicativa. Imagens e
    seus textos alternativos ficam fora do cálculo editorial.
    """
    t = re.sub(r"```.*?```", " ", corpo, flags=re.S)
    t = re.sub(r"\$\$.*?\$\$", "\n@FORMULA@\n", t, flags=re.S)
    t = re.sub(r"(?m)^!\[[^\]]*\]\([^)]+\)\s*$", " ", t)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    prosa = lista = box = tabela = 0

    for linha in t.split("\n"):
        if linha.strip() == "@FORMULA@":
            lista += 12
    t = t.replace("@FORMULA@", "")

    for linha in t.split("\n"):
        s = linha.strip()
        if not s or s == "---" or s.startswith("#"):
            continue
        n = len(re.findall(
            r"[A-Za-zÀ-ÿ0-9]+(?:[-'][A-Za-zÀ-ÿ0-9]+)*",
            re.sub(r"[>#*|_`]", " ", s),
        ))
        if s.startswith(">"):
            box += n
        elif re.match(r"^[-*+]\s|^\d+[.)]\s", s):
            lista += n
        elif s.startswith("|"):
            if not re.match(r"^\|[\s:\-|]+\|$", s):
                tabela += n
        else:
            prosa += n
    return prosa, lista, box, tabela


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
        corrida = 0
        maior = 0
        for bloco in re.split(r"\n\s*\n", corpo.strip()):
            inicio = bloco.lstrip()
            if re.match(r"(?:>|[-*+]\s|\d+[.)]\s|\||```)", inicio):
                corrida = 0
            elif inicio:
                corrida += 1
                maior = max(maior, corrida)
        if maior >= 3:
            achados.append((cabecalho.group(1).strip(), maior))
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
    # O prefixo BL1_/BL2_ identifica o bloco do bimestre. Onde a disciplina o exige
    # (cfg["prefixo_bloco"]), o título sem prefixo é falha; nas demais, é opcional.
    exige_prefixo = cfg.get("prefixo_bloco", False)
    m_titulo = re.match(r"^#\s+(BL(\d)_)?Capítulo\s+\d+\s+—\s+.+", texto.strip())
    if not m_titulo:
        rc |= falha("título não é `# [BL{1|2}_]Capítulo N — Tema`")
    elif exige_prefixo and not m_titulo.group(1):
        rc |= falha("título sem o prefixo de bloco — use `# BL1_Capítulo N — Tema`")
    else:
        ok(f"título no formato `# {m_titulo.group(1) or ''}Capítulo N — Tema`")

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
    teto_duro = TETO_DURO_POR_DISC.get(args.disciplina)
    detalhe_teto = f" · teto de segurança {teto_duro}" if teto_duro else ""
    print(f"\n[2] Extensão por aula (teto {max_pal} · piso de referência {min_pal}{detalhe_teto})")
    for num, tit, corpo in aulas:
        n = contar_conteudo(corpo)
        if teto_duro and n > teto_duro:
            rc |= falha(f"Aula {num} — {tit}: {n} palavras")
        elif n > max_pal * 1.1:
            rc |= falha(f"Aula {num} — {tit}: {n} palavras")
        elif n > max_pal:
            aviso(f"Aula {num} — {tit}: {n} palavras (pouco acima do teto)")
        elif n < min_pal:
            aviso(f"Aula {num} — {tit}: {n} palavras (abaixo do piso — só confira se ficou truncada)")
        else:
            ok(f"Aula {num} — {tit}: {n} palavras")

    if args.disciplina == "sociologia":
        print("\n[2a] Ritmo visual da prosa")
        corridas = subsecoes_com_prosa_corrida(texto)
        for titulo, quantidade in corridas:
            rc |= falha(
                f"{titulo}: {quantidade} parágrafos consecutivos sem quebra visual"
            )
        if not corridas:
            ok("nenhuma sequência de 3+ parágrafos sem lista, tabela ou blockquote")

        print("\n[2b] Organizadores visuais por aula")
        sem_organizador = []
        for num, tit, corpo in aulas:
            partes = re.split(r"(?m)^(?=###\s+)", corpo)
            organizadas = 0
            for parte in partes:
                if not re.match(r"###\s+", parte):
                    continue
                tem_lista = bool(re.search(r"(?m)^\s*[-*+]\s+\S", parte))
                tem_tabela = bool(re.search(r"(?m)^\|.+\|$", parte))
                if tem_lista or tem_tabela:
                    organizadas += 1
            if organizadas < 2:
                sem_organizador.append(
                    f"Aula {num} — {tit}: apenas {organizadas} subseção(ões) com lista ou tabela"
                )
        for item in sem_organizador:
            rc |= falha(item)
        if not sem_organizador:
            ok("todas as aulas possuem ao menos 2 subseções com lista ou tabela")

    # 2b. Prosa × marcadores — diagnóstico, nunca reprova ---------------------
    print(f"\n[2b] Prosa × marcadores (referência ~{int(PROSA_REF * 100)}% prosa · diagnóstico, não reprova)")
    for num, tit, corpo in aulas:
        prosa, lista, box, tabela = perfil_forma(corpo)
        total = prosa + lista + box + tabela
        if not total:
            continue
        proporcao = prosa / total
        estruturado = lista + tabela
        if estruturado == 0:
            marca = "⚠️ "
            obs = "sem lista nem tabela — há algo enumerável aqui?"
        elif proporcao > PROSA_ALERTA:
            marca = "⚠️ "
            obs = "bloco de prosa — veja o que é enumerável"
        else:
            marca = "✓"
            obs = f"{estruturado} pal. em lista/tabela"
        print(f"  {marca} Aula {num} — {tit[:30]}: {proporcao * 100:.0f}% prosa · {obs}")

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

    if args.disciplina == "sociologia":
        inconsistentes = []
        for num, tit, corpo in aulas:
            qtd = sum(1 for linha in corpo.splitlines() if BOX_TITULO.match(linha))
            if qtd != 1:
                inconsistentes.append(f"Aula {num} — {tit}: {qtd}")
        for item in inconsistentes:
            rc |= falha(f"Sociologia exige exatamente 1 box por aula — {item}")
        if not inconsistentes:
            ok("exatamente 1 box por aula")

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
