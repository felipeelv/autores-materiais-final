# Memória do Kit — Física · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **23/07/2026**.

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
4. **Box 🧪 Experimente abolido** — material não propõe experimentos (regra da reorganização; observação/experimento entram só como contexto narrativo). Família mantida: 💭 ⏸️ 💡 📏 ⚡ 📐, com 👤 apenas na última aula para biografia acessória útil · 1–2 por aula · nunca consecutivos · 1–2 frases.
5. **LaTeX no padrão MathJax** — Auto-LaTeX Equations (Google Docs) com renderizador MathJax. Restrições antigas do CodeCogs (proibir `\text{}`, `\;`, `\,`, acentos) **revogadas**. Padrões: unidades `\,\mathrm{}`, vírgula decimal `{,}`, milhar `\,`, vetores `\vec{}`. Se surgir equação química, usar `\mathrm{}` e setas manuais; `\ce{}`/mhchem está proibido após falha confirmada no render final.
6. **Frase de transição obrigatória antes de toda lista** ("Isso acontece porque:") — marca registrada do estilo de Física, mantida.
7. **Nomenclatura didática brasileira** (aprendizado do projeto antigo): isobárica = "Lei de Gay-Lussac (1ª lei)", isocórica = "Lei de Gay-Lussac (2ª lei)" — não "Lei de Charles" para isobárica. Tabela em `regras-editoriais.md` §4.
8. **Abertura de aula:** cena/fenômeno concreto com tensão em 1–2 frases; a lei nunca abre a aula. Progressão: fenômeno → lei → modelo idealizado → expressão matemática.
9. **TikZ exige revisão em duas escalas:** primeiro a figura isolada no original e a 300 px; depois o capítulo já diagramado na largura real da coluna ou página. Na prévia de 300 px, rótulos e traços não relacionados mantêm ao menos 8 px, casos empilhados mantêm 16 px, vetores não cobrem cordas/superfícies/trajetórias e nunca atravessam letras dentro dos corpos. A publicação inicial é provisória até a revisão no capítulo.
10. **Passada específica de exatas + auditoria semântica:** grandeza estabelecida não tem unidade redeclarada; grandeza nova declara unidade uma única vez; inventários de unidades são proibidos; todo valor de cálculo precisa ter sido dado ou obtido antes; exemplos usam uma operação por linha. História essencial fica junto ao conceito e biografia acessória, se útil, vai para um único box 👤 final. Box precisa acrescentar informação e prosa não repete tabela. `validar-capitulo.py` cobre o determinístico; `auditar-fisica.py` usa contrato JSON, confiança alta/média/baixa e envia ao humano apenas conflitos de baixa confiança.

## 4. Estado e próximos passos

