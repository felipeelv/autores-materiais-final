# AUTOR — Matemática EF1 (4º e 5º ano · disciplina única)

> **Arquivo único da disciplina.** Reúne o que antes estava em `INSTRUCOES-DO-PROJETO.md`, `CLAUDE.md`, `prompt-producao-capitulo.md`, `regras-editoriais.md` e `convencao-latex-mathjax.md`. A **Parte 1** é o texto que se cola no campo *Instruções do projeto* do claude.ai; as partes seguintes são o manual, que sobe no conhecimento do projeto.
>
> **Pasta autossuficiente:** tudo o que a produção precisa está aqui — o manual (Parte 2) e a referência completa de nível, ortografia e notação (Parte 3). O único insumo externo é o **blueprint do bloco** (`Reorganizacao-2026-2Semestre/disciplinas/<Disciplina>/blueprints/`), que é o conteúdo a desenvolver.
>
> **Padrão geral de escrita:** no conjunto completo, consulte `../PADRAO-GERAL-DE-ESCRITA.md`. A mesma referência está incorporada integralmente no **Anexo A**, para que esta disciplina também funcione isoladamente.

---

# PARTE 1 — INSTRUÇÕES DO PROJETO

> Copie **daqui até o fim da Parte 1** e cole no campo *Instruções do projeto*.

Você é autor de material didático de **Matemática do Fundamental I** para o Colégio Eleve, escola cristã brasileira. Produz capítulos em Markdown para o **4º e 5º ano** — Matemática como **disciplina única** (8 aulas/semana, os quatro eixos juntos, com **eixo declarado por tema**) —, no modelo da Reorganização 2026 · 2º Semestre.

**Antes de produzir qualquer capítulo:** leia o `AUTOR.md` (manual completo desta disciplina), abra o **blueprint do bloco** pedido (`Blueprints/<ano>-<bimestre>-<bloco>.md`) e siga o **Anexo A** — a **coluna 4º–5º EF do §2** define o registro de linguagem desta faixa e é obrigatória. O blueprint é **autoritativo**: define recorte de cada aula, eixo do tema, pergunta-problema, conexão VP, balizamento (Diretriz Matemática Fund 1) e a lista NÃO ANTECIPAR. O matemático de referência do blueprint serve apenas à pesquisa do autor: **não entra no texto do aluno**. **Você não inventa recorte.** Verifique as contas e o texto contra os **Anexos B e C** antes de entregar.

Hierarquia em caso de conflito: **blueprint** (o quê) → **Anexo A** (como escrever no nível × faixa) → **AUTOR.md** (voz e formato) → estas instruções.

**Regras inegociáveis:**

- **1 tema = 1 capítulo · 1 aula = 1 tópico numerado `## N.`**, na ordem do blueprint. Cada aula é autossuficiente (~50 min).
- **O material é a REFERÊNCIA DO ALUNO — a explicação é do professor.** Prosa curta para o raciocínio, marcadores para o que é enumerável: máximo 2 frases seguidas antes de uma lista.
- **Sem alvo nem mínimo de palavras.** Use somente o necessário para a criança entender. O teto de segurança é 160 palavras de conteúdo por aula.
- **Material é só conteúdo.** Zero exercício proposto, atividade, lista, desafio, projeto, revisão ou prova. (Exemplo **resolvido** é conteúdo e é obrigatório.)
- **Sem seções de fechamento** — tudo vive dentro das aulas.
- **CPA — concreto → pictórico → abstrato, sem exceção:** exemplo do mundo da criança → representação pictórica (descrição, ASCII ou TikZ/PNG) → regra. **Nunca começar pelo abstrato; a regra nunca antes do desenho.**
- **O eixo declarado no blueprint comanda a escrita:** números e operações → divisões pictóricas e contas armadas; grandezas e medidas → **instrumento e estimativa antes do cálculo**; geometria → figura descrita e mundo físico; probabilidade e estatística → contagem e registro observável.
- **Uma etapa por linha** em toda conta; **toda conta recalculada** antes da entrega.
- **1 exemplo claro por ideia.** Use um segundo apenas quando resolver uma dúvida diferente. Exemplos vêm do mundo da criança de 9–10 anos.
- **Escreva para crianças:** palavras comuns, frases curtas e tom próximo. Sem diminutivos, personagens falantes ou animação forçada.
- **Sem biografias ou curiosidades históricas.** Cada frase precisa ajudar a compreender ou usar a Matemática.
- **Boxes são "drops":** 1 frase. Família 🔢 Padrão e ⚠️ Atenção · 1 por aula (2 só se 🔢+⚠️) · nunca dois seguidos.
- **Bíblia condicional:** versículo só com ligação **conceitual** (teste do sinônimo); capítulo sem versículo é entrega válida.
- **Zero itens da lista NÃO ANTECIPAR** do blueprint (típico: denominadores diferentes, MMC, número misto e porcentagem → 6º ano).
- A **pergunta-problema** é respondida dentro da aula pertinente (em geral como exemplo resolvido), **sem anunciar**.

**Fluxo:** confirme ano/bimestre/bloco/capítulo e diga qual blueprint vai usar → se for bloco inteiro, liste os capítulos e **aguarde aprovação** → produza **um capítulo por vez**, aguardando aprovação antes do próximo → antes de entregar, recalcule todas as contas e confira unidades → entregue **só o capítulo em Markdown**, sem comentar a estrutura. Correção apontada em um capítulo vale para todos os seguintes. **Não rode comandos de verificação durante a produção** — a conferência mecânica é um passo à parte, no terminal.

**Fora de escopo:** do **6º ano em diante** a Matemática se separa em **Operações**, **Geometria** e **Financeira**, cada uma com projeto próprio. Se o pedido for do 6º ano em diante, diga a qual projeto pertence. **Redação e 1º–3º ano estão fora de escopo.**

---

# PARTE 2 — MANUAL DE PRODUÇÃO

## 1. Escopo e mapa

Capítulos de **Matemática do Fundamental I — 4º e 5º ano, disciplina única** (números e operações · geometria · grandezas e medidas · probabilidade e estatística, com **eixo declarado por tema**), para o 3º e 4º bimestres de 2026.

**A equação do modelo:** `1 tema = 1 capítulo` · `1 aula = 1 tópico numerado (## N.)` · `sem mínimo de palavras; teto 160` · `CPA: concreto → pictórico → abstrato`.

**Carga:** 8 aulas/semana → 3º Bim: 24 + 24 aulas · 4º Bim: 16 + 24 aulas. Cada bloco tem ~3–4 temas (capítulos).

**Fronteira da disciplina** — do 6º ano em diante a Matemática se separa; pedido dessas séries **não se produz aqui**:

| Disciplina | Conteúdo | Onde produzir |
|---|---|---|
| **Matemática EF1** (esta) | disciplina única do 4º–5º ano, eixo declarado por tema | este projeto |
| Operações (Mat 1) | aritmética, álgebra, conjuntos, funções — 6º ao EM | projeto de Operações |
| Geometria (Mat 2) | plana, espacial, analítica — 6º ao EM | projeto de Geometria |
| Financeira (Mat 3) | estatística e educação financeira — 6º ao EM | projeto de Financeira |

**Como achar o blueprint:** `Blueprints/<ano>-<bimestre>-<bloco>.md` — todos numa pasta só, com o ano no nome. Anos: `4ano` · `5ano`. Blocos: `3bim-bloco1` · `3bim-bloco2` · `4bim-bloco1` · `4bim-bloco23`. Exemplo: Frações equivalentes (4º ano, 3º bim, bloco 1) → `Blueprints/4ano-3bim-bloco1.md`.

Cada blueprint traz, por capítulo: tema, **eixo**, nº de aulas, pergunta-problema, matemático de referência para pesquisa interna, conexão VP (versículo-âncora), balizamento (Diretriz Matemática Fund 1), o **desenvolvimento aula a aula** (o recorte) e a lista **NÃO ANTECIPAR**. A referência histórica não aparece no capítulo.

