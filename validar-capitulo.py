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
  [2c] exatas (unidades, valores declarados e uma operação por linha)
  [7a] TikZ/PNG de Geometria (URL pública, manifesto, fonte e versão publicada)

O QUE ELE NÃO FAZ (fica para a leitura humana / do autor):
  - julgar se o recorte do blueprint foi cumprido ou se algum item do
    NÃO ANTECIPAR apareceu;
  - avaliar qualidade, clareza, adequação de nível ou mistura prosa/marcadores.

Rodar DEPOIS de entregar o capítulo, nunca durante a produção.
Código de saída: 0 se nada falhou; 1 se há falhas (⚠️ são avisos, não falham).
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

# ── Configuração por disciplina ───────────────────────────────────────────────
# boxes: emojis permitidos em linha de box (blockquote)
# fora_box: emojis permitidos FORA de box (ex.: rótulo 📝 Exemplo da Física)
DISC = {
    "portugues":       dict(boxes="💡⚠️📌",     fora_box="",  familia="humanas"),
    "estudos-sociais": dict(boxes="🔎💭👤",       fora_box="",  familia="humanas",
                            prefixo_bloco=True),
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
    "portugues":      (100, 300),   # sem piso editorial; 100 só sinaliza possível truncamento
    "fisica":         (110, 190),
    "quimica":        (180, 240),
    "geometria":      (150, 240),
    "matematica-ef1": (0, 160),
}

# Prosa corrida como fração do conteúdo da aula. É diagnóstico, nunca portão:
# a regra operacional continua sendo estruturar o que é enumerável sem forçar
# marcadores em raciocínios encadeados.
PROSA_REF, PROSA_ALERTA = 0.45, 0.70

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
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


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
    t = IMAGEM_MD.sub(" ", t)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
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
    t = IMAGEM_MD.sub(" ", t)
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


def destino_markdown(conteudo: str) -> str:
    """Extrai o caminho de `destino` ou de `<destino com espaços> "título"`."""
    bruto = conteudo.strip()
    if bruto.startswith("<"):
        fim = bruto.find(">")
        return bruto[1:fim] if fim >= 0 else bruto[1:]
    return bruto.split(None, 1)[0] if bruto else ""


def raiz_tikz_padrao() -> Path:
    """Localiza `_tikz` tanto na raiz quanto a partir da cópia da disciplina."""
    pasta_script = Path(__file__).resolve().parent
    candidatos = (pasta_script / "_tikz", pasta_script.parent / "_tikz")
    for candidato in candidatos:
        if (candidato / "config.json").is_file():
            return candidato
    return candidatos[0]


def carregar_json_tikz(caminho: Path) -> dict:
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    if not isinstance(dados, dict):
        raise ValueError("o JSON não contém um objeto")
    return dados


