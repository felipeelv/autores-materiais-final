# Memória do Kit — Química · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **19/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Química** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Molde replicado do kit piloto de **Português** (pasta ao lado), aprovado com o capítulo de Pronomes (6º ano).

| Arquivo | Papel |
|---|---|
| `prompt-producao-capitulo.md` | Prompt de produção — preencher campos `{ }` e enviar junto com os demais arquivos |
| `regras-editoriais.md` | Voz, tom e densidade (autoritativo em conflito com o prompt) |
| `convencao-latex-mathjax.md` | Fórmulas/equações no padrão MathJax (verificação obrigatória pré-entrega) |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (cópia idêntica à de Português) |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Quimica/blueprints/<série>/<bim>-<bloco>.md` — documento autoritativo de recorte. Séries: 9º ano, 1ª, 2ª e 3ª EM.

## 2. Origem

Kit criado em **19/07/2026** a partir das instruções antigas do projeto Claude.ai de Química (`instruços quimica.rtf`, fluxo antigo por unidades — **absorvido e apagado** após conferência; o que valia foi incorporado aos .md desta pasta).

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Fechamentos abolidos** — a estrutura antiga (Introdução · Aplicações Práticas · "O que a Bíblia diz" · Síntese do Capítulo) não existe mais. Aplicações viram tecido das aulas + boxes 🌍; conexão VP vira versículo + parágrafo curto na aula pertinente (sem "Na prática", sem "Para Conversar"); síntese saiu (blueprints proíbem).
2. **Extensão enxuta: teto de 400 palavras de conteúdo por aula** (tabelas/fórmulas fora da conta). Teto definido pelo Felipe em 20/07 (a faixa de 19/07 saiu prolixa): mais palavras = conteúdo desnecessário. Não inflar.
3. **Exemplo resolvido é conteúdo** (demonstração de cálculo — permitido e incentivado); **exercício proposto ao aluno é proibido** (é do professor).
4. **LaTeX no padrão MathJax** — Felipe usa Auto-LaTeX Equations (Google Docs) com renderizador MathJax. Restrições antigas do CodeCogs (proibir `\text{}`, `\;`, `\,`) **revogadas**.
5. **`\ce{}` (mhchem) é o padrão obrigatório para equações e espécies químicas** — validado por teste real no Google Docs do Felipe em 19/07/2026. `\mathrm{}` fica para unidades/grandezas.
6. **Boxes:** família própria de Química (💡 Você sabia? · 🔎 Curiosidade · 🌍 Fenômeno · 💭 Pense um pouco · ⏸️ Pare e Pense · ⚠️ Atenção), 1–2 por aula, 1 frase única, quebra de linha interna.
7. **Abertura de aula:** fenômeno/cena concreta (família Empíricas — experimento como cena que motiva o conceito, nunca roteiro de prática).

## 4. Estado e próximos passos

- [x] Kit completo e consistente (4 arquivos .md) — 19/07/2026
- [x] mhchem validado no ambiente real — 19/07/2026
- [ ] Subir os arquivos no projeto Claude.ai de Química (substituindo as instruções antigas por unidades)
- [ ] Capítulo piloto para validar o kit (sugestão: Tabela Periódica · 1ª série · blueprint `3bim-bloco1.md`)
- [ ] Após piloto aprovado: registrar ajustes aqui e replicar aprendizados aos kits das próximas disciplinas

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado a partir do RTF antigo, no molde do kit de Português |
| 19/07/2026 | Convenção LaTeX migrada de CodeCogs → MathJax (pesquisa autolatex.com + docs.mathjax.org) |
| 19/07/2026 | `\ce{}`/mhchem validado pelo Felipe no Google Docs → promovido a padrão (convenção v2.1) |
| 19/07/2026 | RTF original apagado após conferência; pasta só com .md |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Quimica/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra. |
