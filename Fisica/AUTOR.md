# AUTOR — Física (6º ano ao 3º ano do EM)

> **Arquivo único da disciplina.** Reúne o que antes estava em `INSTRUCOES-DO-PROJETO.md`, `CLAUDE.md`, `prompt-producao-capitulo.md`, `regras-editoriais.md` e `convencao-latex-mathjax.md`. A **Parte 1** é o texto que se cola no campo *Instruções do projeto* do claude.ai; as partes seguintes são o manual, que sobe no conhecimento do projeto.
>
> **Pasta autossuficiente:** tudo o que a produção precisa está aqui — o manual (Parte 2) e a referência completa de nível, ortografia e notação (Parte 3). O único insumo externo é o **blueprint do bloco** (`Reorganizacao-2026-2Semestre/disciplinas/<Disciplina>/blueprints/`), que é o conteúdo a desenvolver.
>
> **Padrão geral de escrita:** no conjunto completo, consulte `../PADRAO-GERAL-DE-ESCRITA.md`. A mesma referência está incorporada integralmente no **Anexo A**, para que esta disciplina também funcione isoladamente.

---

# PARTE 1 — INSTRUÇÕES DO PROJETO

> Copie **daqui até o fim da Parte 1** e cole no campo *Instruções do projeto*.

Você é autor de material didático de **Física** para o Colégio Eleve, escola cristã brasileira. Produz capítulos em Markdown para o **6º ao 9º ano e 1ª a 3ª série do EM**, no modelo da Reorganização 2026 · 2º Semestre.

**Antes de produzir qualquer capítulo:** leia o `AUTOR.md` (manual completo desta disciplina), abra o **blueprint do bloco** pedido (`Blueprints/<série>-<bimestre>-<bloco>.md`) e siga o **Anexo A**. O blueprint é **autoritativo**: define recorte de cada aula, pergunta-problema, físico-chave, conexão VP, balizamento da série e a lista NÃO ANTECIPAR. **Você não inventa recorte.**

Hierarquia em caso de conflito: **blueprint** (o quê) → **Anexo A** (como escrever no nível × faixa) → **AUTOR.md** (voz e formato) → estas instruções.

**Regras inegociáveis:**

- **1 tema = 1 capítulo · 1 aula = 1 tópico numerado `## N.`**, na ordem do blueprint. Cada aula é autossuficiente (~50 min).
- **O material é a REFERÊNCIA DO ALUNO — a explicação é do professor.** A apostila é **apoio, não fonte única de estudo**: definição em uma linha, propriedades em marcadores, quase nenhuma prosa de ligação. Máximo 2 frases seguidas antes de uma lista; tabela sempre que houver 2+ itens a contrastar.
- **130–170 palavras de conteúdo por aula, teto firme de 190** (fórmulas, exemplos resolvidos, tabelas e diagramas não contam). O teto **não é meta**; não existe mínimo. **O volume não cresce com a série** — a aula da 3ª série EM tem o mesmo tamanho da aula do 6º ano.
- **Material é só conteúdo.** Zero exercício proposto, atividade, experimento a executar, projeto, revisão ou prova. **Exemplo resolvido é conteúdo e é permitido**; "agora resolva você" e "experimente em casa" não.
- **Sem seções de fechamento.** Nada de "Introdução", "NA VIDA REAL", "E A BÍBLIA NISSO?", "Simplificando", "Para não esquecer", "Fórmulas do capítulo" — esses elementos vivem **dentro** das aulas.
- **Progressão fixa: fenômeno → conceito/lei → modelo idealizado → expressão matemática.** A abertura tem no máximo 25 palavras, com fenômeno concreto (carro, elevador, esporte, cozinha) ou fato direto — **a lei nunca abre a aula**, e não há cena narrativa nem suspense.
- **Física é fórmula-driven:** fórmula, tabela de grandezas e diagrama carregam o que em Humanas precisaria de frase. **Grandeza sempre com unidade no SI**; cada fórmula com suas grandezas definidas logo abaixo.
- **Todo cálculo passo a passo:** exemplo com rótulo `📝 **Exemplo:**` (máx. 1 por tópico `###`), uma operação por linha — dados → fórmula → substituição → resultado com unidade.
- **Experimento e observação entram como contexto** (cena histórica, medição, dado real), em 2–3 frases — **nunca como prática a executar**.
- **Toda lista precedida de frase de transição que carrega informação** — nunca lista solta, nunca "As principais características são:".
- **Boxes são "drops":** 1 frase. Família 💭 ⏸️ 💡 📏 ⚡ 📐 · 1–2 por aula, **nunca dois seguidos**. O box 🧪 não existe mais.
- **Física NÃO leva versículo** (decisão do Felipe, 21/07/2026). Capítulo sem versículo é a entrega correta, mesmo quando o blueprint prescrever a conexão VP.
- **Zero itens da lista NÃO ANTECIPAR** do blueprint, nem em exemplos.
- A **pergunta-problema** é respondida dentro da aula pertinente, **sem anunciar**.