def validar_figuras_geometria(
    texto: str, arquivo_capitulo: Path, raiz_tikz: Path | None = None
) -> int:
    """Confere Markdown → manifesto/fonte privados → PNG público."""
    print("\n[7a] Figuras TikZ/PNG")
    rc = 0
    imagens = list(IMAGEM_MD.finditer(texto))

    if not imagens:
        ok("nenhuma figura no capítulo (permitido quando não for necessária)")
        return rc

    raiz_tikz = (raiz_tikz or raiz_tikz_padrao()).resolve()
    try:
        config = carregar_json_tikz(raiz_tikz / "config.json")
        repo_publico = config["repositorio_publico"]
        branch_publicacao = config["branch_publicacao"]
        dono_esperado, repo_esperado = repo_publico.split("/", 1)
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, ValueError) as exc:
        return falha(f"configuração TikZ inválida em {raiz_tikz}: {exc}")

    validas = 0
    cache_manifestos = {}
    for imagem in imagens:
        linha = texto.count("\n", 0, imagem.start()) + 1
        alt = imagem.group(1).strip()
        destino = destino_markdown(imagem.group(2))
        erro = False

        if not alt:
            rc |= falha(f"imagem sem texto alternativo na linha {linha}")
            erro = True

        if not destino:
            rc |= falha(f"imagem sem caminho na linha {linha}")
            continue
        url = urlparse(destino)
        if (
            url.scheme != "https"
            or url.netloc != "raw.githubusercontent.com"
            or url.query
            or url.fragment
        ):
            rc |= falha(
                f"imagem da linha {linha} deve usar URL HTTPS direta do repositório TikZ"
            )
            continue
        partes = [unquote(parte) for parte in url.path.split("/") if parte]
        if len(partes) != 7:
            rc |= falha(f"estrutura de URL TikZ inválida na linha {linha}: {destino}")
            continue
        dono, repo, branch, disciplina, ano_serie, slug_documento, arquivo_png = partes
        if (dono, repo, branch) != (
            dono_esperado,
            repo_esperado,
            branch_publicacao,
        ):
            rc |= falha(
                f"imagem da linha {linha} aponta fora de {repo_publico}/{branch_publicacao}"
            )
            continue
        if disciplina != "geometria":
            rc |= falha(f"imagem da linha {linha} não está na pasta geometria")
            continue
        if Path(arquivo_png).suffix.lower() != ".png":
            rc |= falha(f"imagem da linha {linha} não é PNG: {destino}")
            continue

        manifesto_path = (
            raiz_tikz / disciplina / ano_serie / slug_documento / "manifesto.json"
        ).resolve()
        try:
            manifesto_path.relative_to(raiz_tikz)
        except ValueError:
            rc |= falha(f"caminho público inseguro na linha {linha}")
            continue
        if manifesto_path not in cache_manifestos:
            try:
                manifesto = carregar_json_tikz(manifesto_path)
                figuras = manifesto["figuras"]
                fonte_path = (manifesto_path.parent / manifesto["fonte"]).resolve()
                fonte_path.relative_to(manifesto_path.parent)
                fonte = fonte_path.read_text(encoding="utf-8")
                inicios = fonte.count(r"\begin{tikzpicture}")
                finais = fonte.count(r"\end{tikzpicture}")
                paginas = [figura.get("pagina") for figura in figuras]
                if (
                    manifesto.get("disciplina") != disciplina
                    or manifesto.get("ano_serie") != ano_serie
                    or manifesto.get("slug_documento") != slug_documento
                ):
                    raise ValueError("metadados não correspondem ao caminho público")
                if not isinstance(figuras, list) or not figuras:
                    raise ValueError("lista de figuras vazia")
                if inicios != finais or inicios != len(figuras):
                    raise ValueError("quantidade de tikzpicture não corresponde ao manifesto")
                if paginas != list(range(1, len(figuras) + 1)):
                    raise ValueError("páginas do manifesto não são consecutivas")
                cache_manifestos[manifesto_path] = (manifesto, None)
            except (
                OSError,
                UnicodeError,
                json.JSONDecodeError,
                KeyError,
                TypeError,
                ValueError,
            ) as exc:
                cache_manifestos[manifesto_path] = (None, str(exc))

        manifesto, erro_manifesto = cache_manifestos[manifesto_path]
        if erro_manifesto:
            rc |= falha(
                f"manifesto/fonte inválido para a imagem da linha {linha}: {erro_manifesto}"
            )
            continue
        figura = next(
            (item for item in manifesto["figuras"] if item.get("arquivo") == arquivo_png),
            None,
        )
        if figura is None:
            rc |= falha(
                f"imagem da linha {linha} não está indexada em {manifesto_path.name}"
            )
            continue
        if figura.get("alt", "").strip() != alt:
            rc |= falha(
                f"texto alternativo da linha {linha} diverge do manifesto TikZ"
            )
            erro = True
        resumo = figura.get("sha256")
        if not isinstance(resumo, str) or not SHA256_RE.fullmatch(resumo):
            rc |= falha(f"imagem da linha {linha} ainda não possui renderização registrada")
            erro = True
        elif figura.get("publicado_sha256") != resumo:
            rc |= falha(f"imagem da linha {linha} ainda não foi publicada nesta versão")
            erro = True

        if not erro:
            validas += 1

    if validas == len(imagens):
        ok(
            f"{validas} figura(s) com URL pública, manifesto, fonte TikZ e versão publicada válidos"
        )
    return rc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("capitulo")
    ap.add_argument("--disciplina", required=True, choices=DISC.keys())
    ap.add_argument("--blueprint", help="aceito para compatibilidade; a leitura é semântica")
    ap.add_argument(
        "--raiz-tikz",
        type=Path,
        help="sobrescreve a pasta _tikz (útil em testes e validações isoladas)",
    )
    args = ap.parse_args()

    cfg = DISC[args.disciplina]
    min_pal, max_pal = PAL_POR_DISC.get(args.disciplina, (MIN_PAL, MAX_PAL))
    arquivo_capitulo = Path(args.capitulo).resolve()
    texto = arquivo_capitulo.read_text(encoding="utf-8")
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
    if min_pal == 0:
        print(f"\n[2] Extensão por aula (teto {max_pal} · sem mínimo)")
    elif args.disciplina == "portugues":
        print(f"\n[2] Extensão por aula (teto {max_pal} · aviso de truncamento abaixo de {min_pal})")
    else:
        print(f"\n[2] Extensão por aula (teto {max_pal} · piso de referência {min_pal})")
    for num, tit, corpo in aulas:
        n = contar_conteudo(corpo)
        if n > max_pal * 1.1:
            rc |= falha(f"Aula {num} — {tit}: {n} palavras")
        elif n > max_pal:
            aviso(f"Aula {num} — {tit}: {n} palavras (pouco acima do teto)")
        elif min_pal and n < min_pal:
            sufixo = ("possível truncamento — confira o recorte"
                      if args.disciplina == "portugues"
                      else "abaixo do piso — só confira se ficou truncada")
            aviso(f"Aula {num} — {tit}: {n} palavras ({sufixo})")
        else:
            ok(f"Aula {num} — {tit}: {n} palavras")

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
    # Bugs reais do material do 3º bimestre: `\text{}` não aceita acento,
    # `%` sem escape inicia comentário e `\ce{}` depende de mhchem, extensão
    # ausente no render final.
    formulas = re.findall(r"\$\$(.+?)\$\$", texto, flags=re.S)
    if formulas:
        print("\n[2c] LaTeX seguro no renderizador")
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
    if args.disciplina == "quimica":
        excesso = []
        for num, tit, corpo in aulas:
            qtd = sum(1 for linha in corpo.splitlines() if BOX_TITULO.match(linha))
            if qtd > 1:
                excesso.append(f"Aula {num} — {tit}: {qtd}")
        for item in excesso:
            rc |= falha(f"mais de 1 box na aula — {item}")
        if not excesso:
            ok("no máximo 1 box por aula")
    if args.disciplina == "portugues":
        excesso = []
        for num, tit, corpo in aulas:
            qtd = len(re.findall(r"(?m)^>\s*(?:💡|⚠️|📌)️?\s*\*\*", corpo))
            if qtd > 1:
                excesso.append(f"Aula {num} — {tit}: {qtd}")
        for item in excesso:
            rc |= falha(f"mais de 1 box na aula — {item}")
        if not excesso:
            ok("no máximo 1 box por aula")

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
    if args.disciplina == "portugues":
        padroes_meta = [
            r"\bneste capítulo\b", r"\bnesta aula\b", r"\baqui,?\s+o foco\b",
            r"\bveremos adiante\b", r"\bveremos depois\b",
            r"\bserá (?:estudado|detalhado|aprofundado)(?:a)?\b",
            r"\bserão (?:estudado|detalhado|aprofundado)(?:a)?s\b",
            r"\bpertence(?:m)? a outr[oa] bloco\b",
            r"\bpertence(?:m)? a (?:um )?capítulo posterior\b",
            r"\boutro capítulo\b", r"\bcapítulos seguintes\b", r"\bséries posteriores\b",
            r"\ba análise permanece\b", r"\bcabe lembrar que\b",
            r"\bpergunta do capítulo\b", r"\bo capítulo não\b",
        ]
        meta = [i + 1 for i, l in enumerate(linhas)
                if any(re.search(p, l.lower()) for p in padroes_meta)]
        if meta:
            rc |= falha(f"metadiscurso curricular nas linhas {meta}")
        else:
            ok("sem metadiscurso curricular")

        termos_abstratos = re.compile(
            r"\b(?:elementos?|constituintes?|declaraç(?:ão|ões)|"
            r"determina(?:m|r|va|vam|ndo|do|da|dos|das)?|"
            r"caracteriza(?:m|r|va|vam|ndo|do|da|dos|das)?|"
            r"especifica(?:m|r|va|vam|ndo|do|da|dos|das)?)\b",
            re.I,
        )
        abstratos = [i + 1 for i, l in enumerate(linhas) if termos_abstratos.search(l)]
        if abstratos:
            rc |= falha(f"metalinguagem abstrata evitada nas linhas {abstratos}")
        else:
            ok("sem metalinguagem abstrata evitada")
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
    if args.disciplina == "matematica-ef1":
        ponto = [i + 1 for i, l in enumerate(linhas) if r"\cdot" in l]
        xis_letra = [i + 1 for i, l in enumerate(linhas)
                     if re.search(r"(?<![A-Za-zÀ-ÿ])\d+\s*[xX]\s*\d+", l)]
        blocos_formula = list(re.finditer(r"\$\$.*?\$\$", texto, flags=re.S))
        fragmentadas = [
            texto.count("\n", 0, atual.start()) + 1
            for atual, seguinte in zip(blocos_formula, blocos_formula[1:])
            if not texto[atual.end():seguinte.start()].strip()
        ]
        if ponto:
            rc |= falha(f"multiplicação com `\\cdot` nas linhas {ponto}; no EF1 use `\\times`")
        if xis_letra:
            rc |= falha(f"letra x usada como operador nas linhas {xis_letra}; use `\\times`")
        if not ponto and not xis_letra:
            ok("multiplicação usa `\\times` (×), sem ponto central nem letra x")
        if fragmentadas:
            rc |= falha(
                "cadeia de cálculo fragmentada em blocos LaTeX consecutivos "
                f"perto das linhas {fragmentadas}; use um único bloco `aligned`"
            )
        else:
            ok("nenhuma cadeia de cálculo fragmentada em blocos consecutivos")
    if args.disciplina == "geometria":
        fig = [i + 1 for i, l in enumerate(linhas)
               if re.search(r"figura ao lado|imagem ao lado|veja a figura|veja a imagem", l.lower())]
        if fig:
            rc |= falha(f"referência vaga a figura/imagem nas linhas {fig}")
        else:
            ok("nenhuma referência vaga a figura/imagem")
        rc |= validar_figuras_geometria(texto, arquivo_capitulo, args.raiz_tikz)

    print("\n" + ("═══ ✗ HÁ FALHAS — revisar antes de publicar ═══"
                  if rc else "═══ ✓ TUDO CERTO ═══") + "\n")
    print("Lembrete: recorte do blueprint, dependências conceituais, novidade dos boxes")
    print("e repetição tabela–prosa são tratados por `Fisica/auditar-fisica.py`.\n")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
