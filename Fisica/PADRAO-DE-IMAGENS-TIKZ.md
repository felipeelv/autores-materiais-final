# Padrão de imagens TikZ — Física

Este documento complementa o contrato geral de `_tikz/PADRAO-DE-CONSTRUCAO.md`.
As regras gerais de transparência, legibilidade a 300 px, uma pergunta visual
por PNG e posição junto ao texto continuam obrigatórias.

## 1. Função pedagógica

Uma figura de Física deve tornar visível uma relação que o texto sozinho
esconde: interação, direção, sentido, trajetória, decomposição, campo,
propagação ou transformação. Fórmulas, contas, tabelas e definições já claras
no Markdown não viram imagem.

- Diagrama físico e diagrama de corpo livre são peças distintas quando
  respondem a perguntas diferentes.
- Uma sequência pode compartilhar o PNG somente quando a mudança entre os
  estados é o próprio conceito.
- Ilustrações decorativas, cenas realistas e retratos históricos ficam fora do
  TikZ.
- Medidas e proporções só parecem quantitativas quando o conteúdo fornece
  valores. Nos demais casos, indicar `esquema sem escala` quando houver risco
  de interpretação literal.

## 2. Vocabulário visual

| Elemento | Convenção |
|---|---|
| corpo ou sistema | contorno azul e preenchimento azul-claro |
| superfície, trajetória e estrutura | cinza contínuo |
| força | seta laranja contínua, sempre rotulada |
| componente de força | seta laranja tracejada, sempre rotulada |
| velocidade ou deslocamento | seta azul contínua, sempre rotulada |
| eixo, normal geométrica e construção | cinza fino ou tracejado |
| campo | linha azul com seta incorporada e densidade moderada |
| raio luminoso | azul contínuo com seta de propagação |
| prolongamento virtual | cinza tracejado |
| medida ou ângulo em destaque | laranja, acompanhado de símbolo ou marca |

Cor nunca é o único código. Sentido aparece na ponta da seta; tipo de grandeza,
no rótulo; construção auxiliar, no tracejado.

## 3. Vetores e diagramas de corpo livre

- Toda força recebe notação vetorial: `\vec P`, `\vec N`, `\vec T`,
  `\vec F_{at}` ou equivalente ao capítulo.
- No diagrama de corpo livre, as setas partem de um ponto comum que representa
  o corpo isolado. O ambiente físico não permanece desenhado.
- Em uma cena física, a força pode partir da região de contato quando isso
  ajuda a identificar a interação.
- Vetores de velocidade, aceleração ou força não ficam sobre cordas,
  superfícies, trajetórias ou contornos. Quando forem paralelos a esses
  elementos, aparecem deslocados para uma faixa externa.
- Se as setas partirem do centro do corpo, o nome do corpo fica fora do caminho
  delas. Letras como `A` e `B` nunca são atravessadas por vetores.
- O comprimento das setas só compara módulos quando essa comparação é
  explicitamente indicada. Caso contrário, prevalecem direção e sentido.
- Eixos acompanham a geometria do problema: no plano inclinado, `x` é paralelo
  e `y` é perpendicular à rampa.
- Componentes não são forças adicionais. Por isso, aparecem tracejadas e não
  coexistem sem necessidade com a seta resultante em uma composição carregada.

## 4. Movimento e trajetória

- A velocidade é tangente à trajetória no ponto representado.
- A aceleração ou resultante centrípeta aponta para o centro e deve ser
  distinguida da velocidade por rótulo, cor e orientação.
- Estados sucessivos usam a mesma escala e o mesmo referencial.
- Setas curvas indicam rotação ou sentido de percurso, nunca uma força.

## 5. Gráficos

- Eixos recebem grandeza e unidade quando houver escala quantitativa.
- Gráficos qualitativos usam apenas marcas indispensáveis e declaram a
  transição relevante.
- Não repetir a equação do Markdown dentro do gráfico.
- Pontos de mudança de regime, máximos e limites recebem marca e rótulo.
- Grade só é usada quando a leitura numérica depende dela.

## 6. Óptica, campos e circuitos

- Raios luminosos têm seta no sentido de propagação; normal geométrica e
  prolongamentos virtuais são tracejados.
- Campo elétrico ou magnético usa linhas com sentido e espaçamento legível;
  `\odot` e `\otimes` representam saída e entrada do plano com legenda local.
- Corrente convencional, polaridade e terminais são identificados por símbolo,
  não apenas por cor.
- Imagens ópticas e objetos usam seta vertical e rótulo; imagem virtual recebe
  construção tracejada.

## 7. Composição e texto

- Preferir formato vertical ou quase quadrado.
- Rótulos ficam fora das pontas das setas e não cruzam corpos, superfícies ou
  trajetórias.
- `\large` é o tamanho normal dos rótulos; `\normalsize` permanece o mínimo
  absoluto do contrato geral.
- Não incluir título, legenda longa, fórmula completa nem conclusão dentro do
  PNG.
- Comparações usam faixas verticais ou painéis sem fundo, com os casos na mesma
  escala.
- Casos empilhados reservam um corredor vazio entre o último rótulo ou vetor do
  primeiro caso e o título do seguinte. Na prévia de 300 px, esse corredor deve
  ter pelo menos 16 px.
- Rótulos, pontas de seta e linhas não relacionadas mantêm pelo menos 8 px de
  separação na prévia de 300 px.
- A figura só é considerada final depois de conferida dentro do capítulo
  diagramado, na largura real usada pelo material.

## 8. Estilo e implementação

O pacote `_tikz/estilos/eleve-fisica.sty` concentra cores e estilos semânticos.
As figuras usam `fisica figura` e, conforme o caso:

- `fisica corpo`;
- `fisica superficie`;
- `fisica forca`;
- `fisica componente`;
- `fisica movimento`;
- `fisica trajetoria`;
- `fisica eixo`;
- `fisica campo`;
- `fisica raio`;
- `fisica extensao`;
- `fisica grafico`;
- `fisica rotulo`.

Uma nova convenção só entra no pacote depois de funcionar no capítulo-piloto e
continuar legível na prévia de 300 px sobre fundo branco.

## 9. Checklist específico

- [ ] cada seta representa uma grandeza ou um movimento identificável;
- [ ] força, velocidade e construção auxiliar não podem ser confundidas;
- [ ] o diagrama de corpo livre contém apenas forças sobre o corpo isolado;
- [ ] direção, sentido e ponto de aplicação estão fisicamente corretos;
- [ ] eixos e convenções de sinal coincidem com o Markdown;
- [ ] linhas de campo, raios ou trajetórias possuem sentido quando necessário;
- [ ] comparação de módulos só é sugerida quando sustentada pelo conteúdo;
- [ ] a figura não cria uma precisão ou escala que o texto não fornece;
- [ ] rótulos e pontas de seta permanecem separados a 300 px;
- [ ] vetores não cobrem cordas, superfícies, trajetórias ou nomes de corpos;
- [ ] casos empilhados possuem corredor vazio entre si;
- [ ] capítulo diagramado foi revisado após a indexação;
- [ ] texto alternativo descreve a relação física mostrada.
