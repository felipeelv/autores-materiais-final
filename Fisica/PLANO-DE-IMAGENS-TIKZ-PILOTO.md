# Plano de imagens TikZ — Física · capítulo-piloto

## Análise do conjunto

Os 17 capítulos do 3º bimestre formam cinco famílias visuais:

| Família | Capítulos principais | Necessidades |
|---|---|---|
| forças e movimento | 6º cap. 1; 7º caps. 1–2; 9º caps. 1–2; 1ª série caps. 1–3 | vetores, DCL, trajetória, gráficos e máquinas |
| estrutura e astronomia | 6º cap. 2; 8º cap. 2 | cortes, órbitas, alinhamentos e escalas |
| ondas e óptica | 8º cap. 1; 2ª série caps. 1–2 | propagação, raios, imagens e gráficos |
| magnetismo e indução | 3ª série caps. 1–3 | campos, regra de sentido, fluxo e circuitos |
| máquinas simples | 7º cap. 3; 9º cap. 1 | forças, pontos de apoio, polias e deslocamentos |

O padrão não deve nascer de astronomia, óptica ou magnetismo: cada uma dessas
famílias possui convenções muito próprias. O núcleo compartilhado entre mais
capítulos é a representação de forças e movimento.

## Capítulo escolhido

**1ª série — Capítulo 3: Aplicações da dinâmica.**

Este capítulo é o melhor piloto porque reúne, em seis aulas:

- gráfico qualitativo com mudança de regime;
- diagrama de corpo livre;
- decomposição de vetor em eixos inclinados;
- velocidade tangencial e resultante radial;
- comparação entre posições de uma trajetória;
- corpos ligados por corda e polia.

Ele testa oito decisões reutilizáveis sem antecipar as convenções específicas
de óptica e eletromagnetismo.

## Escopo do piloto

| Ordem | ID do PNG | Pergunta visual e conteúdo | Inserção no Markdown |
|---:|---|---|---|
| 1 | `fig-01-transicao-do-atrito-estatico-ao-cinetico` | Como o atrito acompanha a força aplicada até o limite e depois passa ao regime cinético? Gráfico qualitativo com máximo estático e patamar cinético. | após o parágrafo que compara `\mu_e` e `\mu_c` em 1.1 |
| 2 | `fig-02-diagrama-de-corpo-livre-horizontal` | Quais forças atuam na caixa puxada sobre piso horizontal? Corpo isolado com peso, normal, força aplicada e atrito. | após a lista de forças em 2.1 |
| 3 | `fig-03-decomposicao-do-peso-na-rampa` | Por que surgem `P\sin\theta` e `P\cos\theta`? Bloco, eixos alinhados à rampa, peso e componentes paralela e perpendicular. | após as duas expressões das componentes em 3.1 |
| 4 | `fig-04-velocidade-e-resultante-centripeta` | Como velocidade e resultante se orientam numa trajetória circular? Velocidade tangente e força resultante apontando para o centro. | após a expressão de `F_c` em 4.1 |
| 5 | `fig-05-atrito-na-curva-plana` | Qual força aponta para o centro numa curva plana? Vista superior do carro com trajetória, velocidade tangente e atrito radial. | após a expressão de `v_{max}` em 5.1 |
| 6 | `fig-06-forcas-na-lombada-e-no-vale` | Por que a normal diminui na lombada e aumenta no vale? Comparação vertical dos dois DCLs e do sentido do centro. | após a tabela de pista vertical em 5.1 |
| 7 | `fig-07-forcas-no-topo-e-na-base-do-looping` | Como peso e normal mudam entre topo e base? Dois pontos do looping com setas dirigidas ao centro. | após a condição `N=0` em 5.2 |
| 8 | `fig-08-sistema-de-blocos-e-diagramas` | Quais forças entram na equação de cada bloco ligado? Sistema físico e dois DCLs correspondentes. | após as duas equações em 6.1 |

## Execução

- [x] Produzir e revisar localmente as oito figuras.
- [x] Conferir cada figura a 300 px sobre fundo branco.
- [x] Validar transparência, manifesto, dimensões e hashes locais.
- [x] Aprovar e publicar os oito PNGs no repositório público.
- [x] Indexar as oito URLs no Markdown oficial.
- [x] Validar os hashes públicos e o capítulo completo.
- [x] Sincronizar o Markdown final no Google Drive.
- [ ] Após a validação do padrão pelo usuário, planejar os outros 16 capítulos.

## Estado do piloto — 23/07/2026

As oito figuras estão aprovadas, publicadas e indexadas no capítulo oficial.
Após a revisão no capítulo diagramado, as figuras 6 e 8 receberam mais espaço
entre rótulos, vetores e diagramas. O conjunto vigente está no commit
`9934fd2ba023`, validado por SHA-256 e sincronizado no Google Drive. A galeria
de conferência permanece em `REVISAO-TIKZ-PILOTO.md`.