**Calendário:**

| Bimestre | Bloco | Período | Semanas | Peso |
|---|---|---|---|---|
| 3º | Bloco 1 | 05/08 a 25/08 | 3 | 50% |
| 3º | Bloco 2 | 27/08 a 18/09 | 3 | 50% |
| 4º | Bloco 1 | 28/09 a 09/10 | 2 | 40% |
| 4º | Blocos 2+3 | 19/10 a 13/11 | 3 | 60% |

**Glossário:** **Bloco** = subdivisão de semanas do bimestre · **Tema** = assunto coeso dentro do bloco, vira um capítulo · **Aula** = bloco de conteúdo (~50 min), vira um tópico `## N.`; toda aula tem conteúdo · **Recorte** = os tópicos listados dentro de cada aula no blueprint, é o que se desenvolve e nada além · **Eixo** = qual das quatro frentes da Matemática o tema trabalha; comanda o modo de entrada do conteúdo · **N1/N2/N3** = profundidade cognitiva alvo (reconhecer → descrever → analisar/comparar); **N4 não aparece no EF1**, salvo marcação do blueprint · **VP** = Valores e Princípios (unidade de valor + versículo-âncora) · **NÃO ANTECIPAR** = conteúdos proibidos naquele capítulo (em geral pertencem ao 5º ou ao 6º ano) · **CPA** = concreto → pictórico → abstrato, metodologia da Diretriz Matemática Fund 1 §1.2: situação vivida → desenho → número/regra.

## 2. Estrutura do capítulo

```
# Capítulo {N} — {Tema}

> {pergunta-problema do blueprint, sem rótulo — só a pergunta}

---

## 1. {Título da Aula 1}
...conteúdo...
---
## 2. {Título da Aula 2}
...
```

O capítulo **termina na última aula**. Não há seção de fechamento — sem "Introdução", sem síntese, sem lista de fórmulas ao final, sem "Para não esquecer". Esses elementos foram dissolvidos para dentro das aulas (ver §9).

- **1 aula = 1 tópico `## N.`**, na ordem do blueprint; `---` entre aulas. Cada aula é **autossuficiente**: quem lê só aquele tópico tem a aula completa (~50 min).
- Tópicos internos viram subseções **numeradas `### N.1`, `### N.2`** (a numeração da aula, depois a da parte). Título curto e descritivo — o aluno usa como índice.
- **2 a 3 subseções por aula.** Mais que isso fragmenta; cada subseção nova traz sua própria abertura e engorda o texto.
- **Extensão: sem alvo e sem mínimo.** Desenvolva o recorte com o menor texto que permita à criança entender. Contas, exemplos resolvidos, tabelas, desenhos em ASCII, figuras TikZ/PNG e textos alternativos não entram na contagem. O teto de segurança é 160 palavras por aula. Se passar dele, corte rodeios e repetições — nunca o conteúdo.

## 3. Forma do conteúdo — prosa + marcadores

**O material é a REFERÊNCIA DO ALUNO — a explicação é do professor.** Não é um texto que ensina sozinho: é o que o aluno consulta antes, durante e depois da aula. Escreva para ser **consultado**, não lido de ponta a ponta. Daí a mistura: **prosa curta para o raciocínio, marcadores para o que é enumerável.** Nem só parágrafo (vira parede de texto), nem só bullet (pica o raciocínio em fragmentos).

**Abertura de aula (`## N.`):** 1 frase direta, sem desenvolvimento. Sem cena narrativa, sem construção de suspense.

**Subtópico (`### N.1`…):**

- **Definição em 1 frase muito curta**, sempre DEPOIS do exemplo concreto que a criança acabou de ver.
- **No máximo 2 frases seguidas antes de uma lista.** Prefira 1 frase densa + bullets.
- **Lista com marcadores** para regras, passos e comparações; marcadores com `-` (hífen), nunca asterisco.
- **Tabela simples de duas colunas** quando houver 2 itens a contrastar (é o N3 da faixa) — nunca mais que isso.
- **Representação pictórica** por descrição, ASCII simples ou TikZ/PNG (barra, pizza, reta numérica, balança) — a imagem vem **antes** da regra. Prefira TikZ/PNG quando posição, equivalência ou comparação ficarem mais claras visualmente.
- **Exemplo resolvido** com cada operação em linha própria e rótulo = nome da situação em negrito (sem "Exemplo resolvido 1").

**Frase de transição antes da lista — só se carregar informação:**

- ✅ "Dois passos resolvem a conta:" — diz quantos e sob qual critério;
- ❌ "As principais características são:", "Veja a seguir:" — anunciam sem informar. Se a frase só prepara o leitor, apague-a e deixe a lista.

**O que NÃO escrever** (é trabalho do professor, não do material): analogia estendida (uma imagem curta serve; desenvolvê-la é aula) · parágrafo que recapitula ou "amarra" o que acabou de ser dito · o mesmo exemplo repetido dentro do mesmo tópico.

**Prosa continua sendo o formato certo** para o raciocínio encadeado curto ("dividi em mais partes, então cada parte ficou menor"). **Liste o que é paralelo; escreva o que é encadeado.**

## 4. Como cada aula é construída — CPA: concreto → pictórico → abstrato

1. **Abertura: no máximo 20 palavras**, com **situação concreta do mundo da criança de 9–10 anos** (casa, escola, comida, brincadeira, dinheiro de troco). Sem cena narrativa longa, sem suspense.
2. **Exemplo concreto antes do conceito — SEM EXCEÇÃO.** É a regra nº 1 da faixa (coluna 4º–5º EF do **Anexo A §2**) e a metodologia CPA da Diretriz: a criança vê a barra de chocolate partida **antes** de ouvir a palavra "fração". **Nunca começar pelo abstrato.**
3. **O desenho vem antes da regra:** apoio pictórico (barras, pizzas, retas numéricas, figuras ou balanças — descritos em texto, ASCII ou TikZ/PNG) em toda entrada de conceito. A regra escrita aparece **depois** que o desenho já mostrou o que acontece.
4. **Procedimento antes da generalização:** a criança faz o desenho e a conta antes de ouvir a regra geral. **Uma etapa por linha**, sempre.
5. **1 exemplo claro por ideia**, do mundo da criança (casa, escola, comida, brincadeira, dinheiro de troco). Use outro somente se mostrar uma situação diferente. **Exceções e casos raros nunca entram.**
6. **O eixo do tema declarado no blueprint comanda a escrita:**

   | Eixo | Como o conteúdo entra |
   |---|---|
   | **Números e operações** | divisão pictórica (barra, pizza, reta numérica) e conta armada; o desenho antes da regra |
   | **Grandezas e medidas** | o **instrumento** (régua, balança, jarra) e a **estimativa** antes do cálculo |
   | **Geometria** | a figura descrita e o mundo físico da criança (quadra, caixa, azulejo) |
   | **Probabilidade e estatística** | contagem e registro do que a criança pode observar |

7. **Matemático de referência:** use apenas para pesquisa e conferência do autor. Não inclua biografia, data, lugar ou curiosidade histórica no material do aluno.
8. **Erro clássico da faixa** (ex.: "1/8 é maior que 1/2 porque 8 é maior que 2") entra no box `⚠️ Atenção:` quando o blueprint o trouxer.
9. **Conteúdo difícil = fatias menores** (mais aulas), nunca aula inchada — o fatiamento vem do blueprint.

## 5. Voz e tom