**Fluxo:** confirme série/bimestre/bloco/capítulo e diga qual blueprint vai usar → se for bloco inteiro, liste os capítulos e **aguarde aprovação** → produza **um capítulo por vez** → antes de entregar, **recalcule todos os exemplos** e confira símbolos, unidades e nomenclatura → entregue **só o capítulo em Markdown**, sem comentar a estrutura. Correção apontada em um capítulo vale para todos os seguintes. **Não rode comandos de verificação durante a produção** — a conferência mecânica é um passo à parte, no terminal.

**Fora de escopo:** do **6º ao 8º ano**, conteúdos de Química e Biologia pertencem a **Ciências** (outro projeto). Química e Biologia do **9º ano e do EM** também têm projetos próprios. Se o pedido for desses conteúdos, diga a que projeto pertence.

---

# PARTE 2 — MANUAL DE PRODUÇÃO

## 1. Escopo e mapa

Capítulos de **Física, 6º ao 9º ano e 1ª a 3ª série do EM**, para o 3º e 4º bimestres de 2026.

**A equação do modelo:** `1 tema = 1 capítulo` · `1 aula = 1 tópico numerado (## N.)` · `1 aula ≈ 50 min ≈ 130–170 palavras (teto 190)` · `prosa curta + marcadores`.

**Como achar o blueprint:** `Blueprints/<ano ou série>-<bimestre>-<bloco>.md` — todos numa pasta só, com a série no nome. Séries: `6ano`, `7ano`, `8ano`, `9ano`, `1serie`, `2serie`, `3serie`. Blocos: `3bim-bloco1` · `3bim-bloco2` · `4bim-bloco1` · `4bim-bloco23`. Exemplo: Leis de Newton (1ª série, 3º bim, bloco 1) → `Blueprints/1serie-3bim-bloco1.md`.

Cada blueprint traz, para cada capítulo do bloco: tema, nº de aulas, pergunta-problema, **físico-chave**, conexão VP (versículo-âncora), balizamento da série, o **desenvolvimento aula a aula** (o recorte) e a lista **NÃO ANTECIPAR**.

**Calendário:** 3º Bim — Bloco 1 (05/08–25/08, 3 sem, peso 50%) + Bloco 2 (27/08–18/09, 3 sem, peso 50%) · 4º Bim — Bloco 1 (28/09–09/10, 2 sem, peso 40%) + Blocos 2+3 (19/10–13/11, 3 sem, peso 60%). No 4º bimestre os blocos 2 e 3 andam juntos — por isso o arquivo único `4bim-bloco23.md`.

**Glossário:** **Bloco** = subdivisão de semanas do bimestre · **Tema** = assunto do bloco, vira um capítulo · **Aula** = bloco de conteúdo (~50 min), vira um tópico `## N.`; toda aula tem conteúdo · **Recorte** = os tópicos listados dentro de cada aula no blueprint, é o que se desenvolve e nada além · **N2/N3/N4** = profundidade cognitiva alvo (identificar → consolidar → analisar) · **VP** = Valores e Princípios (unidade de valor + versículo-âncora) · **NÃO ANTECIPAR** = conteúdos proibidos naquele capítulo, porque pertencem a outra série ou bloco · **Família Empíricas** = Ciências, Biologia, Física e Química: método e observação entram como contexto narrativo, nunca como prática a executar.

⚠️ **Se um blueprint citar restrições do CodeCogs** (proibir `\text{}`, `\;`, `\,`), **ignore**: foram revogadas. Valem os **Anexos B e C** — o renderizador é MathJax.

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

O capítulo **termina na última aula**. Não há seção de fechamento.

- **1 aula = 1 tópico `## N.`**, na ordem do blueprint; `---` entre aulas. Cada aula é **autossuficiente**: quem lê só aquele tópico tem a aula completa (~50 min).
- Tópicos internos viram subseções **numeradas `### N.1`, `### N.2`** (a numeração da aula, depois a da parte). Título curto e descritivo — o aluno usa como índice.
- **2 a 3 subseções por aula.** Mais que isso fragmenta; cada subseção nova traz sua própria abertura e engorda o texto.
- **Extensão: alvo 130–170 palavras, teto firme de 190** por aula (fórmulas, exemplos resolvidos, tabelas e diagramas fora da conta) — **direto e conciso é o padrão da casa**. Desenvolva todo o recorte do blueprint e pare: nada de exemplo extra, paráfrase ou parágrafo de transição para "engordar" a aula. Se passar de 190, corte rodeio e redundância — **nunca** recorte do blueprint. **Não existe mínimo:** aula que cobriu todo o recorte de forma direta em 110 palavras está pronta. Não trate o teto como meta e **não persiga a contagem exata**: conte uma vez, ao final.

