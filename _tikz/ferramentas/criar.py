#!/usr/bin/env python3
"""Pipeline privado de figuras TikZ do Colégio Eleve.

Mantém fontes, manifestos e renderizações locais sob ``_tikz/`` e publica
somente PNGs no repositório público configurado. Não apaga arquivos remotos.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote


PNG_ASSINATURA = b"\x89PNG\r\n\x1a\n"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ANO_SERIE_RE = re.compile(r"^(?:[4-9]ano|[1-3]serie)$")
FIGURA_ID_RE = re.compile(r"^fig-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
TIKZ_INICIO = r"\begin{tikzpicture}"
TIKZ_FIM = r"\end{tikzpicture}"


class ErroPipeline(RuntimeError):
    """Falha segura e explicável do pipeline."""


def raiz_padrao() -> Path:
    return Path(__file__).resolve().parents[2]


def slugificar(texto: str) -> str:
    normalizado = unicodedata.normalize("NFKD", texto)
    ascii_texto = normalizado.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_texto).strip("-")


def ler_json(caminho: Path) -> dict:
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ErroPipeline(f"arquivo inexistente: {caminho}") from exc
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ErroPipeline(f"JSON inválido em {caminho}: {exc}") from exc
    if not isinstance(dados, dict):
        raise ErroPipeline(f"o JSON precisa conter um objeto: {caminho}")
    return dados


def salvar_json(caminho: Path, dados: dict) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    conteudo = json.dumps(dados, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=caminho.parent, delete=False
    ) as temporario:
        temporario.write(conteudo)
        nome_temporario = Path(temporario.name)
    os.replace(nome_temporario, caminho)


def caminho_seguro(base: Path, caminho: Path) -> Path:
    resolvido = caminho.resolve()
    try:
        resolvido.relative_to(base.resolve())
    except ValueError as exc:
        raise ErroPipeline(f"caminho fora da área permitida: {resolvido}") from exc
    return resolvido


def carregar_config(raiz: Path) -> dict:
    config = ler_json(raiz / "_tikz" / "config.json")
    if config.get("versao") != 1:
        raise ErroPipeline("versão desconhecida de _tikz/config.json")
    repo = config.get("repositorio_publico")
    branch = config.get("branch_publicacao")
    dpi = config.get("dpi")
    disciplinas = config.get("disciplinas_ativas")
    raizes_markdown = config.get("raizes_markdown_permitidas", ["."])
    if not isinstance(repo, str) or repo.count("/") != 1:
        raise ErroPipeline("repositorio_publico inválido em _tikz/config.json")
    if not isinstance(branch, str) or not branch:
        raise ErroPipeline("branch_publicacao inválida em _tikz/config.json")
    if not isinstance(dpi, int) or not 72 <= dpi <= 600:
        raise ErroPipeline("dpi deve ser um inteiro entre 72 e 600")
    if not isinstance(disciplinas, list) or not all(
        isinstance(item, str) and SLUG_RE.fullmatch(item) for item in disciplinas
    ):
        raise ErroPipeline("disciplinas_ativas inválidas em _tikz/config.json")
    if not isinstance(raizes_markdown, list) or not raizes_markdown:
        raise ErroPipeline(
            "raizes_markdown_permitidas deve ser uma lista não vazia"
        )
    for item in raizes_markdown:
        caminho = Path(item) if isinstance(item, str) else None
        if caminho is None or caminho.is_absolute() or not item.strip():
            raise ErroPipeline(
                "raizes_markdown_permitidas aceita somente caminhos relativos"
            )
    return config


def resolver_markdown(raiz: Path, config: dict, valor: str) -> Path:
    """Resolve um Markdown somente dentro das raízes privadas autorizadas."""
    caminho = Path(valor)
    if caminho.is_absolute() or caminho.suffix.lower() != ".md":
        raise ErroPipeline("arquivo_markdown deve ser um caminho .md relativo")

    resolvido = (raiz / caminho).resolve()
    permitidas = config.get("raizes_markdown_permitidas", ["."])
    for item in permitidas:
        base = (raiz / item).resolve()
        try:
            resolvido.relative_to(base)
            return resolvido
        except ValueError:
            continue
    raise ErroPipeline(
        "arquivo_markdown fora das raízes privadas permitidas: "
        f"{resolvido}"
    )


def contar_tikzpictures(fonte: str) -> int:
    inicios = fonte.count(TIKZ_INICIO)
    finais = fonte.count(TIKZ_FIM)
    if inicios != finais:
        raise ErroPipeline(
            f"fonte TikZ incompleta: {inicios} início(s) e {finais} fim(ns)"
        )
    return inicios


def carregar_manifesto(
    caminho: Path,
    raiz: Path,
    *,
    exigir_markdown: bool = False,
) -> tuple[dict, dict]:
    raiz = raiz.resolve()
    config = carregar_config(raiz)
    caminho = caminho_seguro(raiz / "_tikz", caminho)
    manifesto = ler_json(caminho)

    obrigatorios = (
        "versao",
        "disciplina",
        "ano_serie",
        "titulo_documento",
        "slug_documento",
        "arquivo_markdown",
        "fonte",
        "figuras",
    )
    ausentes = [chave for chave in obrigatorios if chave not in manifesto]
    if ausentes:
        raise ErroPipeline("campos ausentes no manifesto: " + ", ".join(ausentes))
    if manifesto["versao"] != 1:
        raise ErroPipeline("versão desconhecida de manifesto")

    disciplina = manifesto["disciplina"]
    ano_serie = manifesto["ano_serie"]
    slug_documento = manifesto["slug_documento"]
    if disciplina not in config["disciplinas_ativas"]:
        raise ErroPipeline(f"disciplina ainda não ativada no pipeline: {disciplina}")
    if not ANO_SERIE_RE.fullmatch(str(ano_serie)):
        raise ErroPipeline(f"ano_serie inválido: {ano_serie}")
    if not SLUG_RE.fullmatch(str(slug_documento)):
        raise ErroPipeline(f"slug_documento inválido: {slug_documento}")
    if not isinstance(manifesto["titulo_documento"], str) or not manifesto[
        "titulo_documento"
    ].strip():
        raise ErroPipeline("titulo_documento vazio")

    pasta_esperada = (
        raiz / "_tikz" / disciplina / ano_serie / slug_documento
    ).resolve()
    if caminho.parent.resolve() != pasta_esperada:
        raise ErroPipeline(
            "o manifesto deve ficar em "
            f"_tikz/{disciplina}/{ano_serie}/{slug_documento}/manifesto.json"
        )

    markdown_rel = Path(manifesto["arquivo_markdown"])
    markdown = resolver_markdown(raiz, config, markdown_rel.as_posix())
    if exigir_markdown and not markdown.is_file():
        raise ErroPipeline(f"Markdown inexistente: {markdown_rel}")

    fonte_rel = Path(manifesto["fonte"])
    if fonte_rel.is_absolute() or fonte_rel.suffix.lower() != ".tex":
        raise ErroPipeline("fonte deve ser um caminho .tex relativo ao manifesto")
    fonte = caminho_seguro(caminho.parent, caminho.parent / fonte_rel)
    if not fonte.is_file():
        raise ErroPipeline(f"fonte TikZ inexistente: {fonte}")

    figuras = manifesto["figuras"]
    if not isinstance(figuras, list) or not figuras:
        raise ErroPipeline("o manifesto precisa ter ao menos uma figura")

    ids: set[str] = set()
    arquivos: set[str] = set()
    paginas: list[int] = []
    for indice, figura in enumerate(figuras, 1):
        if not isinstance(figura, dict):
            raise ErroPipeline(f"figura {indice} não é um objeto")
        figura_id = figura.get("id")
        pagina = figura.get("pagina")
        arquivo = figura.get("arquivo")
        alt = figura.get("alt")
        if not isinstance(figura_id, str) or not FIGURA_ID_RE.fullmatch(figura_id):
            raise ErroPipeline(f"id inválido na figura {indice}: {figura_id}")
        if not figura_id.startswith(f"fig-{indice:02d}-"):
            raise ErroPipeline(
                f"o id da página {indice} deve começar com fig-{indice:02d}-"
            )
        if figura_id in ids:
            raise ErroPipeline(f"id duplicado: {figura_id}")
        ids.add(figura_id)
        if not isinstance(pagina, int) or pagina < 1:
            raise ErroPipeline(f"página inválida em {figura_id}")
        paginas.append(pagina)
        if arquivo != f"{figura_id}.png" or not isinstance(arquivo, str):
            raise ErroPipeline(
                f"arquivo de {figura_id} deve ser exatamente {figura_id}.png"
            )
        if arquivo in arquivos:
            raise ErroPipeline(f"arquivo duplicado: {arquivo}")
        arquivos.add(arquivo)
        if not isinstance(alt, str) or len(alt.strip()) < 12:
            raise ErroPipeline(f"texto alternativo insuficiente em {figura_id}")
    if paginas != list(range(1, len(figuras) + 1)):
        raise ErroPipeline(
            f"as páginas devem ser consecutivas, na ordem 1..{len(figuras)}: {paginas}"
        )

    fonte_texto = fonte.read_text(encoding="utf-8")
    quantidade = contar_tikzpictures(fonte_texto)
    if quantidade != len(figuras):
        raise ErroPipeline(
            f"a fonte tem {quantidade} tikzpicture(s), mas o manifesto tem "
            f"{len(figuras)} figura(s)"
        )
    return manifesto, config


def caminho_publico(manifesto: dict, figura: dict) -> str:
    return "/".join(
        (
            manifesto["disciplina"],
            manifesto["ano_serie"],
            manifesto["slug_documento"],
            figura["arquivo"],
        )
    )


def url_publica(config: dict, manifesto: dict, figura: dict) -> str:
    return (
        "https://raw.githubusercontent.com/"
        f"{config['repositorio_publico']}/{config['branch_publicacao']}/"
        f"{caminho_publico(manifesto, figura)}"
    )


def sha256(caminho: Path) -> str:
    resumo = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1024 * 1024), b""):
            resumo.update(bloco)
    return resumo.hexdigest()


def cabecalho_png(caminho: Path) -> tuple[int, int, int]:
    with caminho.open("rb") as arquivo:
        cabecalho = arquivo.read(26)
    if len(cabecalho) < 26 or cabecalho[:8] != PNG_ASSINATURA:
        raise ErroPipeline(f"arquivo sem assinatura PNG válida: {caminho}")
    if cabecalho[12:16] != b"IHDR":
        raise ErroPipeline(f"PNG sem bloco IHDR esperado: {caminho}")
    largura, altura = struct.unpack(">II", cabecalho[16:24])
    return largura, altura, cabecalho[25]


def dimensoes_png(caminho: Path) -> tuple[int, int]:
    largura, altura, _ = cabecalho_png(caminho)
    return largura, altura


def validar_transparencia_png(caminho: Path) -> None:
    _, _, tipo_cor = cabecalho_png(caminho)
    if tipo_cor not in {4, 6}:
        raise ErroPipeline(
            f"PNG sem canal alfa: {caminho} — o fundo deve ser transparente"
        )


def executavel(nome: str) -> str:
    caminho = shutil.which(nome)
    if not caminho:
        raise ErroPipeline(f"executável obrigatório não encontrado: {nome}")
    return caminho


def executar(comando: list[str], *, cwd: Path | None = None, env: dict | None = None) -> None:
    resultado = subprocess.run(
        comando,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True,
    )
    if resultado.returncode:
        saida = (resultado.stdout + "\n" + resultado.stderr).strip()
        if len(saida) > 5000:
            saida = saida[-5000:]
        raise ErroPipeline(
            f"comando falhou ({' '.join(comando[:2])}):\n{saida}"
        )


def validar_build(
    caminho_manifesto: Path,
    raiz: Path,
    *,
    exigir_aprovacao: bool = False,
    exigir_publicacao: bool = False,
) -> tuple[dict, dict]:
    manifesto, config = carregar_manifesto(caminho_manifesto, raiz)
    build = caminho_manifesto.parent / "build"
    for figura in manifesto["figuras"]:
        png = build / figura["arquivo"]
        if not png.is_file():
            raise ErroPipeline(f"PNG ainda não renderizado: {png}")
        validar_transparencia_png(png)
        largura, altura = dimensoes_png(png)
        resumo = sha256(png)
        if figura.get("sha256") != resumo:
            raise ErroPipeline(
                f"hash divergente em {figura['id']} — renderize novamente"
            )
        if figura.get("largura_px") != largura or figura.get("altura_px") != altura:
            raise ErroPipeline(
                f"dimensões divergentes em {figura['id']} — renderize novamente"
            )
        if exigir_aprovacao and figura.get("aprovada") is not True:
            raise ErroPipeline(
                f"{figura['id']} ainda não foi aprovada após a revisão visual"
            )
        if exigir_publicacao and figura.get("publicado_sha256") != resumo:
            raise ErroPipeline(f"{figura['id']} ainda não foi publicada nesta versão")
    return manifesto, config


def fonte_inicial(figura_id: str) -> str:
    return rf"""\documentclass[tikz,border=3mm,multi=tikzpicture]{{standalone}}
