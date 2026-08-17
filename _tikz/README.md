# Criador de imagens TikZ

O contrato visual definitivo — unidade pedagógica, divisão das figuras,
tipografia e teste a 300 px — está em `PADRAO-DE-CONSTRUCAO.md`.

Esta é a **única área privada de produção TikZ** do projeto. Fontes `.tex`,
manifestos, estilos, ferramentas e renderizações temporárias ficam sob
`_tikz/`. As pastas das disciplinas não recebem fontes ou PNGs.

O repositório público `felipeelv/imagens-tikz` recebe somente cópias dos PNGs
aprovados. O Markdown privado referencia esses arquivos por URL absoluta.

## Estado salvo — 23/07/2026

- Geometria: 15 documentos/manifestos e 111 figuras;
- 111 PNGs aprovados, publicados e validados por SHA-256;
- 15 Markdown sincronizados com as cópias oficiais no Google Drive;
- repositório público auditado com somente `README.md` e 111 PNGs;
- último commit da produção do 3º bimestre: `2fdcd844d6a909e73c4204a99445dd7d55535447`;
- Física: 17 documentos e 107 figuras aprovadas, publicadas, indexadas,
  revisadas em contexto e sincronizadas no Google Drive;
- Matemática EF1: 18 documentos e 58 figuras aprovadas, publicadas,
  indexadas, revisadas em contexto e salvas no Google Drive;
- Química: 5 documentos e 15 figuras aprovadas, publicadas, indexadas e
  revisadas no original, a 300 px e no capítulo em coluna de 720 px;
- repositório público: 291 PNGs, sendo 111 de Geometria, 107 de Física,
  58 de Matemática EF1 e 15 de Química;
- commit público vigente: `1addc5b0379a44995a89003d50781f5d7d10d764`.

O detalhamento editorial está em `../Geometria/Acompanhamento de produção.md`; os commits da segunda etapa estão em `../Geometria/PLANO-DE-IMAGENS-TIKZ-BLOCO2.md`.
O contrato específico do novo piloto está em
`../Fisica/PADRAO-DE-IMAGENS-TIKZ.md`.
O contrato visual de Química está em
`../Quimica/PADRAO-DE-IMAGENS-TIKZ.md`.

## Revisão de 04/08/2026 — Física · 1ª série · 3º Bim Bloco 1

Auditoria dos dois capítulos contra `../Fisica/PADRAO-DE-IMAGENS-TIKZ.md`:

- seis figuras existentes refeitas por violação de respiro — `fig-02` e
  `fig-03` de Leis de Newton; `fig-01`, `fig-02`, `fig-03` e `fig-05` de
  Forças mecânicas. O caso mais grave era a tração desenhada sobre a própria
  corda, contra a regra de faixa paralela;
- quatro figuras novas: `fig-06-diagrama-de-corpo-livre` e
  `fig-07-par-livro-e-terra` (Leis de Newton);
  `fig-06-diagramas-dos-corpos-ligados` e
  `fig-07-grafico-forca-e-deformacao` (Forças mecânicas). As novas entram
  como páginas 6 e 7 da fonte; a posição no Markdown segue a pergunta
  pedagógica, não o número do arquivo;
- as 14 peças foram revisadas a 300 px, publicadas, validadas por hash e
  indexadas no Markdown privado e na cópia do Google Drive.

Os capítulos podem permanecer fora deste repositório, desde que sua raiz
privada esteja listada em `raizes_markdown_permitidas` no `config.json`. O
manifesto guarda um caminho relativo à raiz do projeto; caminhos absolutos ou
fora da lista continuam bloqueados. Assim, o indexador atualiza diretamente o
conteúdo pronto sem obrigar sua inclusão no repositório dos autores ou no
repositório público de imagens.

## Organização

```text
_tikz/
├── config.json
├── estilos/
│   ├── eleve-geometria.sty
│   ├── eleve-fisica.sty
│   ├── eleve-matematica-ef1.sty
│   └── eleve-quimica.sty
├── ferramentas/
│   └── criar.py
└── <disciplina>/
    └── <ano-serie>/
        └── <titulo-do-documento>/
            ├── figuras.tex
            ├── manifesto.json
            └── build/
                └── fig-*.png
```

Cada ambiente `tikzpicture` de `figuras.tex` gera uma página do PDF e um PNG.
A ordem deve coincidir com `pagina` no manifesto. `build/` é regenerável e não
é versionado.

## Fluxo por disciplina

### 1. Criar o documento

```bash
python3 _tikz/ferramentas/criar.py novo \
  --ano-serie 6ano \
  --titulo "Triângulos: elementos e classificação" \
  --markdown Geometria/modelos/geometria-6ano-modelo.md \
  --id fig-01-elementos-do-triangulo \
  --alt "Triângulo ABC com vértices, lados e ângulos internos identificados"
```

O comando cria o `.tex`, o manifesto e informa o marcador que deve ser colocado
no ponto exato do Markdown:

```md
<!-- tikz:fig-01-elementos-do-triangulo -->
```

### 2. Adicionar outra figura

```bash
python3 _tikz/ferramentas/criar.py adicionar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json \
  --id fig-02-classificacao-por-lados \
  --alt "Três triângulos classificados como equilátero, isósceles e escaleno"
```

Edite os ambientes criados em `figuras.tex`. Não use cor como única forma de
comunicar uma propriedade: combine cor com rótulo, marca ou tipo de linha.

O padrão visual usa tela transparente, sem cartões de fundo nem painéis
brancos. As figuras devem ser pensadas para a largura efetiva mínima de
300 px: prefira composição vertical ou quase quadrada, rótulos grandes e
somente o texto indispensável ao desenho. Títulos, explicações e fórmulas que
já aparecem no conteúdo permanecem no Markdown, evitando repetição e texto
pequeno dentro do PNG.

A revisão visual inclui obrigatoriamente uma cópia reduzida a 300 px sobre
fundo branco. Nessa escala, nenhum texto pode tocar outro texto nem cruzar
segmento, seta ou marca geométrica. Reserve faixas distintas para desenho,
rótulos e explicações; se dois conceitos não couberem lado a lado, empilhe-os
ou separe-os. No TikZ, use `\normalsize` como mínimo e encurte o rótulo antes
de reduzir a fonte. DPI alto não corrige composição sobreposta.

### 3. Renderizar

```bash
python3 _tikz/ferramentas/criar.py renderizar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json
```

São necessários `pdflatex` e `pdftocairo`. A saída padrão é PNG transparente a
300 DPI. O validador rejeita imagens sem canal alfa. Toda mudança de imagem
cancela aprovações e registros de publicação anteriores.

### 4. Revisar e aprovar

Abra os PNGs de `build/` e confira legibilidade, notação, medidas, proporções e
correspondência com o conteúdo. No macOS, gere a prévia de largura real — use
`--resampleWidth`, não `-Z`, pois a altura não deve limitar a redução:

```bash
sips --resampleWidth 300 build/fig-01-exemplo.png \
  --out /tmp/fig-01-exemplo-300px.png
sips -s format jpeg /tmp/fig-01-exemplo-300px.png \
  --out /tmp/fig-01-exemplo-300px-branco.jpg
```

Confira a versão JPEG sobre branco e depois registre a revisão:

```bash
python3 _tikz/ferramentas/criar.py aprovar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json \
  --todas
```

### 5. Validar e simular a publicação

```bash
python3 _tikz/ferramentas/criar.py validar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json \
  --aprovada

python3 _tikz/ferramentas/criar.py publicar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json
```

O segundo comando é somente uma simulação. Ele lista o destino e não envia
nada. Para publicar os PNGs aprovados:

```bash
python3 _tikz/ferramentas/criar.py publicar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json \
  --confirmar
```

O publicador usa a API do GitHub por meio de `gh`, cria um único commit e nunca
remove arquivos. Há uma lista fechada de destino e extensão: somente `.png` em
`felipeelv/imagens-tikz`.

### 6. Indexar no Markdown

```bash
python3 _tikz/ferramentas/criar.py indexar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json
```

O marcador vira um bloco idempotente. Quando a publicação já existe, o
indexador usa o commit publicado na URL, tornando a referência imutável:

```md
<!-- tikz:inicio fig-01-elementos-do-triangulo -->
![Triângulo ABC com vértices, lados e ângulos internos identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/<commit-publicado>/geometria/6ano/triangulos-elementos-e-classificacao/fig-01-elementos-do-triangulo.png)
<!-- tikz:fim fig-01-elementos-do-triangulo -->
```

O indexador normal exige que a mesma versão já esteja publicada. Para montar
uma prévia local antes da publicação, use `--rascunho`.

Depois da indexação, abra o capítulo no mesmo formato de coluna ou página usado
na entrega e faça uma segunda revisão visual. Além da prévia isolada de 300 px,
essa conferência deve verificar o encontro da imagem com tabelas, subtítulos e
imagens vizinhas. A sincronização final só ocorre quando não houver rótulos,
vetores ou casos empilhados próximos o bastante para parecer sobreposição.

### 7. Conferir a publicação real

```bash
python3 _tikz/ferramentas/criar.py validar \
  _tikz/geometria/6ano/triangulos-elementos-e-classificacao/manifesto.json \
  --publicado
```

Esse modo baixa cada URL pública e compara o SHA-256 com o PNG local. Deve ser
executado antes de copiar o Markdown pronto para o Google Drive.

## O que nunca vai ao repositório público

- fontes `.tex`;
- manifestos `.json`;
- Markdown dos capítulos;
- blueprints, memórias e arquivos `AUTOR.md`;
- logs, PDFs intermediários ou credenciais.

Física está ativa com estilo e fluxo aprovados em todos os capítulos do
3º bimestre. Química também está ativa: o piloto e os quatro Capítulos 2
oficiais foram produzidos, publicados e revisados em contexto.