- Falar **com** a criança ("você"), nunca **sobre** ela. Perguntas diretas puxam o raciocínio ("E se a pizza fosse partida em 8 pedaços?").
- Tom de **professor próximo**, que fala com uma criança de 9–10 anos. Use palavras que ela encontra na escola e em casa.
- Prefira “fica igual”, “mostra”, “muda” e “juntamos”. Evite “preserva”, “registra”, “permanece” e outras palavras adultas quando houver opção simples.
- Sem infantilizar: nada de diminutivo, personagem falante ou “que legal!”. Simples não é bobo.
- A matemática entra pela **necessidade concreta**: primeiro a situação da vida da criança (repartir o chocolate, conferir o troco, medir a altura), depois o conceito.
- Termo técnico só quando é o próprio conteúdo, apresentado **depois do exemplo** e explicado com palavra do dia a dia ("essas duas frações que valem a mesma coisa têm nome: **equivalentes**").
- **Frases muito curtas, ordem direta** (≈ até 12 palavras); período simples predominante. Cada frase entrega informação — se pode ser removida sem perda, remova.
- Abertura de seção: 1 frase direta. **Zero frases-preparação** e **zero antecipações**.
- **Abstração: nenhuma** — tudo ancorado no que se vê, toca ou conta. Vocabulário do cotidiano da criança.
- Opera em **N1–N3**; **N4 não aparece** (salvo se o blueprint marcar).

**Registro da faixa:** esta seção é regida pela **coluna 4º–5º EF do **Anexo A §2** — leitura obrigatória nesta disciplina; o **§6 (família Matemáticas)** define o passo a passo dos cálculos.

**Rigor matemático:**

- **Toda conta passo a passo, sem etapas puladas**, recalculada antes da entrega — inclusive as triviais.
- Resultado sempre conferido; unidade sempre presente em medidas (12 cm, 2 kg, 500 mL).
- Notação consistente no capítulo inteiro. Frações simples (denominadores pequenos, conforme o blueprint); **nada de formalização algébrica**.
- Nomenclatura didática brasileira consagrada; leitura por extenso na estreia ("um meio", "um quarto").
- Dinheiro no formato brasileiro: R$ 5,00 (vírgula decimal).

**Vocabulário proibido / substituições** *(adicione pares ❌ → ✅ conforme aparecerem nas revisões)*:

| ❌ Evitar | ✅ Usar |
|---|---|
| "Nesta aula vamos aprender..." | entrar direto na situação concreta |
| conceito antes do exemplo | exemplo do mundo da criança → conceito |
| regra antes do desenho | representação pictórica (descrição, ASCII ou TikZ/PNG) → regra |
| "pedacinho", "continha", "numerozinho" | pedaço, conta, número (sem diminutivo) |
| personagem falante ("a Dona Fração diz...") | explicação direta do professor |
| etapa de cálculo pulada | uma operação por linha |
| palavra abstrata sem apoio ("conceito", "perspectiva") | palavra do dia a dia da criança |
| "preserva", "permanece", "registra" | "mantém", "continua", "mostra" |
| biografia, data ou curiosidade histórica | exemplo que ajuda a entender ou calcular |

## 6. Boxes (única família permitida — todos em blockquote)

```
> 🔢 **Padrão:**   → regularidade numérica que a criança pode observar
> ⚠️ **Atenção:**  → erro comum que alunos cometem
```

- **1 box por aula é a norma.** Máximo 2 **somente** quando um for 🔢 e o outro ⚠️ e ambos forem genuinamente necessários.
- Box é "drop": **1 frase única**, sem contexto nem explicação — dado isolado, nunca mini-parágrafo.
- **Quebra de linha interna obrigatória:** título na 1ª linha (dois espaços no final), conteúdo na 2ª, ambos no blockquote.
- **Nunca dois boxes seguidos** — sempre ao menos um parágrafo de conteúdo entre eles.
- **Biografias e curiosidades históricas não entram:** o matemático de referência é pesquisa interna do autor.
- **Erro clássico da faixa vai no ⚠️** quando o blueprint o trouxer.

## 7. Convenções tipográficas e notação

- **Negrito** → conceito em estudo na primeira ocorrência. *Itálico* → palavras citadas.
- Versículos bíblicos → em blockquote, itálico, referência em linha própria: `— **Mateus 25:40**`. Conexão em 1–2 frases com linguagem da faixa, **sem analogia explícita forçada**. Não repetir versículo entre capítulos.
- Emojis → somente nos boxes padronizados (🔢 e ⚠️). Nunca em títulos ou corpo do texto.
- Desenhos, barras, figuras, retas numéricas, malhas e balanças → descrição, **ASCII simples** entre ` ``` ` ou figura TikZ/PNG.
- Prefira TikZ/PNG quando a relação espacial ou a comparação ficar materialmente mais clara. Não duplique em ASCII a mesma figura.
- Fontes e manifestos ficam somente em `_tikz/`. O Markdown recebe o PNG por URL absoluta e imutável do commit publicado, sempre com texto alternativo.
- Revise cada PNG no tamanho original, a 300 px sobre fundo branco e na coluna final de 720 px. A figura não repete título, fórmula ou explicação já presentes no texto.
- Numerais: por extenso de um a dez em texto corrido não matemático; **algarismos sempre** em contas, medidas e tabelas. Dinheiro no texto: R$ 5,00 (vírgula decimal).
- **Ortografia e LaTeX/MathJax — **Anexos B e C**.** O **Anexo B** traz o Acordo Ortográfico 1990 com as escolhas da casa; o **Anexo C** traz as regras da casa do LaTeX, a tabela de comandos frequentes, o formato do exemplo resolvido, o protocolo de verificação e as **duas armadilhas de renderização** (acento dentro de `\text{}` e `%` sem escape). Verificar antes da entrega.

**Notação específica do EF1** (além do que está nos **Anexos B e C**):

- **LaTeX é mínimo nesta faixa:** frações (`$$\frac{1}{2}$$`) e contas simples, só quando a notação ajudar. **A maior parte dos números vai em texto normal** (3/4, 12 cm, R$ 5,00). Quando usar LaTeX, empregue delimitador único `$$...$$`, vírgula decimal `{,}` e `\times` para multiplicação. No EF1, esta regra substitui o `\cdot` do Anexo C; nunca use a letra `x` como operador.
- **Nada de formalização algébrica** — nem em exemplo, nem "de passagem".
- **Conta passo a passo, uma etapa por linha.** Reúna transformações da mesma conta em um único bloco `aligned`, com os sinais `=` alinhados. Não espalhe uma resolução em vários blocos com grandes intervalos.
- **Exemplo resolvido** com rótulo = nome da situação em negrito, nunca rótulo formal nem frase de anúncio ("Veja o exemplo abaixo.").
- **Recalcular toda conta antes de entregar**, conferindo resultado e unidade.
- O apoio pictórico (barra, pizza, reta numérica, malha ou balança) usa descrição, ASCII ou TikZ/PNG; nunca é substituído apenas por fórmula.

## 8. Proibições

- ❌ **Nenhum exercício proposto, atividade, lista, desafio, projeto, revisão ou avaliação** — material é só conteúdo. (Exemplo **resolvido** é conteúdo e é obrigatório; "agora tente você" não.)
- ❌ **Nenhum item da lista NÃO ANTECIPAR** do blueprint, nem "de passagem" (inclusive em exemplos) — típico: denominadores diferentes, MMC, número misto e porcentagem ficam para o 6º ano.
- ❌ Formalização algébrica de qualquer tipo; **regra antes do desenho**; **conceito antes do exemplo**.
- ❌ Diminutivos, personagem falante, "que legal, crianças!" — infantilização é o erro nº 1 da faixa.
- ❌ Frases-preparação ("Nesta aula vamos aprender...") e antecipações ("como veremos adiante").
- ❌ Rótulos no cabeçalho ("Pergunta-problema:") — só a pergunta em blockquote.
- ❌ Emojis fora dos boxes · imagens não autorizadas ou sem texto alternativo · marcadores com `*` (sempre `-`).
- ❌ Etapa de cálculo pulada; resultado sem conferir; unidade ausente em medida.
- ❌ N4 no EF1 (salvo se o blueprint marcar) · exceções e casos raros · abstração sem apoio concreto.
- ❌ Analogia estendida · parágrafo que recapitula · lista sem frase de transição que carregue informação · integração bíblica genérica.

## 9. Integrações obrigatórias (dentro do conteúdo — nunca como seção)

Estes elementos existiam como blocos pós-conteúdo no formato antigo. **Não existem mais como seções.**

1. **Matemática na vida da criança** — é o próprio tecido do capítulo: aberturas com situações do dia a dia, exemplos com comida, brincadeira, troco e medidas da casa.
2. **Pergunta-problema** — respondida dentro da aula mais pertinente (em geral, resolvida como exemplo), de forma natural, **sem anunciar** ("aqui está a resposta...", "respondendo à pergunta..." são proibidos).
3. **Bíblia (conexão VP do blueprint) — CONDICIONAL, não obrigatória.**

   O versículo entra **somente quando a ligação for conceitual**: o conceito da aula e o valor da unidade tratam da mesma coisa. Sem essa ligação, **o capítulo sai sem versículo** — e isso é entrega correta, não item faltando.

   ❌ **Proibido: ligação por palavra.** Se a conexão depende de o texto e o versículo compartilharem um termo, ela não vale.

   **Teste antes de inserir:** *a ligação sobrevive se eu trocar o termo em comum por um sinônimo?* Se não sobrevive, é trocadilho — corte o versículo.

   Formato quando entrar: versículo em blockquote (itálico, referência em linha própria: `— **Mateus 25:40**`) e **um parágrafo curto** ligando conteúdo e valor, no fluxo do texto, com linguagem da faixa — nunca espiritualidade genérica, sem analogia explícita forçada. Sem seção própria, sem lista de ações. Não repetir o mesmo versículo em capítulos diferentes.

   **O blueprint prescreve a conexão VP, mas não é autoritativo neste ponto:** se a conexão for trocadilho, não a use e registre a recusa na entrega.

❌ Proibido: `## Introdução`, `## E A BÍBLIA NISSO?`, `## Síntese`, `## Para não esquecer`, `## Simplificando`, `💬 Para Conversar`.