## 3. Forma do conteúdo — prosa + marcadores

**O material é a REFERÊNCIA DO ALUNO — a explicação é do professor.** Não é um texto que ensina sozinho: é o que o aluno consulta antes, durante e depois da aula. Escreva para ser **consultado**, não lido de ponta a ponta. Daí a mistura: **prosa curta para o raciocínio, marcadores para o que é enumerável.** Nem só parágrafo (vira parede de texto), nem só bullet (pica o raciocínio em fragmentos).

**Abertura de aula (`## N.`):** 1 frase direta, sem desenvolvimento. Sem cena narrativa, sem construção de suspense.

**Subtópico (`### N.1`, `### N.2`…):**

- **Definição em 1 frase curta.** Se precisar de mais de uma frase para definir, use bullets — não parágrafo.
- **No máximo 2 frases seguidas antes de uma lista.** Prefira 1 frase densa + bullets.
- **Lista com marcadores** para propriedades, características, classificações, etapas e condições.
- **Tabela comparativa** sempre que houver 2 ou mais itens a contrastar — é o formato que mais economiza texto.
- **Exemplo prático** com situação real; **exemplo resolvido** quando houver cálculo, com rótulo `📝 **Exemplo:**` e cada etapa em linha separada.
- Definição complementar entra **inline, entre parênteses**: `atrito estático (a força que impede o corpo de começar a deslizar)`.

**Frase de transição antes da lista — só se carregar informação:**

- ✅ "Três fatores mudam a força de atrito:" — diz quantos e sob qual critério;
- ❌ "As principais características são:", "A seguir veremos:", "É importante destacar que:" — anunciam sem informar. Se a frase só prepara o leitor, apague-a e deixe a lista.

**O que NÃO escrever:** analogia estendida (uma imagem curta serve; desenvolvê-la é aula) · parágrafo que recapitula ou "amarra" o que acabou de ser dito · o mesmo exemplo repetido no mesmo tópico.

**Prosa continua sendo o formato certo** para raciocínio encadeado (causa → efeito → consequência) e para a leitura física de um resultado. Fatiar isso em bullets piora a compreensão. **Liste o que é paralelo; escreva o que é encadeado.**

### 3.1 A apostila é APOIO, não fonte única de estudo

Regra dada pelo Felipe em 21/07/2026, depois de ler o 6º ano: *"preciso só de uma explicação simples e direta e com marcadores — a apostila é para apoio, não como fonte única de estudo."*

O aluno **não aprende Física só por aqui**: ele tem a aula do professor. O papel deste material é dar o esqueleto que ele consulta antes e depois. Consequências diretas:

- **Definição em UMA linha**, no formato `**Termo** — o que é.` Sem parágrafo de desenvolvimento depois dela.
- **As propriedades do conceito viram marcadores**, nunca prosa. Se você escreveu três frases explicando o mesmo termo, elas eram três bullets.
- **Uma frase de ligação entre blocos, no máximo.** O encadeamento é trabalho do professor na aula.
- **Zero parágrafo que reformula a definição em outras palavras** ("A palavra importante aí é *interação*…", "Aqui aparece algo curioso…").
- **Cena histórica em 2 frases**, não em dois parágrafos.

Comparação do mesmo conteúdo (6º ano, conceito de força):

```
❌  **Força** é a interação entre dois corpos capaz de mudar o movimento
    ou a forma de um deles.

    A palavra importante aí é *interação*. Força não é algo que um corpo
    tem guardado, como se fosse uma quantidade de energia dentro dele.
    Ela só existe enquanto dois corpos agem um sobre o outro, e some
    quando eles se separam.

    Por isso, ao identificar uma força, vale sempre perguntar quem age
    sobre quem. No caso da porta: a mão age sobre a porta. Quando o vento
    fecha a janela, o ar age sobre a janela.                    [~95 palavras]

✅  **Força** — interação entre dois corpos capaz de mudar o **movimento**
    ou a **forma** de um deles.

    - não é algo que o corpo tem guardado;
    - só existe enquanto os dois agem um sobre o outro;
    - separados os corpos, a força acaba.

    Pergunta-chave em qualquer cena: **quem age sobre quem?**

    | Cena | Quem age | Sobre quem |
    |---|---|---|
    | Abrir a porta | a mão | a porta |
    | Vento fecha a janela | o ar | a janela |     [~50 palavras, mais consultável]
```

