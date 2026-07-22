# Memória do Kit — Geometria (Matemática 2) · Reorganização 2026 · 2º Semestre

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **19/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Geometria** consome para produzir capítulos (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Cobre **plana, espacial, analítica, trigonometria e transformações**, do 6º ano à 3ª série.

| Arquivo | Papel |
|---|---|
| `INSTRUCOES-DO-PROJETO.md` | texto para colar no campo *Instruções do projeto* |
| `CLAUDE.md` | mapa do conhecimento (índice, blueprint, glossário) |
| `prompt-producao-capitulo.md` | prompt de produção com campos `{ }` |
| `regras-editoriais.md` | voz, **figuras**, **construções**, rigor geométrico |
| `convencao-latex-mathjax.md` | notação geométrica, unidades, ASCII, exemplo resolvido |
| `convencao-ortografica.md` | Acordo Ortográfico + escolhas da casa |

**Blueprints:** `Reorganizacao-2026-2Semestre/disciplinas/Geometria/blueprints/<ano>/` (~46k tokens).

## 2. Origem

Criado em **19/07/2026** a partir do kit único de Matemática, **separado por decisão do Felipe** no mesmo dia: *"eu preciso de uma pasta para cada matemática, porque elas têm regras diferentes"*. As regras próprias vieram da leitura dos blueprints de Geometria.

## 3. Decisões registradas (não reabrir sem o Felipe)

**Herdadas do tronco comum:** fechamentos abolidos · no máximo 400 palavras/aula · passo a passo obrigatório · exemplo resolvido com frase natural + Resolução/Passos(`-`)/Resposta · boxes só 🔢/⚠️ (1 frase) · matemático-referência no texto sem box · LaTeX MathJax (restrições CodeCogs revogadas) · VP sem analogia explícita.

**Próprias desta disciplina:**

1. **Sem imagens — descrever a figura é conteúdo crítico.** Vértices nomeados, posições relativas, medidas, dado × procurado; ASCII simples quando ajudar. **Proibido** "veja a figura ao lado". *(É a maior diferença em relação às outras matemáticas.)*
2. **Construções (régua, compasso, transferidor, GeoGebra) = procedimento descrito, nunca atividade proposta** — regra explícita das regras transversais dos blueprints ("as construções com instrumentos/software entram como procedimento descrito no conteúdo, não como atividade").
3. **Justificativa antes da fórmula** — fórmula sem o "porquê" é decoreba. Demonstração formal só quando o blueprint pedir.
4. **Resultado sempre com unidade** (cm, m², cm³, °) — resultado sem unidade é erro.
5. **Não infantilizar:** quando o conteúdo é novidade crítica da série (transformações no 8º, trigonometria no 9º/EM), o vocabulário técnico é o conteúdo — regra vinda do balizamento dos blueprints.
6. **Abertura visual concreta** (azulejo, rampa, sombra, embalagem, esteira) — a geometria entra pelo olho.
7. **Notação própria** na convenção LaTeX: `\overline{AB}`, `\angle`, `\triangle`, `^{\circ}`, `\parallel`, `\perp`, `\cong`, `\sim`, `\vec{v}`.

## 4. Estado e próximos passos

- [x] Kit completo (6 arquivos + esta memória) — 19/07/2026
- [ ] Montar o projeto no claude.ai (ver `_COMO-MONTAR-OS-PROJETOS.md` na pasta acima)
- [ ] Capítulo piloto: Transformações geométricas · 8º ano · `3bim-bloco1.md` (3 aulas — testa descrição de figura, isometrias e Escher)

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado na separação das três matemáticas, com regras próprias de figura e construção |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |
| 21/07/2026 | **Geometria não leva versículo.** As 4 conexões VP dos blueprints são analogia (invariância geométrica ↦ dignidade), o que o `regras-editoriais.md` desta disciplina já proibia ("sem analogia explícita"). Diferente de Biologia/Financeira, o conteúdo de Geometria nunca levanta a questão do valor humano. Versículos removidos dos 4 capítulos do 3º bim. **Pendente:** rever a conexão VP nos blueprints ou tirar VP da disciplina. |
| 21/07/2026 | **Extensão apertada: alvo 170–210, teto 240** (padrão da casa é 300). Geometria é fórmula-e-figura: o desenho e a tabela carregam o que em Humanas precisaria de frase. Medido antes: **378 palavras/aula**, a maior do projeto, com `"Veja o exemplo abaixo."` em 10 das 12 aulas — frase que o próprio prompt prescrevia. Prompt ganhou "O que é enumerável nesta disciplina" (tabela *o que preserva × o que muda* é o formato mais consultado) e "Filler característico". Os 4 capítulos do 3º bim refeitos: **236 pal./aula, 41% de prosa**. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Geometria/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra (teto próprio de 240 mantido). Pendência herdada: versículo Mateus 25:40 repetido em 3 séries nos blueprints — decisão do Felipe. |
