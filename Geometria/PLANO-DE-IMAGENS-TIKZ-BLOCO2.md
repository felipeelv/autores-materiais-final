# Plano de imagens TikZ — Geometria · 3º bimestre · Bloco 2

Plano visual dos sete capítulos do bloco 2 e do Capítulo 2 da 3ª série, pré-requisito do bloco 1 que foi identificado como ausente durante a produção. O contrato obrigatório permanece em `../_tikz/PADRAO-DE-CONSTRUCAO.md`.

## Escopo fechado

| Ano/série | Capítulo | Aulas | Figuras |
|---|---|---:|---:|
| 6º ano | Área de figuras planas | 3 | 6 |
| 7º ano | Área e perímetro | 3 | 7 |
| 8º ano | Áreas de figuras planas | 3 | 6 |
| 9º ano | Geometria espacial e representações | 3 | 6 |
| 1ª série | Áreas de figuras planas | 6 | 13 |
| 2ª série | Cones | 6 | 10 |
| 3ª série · pré-requisito | Parábola: definição e equações reduzidas | 2 | 4 |
| 3ª série | Parábola e reconhecimento de cônicas | 6 | 8 |
| **Total** | **8 capítulos** | **32** | **60** |

Das 60 figuras, 56 pertencem propriamente ao bloco 2 e 4 recompõem o capítulo introdutório de parábola do bloco 1. Fórmulas, tabelas e cálculos algébricos que já são claros no Markdown não viram imagem.

## 6º ano — Área de figuras planas

Pasta: `_tikz/geometria/6ano/area-de-figuras-planas/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-area-e-perimetro-no-retangulo` | O que pertence ao contorno e o que pertence à superfície? Retângulo com borda marcada e interior quadriculado. | após a tabela de 1.1 |
| 2 | `fig-02-unidades-quadradas-no-retangulo-e-quadrado` | Por que se multiplicam linhas e colunas? Retângulo e quadrado preenchidos por unidades quadradas. | após as duas fórmulas de 1.2 |
| 3 | `fig-03-recomposicao-do-paralelogramo` | Por que a inclinação não muda a área? Triângulo recortado e transladado para formar retângulo. | após `A=b\cdot h` em 2.1 |
| 4 | `fig-04-triangulo-metade-do-paralelogramo` | Por que aparece o fator 1/2? Duas cópias congruentes do triângulo formando paralelogramo. | após `A=\frac{b\cdot h}{2}` em 2.2 |
| 5 | `fig-05-duplicacao-do-trapezio` | De onde vem a soma das bases? Dois trapézios invertidos formando paralelogramo de base `B+b`. | após a fórmula em 3.1 |
| 6 | `fig-06-malha-e-decomposicao-de-area` | Como aproximar uma figura irregular? Malha com quadrados inteiros, partes complementares e decomposição simples. | após a lista de 3.2 |

## 7º ano — Área e perímetro

Pasta: `_tikz/geometria/7ano/area-e-perimetro/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-mesmo-perimetro-areas-diferentes` | Como duas figuras de perímetro 20 m ocupam áreas distintas? Retângulo `1×9` e quadrado `5×5`, com contornos e áreas indicados. | após o último parágrafo de 1.1 |
| 2 | `fig-02-recomposicao-do-paralelogramo` | Como o paralelogramo vira retângulo sem perder área? Recorte lateral e translação. | junto da relação visual do paralelogramo em 2.1 |
| 3 | `fig-03-losango-em-quatro-triangulos` | Por que as diagonais determinam a área do losango? Diagonais perpendiculares dividindo-o em quatro triângulos. | junto da relação visual do losango em 2.1 |
| 4 | `fig-04-duplicacao-do-trapezio` | Por que se usa a média das bases? Duas cópias formando paralelogramo de base `B+b`. | junto da relação visual do trapézio em 2.1 |
| 5 | `fig-05-dois-triangulos-formam-paralelogramo` | Por que a área triangular é metade? Duas cópias congruentes com base e altura correspondentes. | após a fórmula em 2.2 |
| 6 | `fig-06-circulo-reorganizado-em-quase-retangulo` | Como os setores justificam `A=\pi r^2`? Setores alternados aproximando retângulo de base `\pi r` e altura `r`. | após a dedução em 3.1 |
| 7 | `fig-07-composicao-e-subtracao-de-areas` | Quando somar partes e quando retirar um vazio? Mesma figura composta resolvida pelos dois caminhos. | após a lista de 3.2 |

As três frases-âncora de 2.1 já separam paralelogramo, losango e trapézio, evitando imagens consecutivas sem texto intermediário.

## 8º ano — Áreas de figuras planas