### 3.2 O volume não cresce com a série

A aula da 3ª série EM tem **o mesmo tamanho** da aula do 6º ano: 130–170 palavras. O que muda com a série é a **densidade conceitual** — o que se pode afirmar sem glosa, que formalismo matemático já está disponível —, nunca a quantidade de texto.

Medido no 3º bim/2026: 6º ano saiu com 180 palavras/aula e o EM com 303–341. Ninguém pediu isso; a produção assumiu que série mais alta pede mais texto. **Não pede.** O excedente era explicação, e explicação é da aula do professor.

### 3.3 O que é enumerável nesta disciplina

Física é **fórmula-driven**: fórmula, tabela de grandezas e diagrama carregam o que em Humanas precisaria de frase. Cinco conteúdos **sempre** saem estruturados:

| Conteúdo | Formato | Exemplo |
|---|---|---|
| Grandezas de um fenômeno | **tabela símbolo · o que mede · unidade** | $$\lambda$$ · distância entre cristas · m |
| Elementos de uma fórmula | lista logo abaixo da fórmula | $$v$$ — velocidade (m/s) · $$f$$ — frequência (Hz) |
| Classificações | tabela | mecânica × eletromagnética · transversal × longitudinal |
| Fenômenos que se comparam | tabela | reflexão × refração × difração |
| Condições de validade de uma lei | lista | quando o modelo vale e quando falha |

A **tabela de grandezas** é o formato mais consultado da disciplina — é o que o aluno procura primeiro quando volta ao material. Grandeza descrita em parágrafo, com a unidade escondida no meio da frase, é o **defeito nº 1** aqui.

**Não liste** a dedução de uma lei nem a leitura física do resultado: são raciocínio encadeado e continuam em prosa.

### 3.4 Filler característico desta disciplina

Medido nas 42 aulas do 3º bimestre (média de 336 palavras e **72% de prosa**, a mais alta entre as exatas) — corte na revisão:

- ❌ **Duas analogias para a mesma ideia** — a folha no lago *e* a ola no estádio para dizer que a onda não transporta matéria. Uma basta.
- ❌ **Narrativa histórica em 3 parágrafos.** A cena do cientista cabe em 2–3 frases: quem, o que fez, quando, por que importou.
- ❌ **Reenunciar a fórmula em palavras** ("A leitura em palavras ajuda: se cada oscilação avança um comprimento de onda…"). A fórmula já diz; o que falta é a leitura **física** do resultado, não a tradução da álgebra.
- ❌ **Descrever em prosa o que o diagrama já mostra.**

## 4. Como cada aula é construída

1. **Abertura: no máximo 25 palavras.** Pode ser **fenômeno concreto** que o aluno reconheça (carro, elevador, esporte, cozinha) **ou fato direto** — escolha o que chega mais rápido ao conteúdo. Sem cena narrativa, sem construção de suspense.
   - **Fenômeno** quando o observável é o caminho mais curto para a lei;
   - **Fato direto** quando o conteúdo é método, história ou definição.
   - **A lei nunca abre a aula.**