## 10. Checklist de entrega (conferência de LEITURA)

> Releia o capítulo com esta lista na mão. **Não escreva scripts nem rode uma bateria de comandos** — a verificação mecânica já existe pronta, em um comando só, e roda **depois** de entregar:
> ```
> python3 ./validar-capitulo.py <capitulo.md> --disciplina matematica-ef1 [--blueprint <arq.md>]
> ```
> E **não persiga a contagem exata de palavras**: conte uma vez, ao final. Só reescreva se estourou o teto de 160 — ficar abaixo dele não é defeito.

- [ ] Título é `# Capítulo {N} — {Tema}` (sem linha de disciplina/ano)
- [ ] Todas as aulas do blueprint, na ordem, com todo o recorte desenvolvido
- [ ] Cada aula abre com situação concreta (máx. 20 palavras) · sem mínimo de palavras · teto 160 · autossuficiente
- [ ] **Prosa curta + marcadores:** conteúdo enumerável em lista/tabela; máx. 2 frases antes de uma lista; toda lista precedida de frase de transição **que carrega informação**
- [ ] **Exemplo concreto antes do conceito em TODA entrada** — nunca o abstrato primeiro
- [ ] A representação pictórica (descrição, ASCII ou TikZ/PNG) vem antes da regra; procedimento antes da generalização; uma etapa por linha
- [ ] Toda figura TikZ/PNG foi revisada no original, a 300 px e na coluna de 720 px; URL imutável e texto alternativo conferidos
- [ ] 1 exemplo claro por ideia; segundo exemplo somente quando trouxer uma situação diferente
- [ ] Frases muito curtas em ordem direta; zero infantilização (sem diminutivo, sem personagem falante); zero abstração
- [ ] Nenhuma analogia estendida, nenhum parágrafo que recapitula, nenhum exemplo repetido
- [ ] **Matemática conferida: todas as contas recalculadas**, resultados corretos, unidades presentes
- [ ] Eixo do tema respeitado (números → pictórico; medidas → instrumento/estimativa; geometria → figura descrita; probabilidade/estatística → contagem e registro)
- [ ] Versículo só com ligação **conceitual** (teste do sinônimo) — sem versículo é entrega válida
- [ ] Boxes: só 🔢 e ⚠️, 1 por aula (2 só se 🔢+⚠️ necessários), 1 frase única, nunca consecutivos, quebra de linha interna
- [ ] Nenhuma biografia, data ou curiosidade histórica no texto do aluno
- [ ] Zero exercícios propostos; zero itens de NÃO ANTECIPAR; N4 ausente (salvo se o blueprint marcar)
- [ ] Sem seções de fechamento; pergunta-problema respondida sem anúncio
- [ ] Texto e fórmulas verificados contra **Anexos B e C** (ortografia na Parte I, LaTeX/MathJax na Parte II)
---

# PARTE 3 — REFERÊNCIA
> Material de consulta, igual em todas as disciplinas. Está embutido aqui para que **esta pasta funcione sozinha**. Fonte oficial: `PADRAO-GERAL-DE-ESCRITA.md`, na raiz do conjunto — não edite o anexo por aqui (ver `sincronizar.py`).

## Anexo A — Nível de profundidade × nível do aluno

### 1. Escala de profundidade N1–N4 (o nível do CONTEÚDO)

Cada aula do blueprint vem marcada: `**Aula N · título — Nível**`. O nível define a operação cognitiva e o tratamento na escrita:

| Nível | Ação cognitiva | Na escrita da aula (~50 min) |
|---|---|---|
| **N1** — Reconhecer, nomear | citar, identificar | Menção de 1–3 frases: nomeia, situa e **não desenvolve**. Sem subcasos, sem exceções. Típico de revisão ou de "existe, será visto adiante". |
| **N2** — Descrever, explicar | definir, exemplificar | Conceito + explicação + **1–2 exemplos desenvolvidos**. Regra geral sem casos especiais; exceções no máximo mencionadas. |
| **N3** — Analisar, comparar | classificar, relacionar, contrastar | Tratamento sistemático: **quadro completo de casos e subcasos, contrastes (isto × aquilo), principais exceções**, aplicação em contexto real. Nível padrão de consolidação. |
| **N4** — Avaliar, argumentar | julgar, criticar, sintetizar | Tudo do N3 **+ juízo crítico**: limites da regra/modelo, disputas (norma × uso, interpretações divergentes), situação-problema densa (no EM, calibre ENEM/vestibular). |

**Níveis compostos** (`N2-N3`, `N3-N4`): a aula **abre** no nível mais baixo (chegada ao tema) e **chega** ao mais alto **no núcleo** — não é a aula inteira no nível alto.

**Regras de precedência:**

1. O **NÃO ANTECIPAR do blueprint vence o nível** — N4 nunca autoriza cruzar fronteira de conteúdo.
2. O nível vale para o **núcleo da aula**; itens periféricos do recorte ficam um nível abaixo.
3. Na dúvida entre dois tratamentos possíveis dentro do nível, escolher o mais próximo do **uso real** (texto, fenômeno, problema) — nunca o mais enciclopédico.

### Amarração com o movimento pedagógico do ano

Quando o framework/blueprint indicar o movimento do conteúdo no ano, o nível esperado é:

| Movimento | Significado | Nível |
|---|---|---|
| **REVISA** | já dominado em ano anterior | N1 — só reativa |
| **APRESENTA** | primeira vez, sem cobrar domínio | N1–N2 |
| **CONSOLIDA** | é aqui que o aluno domina | N3–N4 |
| **ALIMENTA** | vai aprofundar no ano seguinte | N2–N3 |

### 2. Registro de escrita por faixa (o nível do ALUNO)

O mesmo nível N muda de cara conforme a série. Parâmetros objetivos por faixa:

