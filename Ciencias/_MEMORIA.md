# Memória do Kit — Ciências · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **23/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Ciências** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Molde dos kits de Português/Química/Física/Estudos Sociais/Matemática. Sem arquivo de LaTeX — a disciplina não usa fórmulas (dados numéricos vão em texto normal).

| Arquivo | Papel |
|---|---|
| `prompt-producao-capitulo.md` | Prompt de produção — abre com ESCOPO (6º–8º); campos `{ }` |
| `regras-editoriais.md` | Voz, densidade, progressão fenômeno→modelo, boxes-"drops", integração bíblica |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (cópia idêntica à das outras disciplinas) |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Ciencias/blueprints/<ano>/<bim>-<bloco>.md`.

**Escopo: 4º ao 8º ano.** No **9º ano e no EM a disciplina vira Biologia** (`disciplinas/Biologia/`). O projeto Claude.ai antigo cobria Ciências e Biologia juntas; a reorganização separa as duas disciplinas.

## 2. Origem

Kit criado em **19/07/2026** a partir das instruções + memória do projeto Claude.ai de Ciências (enviadas pelo Felipe no chat, sem arquivo), cruzadas com os blueprints e o molde dos kits anteriores.

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Fechamentos abolidos** — a estrutura antiga (Introdução storytelling · 🤝 Sua Parte · O que a Bíblia diz · Simplificando · Para não esquecer) não existe mais. Aplicação vira tecido das aulas + box 🔬; conexão VP vira versículo + parágrafo curto na aula pertinente (sem "Olhe como você pode fazer", sem lista de ações); resumos saíram. O storytelling (cena → tensão) migrou para a **abertura de cada aula**.
2. **Extensão enxuta: no máximo 400 palavras de conteúdo por aula.** Teto definido pelo Felipe em 20/07; a faixa de 350–500 de 19/07 saiu prolixa na prática.
3. **Boxes:** família real do projeto mantida — 💭 Pense um pouco · ⏸️ Pare e Pense · 💡 Você sabia? · 📏 Medidas Interessantes · 🔬 Ciência do Dia a Dia. Regra dos "drops" (1–2 frases) preservada da memória; **1–2 por aula e nunca consecutivos** (a regra antiga era "mínimo 1 por seção" — virou máximo, coerente com a aula enxuta).
4. **Método/observação só como narrativa histórica** (cena de Hooke, microscópio de Leeuwenhoek) — nunca experimento a executar. Regra da família Empíricas nos blueprints; caiu o antigo box de prática.
5. **Progressão fenômeno → modelo** obrigatória (Diretriz de Ciências, §1.2 citada nos blueprints): nunca abrir pelo modelo abstrato.
6. **Frase de transição antes de toda lista** — preservado da memória do projeto (mesma marca do kit de Física).
7. **Integração bíblica prática e específica ao tema**, nunca genérica — aprendizado explícito da memória do Felipe.
8. **Títulos de subtópico podem ser perguntas orientadoras** (estilo do projeto antigo), desde que cubram o tópico do blueprint.
9. ~~**EF I (4º–5º ano) fora de escopo**~~ — **revogado em 20/07/2026.** O Felipe pediu explicitamente a produção do 4º e do 5º ano, e os blueprints do EF1 já existiam (`blueprints/{4ano,5ano}/`). O kit agora atende **4º ao 8º ano**. Ver decisão 10.
10. **EF1 usa a coluna 4º–5º EF do `_PADROES-DE-ESCRITA.md` (§2), que substitui a seção LINGUAGEM do prompt** — esta é calibrada para 11–14 anos e não serve para 9–10. Parâmetros que mandam no EF1: frases muito curtas em ordem direta (≈ até 12 palavras), **exemplo concreto → conceito sem exceção**, vocabulário do dia a dia com glosa na estreia, **abstração nenhuma**, 2 exemplos por conceito, exceções e casos raros nunca entram, e tom de professor próximo **sem infantilizar, sem diminutivo, sem personagem falante** (o erro típico da faixa é infantilizar, não escrever difícil). Opera em N1–N3; N4 não aparece. A faixa específica de Ciências agora é 140–200 palavras, com teto de 220; o recorte completo prevalece sobre a contagem. Os blueprints do EF1 são autossuficientes e já trazem esses avisos.
11. **Respiro visual em subseções sem estrutura** (21/07/2026, pedido do Felipe após o piloto de Ciências): toda subseção `###` sem lista ou tabela recebe uma frase-chave em blockquote simples (`> ...`). Box padronizado ou versículo já cumpre a função. O blockquote não repete a frase anterior e não vira mini-resumo.
12. **Ciências mais concisa e direta** (recalibrada em 23/07/2026, pedido do Felipe): faixa preferencial própria de **140–200 palavras por aula**, substituindo nesta disciplina o padrão comum de 220–250; teto firme de 220. Parágrafos de uma frase sempre que possível, no máximo duas; sem frase de amarração depois de lista/tabela e sem preenchimento para alcançar contagem.
13. **Profundidade não aumenta o volume** (21/07/2026, pedido do Felipe): do 4º ao 8º ano, toda aula mantém 2–3 subseções, parágrafos de 1–2 frases e o mesmo ritmo visual. A progressão acontece por substituição — vocabulário mais preciso, relações causais, comparação, classificação e limites do modelo — nunca por mais parágrafos, exemplos ou subseções. No EF1, dois exemplos curtos ocupam o espaço que, no 8º ano, recebe maior densidade conceitual.
14. **Respiro distribuído dentro da subseção** (21/07/2026, ajuste do Felipe): um blockquote apenas no fim não resolve uma sequência longa de prosa. Ciências não deixa três parágrafos consecutivos sem lista, tabela, box ou blockquote; antes do terceiro, a ideia de contraste, alerta, exceção ou síntese ganha destaque. O validador da disciplina reprova essa sequência automaticamente.
15. **Alternância entre subtópicos com e sem marcadores** (21/07/2026, ajuste do Felipe): dentro da mesma aula, dois `###` sem bullets não ficam seguidos. Um deles deve organizar em marcadores uma enumeração, etapas, exemplos, causas, efeitos ou contrastes que já existam no conteúdo. Subtópicos com marcadores podem ser consecutivos; não se inventa lista sem função didática.

