# Memória do Kit — Estudos Sociais · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **21/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Estudos Sociais** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Molde replicado dos kits de **Português** (piloto aprovado), **Química** e **Física**. Sem arquivo de LaTeX — a disciplina não usa fórmulas.

| Arquivo | Papel |
|---|---|
| `prompt-producao-capitulo.md` | Prompt de produção — preencher campos `{ }` e enviar junto com os demais arquivos |
| `instrucoes-geografia-historia-EM.md` | **Complemento obrigatório para 1ª–3ª série** (Geografia/História) — o que muda no EM; prevalece sobre o prompt |
| `regras-editoriais.md` | Voz, tom, densidade (regra anti-redundância), tabelas, sensibilidade cultural/religiosa |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (cópia idêntica à das outras disciplinas) |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `disciplinas/Estudos Sociais/blueprints/<ano>/` (Fund), `disciplinas/Geografia/blueprints/<série>/` ou `disciplinas/Historia/blueprints/<série>/` (EM).

**Escopo: a área geo-histórica inteira, num kit só** (decisão do Felipe, 19/07/2026 — "normalmente eu não faço separado"). 6º–9º = **Estudos Sociais** (matéria única); 1ª–3ª EM = **Geografia** e **História** separadas (3 aulas/sem cada), produzidas com o prompt principal **+** `instrucoes-geografia-historia-EM.md`. **Não criar kits separados** para Geografia e História.

## 2. Origem

Kit criado em **19/07/2026** a partir da memória do projeto Claude.ai (`Estudos Sociais.rtf` — continha a memória de Estudos Sociais/Geografia/História e, por engano de colagem, também a de Física, que foi ignorada aqui por já estar absorvida no kit de Física). **Absorvido e apagado** após conferência. Diferente de Química/Física, o RTF não trazia o prompt de instruções — só a memória com as regras de formatação acumuladas; o prompt foi construído sobre elas + blueprints + molde dos kits anteriores.

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Fechamentos abolidos** — a estrutura antiga (Introdução · E para hoje · Simplificando · Para não esquecer · Sua Parte · "Explorando os Conceitos") não existe mais. Pontes com o presente e reflexão viram tecido das aulas + box 💭; conexão VP vira versículo + parágrafo curto na aula pertinente (sem bullets de "valores", sem pergunta de encerramento); resumos saíram.
2. **Extensão enxuta: preferir 180–220 palavras de conteúdo por aula, teto firme de 300 e sem mínimo.** O piloto mostrou que uma aula completa pode ficar em 170 palavras; profundidade vem do tratamento do conceito, não do volume.
3. **Regra anti-redundância é a marca do kit** (principal aprendizado do projeto antigo): nunca parágrafo + lista repetindo o mesmo conteúdo; condensar preservando conceitos (o projeto antigo pedia reduções de 20–35% sem perda).
4. **Tabelas: máx. 2 por capítulo, só para comparações genuínas** (aprendizado do projeto antigo — excesso de tabela deixa o material "estranho" para apostila).
5. **Boxes:** família própria — 🔎 Curiosidade (máx. 2 frases) · 💭 Você já pensou nisso? (2–3 frases) · 👤 Esse foi o "cara" (personagem-chave: 3 bullets + linha de legado, 1×/capítulo). 1–2 por aula, nunca consecutivos, quebra de linha interna. Os nomes vêm do formato antigo; os emojis foram padronizados agora.
6. **Sensibilidade religiosa e cultural** (regra dos blueprints): tradições vivas com dignidade; distinguir relato de tradição × evidência arqueológica ("segundo a tradição..." / "os historiadores debatem..."); sem hierarquia de valor entre culturas.
7. **Versículos não se repetem entre capítulos** (caso Lucas 16:10 do projeto antigo) — o âncora de cada capítulo vem do blueprint.
8. **História = processo** (causas/consequências/rupturas, múltiplas perspectivas) · **Geografia = raciocínio geográfico** (sociedade-natureza, escalas) — balizamento das Diretrizes, reforçado nos blueprints.
9. **Divisão do EM explicada no ESCOPO do prompt** (decisão do Felipe, 19/07): o prompt abre com "ESCOPO — LEIA ANTES DE PRODUZIR", com a tabela segmento × disciplina × blueprints. Motivo: o prompt é o arquivo que a IA lê toda vez.
10. **Geografia e História do EM ficam NESTE kit, não em kits separados** (decisão do Felipe, 19/07 — "normalmente eu não faço separado"). A versão anterior do ESCOPO recusava pedidos de EM e mandava procurar outro kit; foi substituída: agora o prompt atende a área inteira e o EM entra com o complemento `instrucoes-geografia-historia-EM.md`, que trata do que muda:
    - profundidade N3/N4 (interpretar e relacionar, não só narrar); juízo historiográfico e leituras em disputa;
    - **referência-chave no texto, sem box 👤** (o box fica só no Fundamental) — pensador/economista/historiador, único por tema;
    - dados/datas/casos concretos obrigatórios, com referência de tempo e **nenhum número inventado**;
    - neutralidade em temas vivos: nem hagiografia nem demonização, conquistas e limites de cada lado;
    - ENEM mencionado em 1 frase quando natural, **sem** "caso ENEM"/questão/simulado (proibido nos blueprints);
    - um capítulo = uma disciplina (nunca misturar recorte de Geografia e História).