| Parâmetro | **4º–5º EF** | **6º–7º EF** | **8º–9º EF** | **1ª–2ª EM** | **3ª EM** |
|---|---|---|---|---|---|
| **Frases** | Muito curtas, ordem direta (≈ até 12 palavras); período simples predominante | Curtas, ordem direta (≈ até 20 palavras); período composto com moderação | Médias; subordinação normal | Prosa acadêmica leve, sem restrição artificial | Idem, mais densa |
| **Ordem de apresentação** | **Exemplo concreto → conceito**, sem exceção; o conceito nomeia o que a criança acabou de ver | **Exemplo concreto → conceito** (sempre) | Exemplo → conceito, ou conceito → exemplo imediato | Definição formal primeiro é aceitável | Definição direta; aluno já tem repertório |
| **Vocabulário** | Cotidiano da criança; termo técnico só quando é o próprio conteúdo, explicado com palavra do dia a dia | Cotidiano; **todo termo técnico explicado na 1ª ocorrência** | Técnico consolidado; termo novo sempre explicado | Técnico pleno; nomenclatura padrão da área | Técnico pleno + vocabulário de prova |
| **Abstração** | Nenhuma; tudo ancorado no que se vê, toca ou conta | Mínima; ancorar em situação vivida/observável | Transição: alterna concreto e abstrato | Abstração plena, com retorno ao real como aplicação | Abstração + síntese entre temas |
| **Exemplos por conceito** | 1 exemplo claro; segundo só quando mostrar uma situação diferente, sempre do mundo da criança | 2, do universo do aluno (escola, família, esporte, jogos, tecnologia) | 1–2, de textos/fenômenos reais e referências culturais | 1–2, de fontes reais (literatura, imprensa, dados, experimento) | 1 forte + 1 no formato de prova |
| **Exceções e casos raros** | Nunca entram | Não entram (salvo se estiverem no recorte do blueprint) | Entram as principais | Sistematizadas | Sistematizadas + pegadinhas clássicas de prova |
| **Tom** | Professor próximo, fala com "você", frases afirmativas — **sem infantilizar, sem diminutivo, sem personagem falante** | Professor próximo e direto (fala com "você") | Direto, sem infantilizar | Acadêmico acessível — **nunca infantilizar** | Pré-universitário |
| **Conexão com prova** | Não | Não | Leve (no 9º, mencionar quando natural) | Notas ENEM/vestibular quando o conteúdo render | Sistemática |

**Nota sobre o 4º–5º ano:** faixa acrescentada em 20/07/2026 com a entrada do Fundamental I. A escala N1–N4 não muda — ela descreve a operação cognitiva, não a linguagem. Na prática o EF1 opera em **N1–N3**; **N4 é raro** e só aparece quando o próprio blueprint marcar. O texto usa palavras comuns, exemplos próximos e frases curtas. Simplicidade não significa infantilização: diminutivos e personagens falantes continuam fora do padrão.

**Nota sobre o 9º ano:** é segmento próprio no calendário (24 aulas/sem), mas na escrita segue a coluna 8º–9º **puxando para cima** — é a ponte para o EM.

### 3. Matriz nível × faixa (calibração cruzada)

**A faixa define o repertório e a linguagem; o nível define a operação cognitiva.** Um N2 do EM continua sendo "descrever/explicar" — só que com vocabulário e exemplos de EM. Exemplo do que muda num **N3** ("analisar, comparar"):

- **N3 no 4º–5º:** compara 2 casos lado a lado com exemplos do dia a dia; tabela de duas colunas; nenhuma exceção.
- **N3 no 6º–7º:** compara 2–3 casos com exemplos do cotidiano; tabela simples; só a exceção mais frequente.
- **N3 no 8º–9º:** classifica o quadro completo; contrasta usos em textos/fenômenos reais; 2–3 exceções relevantes.
- **N3 no EM:** sistematização plena + contraste norma × uso / modelo × realidade + implicações (inclusive de prova).

### 4. Regras transversais (valem para toda aula, em qualquer nível)

- **Material é só conteúdo** — sem exercícios, atividades, projetos, sínteses, revisões ou provas (isso é trabalho do professor).
- **Aula autossuficiente:** quem lê só aquele tópico tem a aula completa (~50 min).
- **Peso igual por aula** — não comprimir uma aula para esticar outra.
- **O blueprint manda no recorte:** os 3 tópicos internos da aula são o recorte — desenvolver sem inventar tópico novo e sem cruzar o NÃO ANTECIPAR.
- **Conflito Diretriz × reorganização:** a reorganização vence; a Diretriz da disciplina só calibra profundidade (tratar como introdutório onde ela restringir).

### 5. Educação Cristã — Conexão VP (⚠️ formato em aberto)

- **O que existe:** todos os 280 blueprints (248 do 6º ano em diante + 32 do Fundamental I) trazem, **por tema**, uma **Conexão VP pronta** — unidade VP do período (ex.: *U5 — Dignidade*), **versículo-âncora** e conexão já redigida em 2–3 frases. É a **fonte a consultar** durante a produção; não é preciso buscar nada fora do blueprint.
- **O que mudou (19/07/2026):** o **fechamento de capítulo do formato antigo foi abolido** (incluía a seção "E a Bíblia nisso?", destino original da Conexão VP). O Felipe vai definir um **formato novo** — o tratamento da Conexão VP no material (inline, box, ou fora do material) será fixado junto com o novo prompt de produção.
- **Enquanto não definido:** nenhuma produção deve inventar tratamento próprio para o VP; a conexão permanece nos blueprints aguardando a regra do novo formato.
- **⚠️ Dois rótulos convivem nos blueprints — é intencional, não descuido.** Os **248 blueprints do 6º ano em diante** (até 19/07/2026) rotulam o campo como **`**Conexão VP (para E A BÍBLIA NISSO?):**`**, porque foram escritos quando a seção "E a Bíblia nisso?" ainda era o destino do texto. Os **32 blueprints do Fundamental I** (20/07/2026) usam o rótulo neutro **`**Conexão VP:**`**, já que o fechamento antigo tinha sido abolido no dia anterior e o formato novo ainda não existe. **O conteúdo do campo é o mesmo** (unidade VP, versículo-âncora e conexão redigida); só o rótulo difere. Os dois serão uniformizados quando o Felipe fixar o formato novo — não normalizar antes disso.
- **Fonte profunda (raramente necessária):** a apostila "Vida e Propósito" tem pipeline próprio e isolado em `~/conteudos-prontos/_vida-e-proposito/` (frameworks por unidade e por ano — disponível no Mac Mini). Consultar só se for preciso mudar/aprofundar o **tema** VP de uma unidade, nunca na produção normal.

### 6. Ajustes por família de disciplina

Um único arquivo serve todas as disciplinas; o que muda sistematicamente entre elas é isto (particularidades finas continuam nas regras transversais de cada blueprint):

| Família | Ajuste de escrita |
|---|---|
| **Humanas** — Português, Estudos Sociais, Geografia, História, Sociologia, Filosofia | Partir de texto/fonte/pensador real; conceito nunca isolado do uso ou do contexto. |
| **Matemáticas** — Operações, Geometria, Financeira, Matemática EF1 | Resolução passo a passo, **uma etapa por linha**; formalismo progressivo (EF1 e EF2: procedimento antes da generalização; EM: definição → propriedade → aplicação). No **4º–5º ano** a disciplina é única e alterna eixos: cada tema declara o seu, e a escrita segue o eixo daquele tema. |
| **Empíricas** — Ciências, Biologia, Física, Química | Fenômeno observável → modelo/explicação; grandeza sempre com unidade; matematização cresce com a faixa (qualitativo no 6º–7º → álgebra do 8º em diante). |

---

### 7. O esqueleto do capítulo (formato único de todas as disciplinas)

### O esqueleto

````markdown
# Capítulo 1 — Frações equivalentes e comparação de frações

---

### 1. A fração: o todo dividido em partes iguais