Pasta: `_tikz/geometria/8ano/areas-de-figuras-planas/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-altura-no-paralelogramo-e-trapezio` | Qual medida é a altura? Comparação vertical de altura perpendicular e lado inclinado nas duas figuras. | após a primeira frase posterior à tabela em 1.1 |
| 2 | `fig-02-diagonais-do-losango` | Quais medidas entram na fórmula do losango? Diagonais `D` e `d`, com interseção perpendicular. | após a segunda frase posterior à tabela em 1.1 |
| 3 | `fig-03-triangulo-metade-do-paralelogramo` | Como duas cópias justificam a fórmula? Triângulos congruentes compondo paralelogramo. | após a fórmula em 2.1 |
| 4 | `fig-04-tres-pares-de-base-e-altura` | Como a mesma área usa três pares diferentes? Um triângulo com as três bases e alturas, incluindo altura externa no caso obtuso. | após o parágrafo sobre bases e alturas em 2.1 |
| 5 | `fig-05-triangulo-na-malha-quadriculada` | Como conferir a área por contagem? Triângulo na malha dentro de um retângulo complementar. | após o parágrafo da malha em 2.1 |
| 6 | `fig-06-duas-decomposicoes-da-sala-em-l` | Como somar partes ou subtrair o recorte? Planta `8×6` com vazio `3×2` resolvida pelas duas divisões. | após as duas expressões de 3.1 |

## 9º ano — Geometria espacial e representações

Pasta: `_tikz/geometria/9ano/geometria-espacial-e-representacoes/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-posicoes-entre-retas-no-espaco` | Como distinguir paralelas, concorrentes e reversas? Três configurações espaciais com indicação de coplanaridade. | após as frases sobre retas em 1.1 |
| 2 | `fig-02-posicoes-entre-reta-e-plano` | Como uma reta se relaciona com um plano? Casos contida, paralela e secante. | após a frase sobre reta e plano em 1.1 |
| 3 | `fig-03-posicoes-entre-planos` | Como dois planos podem se relacionar? Casos paralelos, secantes e coincidentes. | após a frase sobre planos em 1.1 |
| 4 | `fig-04-elementos-de-um-poliedro` | O que são vértice, aresta e face? Cubo com um exemplo de cada elemento destacado por marca e rótulo. | após a definição de poliedro em 1.1 |
| 5 | `fig-05-objeto-e-tres-vistas-ortogonais` | Como as três projeções compartilham dimensões? Peça em perspectiva ligada às vistas frontal, lateral e superior. | após a tabela de 2.1 |
| 6 | `fig-06-perspectiva-e-arestas-ocultas` | Como uma perspectiva indica profundidade e invisibilidade? Peça em cavaleira com linhas contínuas e tracejadas. | após o último parágrafo de 2.2 |

A aula 3 não recebe TikZ: as potências de dez e conversões já são mais legíveis nas tabelas e fórmulas do próprio Markdown.

## 1ª série — Áreas de figuras planas

Pasta: `_tikz/geometria/1serie/areas-de-figuras-planas/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-teorema-de-pick-na-malha` | Quais pontos contam como interiores e de fronteira? Polígono de rede com `I=8` e `B=10` marcados de modos distintos. | após a fórmula de Pick em 1.2 |
| 2 | `fig-02-demonstracao-da-area-do-paralelogramo` | Como o recorte transforma o paralelogramo em retângulo? Sequência antes, deslocamento e depois. | após `A=b\cdot h` em 2.1 |
| 3 | `fig-03-altura-interna-e-externa-no-paralelogramo` | Por que a fórmula vale quando o pé da altura cai fora? Dois paralelogramos com distâncias perpendiculares equivalentes. | após o último parágrafo de 2.1 |
| 4 | `fig-04-duas-copias-do-triangulo` | Por que o triângulo ocupa metade? Duas cópias formando paralelogramo. | após a fórmula em 3.1 |
| 5 | `fig-05-tres-pares-de-base-e-altura` | Como as três escolhas preservam a área? Mesmo triângulo com cada par base-altura destacado separadamente. | após o segundo parágrafo de 3.1 |
| 6 | `fig-06-altura-do-triangulo-equilatero` | De onde vem `\ell\sqrt3/2`? Equilátero dividido em dois triângulos retângulos, com hipotenusa `\ell` e cateto `\ell/2`. | após a fórmula da altura em 3.2 |
| 7 | `fig-07-losango-em-quatro-triangulos` | Como as meias-diagonais geram a área? Quatro triângulos retângulos com `D/2` e `d/2`. | após a dedução em 4.1 |
| 8 | `fig-08-duplicacao-do-trapezio` | Como duas cópias formam base `B+b`? Trapézios invertidos compondo paralelogramo. | após a primeira dedução de 5.1 |
| 9 | `fig-09-trapezio-decomposto-em-triangulos` | Como a dedução alternativa soma dois triângulos? Diagonal, bases `B` e `b` e altura comum `h`. | após a segunda dedução de 5.1 |
| 10 | `fig-10-poligono-regular-em-triangulos` | Por que aparecem perímetro e apótema? Polígono regular dividido em triângulos centrais, com `a` e `\ell`. | após `A=\frac{p\cdot a}{2}` em 6.1 |
| 11 | `fig-11-poligonos-aproximando-o-circulo` | Como o polígono tende ao círculo? Sequência de polígonos com mais lados, apótema tendendo ao raio. | após a dedução de `A=\pi r^2` em 6.1 |
| 12 | `fig-12-setor-e-segmento-circular` | Como o segmento resulta de uma subtração? Mesmo arco delimitando setor e segmento, com triângulo intermediário. | após a tabela de regiões em 6.1 |
| 13 | `fig-13-coroa-circular` | Qual região corresponde a `\pi(R^2-r^2)`? Dois círculos concêntricos com raios `R` e `r`, somente a faixa destacada. | antes do exemplo de 6.2 |

