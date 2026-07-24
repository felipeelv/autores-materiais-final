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
  [2b] LaTeX que quebra render   [7] regras da família/disciplina
  [2c] exatas (unidades, valores declarados e uma operação por linha)

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
    "sociologia":      dict(boxes="💭⏸️💡🔍",     fora_box="",  familia="humanas"),
    "filosofia":       dict(boxes="💭⏸️💡🔍",     fora_box="",  familia="humanas"),
    "ciencias":        dict(boxes="💭⏸️💡📏🔬",   fora_box="",  familia="empiricas"),
    "biologia":        dict(boxes="💭⏸️💡📏🔬",   fora_box="",  familia="empiricas"),
    "fisica":          dict(boxes="💭⏸️💡📏⚡📐👤", fora_box="📝", familia="empiricas"),
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
    "geometria":      (150, 240),
    "matematica-ef1": (150, 260),   # provisório — calibrar após o piloto
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
IMAGEM_MD = re.compile(r"!\[([^\]\n]*)\]\(([^)\n]+)\)")
FORMULA = re.compile(r"\$\$(.+?)\$\$", flags=re.S)
FORMULA_LINHA = re.compile(r"(?m)^[ \t]*\$\$([^\n]*?)\$\$[ \t]*$")
INICIO_EXEMPLO = re.compile(r"(?m)^📝\s*\*\*Exemplo:\*\*")
FIM_EXEMPLO = re.compile(r"(?m)^(?:#{2,3}\s|---\s*$|>\s*\S)")
UNIDADE_APOS_VIRGULA = re.compile(
    r"\d+,\s*(?:\\mathrm\{|kg\b|g\b|N\b|J\b|W\b|V\b|A\b|T\b|"
    r"m(?:/s(?:\^2)?)?\b|s\b|Hz\b|Pa\b|C\b|rad/s\b)"
)


def falha(msg): print(f"  ✗ {msg}"); return 1
def aviso(msg): print(f"  ⚠️  {msg}"); return 0
def ok(msg):    print(f"  ✓ {msg}"); return 0


def contar_conteudo(corpo: str) -> int:
    """Palavras que o aluno lê na aula.

    Exclui blocos de código/ASCII, LaTeX, imagens e separadores de tabela.
    Inclui prosa, exemplos, versículos, texto de box e de tabela.
    """
    t = re.sub(r"```.*?```", " ", corpo, flags=re.S)
    t = re.sub(r"\$\$.*?\$\$", " ", t, flags=re.S)
    t = IMAGEM_MD.sub(" ", t)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
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


def sem_matematica_codigo(texto: str) -> str:
    """Mantém quebras de linha e remove trechos em que comandos LaTeX são válidos."""
    t = re.sub(r"```.*?```", lambda m: "\n" * m.group().count("\n"), texto, flags=re.S)
    t = FORMULA.sub(lambda m: "\n" * m.group().count("\n"), t)
    t = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group().count("\n"), t, flags=re.S)
    return t


def separar_exemplos(texto: str):
    """Retorna blocos de exemplo até o próximo título, separador ou box."""
    exemplos = []
    for inicio in INICIO_EXEMPLO.finditer(texto):
        resto = texto[inicio.end():]
        fim = FIM_EXEMPLO.search(resto)
        pos_fim = inicio.end() + (fim.start() if fim else len(resto))
        exemplos.append((inicio.start(), texto[inicio.start():pos_fim]))
    return exemplos


def numeros_fisicos(texto: str) -> set[str]:
    """Extrai valores, ignorando expoentes, índices e números dentro de unidades."""
    t = re.sub(r"\\mathrm\{[^}]*\}", " ", texto)
    t = re.sub(r"[\^_]\s*\{?\s*-?\d+\s*\}?", " ", t)
    t = re.sub(r"\\[A-Za-z]+", " ", t)
    valores = set()
    for m in re.finditer(r"(?<![A-Za-zÀ-ÿ0-9])\d+(?:\{,\}\d+|[,.]\d+)?", t):
        bruto = m.group().replace("{,}", ".").replace(",", ".")
        try:
            valores.add(f"{float(bruto):g}")
        except ValueError:
            pass
    return valores


def linha_de(texto: str, pos: int) -> int:
    return texto.count("\n", 0, pos) + 1


