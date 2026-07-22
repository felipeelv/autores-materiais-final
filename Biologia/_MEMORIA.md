# Memória do Kit — Biologia · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **21/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Biologia** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). **Derivado do kit de Ciências** (mesmo projeto antigo cobria as duas), com balizamento de 9º ano/EM e uma convenção LaTeX própria.

| Arquivo | Papel |
|---|---|
| `prompt-producao-capitulo.md` | Prompt de produção — abre com ESCOPO (9º + EM); campos `{ }` |
| `regras-editoriais.md` | Voz, densidade, rigor científico, cálculo a serviço da biologia, boxes-"drops" |
| `convencao-latex-mathjax.md` | Fórmulas (Hardy-Weinberg, proporções, taxas) no padrão MathJax + `\ce{}` p/ fotossíntese/respiração |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (cópia idêntica à das outras disciplinas) |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Biologia/blueprints/<série>/<bim>-<bloco>.md`. Séries: **9º ano, 1ª, 2ª e 3ª EM**.

**Escopo: 9º ano + EM.** Do **6º ao 8º a disciplina é Ciências** (`disciplinas/Ciencias/`, kit próprio) — trava no topo do prompt.

## 2. Origem

Kit criado em **19/07/2026**, derivado do kit de Ciências (as instruções e a memória do projeto Claude.ai que o Felipe enviou cobriam Ciências **e** Biologia — a memória cita meiose no 9º ano, ecologia na 1ª série e fisiologia na 2ª). Sem RTF próprio.

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Herda tudo do kit de Ciências:** fechamentos abolidos (Sua Parte · O que a Bíblia diz · Simplificando · Para não esquecer), storytelling migrado para a abertura de cada aula, 220–250 palavras/aula com teto de 300 (ver item 8), frase de transição antes de listas, progressão **fenômeno → modelo**, método/observação só como narrativa histórica, integração bíblica **prática e específica ao tema**.
2. **Boxes:** mesma família, com `🔬 Biologia no Dia a Dia` no lugar de "Ciência do Dia a Dia". Regra dos "drops" (1–2 frases), 1–2 por aula, nunca consecutivos.
3. **Ganhou convenção LaTeX** (Ciências não tem): a disciplina calcula — Hardy-Weinberg ($$p^2 + 2pq + q^2 = 1$$), proporções mendelianas, taxas. Padrão MathJax; `\ce{}` disponível para fotossíntese/respiração (validado no kit de Química).
4. **Regra própria: cálculo a serviço da interpretação biológica**, nunca álgebra abstrata — vem do balizamento da 3ª série nos blueprints ("Hardy-Weinberg como ferramenta de interpretação"). Todo resultado termina em leitura do fenômeno ("4 em cada 100 pessoas carregam o alelo"). Virou item de autovalidação.
5. **Modelos com suas limitações** quando o nível permitir — pedido da memória do projeto para EM.
6. **Temas de fronteira** (origem da vida, evolução, bioética): ciência com rigor + conexão de valor com honestidade, sem forçar concordância nem criar oposição artificial. (Decisão nova deste kit; conferir com o Felipe no piloto.)
7. **Conteúdo denso = fatias finas** (ciclos, frequências, vias metabólicas) — o fatiamento já vem do blueprint; a aula não incha.
8. **O teto não pode virar meta** (21/07/2026). Com teto 400 + piso 250, as 24 aulas do 3º bim saíram todas na faixa 287–400 (média 337) e **nenhuma violou o validador** — o intervalo "seguro" virou o alvo. Correção: teto para **300**, piso afundado para **180** (só pega aula truncada), e alvo declarado de **220–250** no prompt. **Não reabrir sem o Felipe** — foi ele quem pediu o corte após ler os capítulos do 3º bim.
9. **O material é referência do aluno, não texto autoexplicativo** (21/07/2026). Definido pelo Felipe: *"o material é uma referência para o aluno, mas a explicação vem do professor"*. Consequência medida: os capítulos tinham **o mesmo tamanho** do texto-referência que ele aprovou (255 vs 250 palavras) e ainda assim liam como "texto demais" — porque tinham **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. **Contagem de palavras não detecta esse defeito.** Entrou a seção **FORMA DO CONTEÚDO — prosa + marcadores** no prompt (idêntica nas 9 disciplinas), com a regra operacional que produz a mistura certa: **no máximo 2 frases seguidas antes de uma lista**, tabela para 2+ itens a contrastar, definição em 1 frase (se precisar de mais, vira bullet), abertura ≤ 25 palavras, subseções numeradas `N.1`.
10. **Percentual de prosa é diagnóstico, não portão** (21/07/2026). O validador mede (`[2b] Prosa × marcadores`) mas **não reprova** — pedido do Felipe de "deixar mais solto". Travar num percentual produz bullet forçado e raciocínio picotado; o que vale é a regra operacional do item 9. O único aviso que se sustenta sozinho é o caso inequívoco: aula inteira sem lista nem tabela.
11. **Versículo é condicional, nunca por trocadilho** (21/07/2026). Dos 7 versículos do 3º bim, **4 ligavam por palavra**, não por conceito (organela "menor" ↔ "ao menor destes"; população "pequena" ↔ "pequenino"; "todas as manhãs" ↔ "renovam-se cada manhã"; imune "amigo fiel" ↔ "ama o amigo"). **Os trocadilhos vinham prescritos nos blueprints** — a raiz era a regra "1 versículo obrigatório por capítulo". Agora: versículo só com ligação conceitual, validado pelo **teste do sinônimo** (a ligação sobrevive se eu trocar o termo em comum por um sinônimo?); capítulo sem versículo é entrega válida; o blueprint deixa de ser autoritativo neste ponto. **Pendente:** corrigir as conexões VP nos blueprints.

## 4. Estado e próximos passos

- [x] Kit completo (4 arquivos .md + esta memória) — 19/07/2026
- [ ] Subir os arquivos no projeto Claude.ai de Biologia (substituindo o fluxo antigo por unidades)
- [x] Primeiro modelo por série: Evidências da evolução · 9º ano · `modelos/biologia-9ano-modelo.md` — disponível para validação
- [x] Modelos da 1ª, 2ª e 3ª séries produzidos e disponíveis em `modelos/`
- [ ] Confirmar com o Felipe a regra de temas de fronteira (item 6)
- [ ] Após piloto aprovado: registrar ajustes aqui

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado, derivado do kit de Ciências (memória do projeto Claude.ai cobria as duas disciplinas) |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Teto virou meta — recalibrado de novo.** As 24 aulas do 3º bim passaram no validador com média de 337 palavras; o Felipe leu e achou extenso demais. `MIN_PAL, MAX_PAL = 250, 400` → **`180, 300`**; prompt, CLAUDE.md e INSTRUCOES passaram a declarar **alvo 220–250 · teto 300**, com aviso explícito de que o teto não é meta. Prompt ganhou seção "onde a gordura aparece" (4 padrões diagnosticados nos capítulos do 3º bim). Capítulos do 3º bim reproduzidos com o kit novo |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |
| 21/07/2026 | **Resultado final da recalibragem:** 337 → **232 pal./aula**, prosa 78% → 51%, zero aulas sem lista (eram 11 de 24). Versículos de 7 para 2 — sobreviveram Gn 1:27 no código genético universal (9º ano) e em Hardy-Weinberg/"não existe indivíduo geneticamente superior" (3ª série), os dois casos em que o conteúdo levanta a questão do valor humano por conta própria. |
| 21/07/2026 | Capítulo-piloto do 9º ano transferido para `modelos/biologia-9ano-modelo.md`; criada a organização de um modelo por série, com validação independente. |
| 21/07/2026 | Conjunto de modelos concluído: 9º ano e 1ª–3ª séries do EM, todos conferidos com o validador de Biologia. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Biologia/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra. |