\usepackage{{eleve-geometria}}

\begin{{document}}

% FIGURA 1 — {figura_id}
% Substitua o desenho-base pela configuração descrita no conteúdo.
\begin{{tikzpicture}}[eleve figura, scale=1.15]
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (1.1,2.6);

  \draw[eleve preenchimento] (A) -- (B) -- (C) -- cycle;
  \EleveVertice{{A}}{{below left}}{{A}}
  \EleveVertice{{B}}{{below right}}{{B}}
  \EleveVertice{{C}}{{above}}{{C}}
\end{{tikzpicture}}

\end{{document}}
"""


def bloco_tikz(figura_id: str, pagina: int) -> str:
    return rf"""
% FIGURA {pagina} — {figura_id}
% Substitua o desenho-base pela configuração descrita no conteúdo.
\begin{{tikzpicture}}[eleve figura, scale=1.15]
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (1.1,2.6);

  \draw[eleve preenchimento] (A) -- (B) -- (C) -- cycle;
  \EleveVertice{{A}}{{below left}}{{A}}
  \EleveVertice{{B}}{{below right}}{{B}}
  \EleveVertice{{C}}{{above}}{{C}}
\end{{tikzpicture}}
"""


def comando_novo(args: argparse.Namespace) -> None:
    raiz = args.raiz.resolve()
    config = carregar_config(raiz)
    disciplina = slugificar(args.disciplina)
    ano_serie = slugificar(args.ano_serie)
    slug_documento = args.slug or slugificar(args.titulo)
    figura_id = args.id
    if disciplina not in config["disciplinas_ativas"]:
        raise ErroPipeline(f"disciplina ainda não ativada: {disciplina}")
    if not ANO_SERIE_RE.fullmatch(ano_serie):
        raise ErroPipeline(f"ano/série inválido: {ano_serie}")
    if not SLUG_RE.fullmatch(slug_documento):
        raise ErroPipeline(f"slug inválido: {slug_documento}")
    if not FIGURA_ID_RE.fullmatch(figura_id):
        raise ErroPipeline(
            "id inválido; use, por exemplo, fig-01-elementos-do-triangulo"
        )
    if len(args.alt.strip()) < 12:
        raise ErroPipeline("o texto alternativo precisa descrever a figura")

    markdown = Path(args.markdown)
    resolver_markdown(raiz, config, markdown.as_posix())

    pasta = raiz / "_tikz" / disciplina / ano_serie / slug_documento
    if pasta.exists():
        raise ErroPipeline(f"a pasta do documento já existe: {pasta}")
    pasta.mkdir(parents=True)
    fonte = pasta / "figuras.tex"
    fonte.write_text(fonte_inicial(figura_id), encoding="utf-8")
    manifesto = {
        "versao": 1,
        "disciplina": disciplina,
        "ano_serie": ano_serie,
        "titulo_documento": args.titulo.strip(),
        "slug_documento": slug_documento,
        "arquivo_markdown": markdown.as_posix(),
        "fonte": "figuras.tex",
        "figuras": [
            {
                "id": figura_id,
                "pagina": 1,
                "arquivo": f"{figura_id}.png",
                "alt": args.alt.strip(),
                "aprovada": False,
            }
        ],
    }
    salvar_json(pasta / "manifesto.json", manifesto)
    print(f"✓ documento TikZ criado em {pasta.relative_to(raiz)}")
    print(f"  marcador para o Markdown: <!-- tikz:{figura_id} -->")
    print("  edite figuras.tex e depois rode o comando renderizar")


def comando_adicionar(args: argparse.Namespace) -> None:
    caminho = args.manifesto.resolve()
    manifesto, _ = carregar_manifesto(caminho, args.raiz)
    if not FIGURA_ID_RE.fullmatch(args.id):
        raise ErroPipeline("id de figura inválido")
    if any(figura["id"] == args.id for figura in manifesto["figuras"]):
        raise ErroPipeline(f"id já existe: {args.id}")
    if len(args.alt.strip()) < 12:
        raise ErroPipeline("o texto alternativo precisa descrever a figura")

    pagina = len(manifesto["figuras"]) + 1
    fonte = caminho.parent / manifesto["fonte"]
    texto = fonte.read_text(encoding="utf-8")
    marca = r"\end{document}"
    if texto.count(marca) != 1:
        raise ErroPipeline("a fonte precisa ter exatamente um \\end{document}")
    texto = texto.replace(marca, bloco_tikz(args.id, pagina) + "\n" + marca)
    fonte.write_text(texto, encoding="utf-8")
    manifesto["figuras"].append(
        {
            "id": args.id,
            "pagina": pagina,
            "arquivo": f"{args.id}.png",
            "alt": args.alt.strip(),
            "aprovada": False,
        }
    )
    salvar_json(caminho, manifesto)
    print(f"✓ {args.id} adicionada como página {pagina}")
    print(f"  marcador para o Markdown: <!-- tikz:{args.id} -->")


def comando_renderizar(args: argparse.Namespace) -> None:
    caminho = args.manifesto.resolve()
    manifesto, config = carregar_manifesto(caminho, args.raiz)
    pdflatex = executavel("pdflatex")
    pdftocairo = executavel("pdftocairo")
    fonte = caminho.parent / manifesto["fonte"]
    build = caminho.parent / "build"
    build.mkdir(exist_ok=True)

    env = os.environ.copy()
    estilos = args.raiz.resolve() / "_tikz" / "estilos"
    prefixo_tex = f"{estilos}//{os.pathsep}"
    env["TEXINPUTS"] = prefixo_tex + env.get("TEXINPUTS", "")

    with tempfile.TemporaryDirectory(prefix="eleve-tikz-") as tmp:
        temporario = Path(tmp)
        executar(
            [
                pdflatex,
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-output-directory={temporario}",
                str(fonte),
            ],
            cwd=fonte.parent,
            env=env,
        )
        pdf = temporario / f"{fonte.stem}.pdf"
        if not pdf.is_file():
            raise ErroPipeline("o pdflatex terminou sem produzir PDF")
        prefixo = temporario / "pagina"
        executar(
            [
                pdftocairo,
                "-png",
                "-transp",
                "-r",
                str(config["dpi"]),
                str(pdf),
                str(prefixo),
            ]
        )
        paginas = sorted(
            temporario.glob("pagina-*.png"),
            key=lambda item: int(item.stem.rsplit("-", 1)[1]),
        )
        if len(paginas) != len(manifesto["figuras"]):
            raise ErroPipeline(
                f"foram renderizadas {len(paginas)} páginas para "
                f"{len(manifesto['figuras'])} figuras"
            )

        for figura, origem in zip(manifesto["figuras"], paginas):
            destino = build / figura["arquivo"]
            temporario_png = build / f".{figura['arquivo']}.tmp"
            shutil.copyfile(origem, temporario_png)
            validar_transparencia_png(temporario_png)
            largura, altura = dimensoes_png(temporario_png)
            resumo = sha256(temporario_png)
            os.replace(temporario_png, destino)

            mudou = figura.get("sha256") != resumo
            figura["sha256"] = resumo
            figura["largura_px"] = largura
            figura["altura_px"] = altura
            if mudou:
                figura["aprovada"] = False
                figura.pop("publicado_sha256", None)
                figura.pop("publicado_commit", None)
            print(
                f"✓ {figura['arquivo']} · {largura}×{altura}px · {resumo[:12]}"
            )

    salvar_json(caminho, manifesto)
    print("Revisão visual obrigatória antes de `aprovar` e `publicar`.")


def comando_aprovar(args: argparse.Namespace) -> None:
    caminho = args.manifesto.resolve()
    manifesto, _ = validar_build(caminho, args.raiz)
    selecionadas = set(args.id or [])
    if not args.todas and not selecionadas:
        raise ErroPipeline("informe --todas ou ao menos um --id")
    ids_existentes = {figura["id"] for figura in manifesto["figuras"]}
    desconhecidas = selecionadas - ids_existentes
    if desconhecidas:
        raise ErroPipeline("ids inexistentes: " + ", ".join(sorted(desconhecidas)))
    for figura in manifesto["figuras"]:
        if args.todas or figura["id"] in selecionadas:
            figura["aprovada"] = True
            print(f"✓ revisão visual registrada: {figura['id']}")
    salvar_json(caminho, manifesto)


def baixar_url(url: str) -> bytes:
    requisicao = urllib.request.Request(url, headers={"User-Agent": "eleve-tikz/1"})
    try:
        with urllib.request.urlopen(requisicao, timeout=20) as resposta:
            return resposta.read()
    except (urllib.error.URLError, TimeoutError) as exc:
        raise ErroPipeline(f"não foi possível acessar {url}: {exc}") from exc


def verificar_publicacao(config: dict, manifesto: dict, figura: dict) -> None:
    commit = figura.get("publicado_commit", "")
    sufixo = f"?v={quote(commit)}" if commit else ""
    url = url_publica(config, manifesto, figura) + sufixo
    dados = baixar_url(url)
    if not dados.startswith(PNG_ASSINATURA):
        raise ErroPipeline(f"a URL não retornou um PNG: {url}")
    remoto = hashlib.sha256(dados).hexdigest()
    if remoto != figura.get("sha256"):
        raise ErroPipeline(
            f"a versão pública diverge do build local em {figura['id']}"
        )


def comando_validar(args: argparse.Namespace) -> None:
    caminho = args.manifesto.resolve()
    manifesto, config = validar_build(
        caminho,
        args.raiz,
        exigir_aprovacao=args.aprovada or args.publicado,
        exigir_publicacao=args.publicado,
    )
    print(f"✓ manifesto, fonte e {len(manifesto['figuras'])} PNG(s) locais válidos")
    if args.publicado:
        for figura in manifesto["figuras"]:
            verificar_publicacao(config, manifesto, figura)
            print(f"✓ publicação confirmada: {url_publica(config, manifesto, figura)}")


def executar_gh_json(
    metodo: str, endpoint: str, payload: dict | None = None
) -> dict:
    comando = [executavel("gh"), "api", "--method", metodo, endpoint]
    entrada = None
    if payload is not None:
        comando.extend(("--input", "-"))
        entrada = json.dumps(payload)
    resultado = subprocess.run(
        comando,
        input=entrada,
        capture_output=True,
        text=True,
    )
    if resultado.returncode:
        raise ErroPipeline(
            f"GitHub recusou {metodo} {endpoint}: "
            f"{(resultado.stderr or resultado.stdout).strip()}"
        )
    try:
        return json.loads(resultado.stdout)
    except json.JSONDecodeError as exc:
        raise ErroPipeline("resposta inválida da API do GitHub") from exc


def publicar_atomico(
    config: dict, manifesto: dict, caminho_manifesto: Path
) -> str:
    repo = config["repositorio_publico"]
    branch = config["branch_publicacao"]
    meta = executar_gh_json("GET", f"repos/{repo}")
    if meta.get("full_name", "").lower() != repo.lower():
        raise ErroPipeline("o GitHub respondeu com um repositório inesperado")
    if meta.get("private") is not False:
        raise ErroPipeline("o repositório de imagens precisa ser público")

    referencia = executar_gh_json(
        "GET", f"repos/{repo}/git/ref/heads/{quote(branch, safe='')}"
    )
    commit_base = referencia["object"]["sha"]
    commit_atual = executar_gh_json("GET", f"repos/{repo}/git/commits/{commit_base}")
    arvore_base = commit_atual["tree"]["sha"]

    elementos = []
    build = caminho_manifesto.parent / "build"
    for figura in manifesto["figuras"]:
        png = build / figura["arquivo"]
        conteudo = base64.b64encode(png.read_bytes()).decode("ascii")
        blob = executar_gh_json(
            "POST",
            f"repos/{repo}/git/blobs",
            {"content": conteudo, "encoding": "base64"},
        )
        elementos.append(
            {
                "path": caminho_publico(manifesto, figura),
                "mode": "100644",
                "type": "blob",
                "sha": blob["sha"],
            }
        )

    arvore = executar_gh_json(
        "POST",
        f"repos/{repo}/git/trees",
        {"base_tree": arvore_base, "tree": elementos},
    )
    mensagem = (
        f"Publica TikZ: {manifesto['disciplina']} · "
        f"{manifesto['ano_serie']} · {manifesto['titulo_documento']}"
    )
    commit = executar_gh_json(
        "POST",
        f"repos/{repo}/git/commits",
        {"message": mensagem, "tree": arvore["sha"], "parents": [commit_base]},
    )
    executar_gh_json(
        "PATCH",
        f"repos/{repo}/git/refs/heads/{quote(branch, safe='')}",
        {"sha": commit["sha"], "force": False},
    )
    return commit["sha"]


def comando_publicar(args: argparse.Namespace) -> None:
    caminho = args.manifesto.resolve()
    manifesto, config = validar_build(
        caminho, args.raiz, exigir_aprovacao=True
    )
    print(f"Destino: https://github.com/{config['repositorio_publico']}")
    for figura in manifesto["figuras"]:
        print(f"  · {caminho_publico(manifesto, figura)}")
    if not args.confirmar:
        print("Simulação concluída; nenhum arquivo foi enviado.")
        print("Use `publicar --confirmar` após conferir a lista.")
        return

    commit = publicar_atomico(config, manifesto, caminho)
    for figura in manifesto["figuras"]:
        figura["publicado_sha256"] = figura["sha256"]
        figura["publicado_commit"] = commit

    ultima_falha: ErroPipeline | None = None
    for tentativa in range(5):
        try:
            for figura in manifesto["figuras"]:
                verificar_publicacao(config, manifesto, figura)
            ultima_falha = None
            break
        except ErroPipeline as exc:
            ultima_falha = exc
            if tentativa < 4:
                time.sleep(1)
    if ultima_falha:
        raise ultima_falha
    salvar_json(caminho, manifesto)
    print(f"✓ {len(manifesto['figuras'])} PNG(s) publicados no commit {commit[:12]}")


def bloco_markdown(config: dict, manifesto: dict, figura: dict) -> str:
    return (
        f"<!-- tikz:inicio {figura['id']} -->\n"
        f"![{figura['alt']}]({url_publica(config, manifesto, figura)})\n"
        f"<!-- tikz:fim {figura['id']} -->"
    )


def comando_indexar(args: argparse.Namespace) -> None:
    caminho = args.manifesto.resolve()
    manifesto, config = carregar_manifesto(
        caminho, args.raiz, exigir_markdown=True
    )
    if not args.rascunho:
        for figura in manifesto["figuras"]:
            resumo = figura.get("sha256")
            if (
                not isinstance(resumo, str)
                or not SHA256_RE.fullmatch(resumo)
                or figura.get("publicado_sha256") != resumo
            ):
                raise ErroPipeline(
                    f"{figura['id']} ainda não foi publicada nesta versão"
                )
    markdown = resolver_markdown(
        args.raiz.resolve(), config, manifesto["arquivo_markdown"]
    )
    texto = markdown.read_text(encoding="utf-8")
    faltantes = []
    for figura in manifesto["figuras"]:
        inicio = f"<!-- tikz:inicio {figura['id']} -->"
        fim = f"<!-- tikz:fim {figura['id']} -->"
        marcador = f"<!-- tikz:{figura['id']} -->"
        novo_bloco = bloco_markdown(config, manifesto, figura)
        padrao_bloco = re.compile(
            re.escape(inicio) + r".*?" + re.escape(fim), flags=re.S
        )
        if padrao_bloco.search(texto):
            texto = padrao_bloco.sub(novo_bloco, texto, count=1)
        elif marcador in texto:
            texto = texto.replace(marcador, novo_bloco, 1)
        else:
            faltantes.append(marcador)
    if faltantes:
        raise ErroPipeline(
            "marcadores ausentes no Markdown:\n  " + "\n  ".join(faltantes)
        )
    temporario = markdown.with_name(f".{markdown.name}.tikz.tmp")
    temporario.write_text(texto, encoding="utf-8")
    os.replace(temporario, markdown)
    print(f"✓ {len(manifesto['figuras'])} imagem(ns) indexada(s) em {markdown}")


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Cria, renderiza, valida, publica e indexa figuras TikZ."
    )
    parser.add_argument(
        "--raiz",
        type=Path,
        default=raiz_padrao(),
        help="raiz do projeto autores-materiais-final",
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    novo = sub.add_parser("novo", help="cria fonte e manifesto de um documento")
    novo.add_argument("--disciplina", default="geometria")
    novo.add_argument("--ano-serie", required=True)
    novo.add_argument("--titulo", required=True)
    novo.add_argument("--slug")
    novo.add_argument("--markdown", required=True)
    novo.add_argument("--id", required=True)
    novo.add_argument("--alt", required=True)
    novo.set_defaults(funcao=comando_novo)

    adicionar = sub.add_parser("adicionar", help="adiciona uma página/figura")
    adicionar.add_argument("manifesto", type=Path)
    adicionar.add_argument("--id", required=True)
    adicionar.add_argument("--alt", required=True)
    adicionar.set_defaults(funcao=comando_adicionar)

    renderizar = sub.add_parser("renderizar", help="compila o .tex e gera PNGs")
    renderizar.add_argument("manifesto", type=Path)
    renderizar.set_defaults(funcao=comando_renderizar)

    aprovar = sub.add_parser("aprovar", help="registra a revisão visual")
    aprovar.add_argument("manifesto", type=Path)
    aprovar.add_argument("--id", action="append")
    aprovar.add_argument("--todas", action="store_true")
    aprovar.set_defaults(funcao=comando_aprovar)

    validar = sub.add_parser("validar", help="valida fonte, manifesto e PNGs")
    validar.add_argument("manifesto", type=Path)
    validar.add_argument("--aprovada", action="store_true")
    validar.add_argument("--publicado", action="store_true")
    validar.set_defaults(funcao=comando_validar)

    publicar = sub.add_parser("publicar", help="envia somente os PNGs ao GitHub")
    publicar.add_argument("manifesto", type=Path)
    publicar.add_argument("--confirmar", action="store_true")
    publicar.set_defaults(funcao=comando_publicar)

    indexar = sub.add_parser("indexar", help="atualiza as URLs no Markdown")
    indexar.add_argument("manifesto", type=Path)
    indexar.add_argument(
        "--rascunho",
        action="store_true",
        help="permite indexar antes da publicação apenas para revisão local",
    )
    indexar.set_defaults(funcao=comando_indexar)
    return parser


def main() -> int:
    parser = criar_parser()
    args = parser.parse_args()
    args.raiz = args.raiz.resolve()
    try:
        args.funcao(args)
    except ErroPipeline as exc:
        print(f"✗ {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