## 2ª série — Cones

Pasta: `_tikz/geometria/2serie/cones/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-geracao-do-cone-por-rotacao` | Como o triângulo retângulo gera o cone? Triângulo, eixo de rotação e posição varrida pela hipotenusa. | após a abertura de 1.1 |
| 2 | `fig-02-elementos-do-cone` | Onde ficam `r`, `h`, `g`, eixo, vértice e base? Cone reto com secção axial visível. | após a lista de elementos em 1.1 |
| 3 | `fig-03-cone-reto-e-obliquo` | O que muda quando o eixo deixa de ser perpendicular? Comparação vertical com eixo e altura diferenciados por marca. | após as duas definições em 2.1 |
| 4 | `fig-04-seccao-meridiana-do-cone-equilatero` | Por que `g=2r` e `h=r\sqrt3`? Secção equilátera de base `2r`, dividida pela altura. | após as duas relações em 2.1 |
| 5 | `fig-05-planificacao-da-area-lateral` | Por que a lateral vira setor de raio `g`? Cone aberto ligado ao setor, com arco igual a `2\pi r`. | após a dedução de `A_L=\pi rg` em 3.1 |
| 6 | `fig-06-planificacao-da-area-total` | Quais peças compõem a superfície total? Setor lateral e círculo da base separados, sem painel externo. | após `A_T=\pi r(g+r)` em 4.1 |
| 7 | `fig-07-tres-cones-preenchem-um-cilindro` | Por que o volume tem fator 1/3? Cilindro e três porções cônicas equivalentes, com mesma base e altura. | após o primeiro parágrafo de 5.1 |
| 8 | `fig-08-elementos-do-tronco-de-cone` | Onde ficam `R`, `r`, `h` e `g`? Tronco reto com duas bases e eixo. | após a definição em 6.1 |
| 9 | `fig-09-triangulo-gerador-do-tronco` | Por que aparece `R-r`? Secção lateral isolando triângulo retângulo de catetos `h` e `R-r`. | após a relação pitagórica de 6.1 |
| 10 | `fig-10-tronco-como-cone-recortado` | Como o tronco se relaciona ao cone completo? Cone, secção paralela e pequeno cone retirado, com correspondência de lados. | após o último parágrafo de 6.1 |

## 3ª série — Parábola: definição e equações reduzidas

Pasta: `_tikz/geometria/3serie/parabola-definicao-e-equacoes-reduzidas/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-definicao-por-foco-e-diretriz` | Por que `PF=d(P,d)`? Ponto `P`, foco, diretriz, perpendicular e segmentos de mesma marca. | após a igualdade em 1.1 |
| 2 | `fig-02-elementos-da-parabola` | Onde ficam foco, vértice, diretriz, eixo e parâmetro `p`? Parábola vertical com todos os elementos separados. | após o parágrafo dos elementos em 1.1 |
| 3 | `fig-03-parabolas-verticais` | Como o sinal orienta as formas `x²=4py`? Casos para cima e para baixo, com focos e diretrizes. | após a frase-âncora das formas verticais em 2.1 |
| 4 | `fig-04-parabolas-horizontais` | Como o sinal orienta as formas `y²=4px`? Casos para direita e esquerda, com focos e diretrizes. | após a frase-âncora das formas horizontais em 2.1 |

As duas frases-âncora de 2.1 já separam as famílias vertical e horizontal, evitando imagens sem transição depois da tabela.

