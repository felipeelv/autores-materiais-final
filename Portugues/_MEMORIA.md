# Memória do Kit — Português · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **23/07/2026**.

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
| `portugues-6ano-3bim-cap1-completo.md` | nome histórico mantido por compatibilidade; conteúdo sincronizado com o modelo vigente do 6º ano |
| `modelos/` | **nove capítulos-modelo vigentes**, um por ano/série, com índice próprio |

**Insumo por capítulo (fora desta pasta):** blueprint em `~/Reorganizacao-2026-2Semestre/disciplinas/Portugues/blueprints/<ano>/<bim>-<bloco>.md`. Anos/séries: 4º–9º + 1ª–3ª EM.

## 2. Capítulos-modelo

`modelos/` reúne o Capítulo 1 do 3º bimestre, Bloco 1, de cada ano/série: 4º, 5º, 6º, 7º, 8º e 9º anos; 1ª, 2ª e 3ª séries do EM. Os nove arquivos foram criados e validados em **23/07/2026** segundo o `AUTOR.md` vigente. O índice e o comando de validação ficam em `modelos/README.md`.

O nome `portugues-6ano-3bim-cap1-completo.md` foi mantido para compatibilidade com referências antigas. Em 23/07/2026, seu conteúdo foi substituído pela versão concisa e sincronizada de `modelos/portugues-6ano-modelo.md`; ele não representa mais um padrão editorial diferente.

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Extensão enxuta: sem faixa-alvo nem mínimo; teto firme de 300 por aula.** O aviso abaixo de 100 palavras serve apenas para detectar possível truncamento. Vale o princípio do Felipe: *"se colocar mais palavras a tendência é criar conteúdos desnecessários"*.
2. **Fechamentos abolidos** — "Fechamento do tema", "A língua no dia a dia", "E a Bíblia nisso?", "Simplificando", "Para não esquecer" não existem. Viraram integrações **dentro** das aulas.
3. **Toda aula abre com texto real** (diálogo, bilhete, mensagem, manchete) — "regra gramatical nunca isolada".
4. **Voz de dentro do Brasil:** "no dia a dia, usamos…", nunca "o brasileiro usa…".
5. **Norma × Uso sem "certo × errado"** — uso corrente legítimo na fala, norma-padrão como exigência da escrita formal.
6. **Boxes:** apenas 💡 Dica · ⚠️ Atenção · 📌 Aplicação prática. Referência-chave, pesquisador, curiosidade e nota histórica lateral não viram box nem conteúdo obrigatório.
7. **Cada ideia aparece uma vez.** Conceito novo segue definição curta → exemplo → no máximo uma observação; aplicação ou contraste começa pelo exemplo/tabela. Zero metadiscurso, reforço abstrato ou subseção sem conteúdo novo.
8. **A convenção ortográfica desta pasta é a matriz** — ao corrigi-la, replicar a cópia nas outras seis pastas.

## 4. Estado e próximos passos

- [x] Kit completo · capítulo piloto produzido e aprovado — 19/07/2026
- [x] Arquivos de Claude Projects (`INSTRUCOES-DO-PROJETO.md` + `CLAUDE.md`) — 19/07/2026
- [x] Nove capítulos-modelo vigentes, um por ano/série — 23/07/2026
- [x] Produção do 3º bimestre: 64 capítulos e 348 aulas produzidos e validados — 23/07/2026
- [x] Pasta oficial criada; 64 capítulos enviados e conferidos por SHA-256 — 23/07/2026
- [ ] Montar o projeto no claude.ai (ver `_COMO-MONTAR-OS-PROJETOS.md` na pasta acima)

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
| 23/07/2026 | Criados em `modelos/` os nove capítulos-modelo de Português, um por ano/série, todos baseados no Capítulo 1 do 3º bimestre, Bloco 1, e validados no padrão vigente. O piloto histórico do 6º ano foi preservado, mas deixou de ser a referência principal. |
| 23/07/2026 | Definições gramaticais recalibradas por decisão do Felipe: função em linguagem cotidiana; proibido “X é o termo/elemento que…”; “frase” antes de “oração”; até 15 palavras na definição inicial; 1ª pessoa do plural; definição e exemplo ligados por dois-pontos. Os nove modelos foram revisados com esse tom. |
| 23/07/2026 | Família de boxes de Português reduzida a 💡 Dica, ⚠️ Atenção e 📌 Aplicação prática. Removidos `👤 Quem pesquisou isso` e `🔎 Curiosidade` dos modelos e do piloto histórico; referências-chave dos blueprints não entram mais automaticamente no material. |
| 23/07/2026 | Aplicada a regra de concisão aprovada: cada ideia uma vez; conceito novo em definição curta → exemplo → uma observação; zero metadiscurso e vocabulário abstrato evitado; no máximo um box por aula; tabela de consolidação somente na última subseção pertinente. Retirada a faixa-alvo de palavras, mantido o teto 300 e criado aviso de truncamento abaixo de 100. Os nove modelos passaram de média 162,5 para 146,8 palavras por aula (-9,7%), sem retirar recortes dos blueprints. O arquivo histórico do 6º ano foi sincronizado com o modelo vigente. |
| 23/07/2026 | Concluída a produção sequencial dos 64 capítulos e das 348 aulas do 3º bimestre, do 4º ano à 3ª série do EM. Todos passam no validador; as aulas ficaram entre 55 e 217 palavras, com média 100,0. Os avisos de possível truncamento foram conferidos contra os blueprints. |
| 23/07/2026 | Criada a pasta oficial `Segundo Semestre/Português`, com nove pastas de ano/série. Os 64 arquivos foram enviados e comparados por SHA-256, sem divergências. Decisão permanente: quando a pasta oficial não existir, criá-la e salvar diretamente nela; não manter cópia final em `conteudos-prontos` ou outro destino intermediário. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Portugues/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** escopo estendido ao EF1 (4º–5º — blueprints já existiam; piloto pendente, confirmar com o Felipe); seção ESCOPO criada no prompt; herdado `referencia-exemplos-linguagem.md` do autor antigo (reformatado, com nota de precedência) e adicionado como insumo 5 do prompt; linha de linguagem 4º–5º EF adicionada. |
