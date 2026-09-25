# Modelos de Química por série

> Estes capítulos são referências de linguagem, ritmo, notação e organização. O conteúdo sempre vem do blueprint; o modelo não autoriza copiar recortes, exemplos ou dados para outro capítulo. Se houver divergência, prevalecem o blueprint e o `AUTOR.md` atual.

Em 23/07/2026, cópias idênticas dos quatro modelos foram formalizadas como os Capítulos 1 oficiais do 3º bimestre. Os arquivos desta pasta continuam como referências editoriais.

| Série | Arquivo | Tema de referência | Situação |
|---|---|---|---|
| 9º ano | `quimica-9ano-modelo.md` | Ácidos e bases | Validado e aprovado |
| 1ª série EM | `quimica-1serie-modelo.md` | Tabela periódica | Atualizado e validado |
| 2ª série EM | `quimica-2serie-modelo.md` | Equilíbrio químico | Revisado, ilustrado e validado |
| 3ª série EM | `quimica-3serie-modelo.md` | Isomeria | Atualizado e validado |

## O que os quatro modelos calibram

- **9º ano:** fato observável em uma frase, definição imediata, pH qualitativo e linguagem introdutória;
- **1ª série:** configuração eletrônica, valores tabelados e explicação das tendências periódicas;
- **2ª série:** físico-química com uma etapa de cálculo por linha, prosa curta,
  marcadores e figuras de equilíbrio dinâmico e processo industrial;
- **3ª série:** representação estrutural, análise espacial e aplicações biológicas com ressalvas científicas.

As conexões VP dos blueprints não foram incluídas: nos quatro capítulos, elas não passaram no teste de ligação conceitual exigido pelo `AUTOR.md`.

## Cadência aprovada

O modelo do 9º ano fixa a escrita direta para os próximos capítulos de Química:

**fato observável → definição → representação ou fórmula → exemplo/tabela → ressalva**

- preferir 180–210 palavras de conteúdo por aula, com teto de 240 e sem mínimo obrigatório;
- usar contexto cotidiano curto, sem transformar a abertura em história;
- manter um exemplo reconhecível por conceito;
- registrar o químico-chave em uma frase factual, sem biografia;
- usar tabelas, fórmulas e esquemas para carregar informação e evitar paráfrases;
- usar MathJax básico com `\mathrm{}` e setas manuais; `\ce{}`/mhchem é incompatível com o render final;
- usar no máximo 1 box por aula, somente quando acrescentar informação.

Na revisão aprovada em 23/07/2026, o capítulo do 9º ano passou de 713 para 568 palavras pelo método do validador (**redução de 20,3%**) e preservou o recorte do blueprint.

Na revisão inicial dos três modelos do Ensino Médio, as 18 aulas ficaram entre
180 e 209 palavras. A 1ª série totaliza 1.162 palavras e a 3ª, 1.137.

Em uma segunda revisão da 2ª série, a prosa corrida foi reorganizada em
marcadores sem reduzir o recorte. O capítulo passou a 1.082 palavras pelo
método do validador, com 164–199 palavras por aula e sem mínimo obrigatório.
O diagnóstico de forma registra 26%–51% de prosa por aula.

O modelo da 2ª série também recebeu três figuras TikZ/PNG:

- velocidades e concentrações no equilíbrio dinâmico;
- efeito da pressão na síntese da amônia;
- fluxo Haber–Bosch com separação e recirculação.

As imagens foram revisadas no original, a 300 px sobre branco e no capítulo em
coluna de 720 px, publicadas no commit
`e637319bb635434380a7a194e2ad18c7e0111dfd` e indexadas por URL imutável.

## Validar os modelos

Na pasta `Quimica/`:

```bash
python3 validar-capitulo.py modelos/quimica-9ano-modelo.md --disciplina quimica
```

Para validar as imagens da 2ª série, a partir da raiz do repositório:

```bash
python3 _tikz/ferramentas/criar.py validar \
  _tikz/quimica/2serie/equilibrio-quimico/manifesto.json --publicado
```

Para validar todos os modelos disponíveis, execute `python3 validar-modelos.py` na raiz do repositório.