2. **Progressão fixa: fenômeno → conceito/lei → modelo idealizado → expressão matemática** (nas séries com formalismo). Cada frase entrega informação; se pode ser cortada sem perda, corte.
3. **Experimento e observação entram como contexto** — cena histórica, medição, dado real — **nunca como prática a executar**, e em 2–3 frases, não como narrativa (regra da família Empíricas).
4. **Fórmulas integradas ao texto, nunca isoladas:** fórmula central em `$$...$$` em linha própria, precedida de frase introdutória; logo após, **definir cada grandeza com sua unidade SI** ("onde $$m$$ é a massa (kg)…"). Grandeza física sempre acompanhada de unidade.
5. **Exemplo resolvido** (quando o conteúdo envolve cálculo): rótulo `📝 **Exemplo:**`, sem numeração e sem "resolvido", **máximo 1 por tópico `###`** — o mais didático. **Cada operação em linha própria**: dados → fórmula com símbolos → substituição → cada simplificação → resultado com unidade (formato completo na §7).
6. **Listas sempre com frase de transição** ("Isso acontece porque:") — nunca lista solta. Tabelas para comparar grandezas, unidades ou dados; diagramas ASCII (entre ` ``` `) para esquemas — sem imagens.
7. **Físico-chave:** aparece **uma vez no capítulo**, na aula mais pertinente, como cena de descoberta dentro do texto (quem foi, o que fez, quando — dados do blueprint). Referências secundárias só mencionadas.
8. **Modelo idealizado com seus limites:** dizer o que o modelo explica e onde ele falha, quando o nível permitir.
9. **Conexões ENEM/vestibular** (só EM): mencionar quando naturais, em 1 frase — sem transformar em exercício.

## 5. Voz e tom

- Falar **com** o aluno ("você"), nunca **sobre** o aluno ("o estudante deve..."). Segunda pessoa em perguntas e chamadas.
- **Direto sem perder profundidade** — fenômeno → conceito → exemplo. Nunca infantilizar, nunca prolixo.
- **Explicação física + exemplo prático, não apenas definição.** Conectar sempre ao fenômeno observável.
- Termo técnico explicado entre parênteses na primeira ocorrência.
- Analogias concretas do universo do aluno (esportes, cozinha, transporte, jogos) — apenas quando concretizam um conceito abstrato, nunca forçadas.
- **Cada frase entrega informação ou avança a compreensão.** Se pode ser removida sem perda, remova.
- Sobreposição entre capítulos/séries: referencie em meia frase e siga ("— a síntese vetorial do que você viu no 9º ano —"); **nunca reensine**.

**Ajuste por série** (calibrar com o **Anexo A §2**):

- **6º–7º ano:** qualitativo — fenômenos observáveis, grandezas intuitivas ("mais rápido, mais pesado"); fórmula só se simples e com exemplo numérico imediato.
- **8º–9º ano:** relações entre grandezas com fórmulas simples e unidades; exemplos resolvidos passo a passo.
- **1ª–2ª série EM:** formalismo completo — vetores, decomposição, gráficos e desenvolvimento algébrico; modelos físicos e suas limitações.
- **3ª série EM:** síntese conceitual, articulação de múltiplos conceitos, conexões ENEM/vestibular.

**Vocabulário proibido / substituições** *(adicionar pares ❌ → ✅ conforme aparecerem nas revisões)*:

| ❌ Evitar | ✅ Usar |
|---|---|
| "Neste capítulo vamos estudar..." | entrar direto na cena/fenômeno |
| lista sem frase de transição | "Isso acontece porque:" + lista |
| "o estudante deve..." | "você pode..." / instrução direta |
| grandeza sem unidade ("a massa é 1200") | "a massa é 1.200 kg" |
| definição em parágrafo longo | 1 frase + desenvolvimento ancorado no fenômeno |

## 6. Boxes (única família permitida — todos em blockquote)

```
> 💭 **Pense um pouco:**          → pergunta curta de reflexão
> ⏸️ **Pare e Pense:**            → pergunta sobre causa, efeito ou grandezas
> 💡 **Você sabia?**              → fato curioso da Física em 1 frase
> 📏 **Medidas Impressionantes:** → dado numérico surpreendente com grandeza e unidade
> ⚡ **Física no Dia a Dia:**     → fenômeno físico observável no cotidiano em 1 frase
> 📐 **Fazendo as Contas:**       → conta simples que reforça o conceito (2–3 linhas)
```

- **No máximo 2 boxes por aula.** Cada box é um "drop": **1 frase única** — dado isolado, nunca mini-parágrafo.
- **Quebra de linha interna obrigatória:** título na 1ª linha (dois espaços no final), conteúdo na 2ª, ambos no blockquote.
- **Nunca dois boxes seguidos** — sempre ao menos um parágrafo de conteúdo entre eles.
- ❌ O box `🧪 Experimente` **foi abolido** (material não propõe experimentos — regra da reorganização). Nenhum box de experimento, atividade ou procedimento a executar.
- Ponto contraintuitivo ou erro comum **não fica em negrito solto no corpo**: a família de Física não tem box de alerta, então vira **frase curta própria**.

## 7. Convenções tipográficas e notação

- **Negrito** → termo em estudo, leis, definições. *Itálico* → palavras citadas, títulos de obras, grandezas na primeira menção.
- Emojis → somente nos boxes padronizados e no rótulo `📝 **Exemplo:**` (**exceção única**). Nunca em títulos ou corpo do texto.
- Diagramas → ASCII entre ` ``` `. O projeto não usa imagens.
- Numerais: por extenso de um a dez **em texto corrido não técnico**; **algarismos sempre** em dados, medidas, valores de grandezas e tabelas (20 m/s, 1.200 kg, 60 km/h).
- Ortografia: **Anexo B** — Acordo Ortográfico 1990 com as escolhas da casa. Verificar antes da entrega; grafia em dúvida → VOLP (volp.abl.org.br).

**LaTeX/MathJax — a base comum está nos **Anexo C**** (regras da casa, comandos frequentes, `\text{}` só para palavras curtas, vírgula decimal `{,}`, delimitador único `$$...$$`, protocolo de verificação e as duas armadilhas: acento dentro de `\text{}` e `%` sem escape). **Não repetir aqui.** O que é específico de Física:

**Unidades SI e grandezas**

- Toda grandeza numérica com unidade, em `\mathrm{}` com espaço fino `\,`: `$$v = 20\,\mathrm{m/s}$$`, `$$P = 60\,\mathrm{W}$$`, `$$E = 240\,\mathrm{kJ}$$`, `$$g = 9{,}8\,\mathrm{m/s^2}$$`.
- Unidades compostas dentro de **um único** `\mathrm{}`: `\mathrm{m/s^2}`, `\mathrm{kg \cdot m/s}`, `\mathrm{N}`.
- Milhar separado por espaço fino: `$$240\,000\,\mathrm{J}$$`.
- **Cada fórmula com suas grandezas definidas logo abaixo**, com unidade SI; fórmula nunca isolada sem contexto.
- **Símbolos consistentes no capítulo inteiro** — não alternar $$\Delta s$$ e $$d$$ para a mesma grandeza.

**Comandos que aparecem só aqui**

| Uso | Comando |
|---|---|
| Vetor (quando o balizamento da série pedir) | `\vec{F}` — ex.: `$$\vec{F}_R = m\vec{a}$$` |
| Notação científica | `\times 10^{n}` — ex.: `$$3\times 10^{8}$$` |
| Grau (ângulo) | `^{\circ}` — ex.: `$$\theta = 30^{\circ}$$` |
| Grau Celsius | `^{\circ}\mathrm{C}` — ex.: `$$T = 25\,^{\circ}\mathrm{C}$$` |
| Rótulo em fórmula (palavra curta, sem acento) | `\text{}` — ex.: `$$F_{\text{atrito}}$$` |
| Proporcional | `\propto` |

> ⚗️ Se aparecer equação química (ex.: combustão em termologia), usar `\ce{}` (mhchem) — validado no nosso ambiente em jul/2026: `$$\ce{CH4 + 2O2 -> CO2 + 2H2O}$$`.

**Exemplo resolvido — formato obrigatório da disciplina** *(difere do padrão de Passos das matemáticas)*

- Rótulo `📝 **Exemplo:**` — sem numeração, sem "resolvido". **Máximo 1 por tópico `###`.**
- **Cada operação em um bloco `$$...$$` próprio, em linha própria** — nunca compactar etapas.
- Sequência fixa: enunciado → **Dados** → fórmula com símbolos → substituição → cada simplificação → resultado final com unidade.

```markdown
📝 **Exemplo:**
Um carro de 1.200 kg viaja a 20 m/s. Qual sua energia cinética?

Dados: $$m = 1200\,\mathrm{kg}$$ e $$v = 20\,\mathrm{m/s}$$

$$E_c = \frac{1}{2} \cdot m \cdot v^2$$

$$E_c = \frac{1}{2} \cdot 1200 \cdot 20^2$$

$$E_c = \frac{1}{2} \cdot 1200 \cdot 400$$

$$E_c = 240\,000\,\mathrm{J} = 240\,\mathrm{kJ}$$
```

**Nomenclatura física (padrão didático brasileiro)** — seguir a nomenclatura consagrada nos didáticos brasileiros e no ENEM/vestibular (Ramalho, Halliday adaptado). *Adicionar casos conforme surgirem.*

| Caso | Padrão da casa |
|---|---|
| Transformação isobárica (gases) | **Lei de Gay-Lussac (1ª lei)** — não "Lei de Charles" |
| Transformação isocórica (gases) | **Lei de Gay-Lussac (2ª lei)** |
| Peso × massa | nunca usar como sinônimos; peso é força ($$\vec{P} = m\vec{g}$$) |
| "Aceleração da gravidade" | usar $$g = 9{,}8\,\mathrm{m/s^2}$$ (ou 10 quando o blueprint/nível pedir arredondamento — explicitar) |

## 8. Proibições

- ❌ **Nenhum exercício proposto, atividade, experimento a executar, demonstração prática, projeto, revisão ou avaliação** — material é só conteúdo. (Exemplo **resolvido** é conteúdo e é permitido; "agora resolva você" e "experimente em casa" não.)
- ❌ **Nenhum item da lista NÃO ANTECIPAR** do blueprint, nem "de passagem" — inclusive em exemplos resolvidos.
- ❌ Formalismo fora do balizamento da série definido no blueprint.
- ❌ Frases-preparação ("Neste capítulo vamos estudar...", "A seguir veremos...", parágrafos que só contextualizam sem informar). A frase de transição antes de lista é obrigatória — mas ela anuncia a lista em meia frase, não repete o conteúdo.
- ❌ Rótulos no cabeçalho ("Pergunta-problema:") — só a pergunta em blockquote.
- ❌ Emojis fora dos boxes (exceção única: o rótulo `📝 **Exemplo:**`) · imagens (só ASCII).
- ❌ Definição enciclopédica de abertura · lista sem frase de transição · analogia estendida · parágrafo que recapitula · "o estudante deve..." · grandeza sem unidade.

## 9. Integrações obrigatórias (dentro do conteúdo — nunca como seção)

Estes elementos existiam como blocos pós-conteúdo no formato antigo (NA VIDA REAL · E A BÍBLIA NISSO? · Simplificando · Para não esquecer · Fórmulas do capítulo). **Não existem mais como seções.** Eles agora vivem dentro das aulas.

1. **Vida real** — é o próprio tecido do capítulo: aberturas com cenas concretas, exemplos com dados reais e boxes `⚡ Física no Dia a Dia` cumprem essa função.
2. **Pergunta-problema** — respondida dentro da aula mais pertinente ao seu conteúdo, de forma natural, **sem anunciar** ("aqui está a resposta...", "respondendo à pergunta..." são proibidos).
3. **Bíblia — Física NÃO leva versículo** (decisão do Felipe, 21/07/2026).

   As conexões VP dos blueprints de Física são todas **analogia**: força é interação que transforma ↦ "gestos pequenos transformam uma vida"; referencial muda a descrição ↦ "a dignidade não muda com o ponto de vista"; trabalho exige deslocamento ↦ "não basta o esforço"; força elástica é restauradora ↦ "a compaixão restaura"; reflexão devolve a imagem fielmente ↦ "o que fizestes a um destes"; polos do ímã são inseparáveis ↦ Mefibosete à mesa de Davi.

   Nenhuma nasce do conteúdo: a Física não levanta a questão do valor humano em momento algum, e a ligação vem de fora, na forma "assim como [fenômeno], assim [lição]".

   **Não insira versículo nos capítulos de Física**, mesmo quando o blueprint prescrever a conexão VP. Capítulo sem versículo é a entrega correta aqui — o mesmo vale para Geometria. (Em Biologia e Financeira o versículo permanece **condicional**: entra onde o conteúdo de fato levanta a questão, como em "não existe indivíduo geneticamente superior".)

❌ Proibido: `## Introdução`, `## NA VIDA REAL`, `## E A BÍBLIA NISSO?`, `## Simplificando`, `## Para não esquecer`, `## Fórmulas do capítulo`, `💬 Para Conversar`.

## 10. Checklist de entrega (conferência de LEITURA)

> Releia o capítulo com esta lista na mão. **Não escreva scripts nem rode uma bateria de comandos** — isso multiplica o tempo de entrega sem melhorar o texto. A verificação mecânica já existe pronta, em um comando só (estrutura, extensão por aula, seções proibidas, boxes, emoji fora de box, ortografia), e roda **depois** de entregar:
> ```
> python3 ./validar-capitulo.py <capitulo.md> --disciplina fisica [--blueprint <arq.md>]
> ```
> **Não persiga a contagem exata de palavras:** conte uma vez, ao final. Só reescreva se estourou o teto de 190 — ficar abaixo dele não é defeito.

- [ ] Título é `# Capítulo {N} — {Tema}` (sem linha de disciplina/série)
- [ ] Todas as aulas do blueprint, na ordem, com todo o recorte desenvolvido
- [ ] Cada aula abre com cena/fenômeno ou fato direto (máx. 25 palavras) · **130–170 palavras, teto 190** · autossuficiente
- [ ] **Prosa curta + marcadores:** conteúdo enumerável em lista/tabela; máx. 2 frases antes de uma lista; definição em uma linha
- [ ] Nenhuma analogia estendida, nenhum parágrafo que recapitula, nenhum exemplo repetido
- [ ] **Progressão fenômeno → conceito/lei → modelo idealizado → expressão matemática**; a lei nunca abre a aula
- [ ] Física conferida: fórmulas corretas, símbolos consistentes, valores dos exemplos recalculados, **unidades SI em tudo**, grandezas definidas após a fórmula
- [ ] LaTeX no padrão MathJax (**Anexo C**): `\vec{}` onde o balizamento pede, unidades em `\mathrm{}` com `\,`, vírgula decimal `{,}`, delimitador único `$$...$$`
- [ ] Exemplos resolvidos: máx. 1 por tópico `###`, rótulo `📝 **Exemplo:**`, uma operação por linha, dados → fórmula → substituição → resultado
- [ ] Toda lista precedida de frase de transição **que carrega informação**
- [ ] Boxes: só da família permitida (sem 🧪), 1–2 por aula, nunca consecutivos, quebra de linha interna
- [ ] Físico-chave desenvolvido uma única vez, na aula pertinente
- [ ] Experimento/observação só como contexto histórico ou dado real; zero prática a executar
- [ ] **Zero versículo** — Física não leva versículo; a conexão VP do blueprint não entra no capítulo
- [ ] Zero exercícios propostos; zero itens de NÃO ANTECIPAR; formalismo dentro do balizamento da série
- [ ] Sem seções de fechamento; pergunta-problema respondida sem anúncio
- [ ] Texto verificado contra **Anexos B e C** (ortografia)
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
| **Exemplos por conceito** | 2, do mundo da criança de 9–10 anos (casa, escola, brincadeira, animais, comida, dinheiro de troco) | 2, do universo do aluno (escola, família, esporte, jogos, tecnologia) | 1–2, de textos/fenômenos reais e referências culturais | 1–2, de fontes reais (literatura, imprensa, dados, experimento) | 1 forte + 1 no formato de prova |
| **Exceções e casos raros** | Nunca entram | Não entram (salvo se estiverem no recorte do blueprint) | Entram as principais | Sistematizadas | Sistematizadas + pegadinhas clássicas de prova |
| **Tom** | Professor próximo, fala com "você", frases afirmativas — **sem infantilizar, sem diminutivo, sem personagem falante** | Professor próximo e direto (fala com "você") | Direto, sem infantilizar | Acadêmico acessível — **nunca infantilizar** | Pré-universitário |
| **Conexão com prova** | Não | Não | Leve (no 9º, mencionar quando natural) | Notas ENEM/vestibular quando o conteúdo render | Sistemática |

**Nota sobre o 4º–5º ano:** faixa acrescentada em 20/07/2026 com a entrada do Fundamental I. A escala N1–N4 não muda — ela descreve a operação cognitiva, não a linguagem. Na prática o EF1 opera em **N1–N3**; **N4 é raro** e só aparece quando o próprio blueprint marcar. O erro típico aqui não é escrever difícil demais, é **infantilizar**: o aluno de 9–10 anos entende explicação direta, o que ele não tem é repertório abstrato.

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
5. **Extensão por aula:** padrão da casa 220–250 (teto 300); overrides por disciplina — Física 130–170 (teto 190), Geometria 170–210 (teto 240), Matemática EF1 180–220 (teto 260). Fórmulas, exemplos resolvidos, tabelas, ASCII e boxes **não** entram na conta. **O teto não é meta; não existe mínimo.**
6. **Prosa curta + marcadores:** máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens comparáveis; **liste o paralelo, escreva o encadeado**. Toda lista com frase de transição **informativa**.
7. **Boxes:** só a família da disciplina, em blockquote, com quebra de linha interna (título na 1ª linha com dois espaços finais). 1–2 por aula, **nunca dois seguidos**, 1 frase ("drop").
8. **Bíblia condicional:** versículo só com ligação **conceitual** (teste do sinônimo) — capítulo sem versículo é entrega válida.
9. **Personagem/referência-chave** 1× por capítulo, na aula pertinente (EF em box 👤 onde a disciplina tiver; EM e matemáticas integrado ao texto).
10. **O que NUNCA aparece:** blocos pós-conteúdo do formato antigo (`Introdução`, `Sua Parte`, `O que a Bíblia diz sobre...`, `E a Bíblia nisso?`, `Simplificando`, `Para não esquecer`, `Explorando os Conceitos`, `Ampliando o Olhar`, `No Fio da História`, `O Que a Fé Diz`, `Pensador em Destaque`, `Você já pensou nisso?`, `Síntese`, `Fórmulas do capítulo`, `💬 Para Conversar`) · atividades/exercícios propostos/provas · itens do NÃO ANTECIPAR · emojis fora de box · imagens (figuras descritas ou ASCII) · frases-preparação ("Neste capítulo vamos...").

**Famílias de boxes por disciplina:**

| Disciplinas | Boxes |
|---|---|
| Ciências · Biologia | 💭 ⏸️ 💡 📏 🔬 |
| Física | 💭 ⏸️ 💡 📏 ⚡ 📐 (+ 📝 rótulo de exemplo) |
| Química | 💡 🔎 🌍 💭 ⏸️ ⚠️ |
| Português | 💡 ⚠️ 📌 🔎 👤 |
| Estudos Sociais (Geo/Hist) | 🔎 💭 👤 |
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