def parece_inventario_unidades(linha: str) -> bool:
    """Reconhece apenas inventários de alta confiança; definição única é permitida."""
    s = linha.strip()
    baixo = s.lower()
    if re.search(r"\b(as|essas|estas) grandezas são\b", baixo):
        return True
    if re.search(r"\btodas? as (?:grandezas|energias|forças|distâncias)\b", baixo):
        return bool(re.search(r"\b(medid|unidade|newton|joule|metro|segundo)", baixo))
    if not re.search(r"\bness(?:a|as|e|es) (?:express(?:ão|ões)|relaç(?:ão|ões))\b", baixo):
        return False
    simbolos = len(re.findall(r"\$\$[^$]+\$\$", s))
    pistas = len(re.findall(
        r"\b(?:medid[ao]s?|unidades?|newtons?|joules?|metros?|segundos?|"
        r"quilogramas?|sem unidade|não possui unidade)\b|\([^)]{1,18}\)",
        baixo,
    ))
    return simbolos >= 2 and pistas >= 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("capitulo")
    ap.add_argument("--disciplina", required=True, choices=DISC.keys())
    ap.add_argument("--blueprint", help="aceito para compatibilidade; a leitura é semântica")
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
    print(f"\n[2] Extensão por aula (teto {max_pal} · piso de referência {min_pal})")
    for num, tit, corpo in aulas:
        n = contar_conteudo(corpo)
        if n > max_pal * 1.1:
            rc |= falha(f"Aula {num} — {tit}: {n} palavras")
        elif n > max_pal:
            aviso(f"Aula {num} — {tit}: {n} palavras (pouco acima do teto)")
        elif n < min_pal:
            aviso(f"Aula {num} — {tit}: {n} palavras (abaixo do piso — só confira se ficou truncada)")
        else:
            ok(f"Aula {num} — {tit}: {n} palavras")

    # 2b. LaTeX que quebra a renderização -------------------------------------
    # Bugs reais do material do 3º bimestre: `\text{}` não aceita acento,
    # `%` sem escape inicia comentário e `\ce{}` depende de mhchem, extensão
    # ausente no render final.
    formulas = re.findall(r"\$\$(.+?)\$\$", texto, flags=re.S)
    if formulas:
        print("\n[2b] LaTeX seguro no renderizador")
        acento = [f.strip()[:60] for f in formulas
                  if re.search(r"\\text\{[^}]*[À-ÿ][^}]*\}", f)]
        pct = [f.strip()[:60] for f in formulas if re.search(r"(?<!\\)%", f)]
        mhchem = [f.strip()[:60] for f in formulas if r"\ce{" in f]
        for f in acento:
            rc |= falha(f"acento dentro de \\text{{}} — não renderiza: {f}")
        for f in pct:
            rc |= falha(f"`%` sem escape (vira comentário e some): {f}")
        for f in mhchem:
            rc |= falha(f"`\\ce{{}}` requer mhchem e aparece literal: {f}")
        if not acento and not pct and not mhchem:
            ok("sem \\ce{}, nenhum acento em \\text{} e todo `%` escapado")

    # 2c. Regras determinísticas de exatas -----------------------------------
    if args.disciplina == "fisica":
        print("\n[2c] Passada específica de exatas")

        fora_matematica = sem_matematica_codigo(texto)
        espaco_fino_fora = [
            i for i, l in enumerate(fora_matematica.splitlines(), 1) if r"\," in l
        ]
        if espaco_fino_fora:
            rc |= falha(f"`\\,` fora de ambiente matemático nas linhas {espaco_fino_fora}")
        else:
            ok("`\\,` aparece somente dentro de ambiente matemático")

        virgula_unidade = [
            i for i, l in enumerate(linhas, 1) if UNIDADE_APOS_VIRGULA.search(l)
        ]
        if virgula_unidade:
            rc |= falha(
                f"vírgula usada como espaço antes de unidade nas linhas {virgula_unidade}"
            )
        else:
            ok("nenhum caso como `10,kg` ou `10, kg`")

        inventarios = [
            i for i, l in enumerate(linhas, 1) if parece_inventario_unidades(l)
        ]
        if inventarios:
            rc |= falha(f"parágrafo-inventário de unidades nas linhas {inventarios}")
        else:
            ok("nenhum inventário de unidades de alta confiança")

        cadeias = []
        valores_novos = []
        for pos_exemplo, exemplo in separar_exemplos(texto):
            formulas_exemplo = list(FORMULA_LINHA.finditer(exemplo))
            if not formulas_exemplo:
                continue
            contexto_inicio = max(
                texto.rfind("\n### ", 0, pos_exemplo),
                texto.rfind("\n## ", 0, pos_exemplo),
                0,
            )
            conhecidos = numeros_fisicos(
                texto[contexto_inicio:pos_exemplo]
                + exemplo[:formulas_exemplo[0].start()]
            )
            for formula in formulas_exemplo:
                linha = linha_de(texto, pos_exemplo + formula.start())
                conteudo = formula.group(1)
                if conteudo.count("=") > 1:
                    cadeias.append(linha)
                atuais = numeros_fisicos(conteudo)
                sem_unidades = re.sub(r"\\mathrm\{[^}]*\}", " ", conteudo)
                sem_indices = re.sub(r"[\^_]\s*\{?\s*-?\d+\s*\}?", " ", sem_unidades)
                tem_operacao = bool(
                    re.search(r"\\(?:cdot|frac|sqrt)|[+\-*/]", sem_indices)
                )
                partes = re.split(r"=|\\approx", sem_indices)
                lados = []
                for lado in partes:
                    lado = re.sub(r"\\[A-Za-z]+|\\[,;! ]", " ", lado)
                    lados.append(re.sub(r"[{}\s]", "", lado))
                lado_numerico = any(
                    re.fullmatch(r"-?\d+(?:,\d+|\.\d+)?", lado) for lado in lados
                )
                if tem_operacao and not lado_numerico:
                    novos = sorted(
                        valor for valor in atuais - conhecidos
                        if valor not in {"0", "1", "2"}
                    )
                    if novos:
                        valores_novos.append((linha, novos))
                conhecidos.update(atuais)

        if cadeias:
            rc |= falha(
                f"mais de uma operação/etapa na mesma linha de exemplo: {cadeias}"
            )
        else:
            ok("uma operação por linha nos exemplos")

        if valores_novos:
            for linha, valores in valores_novos:
                aviso(
                    f"linha {linha}: conferir origem dos valores "
                    + ", ".join(valores)
                    + " (não apareceram antes no exemplo)"
                )
        else:
            ok("nenhum valor numérico novo surgiu durante os cálculos")

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
    print("Lembrete: recorte do blueprint, dependências conceituais, novidade dos boxes")
    print("e repetição tabela–prosa são tratados por `auditar-fisica.py`.\n")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
