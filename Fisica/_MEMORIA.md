# Memória do Kit — Física · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **19/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Física** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Molde replicado dos kits de **Português** (piloto aprovado) e **Química**.

| Arquivo | Papel |
|---|---|
| `prompt-producao-capitulo.md` | Prompt de produção — preencher campos `{ }` e enviar junto com os demais arquivos |
| `regras-editoriais.md` | Voz, tom, densidade e nomenclatura física (autoritativo em conflito com o prompt) |
| `convencao-latex-mathjax.md` | Fórmulas/unidades SI/exemplos resolvidos no padrão MathJax (verificação obrigatória) |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (cópia idêntica à de Português/Química) |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Fisica/blueprints/<série>/<bim>-<bloco>.md`. Séries: **6º ao 9º ano + 1ª, 2ª e 3ª EM** (7 séries).

## 2. Origem

Kit criado em **19/07/2026** a partir das instruções + memória do projeto Claude.ai de Física (`Fisica.rtf`, fluxo antigo por unidades — **absorvido e apagado** após conferência; o que valia foi incorporado aos .md desta pasta).

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Fechamentos abolidos** — a estrutura antiga (Introdução storytelling · NA VIDA REAL · E A BÍBLIA NISSO? · Simplificando · Para não esquecer · Fórmulas do capítulo) não existe mais. Vida real vira tecido das aulas + box ⚡; conexão VP vira versículo + parágrafo curto na aula pertinente (sem princípios numerados, sem "Para Conversar"); resumos e lista de fórmulas saíram. O storytelling (cena → tensão) migrou para a **abertura de cada aula**.
2. **Extensão enxuta: teto de 400 palavras de conteúdo por aula** (fórmulas/exemplos/tabelas fora da conta). Teto definido pelo Felipe em 20/07; a faixa de 350–500 de 19/07 saiu prolixa na prática.
3. **Exemplo resolvido é conteúdo** (permitido e incentivado — rótulo `📝 **Exemplo:**`, máx. 1 por tópico `###`, uma operação por linha, dados → fórmula → substituição → resultado). **Exercício proposto ao aluno é proibido.** O rótulo 📝 é a única exceção a "emoji só em box".
4. **Box 🧪 Experimente abolido** — material não propõe experimentos (regra da reorganização; observação/experimento entram só como contexto narrativo). Família mantida: 💭 ⏸️ 💡 📏 ⚡ 📐 · 1–2 por aula · nunca consecutivos · 1–2 frases.
5. **LaTeX no padrão MathJax** — Auto-LaTeX Equations (Google Docs) com renderizador MathJax. Restrições antigas do CodeCogs (proibir `\text{}`, `\;`, `\,`, acentos) **revogadas**. Padrões: unidades `\,\mathrm{}`, vírgula decimal `{,}`, milhar `\,`, vetores `\vec{}`, `\ce{}` disponível se surgir equação química (validado em jul/2026 no kit de Química).
6. **Frase de transição obrigatória antes de toda lista** ("Isso acontece porque:") — marca registrada do estilo de Física, mantida.
7. **Nomenclatura didática brasileira** (aprendizado do projeto antigo): isobárica = "Lei de Gay-Lussac (1ª lei)", isocórica = "Lei de Gay-Lussac (2ª lei)" — não "Lei de Charles" para isobárica. Tabela em `regras-editoriais.md` §4.
8. **Abertura de aula:** cena/fenômeno concreto com tensão em 1–2 frases; a lei nunca abre a aula. Progressão: fenômeno → lei → modelo idealizado → expressão matemática.

## 4. Estado e próximos passos

- [x] Kit completo e consistente (4 arquivos .md + esta memória) — 19/07/2026
- [ ] Subir os arquivos no projeto Claude.ai de Física (substituindo as instruções antigas por unidades)
- [ ] Capítulo piloto para validar o kit (sugestão: Leis de Newton · 1ª série · blueprint `3bim-bloco1.md` — capítulo de 3 aulas, bom para teste rápido)
- [ ] Após piloto aprovado: registrar ajustes aqui e replicar aprendizados aos próximos kits

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado a partir do `Fisica.rtf` (instruções + memória do projeto antigo), no molde de Português/Química |
| 19/07/2026 | LaTeX já nasce no padrão MathJax (herda pesquisa e validação mhchem do kit de Química) |
| 19/07/2026 | RTF original apagado após conferência; pasta só com .md |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |
| 21/07/2026 | **Física não leva versículo + volume não cresce com a série.** As 9 conexões VP dos blueprints são analogia ("assim como [fenômeno], assim [lição]"), e a Física nunca levanta a questão do valor humano — mesma conclusão de Geometria. Versículos removidos dos 9 capítulos do 3º bim. Junto: extensão apertada duas vezes (240 → **190**, piso 110) porque o 6º ano continuava com "muita explicação", e registrada a regra de que **o volume não cresce com a série** — a produção vinha entregando 180 pal./aula no 6º ano e 303–341 no EM sem que nada no kit pedisse isso. **Pendente:** rever a conexão VP nos blueprints ou tirar VP da disciplina. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Fisica/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra (teto próprio de 190 mantido). |