- [x] Kit completo e consistente (4 arquivos .md + esta memória) — 19/07/2026
- [ ] Subir os arquivos no projeto Claude.ai de Física (substituindo as instruções antigas por unidades)
- [x] Capítulo piloto: Leis de Newton · 1ª série · `modelos/fisica-1serie-modelo.md`
- [x] Modelos do 6º ao 9º ano e da 1ª à 3ª série produzidos e disponíveis em `modelos/`
- [x] Produção do 3º bimestre concluída: 17 capítulos · 84 aulas · arquivos locais e pasta oficial sincronizados
- [x] Padrão TikZ de Física criado e capítulo-piloto `Aplicações da dinâmica` renderizado com oito figuras locais
- [x] Oito figuras do piloto aprovadas, publicadas, indexadas e sincronizadas
- [x] Padrão editorial de exatas consolidado no `AUTOR.md`; capítulo-piloto revisado e contrato semântico criado
- [x] Sete modelos revisados e 17 capítulos aprovados pela validação mecânica
- [ ] Replicar contratos semânticos quando cada capítulo entrar em nova revisão editorial
- [x] Plano dos demais capítulos concluído: 95 figuras distribuídas em 16 documentos
- [x] Fontes, manifestos e 95 PNGs locais criados, renderizados e validados; revisão isolada no original e a 300 px concluída
- [x] Galerias aprovadas; 95 PNGs publicados, indexados e validados por SHA-256
- [x] Dezesseis capítulos revisados em coluna de 720 px, validados e sincronizados no Google Drive com leitura de retorno idêntica
- [ ] **Próximo chamado:** não há pendência nas imagens do 3º bimestre; manter o mesmo fluxo de revisão dupla nas próximas produções
- [ ] Validar visualmente os sete modelos com o Felipe
- [ ] Após piloto aprovado: registrar ajustes aqui e replicar aprendizados aos próximos kits

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado a partir do `Fisica.rtf` (instruções + memória do projeto antigo), no molde de Português/Química |
| 19/07/2026 | LaTeX já nasce no padrão MathJax; a validação inicial de mhchem foi posteriormente revogada |
| 19/07/2026 | RTF original apagado após conferência; pasta só com .md |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |
| 21/07/2026 | **Física não leva versículo + volume não cresce com a série.** As 9 conexões VP dos blueprints são analogia ("assim como [fenômeno], assim [lição]"), e a Física nunca levanta a questão do valor humano — mesma conclusão de Geometria. Versículos removidos dos 9 capítulos do 3º bim. Junto: extensão apertada duas vezes (240 → **190**, piso 110) porque o 6º ano continuava com "muita explicação", e registrada a regra de que **o volume não cresce com a série** — a produção vinha entregando 180 pal./aula no 6º ano e 303–341 no EM sem que nada no kit pedisse isso. **Pendente:** rever a conexão VP nos blueprints ou tirar VP da disciplina. |
| 21/07/2026 | **Conjunto de modelos concluído:** um capítulo por ano/série, do 6º ano à 3ª série EM. Os capítulos do 3º bimestre serviram apenas de matéria-prima e foram reescritos no padrão atual: 130–170 palavras por aula, subtópicos numerados, prosa curta + marcadores, fórmulas com grandezas e unidades SI, exemplos em etapas e zero versículo. Os sete passam no validador de Física. |
| 23/07/2026 | **3º bimestre concluído:** produzidos os oito capítulos do Bloco 2, totalizando 42 novas aulas entre 113 e 190 palavras, com média de 167,4. O bimestre fecha com 17 capítulos e 84 aulas. Todos os novos arquivos foram validados e enviados para `Segundo Semestre/Física`; `Força e movimento.md` e `Forças mecânicas.md`, já prontos, também foram sincronizados. Controle final em `Acompanhamento de produção.md`. |
| 23/07/2026 | **Piloto TikZ iniciado:** os 17 capítulos foram agrupados em cinco famílias visuais. `Aplicações da dinâmica` (1ª série, cap. 3) foi escolhido por reunir gráfico, DCL, decomposição vetorial, movimento circular e sistema com polia. Criados `PADRAO-DE-IMAGENS-TIKZ.md`, estilo `eleve-fisica.sty` e oito figuras locais, validadas e revisadas a 300 px. Nada foi aprovado, publicado, indexado ou sincronizado nesta etapa. |
| 23/07/2026 | **Piloto TikZ concluído:** após solicitação do Felipe para visualizar o capítulo pronto, as oito figuras foram aprovadas e publicadas; as URLs foram indexadas no Markdown, os hashes públicos foram confirmados e `Aplicações da dinâmica.md` foi atualizado no Google Drive. Prints da diagramação revelaram proximidade excessiva nas figuras 6 e 8; os espaços internos e as setas de aceleração foram corrigidos e republicados no commit vigente `9934fd2ba023`. |
| 23/07/2026 | **Regra antissobreposição consolidada:** o problema só ficou evidente no capítulo diagramado, embora as figuras isoladas passassem a 300 px. O padrão geral e o de Física agora exigem revisão dupla, respiros mínimos de 8/16 px, vetores fora de cordas e superfícies e identificadores livres do caminho das setas. |
| 23/07/2026 | **Regras de exatas implementadas:** o `AUTOR.md` passou a proibir inventário de unidades, redeclaração de grandezas estabelecidas, valores implícitos e cálculos encadeados; também separa história essencial de biografia acessória e exige novidade em boxes e complemento entre tabela e prosa. O validador ganhou a passada `[2c]`; `auditar-fisica.py`, `CONTRATO-SEMANTICO.md` e o contrato do piloto automatizam sequenciamento, novidade de box, repetição tabela–prosa e classificação histórica por confiança. O piloto passou sem achados; correções mecânicas foram aplicadas aos demais capítulos; os sete modelos foram revisados. |
| 23/07/2026 | **Sincronização da revisão de exatas:** as versões corrigidas de `Aplicações da dinâmica`, `Máquinas simples`, `Energia mecânica e potência`, `Refração e lentes`, `Força magnética` e `Indução eletromagnética` substituíram os mesmos seis arquivos na pasta oficial do Google Drive. A leitura de retorno confirmou IDs, títulos, tamanhos em bytes e marcadores exclusivos dos novos conteúdos. |
| 23/07/2026 | **Demais imagens de Física produzidas localmente:** os 16 capítulos restantes foram mapeados em `PLANO-DE-IMAGENS-TIKZ.md`; 95 fontes/páginas TikZ e seus manifestos foram criados, renderizados em PNG transparente a 300 DPI, revisados no original e a 300 px sobre branco e validados localmente. As galerias estão em `REVISAO-TIKZ-DEMAIS-CAPITULOS.md`. Publicação, indexação, revisão diagramada e sincronização aguardam aprovação visual. |
| 23/07/2026 | **Coleção TikZ de Física concluída:** após aprovação do Felipe, as 95 figuras restantes foram registradas como aprovadas, publicadas nos commits por capítulo até `8a79200b98f7`, indexadas nos 16 Markdown e conferidas em coluna de 720 px. Os 95 hashes públicos coincidem com os builds locais; os 16 capítulos passam no validador e foram substituídos nos mesmos arquivos do Google Drive. A leitura de retorno confirmou conteúdo byte a byte idêntico e exatamente 95 blocos TikZ. A coleção fecha com 103 PNGs de Física. |
| 23/07/2026 | **Convenção química corrigida:** a falha de mhchem confirmada no render de Química foi propagada para Física. O autor passou a usar `\mathrm{}` e `\rightarrow` em eventuais equações químicas, e o validador reprova qualquer ocorrência de `\ce{}`. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Fisica/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra (teto próprio de 190 mantido). |