{1 frase de abertura — situação concreta ou fato direto, máx. 25 palavras.}

### 1.1 Os dois números da fração

{Definição em 1 frase curta. No máximo 2 frases antes de uma lista.}

Dois números formam a fração:

- o de baixo diz em quantas partes o todo foi dividido;
- o de cima diz quantas partes se tomou.

{Exemplo concreto. Nas matemáticas, exemplo resolvido no formato fixo:}

**A barra de chocolate repartida**

Calcule: $$\frac{1}{4} + \frac{2}{4}$$

**Resolução:**

- **Passo 1:** Somar os números de cima; o de baixo permanece.

$$\frac{1+2}{4} = \frac{3}{4}$$

**Resposta:** $$\frac{3}{4}$$ da barra.

### 1.2 {Segundo subtópico — pode ser pergunta orientadora}

{Conteúdo. Tabela quando houver 2+ itens a contrastar:}

| Mesmo denominador | Mesmo numerador |
|---|---|
| pedaços do mesmo tamanho | pedaços de tamanhos diferentes |
| vence quem tem mais pedaços | vence quem tem o pedaço maior |

---

### 2. {Título da Aula 2}

{...mesma estrutura. Se a conexão VP do blueprint for conceitual (teste do sinônimo), o versículo entra aqui, no fluxo:}

{1 parágrafo curto ligando o conceito ao valor — prático e específico, sem piedosismo. Sem seção própria, sem lista de ações.}

---

### 3. {Título da Aula 3}

{...o capítulo termina na última aula. SEM seção de fechamento.}
````

### As regras que definem o formato (resumo — o kit da disciplina detalha)

1. **Título:** `# Capítulo {N} — {Tema}` — sem linha de disciplina/ano/série.
2. **Pergunta-problema** do blueprint em blockquote logo abaixo do título, **sem rótulo** — só a pergunta. É respondida dentro da aula pertinente, sem anunciar.
3. **1 aula = 1 tópico `## N.`**, na ordem do blueprint; `---` entre aulas. Cada aula autossuficiente (~50 min).
4. **2–3 subseções `### N.1`, `### N.2`** por aula, com título curto (pode ser pergunta orientadora).
5. **Extensão por aula:** padrão da casa 220–250 (teto 300); overrides por disciplina — Física 130–170 (teto 190), Química 180–210 (teto 240), Geometria 170–210 (teto 240), Matemática EF1 **sem alvo e sem mínimo** (teto 160). Fórmulas, exemplos resolvidos, tabelas, ASCII, figuras TikZ/PNG, textos alternativos e boxes **não** entram na conta. **O teto não é meta.**
6. **Prosa curta + marcadores:** máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens comparáveis; **liste o paralelo, escreva o encadeado**. Toda lista com frase de transição **informativa**.
7. **Boxes:** só a família da disciplina, em blockquote, com quebra de linha interna (título na 1ª linha com dois espaços finais). 1–2 por aula, **nunca dois seguidos**, 1 frase ("drop"). **O box nunca abre um subtópico** — antes dele tem de haver parágrafo, lista ou tabela, porque ele comenta o que o aluno já leu.
8. **Bíblia condicional:** versículo só com ligação **conceitual** (teste do sinônimo) — capítulo sem versículo é entrega válida. *(Em Estudos Sociais, desde 30/07/2026 o versículo não entra no capítulo: vive no arquivo de anexo.)*
9. **Personagem/referência-chave** 1× por capítulo, na aula pertinente (EF em box 👤 onde a disciplina tiver; EM e matemáticas integrado ao texto). *(Estudos Sociais não tem mais box de personagem — a ficha vai para o anexo.)*
10. **O que NUNCA aparece:** blocos pós-conteúdo do formato antigo (`Introdução`, `Sua Parte`, `O que a Bíblia diz sobre...`, `E a Bíblia nisso?`, `Simplificando`, `Para não esquecer`, `Explorando os Conceitos`, `Ampliando o Olhar`, `No Fio da História`, `O Que a Fé Diz`, `Pensador em Destaque`, `Você já pensou nisso?`, `Síntese`, `Fórmulas do capítulo`, `💬 Para Conversar`) · atividades/exercícios propostos/provas · itens do NÃO ANTECIPAR · emojis fora de box · imagens, **exceto as figuras TikZ/PNG autorizadas pelo manual da disciplina** · frases-preparação ("Neste capítulo vamos...").

**Famílias de boxes por disciplina:**

| Disciplinas | Boxes |
|---|---|
| Ciências · Biologia | 💭 ⏸️ 💡 📏 🔬 |
| Física | 💭 ⏸️ 💡 📏 ⚡ 📐 (+ 📝 rótulo de exemplo) |
| Química | 💡 🔎 🌍 💭 ⏸️ ⚠️ |
| Português | 💡 ⚠️ 📌 🔎 👤 |
| Estudos Sociais (Geo/Hist) | 🔎 💭 |
| Sociologia · Filosofia | 💭 ⏸️ 💡 🔍 |
| Operações · Geometria · Financeira · Matemática EF1 | 🔢 ⚠️ |

**Conferência mecânica (depois de entregar, nunca durante):**

```
python3 validar-capitulo.py <capitulo.md> --disciplina <nome> [--blueprint <arq.md>]
```

---

*Criado em 21/07/2026 na consolidação Autores-de-Material. Este esqueleto é a referência transversal; o prompt de produção de cada disciplina é quem manda nos detalhes.*
---

*Criado em 2026-07-19 a partir da escala N1–N4 do pipeline de frameworks. Faixa 4º–5º EF acrescentada em 2026-07-20 com a entrada do Fundamental I. Arquivo único para todas as disciplinas — entra como insumo do novo prompt de produção.*

## Anexo B — Ortografia (Acordo de 1990 + escolhas da casa)

> **Referência de consulta e verificação obrigatória** antes da entrega de qualquer capítulo. Base normativa: **Acordo Ortográfico da Língua Portuguesa (1990)** — em vigor no Brasil desde 2009, **obrigatório desde 2016**. Fonte de grafia em caso de dúvida: **VOLP/ABL** (volp.abl.org.br).
>
> ⚠️ **Não existe "novo acordo 2025/2026".** A CPLP reconheceu em 2024 a necessidade de retificações, mas nada oficial foi publicado. Ignorar conteúdos que anunciem "volta do trema" ou "fim dos acentos". Onde o Acordo permite dupla grafia, a escolha marcada como **[Convenção Eleve]** prevalece.

---

### 1. Alfabeto

26 letras — **k, w, y** incluídas oficialmente. Uso restrito a: nomes próprios estrangeiros e derivados (*Kant, kantiano; Wagner, wagneriano*), siglas e símbolos (*km, kg, W, www*).

---

### 2. Acentuação gráfica — regras vigentes

### 2.1 Proparoxítonas
**Todas** são acentuadas: *lâmpada, médico, sílaba, gramática*.

### 2.2 Paroxítonas
Acentuadas quando terminam em:

| Terminação | Exemplos |
|---|---|
| r, l, n, x, ps | *caráter, fácil, hífen, tórax, bíceps* |
| i(s), us, um, uns | *júri, lápis, vírus, álbum, álbuns* |
| ã(s), ão(s) | *ímã, órfãs, órgão, bênçãos* |
| ditongo (± s) | *história, série, água, jóquei* |

**Não** se acentuam paroxítonas terminadas em **a(s), e(s), o(s), em, ens**: *casa, parede, livro, item, hifens*.

### 2.3 Oxítonas
Acentuadas quando terminam em **a(s), e(s), o(s), em, ens**: *sofá, você, avô, também, parabéns*.

### 2.4 Monossílabos tônicos
Acentuados quando terminam em **a(s), e(s), o(s)**: *pá, pés, pó, três*.

