# Memória do Kit — Financeira (Matemática 3) · Reorganização 2026 · 2º Semestre

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **19/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Financeira** consome para produzir capítulos (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Cobre **estatística, probabilidade e educação financeira**, do 6º ano à 3ª série.

| Arquivo | Papel |
|---|---|
| `INSTRUCOES-DO-PROJETO.md` | texto para colar no campo *Instruções do projeto* |
| `CLAUDE.md` | mapa do conhecimento (índice, blueprint, glossário) |
| `prompt-producao-capitulo.md` | prompt de produção com campos `{ }` |
| `regras-editoriais.md` | voz, dados, **ética financeira**, notas críticas |
| `convencao-latex-mathjax.md` | notação estatística/financeira, tabelas, exemplo resolvido |
| `convencao-ortografica.md` | Acordo Ortográfico + escolhas da casa |

**Blueprints:** `Reorganizacao-2026-2Semestre/disciplinas/Financeira/blueprints/<ano>/` (~46k tokens).

## 2. Origem

Criado em **19/07/2026** a partir do kit único de Matemática, **separado por decisão do Felipe** no mesmo dia: *"eu preciso de uma pasta para cada matemática, porque elas têm regras diferentes"*. As regras próprias vieram da leitura dos blueprints de Financeira.

## 3. Decisões registradas (não reabrir sem o Felipe)

**Herdadas do tronco comum:** fechamentos abolidos · no máximo 400 palavras/aula · passo a passo obrigatório · exemplo resolvido com frase natural + Resolução/Passos(`-`)/Resposta · boxes só 🔢/⚠️ (1 frase) · referência-chave no texto sem box · LaTeX MathJax (restrições CodeCogs revogadas) · VP sem analogia explícita.

**Próprias desta disciplina:**

1. **O número nunca é o fim: todo cálculo termina em interpretação.** "s ≈ 2,24" não é resposta; "as notas se afastam da média cerca de 2 pontos" é. Vale para tabelas e gráficos também.
2. **Honestidade com dados:** proibido inventar estatística oficial (IBGE, IPCA, Selic). Dado hipotético permitido **se declarado**; dado real com referência de tempo.
3. **Ética financeira:** mecanismos e consequências, sim; **zero recomendação de investimento/produto/instituição**, zero promessa de rentabilidade, **zero julgamento de quem se endivida**. *(Decisão nova deste kit — não vinha dos blueprints; confirmar com o Felipe no piloto.)*
4. **Nota crítica sobre referência-chave é obrigatória quando o blueprint pedir** — o caso explícito é **Francis Galton** (fundador da estatística moderna e do eugenismo): reconhecer a contribuição técnica sem endossar a ideologia, em 1 frase, sem sermão.
5. **Cálculo estatístico com conjuntos pequenos (5–8 valores)** e sequência fixa: média → desvios → quadrados → soma → variância → desvio padrão → CV. **Populacional × amostral explicitados** ($$N$$ × $$n-1$$).
6. **Dinheiro com 2 casas e moeda** (R$ 1.061,21); **taxa sempre com período** ("2% ao mês").
7. **Tabelas são ferramenta central** — em **Markdown**, nunca em LaTeX, com cabeçalho e unidade. Gráficos descritos em texto/ASCII.
8. **Abertura por dado ou decisão real** (duas turmas com a mesma média, o preço que subiu, a parcela que parece pequena).

## 4. Estado e próximos passos

- [x] Kit completo (6 arquivos + esta memória) — 19/07/2026
- [ ] Montar o projeto no claude.ai (ver `_COMO-MONTAR-OS-PROJETOS.md` na pasta acima)
- [ ] **Confirmar com o Felipe a regra de ética financeira** (item 3)
- [ ] Capítulo piloto: Medidas de dispersão · 1ª série · `3bim-bloco1.md` (3 aulas — testa cálculo passo a passo, interpretação e a nota crítica sobre Galton)

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado na separação das três matemáticas, com regras próprias de dados, dinheiro e ética |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Financeira/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra. |
