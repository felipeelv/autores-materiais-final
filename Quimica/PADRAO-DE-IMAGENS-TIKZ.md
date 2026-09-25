# Padrão de imagens TikZ — Química

Este documento complementa `_tikz/PADRAO-DE-CONSTRUCAO.md`. Permanecem
obrigatórios o fundo transparente, a revisão a 300 px, uma pergunta visual por
PNG e a conferência da imagem dentro do capítulo.

## 1. Quando usar

Uma figura de Química deve tornar visível uma relação que a prosa ou a fórmula
isolada não mostra com clareza:

- evolução simultânea de grandezas em um gráfico;
- comparação espacial entre partículas, estruturas ou estados;
- sequência de um processo químico ou industrial;
- geometria molecular, estereoquímica ou mecanismo permitido pelo blueprint;
- montagem conceitual de um sistema, sem virar roteiro de experimento.

Tabelas continuam sendo preferidas para classificações e valores. Fórmulas
continuam no Markdown. Não criar béqueres, vidrarias ou moléculas apenas como
decoração.

## 2. Correção química

- Equações, espécies, cargas, estados físicos e proporções devem coincidir com
  o capítulo e estar quimicamente corretos.
- Contagens de partículas só representam proporções estequiométricas quando
  isso for explicitado pelo texto.
- Cor nunca identifica sozinha uma espécie: cada curva, partícula ou fluxo
  recebe rótulo, padrão de linha ou forma própria.
- Esquemas qualitativos não sugerem escala numérica. Eixos sem valores mostram
  apenas tendências.
- Equilíbrio usa setas nos dois sentidos; processo industrial usa fluxo e
  recirculação sem sugerir conversão total.
- Estruturas moleculares não podem criar ligações, ângulos ou orientações
  incompatíveis com o modelo apresentado.

## 3. Gráficos

- Eixos recebem a grandeza e a variável independente.
- Curvas que representam processos diferentes usam cor, tipo de linha e
  rótulo.
- No equilíbrio dinâmico, velocidades convergem para o mesmo valor, enquanto
  concentrações atingem patamares constantes que não precisam ser iguais.
- Linhas auxiliares são tracejadas e não competem com as curvas.
- Não repetir dentro da imagem a fórmula já exibida no Markdown.

## 4. Partículas e processos

- Partículas aparecem em quantidade mínima para comunicar a relação.
- Átomos ou espécies diferentes usam rótulos e contornos distintos.
- Diagramas de processo mostram entrada, transformação, separação, saída e
  reciclo quando esses fluxos forem conceitualmente relevantes.
- Condições como pressão, temperatura e catalisador ficam junto da etapa em que
  atuam, em rótulos curtos.
- Produto retirado e reagentes recirculados usam caminhos visualmente
  diferentes.

## 5. Vocabulário visual

O pacote `_tikz/estilos/eleve-quimica.sty` concentra as convenções:

- azul contínuo: processo direto, fluxo principal ou espécie de referência;
- laranja tracejado: processo inverso, retorno ou reciclo;
- verde: separação ou produto retirado;
- cinza tracejado: construção auxiliar;
- rótulos em `\large`, com `\normalsize` como mínimo absoluto.

## 6. Checklist

- [ ] uma relação química por PNG;
- [ ] proporções, setas e espécies conferidas;
- [ ] nenhum título, fórmula ou parágrafo duplicado na imagem;
- [ ] texto alternativo descreve a relação mostrada;
- [ ] rótulos legíveis e separados a 300 px;
- [ ] fundo transparente e canal alfa presente;
- [ ] imagem posicionada junto da explicação correspondente;
- [ ] capítulo diagramado revisado após a indexação;
- [ ] hash local igual ao arquivo publicado.