## 4. Estado e próximos passos

- [x] Kit completo (3 arquivos .md + esta memória) — 19/07/2026
- [ ] Subir os arquivos no projeto Claude.ai de Ciências (substituindo o fluxo antigo por unidades)
- [x] Primeiro modelo por ano: A célula, unidade da vida · 6º ano · `modelos/ciencias-6ano-modelo.md` — disponível para validação
- [x] Modelos do 4º ao 8º ano produzidos e disponíveis em `modelos/`
- [x] 3º bimestre concluído: 21 capítulos, 90 aulas, zero falhas e entrega oficial no Google Drive
- [x] Padrão final de concisão: preferência de 140–200 palavras, teto de 220 e média real de 160
- [ ] Criar o kit de **Biologia** (9º + EM) derivado deste, quando for a vez
- [ ] Após piloto aprovado: registrar ajustes aqui

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado a partir das instruções + memória do projeto Claude.ai (coladas no chat), no molde dos kits anteriores |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 20/07/2026 | **Escopo estendido ao Fundamental I por pedido do Felipe** (decisões 9 e 10 acima). O kit passa a valer do **4º ao 8º ano**; 9º e EM continuam em Biologia. A seção ESCOPO do `prompt-producao-capitulo.md` ainda diz "6º ao 8º" — **atualizar** ao mexer no arquivo |
| 20/07/2026 | **Bloco 1 do 3º Bimestre produzido inteiro: 10 capítulos, 45 aulas** (4º ao 8º ano), em `conteudos-prontos/Ciencias/<ano>/`. Todos passam no validador. Aprendizado da rodada: o teto de 400 é a regra mais violada — **9 das 45 aulas saíram acima e precisaram de corte**, inclusive uma em 463. Vale exigir a contagem antes da entrega, não depois |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |
| 21/07/2026 | **Ajuste após o piloto de Ciências:** subseção sem lista/tabela ganha respiro visual em blockquote simples; faixa preferencial passa a 180–220 palavras por aula; parágrafos ficam limitados a 1–2 frases, sem recapitulação ou preenchimento. |
| 21/07/2026 | **Volume uniforme do 4º ao 8º ano:** profundidade passa a ser tratada como densidade conceitual dentro da mesma extensão, nunca como aumento de texto. Regra registrada no manual e no checklist. |
| 21/07/2026 | Capítulo-piloto do 6º ano transferido para `modelos/ciencias-6ano-modelo.md`; criada a organização de um modelo por ano, com validação independente. |
| 21/07/2026 | Conjunto de modelos concluído do 4º ao 8º ano; capítulos antigos foram recalibrados para 180–220 palavras, profundidade uniforme e respiro visual. |
| 21/07/2026 | Respiro visual refinado nos cinco modelos: não pode haver três parágrafos consecutivos de prosa. Contrastes e sínteses foram distribuídos em blockquotes; o validador de Ciências ganhou a checagem `[2a] Ritmo visual da prosa`. |
| 21/07/2026 | Alternância de subtópicos refinada nos cinco modelos: dois `###` consecutivos não podem ficar ambos sem marcadores. O validador de Ciências ganhou a checagem `[2b] Alternância de subtópicos`. |
| 23/07/2026 | **3º bimestre concluído:** os dez capítulos antigos foram revisados e onze novos foram produzidos, totalizando 21 capítulos e 90 aulas. Todos passam no validador. Média final de 160,3 palavras por aula, sem nenhuma acima de 220. |
| 23/07/2026 | Os 21 arquivos foram salvos na pasta oficial de Ciências no Google Drive, organizados do 4º ao 8º ano e conferidos sem divergência de tamanho. O acompanhamento final está em `Ciencias/Acompanhamento de produção.md`. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Ciencias/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** aplicada a atualização pendente das decisões 9–10 — ESCOPO do prompt agora diz 4º ao 8º ano, e a seção LINGUAGEM ganhou a linha do 4º–5º EF (via `_PADROES-DE-ESCRITA.md` §2). INSTRUCOES-DO-PROJETO e CLAUDE.md atualizados no mesmo sentido. |