## 3ª série — Parábola e reconhecimento de cônicas

Pasta: `_tikz/geometria/3serie/parabola-e-reconhecimento-de-conicas/`

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-reflexao-em-antena-e-farol` | Como a propriedade reflexiva funciona nos dois sentidos? Antena concentrando raios e farol emitindo raios paralelos, em composição vertical. | após o primeiro parágrafo de 1.1 |
| 2 | `fig-02-trajetoria-ideal-e-com-resistencia` | Quando a trajetória é parábola exata? Comparação entre curva ideal e trajetória alterada pelo ar. | após o segundo parágrafo de 1.1 |
| 3 | `fig-03-medidas-de-uma-antena-parabolica` | Onde medir `D`, `h` e `p`? Secção da antena com vértice, eixo e receptor no foco. | após a fórmula do foco em 1.1 |
| 4 | `fig-04-conica-alinhada-e-rotacionada` | O que o termo `Bxy` sinaliza? Mesma elipse com eixos alinhados e rotacionados em relação ao sistema cartesiano. | após o segundo parágrafo de 2.1 |
| 5 | `fig-05-continuum-e-discriminante-das-conicas` | Como o sinal de `\Delta` acompanha a mudança de forma? Elipse, parábola e hipérbole em sequência, com os três sinais. | após o parágrafo de Poncelet em 3.1 |
| 6 | `fig-06-circunferencia-e-elipse` | Como reconhecer visualmente o caso `A=C`? Circunferência e elipse de eixos diferentes, na mesma escala. | após a primeira frase sobre o caso elíptico em 4.1 |
| 7 | `fig-07-casos-degenerados-de-conicas` | Que formas podem substituir uma cônica regular? Ponto, par de retas e reta dupla, em três peças verticais simples. | após a menção aos casos degenerados em 4.1 |
| 8 | `fig-08-translacao-de-uma-hiperbole` | O que muda numa translação? Hipérbole na origem e cópia com centro `(h,k)`, ligadas pelo vetor e com assíntotas preservadas. | após os parágrafos de 6.1 |

As aulas 2, 5 e 6 mantêm os passos algébricos no Markdown. TikZ será usado apenas para a geometria que as expressões escondem, não para converter contas em imagem.

## Ordem de execução concluída

1. Fundamental II: 25 figuras em quatro documentos;
2. 1ª série: 13 figuras;
3. 2ª série: 10 figuras;
4. 3ª série: 12 figuras em dois documentos.

Cada capítulo passou pelo ciclo completo: manifesto e fonte privados, marcadores, renderização transparente, revisão no original e a 300 px sobre branco, aprovação, publicação em commit próprio, indexação, validação dos hashes e atualização da cópia oficial do Google Drive.

## Resultado

- [x] 25 figuras do Fundamental II;
- [x] 13 figuras da 1ª série;
- [x] 10 figuras da 2ª série;
- [x] 12 figuras da 3ª série;
- [x] 60 PNGs transparentes publicados em oito commits;
- [x] oito Markdown indexados, validados e sincronizados no Google Drive;
- [x] repositório público auditado com 111 PNGs acumulados e nenhum arquivo privado.

## Checkpoint de publicação

| Ano/série | Capítulo | PNGs | Commit público |
|---|---|---:|---|
| 6º ano | Área de figuras planas | 6 | `aa494bd59b159af92efc55a6b232fe525c89d56d` |
| 7º ano | Área e perímetro | 7 | `8d4b2c462ff20696e7687269458e49f45d3f2636` |
| 8º ano | Áreas de figuras planas | 6 | `bc449b5a2623fb16ae62a59aa3bde80180f000b0` |
| 9º ano | Geometria espacial e representações | 6 | `c19b60f726a803a0640ce1c4efc0732d8403028d` |
| 1ª série | Áreas de figuras planas | 13 | `f6909aaaf83bd8451bdb70d36bdbd10754416665` |
| 2ª série | Cones | 10 | `91280df1a49efd6f1263bb5b527675bdc40521e4` |
| 3ª série | Parábola: definição e equações reduzidas | 4 | `e74683713cc205aa327f4ff065fc6751227d6a77` |
| 3ª série | Parábola e reconhecimento de cônicas | 8 | `2fdcd844d6a909e73c4204a99445dd7d55535447` |
| **Total desta etapa** | **8 capítulos** | **60** | **8 commits** |

Checkpoint confirmado em **22/07/2026**: 15 manifestos, 111 figuras aprovadas e 111 versões publicadas. As 15 cópias oficiais no Google Drive contêm exatamente 111 referências de imagem.
