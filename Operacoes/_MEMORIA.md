# Memória do Kit — Operações (Matemática 1) · Reorganização 2026 · 2º Semestre

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **19/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Operações** consome para produzir capítulos (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Cobre **aritmética, álgebra, conjuntos e funções**, do 6º ano à 3ª série.

| Arquivo | Papel |
|---|---|
| `INSTRUCOES-DO-PROJETO.md` | texto para colar no campo *Instruções do projeto* |
| `CLAUDE.md` | mapa do conhecimento (índice, blueprint, glossário) |
| `prompt-producao-capitulo.md` | prompt de produção com campos `{ }` |
| `regras-editoriais.md` | voz, densidade, rigor matemático |
| `convencao-latex-mathjax.md` | fórmulas, exemplo resolvido, notação |
| `convencao-ortografica.md` | Acordo Ortográfico + escolhas da casa |

**Blueprints:** `Reorganizacao-2026-2Semestre/disciplinas/Operacoes/blueprints/<ano>/` (~72k tokens).

## 2. Origem

Criado em **19/07/2026** a partir do kit único de Matemática (que atendia as três disciplinas), **separado por decisão do Felipe** no mesmo dia: *"eu preciso de uma pasta para cada matemática, porque elas têm regras diferentes"*. Herda a memória e as instruções do projeto Claude.ai de Matemática 1, incorporadas em 19/07.

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Fechamentos abolidos**; VP vira versículo + 1–2 frases diretas na aula pertinente, **sem analogia explícita** ("assim como X, Y").
2. **no máximo 400 palavras/aula**; conteúdo difícil vira fatias menores.
3. **Regra de ouro: todo cálculo passo a passo, uma operação por linha, resultado sempre simplificado.**
4. **Exemplo resolvido:** frase natural ("Veja o exemplo abaixo.") → `**Resolução:**` → `- **Passo N:**` → `**Resposta:**`. Sem rótulo, sem emoji, marcadores `-`.
5. **Boxes:** só `🔢 Padrão` e `⚠️ Atenção`, 1 frase, 1 por aula (2 só se um de cada tipo).
6. **Matemático-referência integrado ao texto**, sem box.
7. **LaTeX MathJax** — restrições CodeCogs dos blueprints revogadas. Intervalos `]a, b[`, matrizes uma por bloco (2ª série).
8. **Fund: apoio pictórico na entrada** (barras, reta numérica, dinheiro) + procedimento seguro como régua; **EM: formalização direta**.

## 4. Estado e próximos passos

- [x] Kit completo (6 arquivos + esta memória) — 19/07/2026
- [ ] Montar o projeto no claude.ai (ver `_COMO-MONTAR-OS-PROJETOS.md` na pasta acima)
- [ ] Capítulo piloto: Representação e comparação de racionais · 7º ano · `3bim-bloco1.md` (4 aulas)

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit único de Matemática criado a partir dos blueprints |
| 19/07/2026 | Memória + instruções do projeto Claude.ai incorporadas |
| 19/07/2026 | Kit separado em três pastas (Operações, Geometria, Financeira) por regras distintas |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Operacoes/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra. Serviu de molde para o kit novo de Matemática EF1. |