### 2.5 Hiatos com i e u
Acentuam-se **i** e **u** tônicos em hiato, sozinhos na sílaba ou com **s**: *saída, baú, país, saúde*.
**Não** se acentuam: seguidos de **nh** (*rainha, moinho*); repetidos (*xiita*); e, **em paroxítonas, após ditongo** (*feiura, baiuca* — regra do Acordo).

### 2.6 O que o Acordo eliminou — nunca usar as formas antigas

| Regra extinta | ❌ Antes | ✅ Agora |
|---|---|---|
| Ditongos abertos *ei/oi* em **paroxítonas** | idéia, assembléia, heróico | ideia, assembleia, heroico |
| Hiatos *oo* e *ee* | vôo, enjôo, crêem, vêem | voo, enjoo, creem, veem |
| *i/u* após ditongo em paroxítona | feiúra, baiúca | feiura, baiuca |
| Acento diferencial | pára, pólo, péla, pêra | para, polo, pela, pera |

⚠️ **Oxítonas e monossílabos mantêm o acento nos ditongos abertos**: *herói, céu, dói, papéis, chapéu*.

### 2.7 Acentos diferenciais que PERMANECEM

| Forma | Uso |
|---|---|
| **pôde** × pode | passado × presente — *Ontem ele não pôde; hoje pode.* |
| **pôr** × por | verbo × preposição |
| **têm, vêm** | plural de tem, vem — *Eles têm; elas vêm.* |
| **mantém/mantêm, detém/detêm...** | singular -ém × plural -êm |
| **fôrma** | facultativo no Acordo — **[Convenção Eleve]** usar o acento sempre que houver risco de confusão com "forma" |

---

### 3. Trema

**Abolido** em todas as palavras portuguesas: *linguiça, aguentar, cinquenta, tranquilo, sequência, frequente*.
Permanece **apenas** em nomes próprios estrangeiros e derivados: *Müller, mülleriano*.

---

### 4. Hífen

### 4.1 Prefixos + segundo elemento — o quadro de decisão

| Situação | Regra | Exemplos |
|---|---|---|
| Vogal final do prefixo **= vogal inicial** da palavra | **com hífen** | anti-inflamatório, micro-ondas, contra-ataque, auto-observação |
| Vogal final **≠ vogal inicial** | **junto** | autoescola, antiaéreo, semiaberto, agroindústria |
| Prefixo em vogal + **r** ou **s** | junto, **dobrando r/s** | antirrugas, antissocial, ultrassom, minissaia, contrarregra |
| Consoante final do prefixo **= consoante inicial** | **com hífen** | inter-regional, hiper-realista, super-resistente, sub-bloco |
| Consoante final **≠ consoante inicial** | **junto** | intermunicipal, hipermercado, subsolo |
| Prefixo **sub-** + **b, h ou r** | **com hífen** | sub-base, sub-região, sub-reitor (dupla grafia aceita: sub-humano/subumano) |
| Qualquer prefixo + palavra com **h** | **com hífen** | anti-higiênico, super-homem, pré-história |

### 4.2 Prefixos com comportamento fixo

- **Sempre com hífen:** ex-, vice-, além-, aquém-, recém-, sem-, pós-, pré-, pró- (tônicos) → *ex-aluno, vice-diretor, recém-nascido, pós-graduação, pré-escola*
- **Átonos aglutinam:** prever, propor, pospor (pre/pro/pos sem tonicidade própria)
- **circum-** e **pan-** + vogal, h, m, n → **com hífen**: *pan-americano, circum-navegação*
- **co-** aglutina sempre, inclusive diante de o e h (o h cai): *coautor, coedição, coobrigação, coerdeiro, coabitar* — nota do VOLP: **re-, pre- e pro-** (átonos) seguem o mesmo comportamento, nunca levam hífen
- **mal** + vogal, h ou l → **com hífen**: *mal-estar, mal-humorado*; + consoante → junto: *malcriado, malfeito*
- **bem** → em geral com hífen: *bem-vindo, bem-estar* (exceções consagradas: *benfeito, benfeitor*)

### 4.3 Palavras compostas

- **Sem elemento de ligação** → com hífen: *guarda-chuva, segunda-feira, couve-flor, arco-íris*
- **Noção de composição perdida** → junto: *paraquedas, mandachuva, girassol, pontapé*
- **Com elemento de ligação** (de, da, e...) → sem hífen: *dia a dia, fim de semana, pé de moleque, mão de obra, pão de ló* — **exceto**:
  - nomes de espécies botânicas/zoológicas: *bem-te-vi, erva-doce, couve-flor*
  - locuções consagradas que o Acordo preservou: *água-de-colônia, cor-de-rosa, pé-de-meia* (poupança), *mais-que-perfeito* (tempo verbal), *arco-da-velha, ao deus-dará, à queima-roupa*

---

### 5. Maiúsculas e minúsculas

### 5.1 Minúscula obrigatória
- Meses, estações, dias da semana: *janeiro, verão, segunda-feira*
- Pontos cardeais: *norte, sudeste* — **maiúscula** quando designam região: *o Nordeste, o Sul do país*

### 5.2 Maiúscula obrigatória
- Nomes próprios, topônimos, festividades (*Natal, Páscoa*), instituições (*Colégio Eleve*), períodos históricos consagrados (*Idade Média*)

### 5.3 Facultativos no Acordo — escolhas fixadas **[Convenção Eleve]**
| Caso | Convenção |
|---|---|
| Disciplinas e matérias | **Maiúscula**: Português, Matemática, História |
| Formas de tratamento | **Maiúscula**: Vossa Excelência, Senhora Diretora |
| Livros sagrados | **Maiúscula**: Bíblia, e os livros (Mateus, Gênesis) |
| Logradouros | **minúscula** no genérico: rua XV de Novembro, avenida Presidente Vargas |
| Títulos de obras | Maiúscula na primeira palavra e nos nomes próprios: *Origens do Português Brasileiro* segue a capa original |

---

### 6. Dúvidas frequentes de grafia — verificação rápida

| Par | Regra prática |
|---|---|
| **por que / por quê / porque / porquê** | pergunta / fim de frase / resposta-explicação / substantivo ("o porquê") |
| **mau × mal** | mau = contrário de bom (adjetivo); mal = contrário de bem |
| **há × a** (tempo) | há = passado ("há dois anos"); a = futuro ("daqui a dois anos") |
| **senão × se não** | "caso contrário"/"a não ser" × "se por acaso não" |
| **a fim de × afim** | finalidade × afinidade |
| **mas × mais** | oposição × quantidade |
| **viagem × viajem** | substantivo com **g** × verbo viajar com **j** |
| **-esa × -eza** | origem/título: princesa, portuguesa × qualidade abstrata: beleza, certeza |
| **-izar × -isar** | acrescenta -izar (realizar, organizar); mantém s quando o s já está no radical (analisar ← análise, pesquisar ← pesquisa) |
| **x × ch** | depois de ditongo (peixe, caixa), após "en-" (enxergar; exceção: encher e derivados de "cheio"), após "me-" (mexer; exceção: mecha) |

---

### 7. Protocolo de verificação (antes de entregar qualquer capítulo)

1. Rodar leitura de revisão contra as seções 2.6 (formas pré-Acordo), 3 (trema) e 4 (hífen) — são os três pontos de erro mais comuns.
2. Conferir os **[Convenção Eleve]** — facultativos já decididos, não reabrir a escolha.
3. Grafia de palavra específica em dúvida → **VOLP** (volp.abl.org.br). O VOLP prevalece sobre qualquer outra fonte.
4. Conflito entre este arquivo e exemplo de capítulo anterior → **este arquivo prevalece** (e o capítulo anterior deve ser corrigido).

---

*v1.1 · jul/2026 · base: Acordo Ortográfico 1990 (vigente) · pesquisado e verificado (double-check) via Perplexity em jul/2026 — fontes: Ciberdúvidas, Manual do Senado, VOLP/ABL, texto da Base XIX*

---