11. **Paragrafação enxuta e respiro visual** (piloto de 21/07): cada parágrafo traz uma ideia principal, preferencialmente em uma frase curta; duas frases só quando completam o mesmo encadeamento. Blockquote simples (`>`) destaca ressalva histórica, distinção entre fontes, contraste ou síntese; não tem emoji nem título, não é box e não entra no limite de boxes. Nunca há três parágrafos consecutivos sem lista, tabela, box ou blockquote; preferir um respiro por subseção e usar um segundo apenas quando necessário para interromper outra sequência.
12. **Alternância entre subtópicos com e sem marcadores** (21/07/2026, ajuste do Felipe): dentro da mesma aula, dois `###` sem bullets não ficam seguidos. Um deles deve organizar em marcadores causas, consequências, etapas, exemplos, grupos ou contrastes já presentes no conteúdo. Subtópicos com marcadores podem ser consecutivos; lista sem função didática continua proibida.

## 4. Estado e próximos passos

- [x] Kit completo e consistente (4 arquivos .md + esta memória) — 19/07/2026
- [x] Instruções de Geografia e História (EM) criadas dentro deste kit — 19/07/2026
- [ ] Subir os arquivos no projeto Claude.ai (substituindo o fluxo antigo por unidades) — **os 4 .md juntos**
- [x] Primeiro modelo por ano: Civilizações do Oriente Antigo · 6º ano · `modelos/estudos-sociais-6ano-modelo.md` — usado para calibrar concisão e respiro visual
- [x] Modelos do 4º ao 9º ano produzidos e disponíveis em `modelos/`
- [ ] Capítulo piloto do EM (sugestão: Fundamentos e regulação do comércio internacional · Geografia · 2ª série · `3bim-bloco2.md` — testa densidade conceitual, dados e Smith × Prebisch sem escolher lado)
- [ ] Após pilotos aprovados: registrar ajustes aqui

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado a partir da memória do projeto antigo (RTF), no molde de Português/Química/Física |
| 19/07/2026 | RTF original apagado após conferência (continha também memória de Física, já absorvida no kit dela); pasta só com .md |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |
| 21/07/2026 | **Piloto de Estudos Sociais ajustado com o Felipe:** faixa preferencial passou a 180–220 palavras (teto 300, sem mínimo); parágrafo passou a uma ideia principal, preferencialmente em uma frase; blockquote simples passou a funcionar como respiro visual para ressalva histórica, contraste, distinção entre fontes ou síntese, sem ser confundido com box. |
| 21/07/2026 | Capítulo-piloto do 6º ano transferido para `modelos/estudos-sociais-6ano-modelo.md`; criada a organização de um modelo por ano, com validação independente. |
| 21/07/2026 | Conjunto de modelos do Fundamental concluído do 4º ao 9º ano; todos recalibrados para parágrafos enxutos, 180–220 palavras e respiro visual. |
| 21/07/2026 | Regras visuais de Ciências aplicadas a Estudos Sociais: nenhum trecho com três parágrafos corridos e nenhum par de subtópicos sem marcadores. Os seis modelos foram revisados, e o validador ganhou as checagens `[2a] Ritmo visual da prosa` e `[2b] Alternância de subtópicos`. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Estudos Sociais/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** aplicada a atualização pendente registrada em `conteudos-prontos/_PROGRESSO.md` — tabela de ESCOPO ganhou a linha do 4º–5º ano, e a seção LINGUAGEM ganhou a linha do 4º–5º EF (com o lembrete de sensibilidade histórica). INSTRUCOES-DO-PROJETO e CLAUDE.md atualizados no mesmo sentido. |
