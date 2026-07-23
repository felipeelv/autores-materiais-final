# Padrão de construção das figuras TikZ

Este documento fixa o contrato visual e editorial das figuras produzidas em
`_tikz/`. O fluxo operacional de renderização, aprovação, publicação e
indexação continua em `README.md`.

## 1. Unidade pedagógica

- Cada PNG responde a **uma pergunta visual** e ocupa o ponto do Markdown em
  que essa pergunta aparece.
- Conceitos independentes ficam em arquivos separados. Elementos não dividem
  imagem com classificação; famílias diferentes, como paralelogramos e
  trapézios, também não dividem a mesma peça.
- Uma comparação pode reunir vários casos somente quando a comparação é o
  próprio conceito — por exemplo, secante × tangente × externa — e todos os
  casos permanecem legíveis a 300 px.
- Se cada parte tiver explicação própria no texto, cada parte recebe seu PNG e
  fica junto da respectiva explicação.
- Não duplicar título, fórmula, tabela ou parágrafo já presente no Markdown.
  Dentro da imagem ficam apenas nomes, medidas, relações e marcas necessárias
  para ler o desenho.

## 2. Composição

- Fundo sempre transparente, sem cartão externo ou painéis brancos.
- Preferir composição vertical ou quase quadrada. Formato horizontal é
  reservado a uma única configuração simples.
- Desenho, rótulos e explicações ocupam faixas exclusivas.
- Nenhum texto pode tocar outro texto nem cruzar segmento, arco, seta, vértice
  ou marca de congruência.
- `\normalsize` é o tamanho mínimo; primeiro encurte o rótulo, depois aumente
  a área útil e, se ainda necessário, divida a figura. Nunca recupere espaço
  reduzindo a fonte.
- Cor nunca é o único código: combinar cor com rótulo, seta, marca, espessura
  ou tipo de linha.

## 3. Escala real de aprovação

Toda figura é revisada no tamanho original e em uma cópia com **300 px de
largura sobre fundo branco**. No macOS:

```bash
sips --resampleWidth 300 build/fig-01-exemplo.png \
  --out /tmp/fig-01-exemplo-300px.png
sips -s format jpeg /tmp/fig-01-exemplo-300px.png \
  --out /tmp/fig-01-exemplo-300px-branco.jpg
```

Usar `--resampleWidth`, nunca `-Z`: a altura da figura não pode reduzir a
largura usada no teste. DPI alto melhora definição, mas não corrige texto
pequeno, excesso de conteúdo ou sobreposição.

## 4. Fonte, nome e localização

- Um documento usa um `figuras.tex` multipágina e um `manifesto.json`.
- Cada ambiente `tikzpicture` corresponde a um PNG e a uma entrada do
  manifesto.
- O nome segue `fig-NN-descricao-curta.png`, sem acentos e sem termos vagos.
- O texto alternativo descreve a relação pedagógica, não apenas enumera
  objetos visíveis.
- O bloco de imagem fica imediatamente após a definição, lista, tabela ou
  frase que o introduz. Não concentrar imagens no início ou no fim da aula.
- O repositório público recebe somente os PNGs vigentes. Arquivo substituído é
  retirado após a nova versão ser publicada e validada; o histórico do GitHub
  preserva a recuperação.

## 5. Critério de divisão

Antes de renderizar, responder em ordem:

1. A imagem responde a uma única pergunta visual?
2. Todas as partes pertencem ao mesmo trecho do Markdown?
3. A comparação entre as partes é indispensável?
4. A prévia a 300 px mantém rótulos e marcas legíveis e separados?

Se alguma resposta for “não”, dividir a figura. A divisão correta aumenta a
quantidade de PNGs, mas reduz a altura de cada peça e melhora a leitura no
material em colunas.

## 6. Checklist de aprovação

- [ ] canal alfa presente e fundo realmente transparente;
- [ ] uma pergunta visual por PNG;
- [ ] posição correta no Markdown;
- [ ] notação e medidas iguais às do capítulo;
- [ ] nenhum texto ou traço sobreposto na prévia de 300 px;
- [ ] fonte mínima `\normalsize`;
- [ ] sem título, fórmula ou explicação redundante;
- [ ] texto alternativo idêntico ao manifesto;
- [ ] hash local igual ao arquivo público;
- [ ] somente PNGs vigentes no repositório público.