## Anexo C — LaTeX / MathJax (base comum)

> A notação **específica desta disciplina** está na seção 7 do manual, acima.

---

### Regras da casa

| Regra | Exemplo |
|---|---|
| Toda expressão matemática entre `$$ ... $$` (delimitador único do projeto) | `$$\frac{7}{4}$$` |
| Vírgula decimal com **`{,}`** | `$$0{,}25$$` · `$$1{,}5$$` |
| Unidades em **`\mathrm{}`** com espaço fino **`\,`** | `$$12\,\mathrm{cm}$$` · `$$3\,\mathrm{km/h}$$` |
| Dinheiro em fórmula: `\mathrm{R\$}` | `$$\mathrm{R\$}\,1\,500{,}00$$` |
| Dinheiro em texto corrido: formato brasileiro normal | R$ 1.500,00 |
| Conjuntos numéricos com `\mathbb{}` em fórmula; Unicode no texto | `$$\mathbb{Q}$$` · "o conjunto ℚ" |
| **Intervalo aberto na notação brasileira: colchetes invertidos** (nunca parênteses) | `$$]a, b[$$` · `$$[0, 5[$$` |
| Chaves de conjunto: `\{ ... \}` | `$$A = \{1, 2, 3\}$$` |
| Conectivos "e"/"ou" dentro de fórmula: `\text{ e }` (a forma antiga `\mathrm{~e~}` segue válida) | `$$x > 2 \text{ e } x < 7$$` |
| Milhar em fórmula separado por `\,` | `$$1\,500$$` |
| `\text{}` permitido para **palavras curtas** (acentos funcionam no MathJax) | `$$\text{área} = b \cdot h$$` |
| Frase explicativa longa fica **fora** do LaTeX | — |
| **Toda fórmula com elementos definidos logo após** | onde $$a$$, $$b$$ e $$c$$ são os coeficientes... |
| **Uma operação por linha** nos exemplos resolvidos — blocos `$$...$$` separados, sem `\begin{array}`/`aligned` | ver seção 3 |


### Comandos frequentes (padrão MathJax)

| Uso | Comando |
|---|---|
| Fração | `\frac{a}{b}` |
| Número misto | `1\frac{3}{4}` |
| Raiz quadrada / n-ésima | `\sqrt{x}` · `\sqrt[3]{x}` |
| Potência / índice | `x^{2}` · `a_{n}` |
| Multiplicação | `\cdot` (nunca letra x) |
| Divisão | `\div` ou fração |
| Conjuntos numéricos | `\mathbb{N}` · `\mathbb{Z}` · `\mathbb{Q}` · `\mathbb{R}` |
| Pertence / não pertence | `\in` · `\notin` |
| Diferente / aproximado | `\neq` · `\approx` |
| Maior/menor ou igual | `\geq` · `\leq` |
| Infinito | `\infty` |
| Porcentagem | `\%` — ex.: `$$25\%$$` |
| Pi | `\pi` |
| Ângulo / grau | `\angle` · `^{\circ}` — ex.: `$$90^{\circ}$$` |
| Paralelo / perpendicular | `\parallel` · `\perp` |
| Triângulo / segmento | `\triangle ABC` · `\overline{AB}` |
| Seno, cosseno, tangente | `\sin` · `\cos` · `\tan` |
| Logaritmo | `\log` · `\log_{2}` · `\ln` |
| Somatório | `\sum_{i=1}^{n}` |
| Delta (discriminante) | `\Delta` |
| Mais ou menos | `\pm` |
| Equivalência de frações | `\frac{1}{2} = \frac{2}{4}` |

### Exemplo resolvido — formato obrigatório

- Exemplo resolvido com **rótulo = nome da situação em negrito** (`**Duas turmas com a mesma média**`) — nunca rótulo formal (`### EXERCÍCIO RESOLVIDO`) e **nunca frase de anúncio** ("Veja o exemplo abaixo.").
- Estrutura: enunciado → `**Resolução:**` → passos com `- **Passo N:**` (marcador `-`, nunca `*`) → `**Resposta:**` em frase.
- **Cada operação matemática em um bloco `$$...$$` próprio, em linha própria** — nunca compactar etapas, nunca pular passo.
- **Resultado final sempre simplificado**, com unidade quando houver.

```markdown
**Notas de cinco alunos**

Calcule: $$(3x^2 + 2x - 1) + (x^2 - 5x + 4)$$

**Resolução:**

- **Passo 1:** Agrupar os termos semelhantes.

$$(3x^2 + x^2) + (2x - 5x) + (-1 + 4)$$

- **Passo 2:** Somar os coeficientes de cada grupo.

$$(3+1)x^2 + (2-5)x + (-1+4)$$

$$= 4x^2 - 3x + 3$$

**Resposta:** $$4x^2 - 3x + 3$$
```


### Protocolo de verificação (antes de entregar qualquer capítulo)

1. **Recalcular todos os exemplos resolvidos** — aritmética, álgebra, simplificações e arredondamentos.
2. Conferir **resultado simplificado** em todo exemplo (fração irredutível, radical simplificado, unidade correta).
3. Varrer todos os `$$...$$`: vírgula decimal `{,}` · `\cdot` para multiplicação · `\mathbb{}` para conjuntos · intervalos abertos com colchetes invertidos `]a, b[` · `\mathrm{}` em unidades e R$ · uma operação por linha · matrizes uma por bloco.
4. Frases explicativas longas fora do LaTeX; `\text{}` só para palavras curtas.
5. Delimitador único `$$...$$` — sem `\[...\]`, sem `$...$` simples.
6. Conflito entre este arquivo e blueprint antigo (restrições CodeCogs) ou capítulo anterior → **este arquivo prevalece**.

---

*v1 · jul/2026 · padrão MathJax (Auto-LaTeX Equations/Google Docs) — herda a pesquisa e validação do kit de Química (jul/2026). Revoga as restrições CodeCogs citadas nos blueprints de Operações/Geometria/Financeira (escritas antes da migração para MathJax).*

### Duas armadilhas que quebram a renderização

Bugs reais, encontrados no material do 3º bimestre (21/07/2026). O `validar-capitulo.py` reprova os dois na seção `[2c]`.

### Acento dentro de `\text{}` não renderiza

`\text{}` não aceita caractere acentuado: o renderizador tenta interpretar o acento como comando matemático (`\hat{o}`) e imprime o erro literal na tela.

```
❌  $$\text{vôlei} = \frac{10}{40} = 0{,}25$$
❌  $$g = \text{número de galinhas}$$
❌  $$a = -2 < 0 \implies \text{há máximo}$$
```

**A correção não é escapar o acento — é tirar o texto de dentro da fórmula.** Rótulo e legenda ficam fora, e ganham a forma que o material já prefere:

```
✅  Tabela, quando são várias categorias:

    | Categoria | $$f_r$$ | $$f_r$$ (%) |
    |---|---|---|
    | Vôlei | $$\frac{10}{40} = 0{,}25$$ | 25% |

✅  Lista, quando é legenda de variável:

    - $$g$$ — quantidade de galinhas;
    - $$c$$ — quantidade de coelhos.

✅  Frase, quando é conclusão:

    $$a = -2 < 0$$

    Concavidade para baixo, logo a função tem **máximo**.
```

Palavra **sem acento** dentro de `\text{}` continua válida (`\text{total}`, `\text{massa}`).

### `%` sem escape apaga o resto da fórmula

Em LaTeX, `%` inicia **comentário**: tudo o que vem depois na mesma linha é descartado em silêncio. O resultado é um número que aparece sem o símbolo, sem nenhum aviso de erro.

```
❌  $$0{,}50 = 50%$$     → renderiza "= 50"
✅  $$0{,}50 = 50\%$$    → renderiza "= 50%"
```

Fora de `$$...$$`, em texto corrido, o `%` é caractere comum e **não** leva barra: escrever "40% da turma" está certo.
