# Memória do Kit — Português · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **19/07/2026**.

---

## 1. O que é este kit

Foi o **kit piloto** — o molde de todos os outros (Química, Física, Estudos Sociais, Matemática, Ciências, Biologia). Arquivos que o projeto **Claude.ai de Português** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`).

| Arquivo | Papel |
|---|---|
| `INSTRUCOES-DO-PROJETO.md` | texto para colar no campo *Instruções do projeto* do Claude Project |
| `CLAUDE.md` | mapa do projeto (índice do conhecimento, como achar o blueprint, glossário) |
| `prompt-producao-capitulo.md` | prompt de produção com campos `{ }` |
| `regras-editoriais.md` | voz, estilo, tom, ortografia |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (**arquivo-mestre**: as outras disciplinas usam cópia deste) |
| `portugues-6ano-3bim-cap1-completo.md` | **capítulo piloto aprovado** — referência de estilo |

**Insumo por capítulo (fora desta pasta):** blueprint em `~/Reorganizacao-2026-2Semestre/disciplinas/Portugues/blueprints/<ano>/<bim>-<bloco>.md`. Séries: 6º–9º + 1ª–3ª EM.

## 2. O capítulo piloto

`portugues-6ano-3bim-cap1-completo.md` — Pronomes: classes e emprego (6º ano · 3º Bim · Bloco 1). **Analisado e aprovado em 19/07/2026.** Cumpre o blueprint integralmente, zero itens de NÃO ANTECIPAR, voz inclusiva aplicada, Mateus 25:40 integrado como texto-exemplo.

Dois desvios apontados na análise (não corrigidos por decisão do Felipe):
- a frase que **anuncia** a resposta da pergunta-problema na Aula 4 ("Aqui está a resposta para a última parte daquela pergunta…") — o prompt proíbe anunciar;
- ✅/❌ em linhas de exemplo (as regras editoriais os restringem a quadros comparativos).

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Extensão enxuta: no máximo 400 palavras de conteúdo por aula.** O piloto saiu com 342–489 palavras sob a faixa antiga (350–500); em 20/07 o teto caiu para 400, porque as aulas seguiam prolixas. Vale o princípio do Felipe: *"se colocar mais palavras a tendência é criar conteúdos desnecessários"*.
2. **Fechamentos abolidos** — "Fechamento do tema", "A língua no dia a dia", "E a Bíblia nisso?", "Simplificando", "Para não esquecer" não existem. Viraram integrações **dentro** das aulas.
3. **Toda aula abre com texto real** (diálogo, bilhete, mensagem, manchete) — "regra gramatical nunca isolada".
4. **Voz de dentro do Brasil:** "no dia a dia, usamos…", nunca "o brasileiro usa…".
5. **Norma × Uso sem "certo × errado"** — uso corrente legítimo na fala, norma-padrão como exigência da escrita formal.
6. **Boxes:** 💡 Dica · ⚠️ Atenção · 📌 Aplicação prática · 🔎 Curiosidade · 👤 Quem pesquisou isso (personagem-chave, 1× por capítulo).
7. **A convenção ortográfica desta pasta é a matriz** — ao corrigi-la, replicar a cópia nas outras seis pastas.

## 4. Estado e próximos passos

- [x] Kit completo · capítulo piloto produzido e aprovado — 19/07/2026
- [x] Arquivos de Claude Projects (`INSTRUCOES-DO-PROJETO.md` + `CLAUDE.md`) — 19/07/2026
- [ ] Montar o projeto no claude.ai (ver `_COMO-MONTAR-OS-PROJETOS.md` na pasta acima)
- [ ] Produzir os demais capítulos do 6º ano e expandir para as outras séries

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Capítulo piloto (Pronomes, 6º ano) analisado e aprovado |
| 19/07/2026 | Faixa de extensão corrigida para 350–500 palavras/aula (padrão da casa, replicado a todas as disciplinas) |
| 19/07/2026 | Kit virou molde dos kits de Química, Física, Estudos Sociais, Matemática, Ciências e Biologia |
| 19/07/2026 | Criados `INSTRUCOES-DO-PROJETO.md` e `CLAUDE.md` para uso em Claude Projects |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Portugues/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** escopo estendido ao EF1 (4º–5º — blueprints já existiam; piloto pendente, confirmar com o Felipe); seção ESCOPO criada no prompt; herdado `referencia-exemplos-linguagem.md` do autor antigo (reformatado, com nota de precedência) e adicionado como insumo 5 do prompt; linha de linguagem 4º–5º EF adicionada. |
