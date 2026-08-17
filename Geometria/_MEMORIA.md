# Memória do Kit — Geometria (Matemática 2) · Reorganização 2026 · 2º Semestre

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **22/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Geometria** consome para produzir capítulos (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Cobre **plana, espacial, analítica, trigonometria e transformações**, do 6º ano à 3ª série.

| Arquivo | Papel |
|---|---|
| `INSTRUCOES-DO-PROJETO.md` | texto para colar no campo *Instruções do projeto* |
| `CLAUDE.md` | mapa do conhecimento (índice, blueprint, glossário) |
| `prompt-producao-capitulo.md` | prompt de produção com campos `{ }` |
| `regras-editoriais.md` | voz, **figuras**, **construções**, rigor geométrico |
| `convencao-latex-mathjax.md` | notação geométrica, unidades, ASCII, exemplo resolvido |
| `convencao-ortografica.md` | Acordo Ortográfico + escolhas da casa |

**Blueprints:** `Reorganizacao-2026-2Semestre/disciplinas/Geometria/blueprints/<ano>/` (~46k tokens).

## 2. Origem

Criado em **19/07/2026** a partir do kit único de Matemática, **separado por decisão do Felipe** no mesmo dia: *"eu preciso de uma pasta para cada matemática, porque elas têm regras diferentes"*. As regras próprias vieram da leitura dos blueprints de Geometria.

## 3. Decisões registradas (não reabrir sem o Felipe)

**Herdadas do tronco comum:** fechamentos abolidos · no máximo 400 palavras/aula · passo a passo obrigatório · exemplo resolvido com frase natural + Resolução/Passos(`-`)/Resposta · boxes só 🔢/⚠️ (1 frase) · matemático-referência no texto sem box · LaTeX MathJax (restrições CodeCogs revogadas) · VP sem analogia explícita.

**Próprias desta disciplina:**

1. **Figuras TikZ/PNG são permitidas e integram o conteúdo quando a configuração visual favorece a compreensão.** Toda a produção privada fica exclusivamente em `../_tikz/<disciplina>/<ano-serie>/<titulo>/`: fonte `.tex`, manifesto e `build/`. Somente o PNG transparente aprovado vai ao repositório público `felipeelv/imagens-tikz`; o Markdown privado usa URL absoluta e texto alternativo idêntico ao manifesto. O padrão não usa cartão de fundo nem painéis brancos, prioriza composição vertical ou quase quadrada e exige revisão na largura efetiva mínima de 300 px sobre branco, sem contato ou cruzamento entre textos, linhas, setas e marcas. ASCII simples continua permitido quando for suficiente. Referências vagas como "veja a figura ao lado" não substituem a identificação do que deve ser observado.
2. **Construções (régua, compasso, transferidor, GeoGebra) = procedimento descrito, nunca atividade proposta** — regra explícita das regras transversais dos blueprints ("as construções com instrumentos/software entram como procedimento descrito no conteúdo, não como atividade").
3. **Justificativa antes da fórmula** — fórmula sem o "porquê" é decoreba. Demonstração formal só quando o blueprint pedir.
4. **Resultado sempre com unidade** (cm, m², cm³, °) — resultado sem unidade é erro.
5. **Não infantilizar:** quando o conteúdo é novidade crítica da série (transformações no 8º, trigonometria no 9º/EM), o vocabulário técnico é o conteúdo — regra vinda do balizamento dos blueprints.
6. **Abertura visual concreta** (azulejo, rampa, sombra, embalagem, esteira) — a geometria entra pelo olho.
7. **Notação própria** na convenção LaTeX: `\overline{AB}`, `\angle`, `\triangle`, `^{\circ}`, `\parallel`, `\perp`, `\cong`, `\sim`, `\vec{v}`.

## 4. Estado e próximos passos

- [x] Kit completo (6 arquivos + esta memória) — 19/07/2026
- [ ] Montar o projeto no claude.ai (ver `_COMO-MONTAR-OS-PROJETOS.md` na pasta acima)
- [x] Capítulo piloto: Transformações geométricas · 8º ano · `modelos/geometria-8ano-modelo.md`
- [x] Sete capítulos-modelo, um por ano/série do 6º ano à 3ª série do Ensino Médio, em `modelos/`
- [x] Criador TikZ privado em `../_tikz/`, com estilo, manifesto, renderização, revisão, publicação e indexação
- [x] Repositório público exclusivo `felipeelv/imagens-tikz`, inicializado sem fontes ou conteúdos privados
- [x] Modelo do 6º ano com seis figuras TikZ aprovadas, publicadas e indexadas
- [x] Padrão definitivo salvo em `../_tikz/PADRAO-DE-CONSTRUCAO.md` e plano das 45 figuras restantes em `PLANO-DE-IMAGENS-TIKZ.md`
- [x] Sete capítulos inicialmente tratados do bloco 1 com 51 figuras transparentes publicadas e sincronizadas no Google Drive
- [x] Lacuna curricular da 3ª série identificada: o Capítulo 2 do bloco 1, **Parábola: definição e equações reduzidas**, ainda não havia sido produzido
- [x] Sete capítulos do bloco 2 e o pré-requisito ausente da 3ª série produzidos, validados e copiados para o Google Drive — 8 capítulos e 32 aulas
- [x] Plano das 60 novas figuras consolidado em `PLANO-DE-IMAGENS-TIKZ-BLOCO2.md` — 56 do bloco 2 e 4 da correção de continuidade
- [x] Produzir, revisar, publicar e indexar as 60 figuras planejadas — total acumulado de 111 PNGs
- [x] Checkpoint técnico salvo no plano do bloco 2, com os oito commits públicos e a auditoria dos 111 arquivos
- [ ] Validar visual e editorialmente os sete modelos com o Felipe

## 5. Histórico

| Data | O quê |
|---|---|
| 19/07/2026 | Kit criado na separação das três matemáticas, com regras próprias de figura e construção |
| 20/07/2026 | Extensão recalibrada: **teto firme de 400 palavras/aula** (as aulas estavam saindo prolixas) e piso de 350 abolido — 250–300 palavras bastam se o recorte foi coberto. No validador o teto reprova; ficar abaixo do piso só avisa |
| 20/07/2026 | `validar-capitulo.py`: seção de fechamento passou a comparar o título inteiro ("fotossíntese"/"síntese proteica" eram reprovadas por substring) e a extensão deixou de falhar por aula curta — as duas travavam a produção |
| 21/07/2026 | **Recalibragem de forma e extensão (vale para as 9 disciplinas).** Diagnóstico em Biologia: os capítulos tinham o mesmo tamanho do texto-referência aprovado pelo Felipe (255 vs 250 palavras) e ainda liam como "texto demais" — **78% de prosa corrida contra 46% da referência**, e 11 de 24 aulas sem uma única lista. Mudanças: `MIN_PAL, MAX_PAL = 180, 300` (era 250, 400 — o teto virava meta); prompt ganhou a seção **FORMA DO CONTEÚDO — prosa + marcadores** (o material é referência do aluno, a explicação é do professor; máx. 2 frases seguidas antes de uma lista; tabela para 2+ itens; subseções numeradas `N.1`); validador ganhou `[2b] Prosa × marcadores`, que **diagnostica e não reprova** (travar num percentual só produz bullet forçado). Versículo virou **condicional**: só com ligação conceitual, validada pelo **teste do sinônimo** — 4 dos 7 versículos de Biologia ligavam por trocadilho, todos prescritos nos blueprints. |
| 21/07/2026 | **Geometria não leva versículo.** As 4 conexões VP dos blueprints são analogia (invariância geométrica ↦ dignidade), o que o `regras-editoriais.md` desta disciplina já proibia ("sem analogia explícita"). Diferente de Biologia/Financeira, o conteúdo de Geometria nunca levanta a questão do valor humano. Versículos removidos dos 4 capítulos do 3º bim. **Pendente:** rever a conexão VP nos blueprints ou tirar VP da disciplina. |
| 21/07/2026 | **Extensão apertada: alvo 170–210, teto 240** (padrão da casa é 300). Geometria é fórmula-e-figura: o desenho e a tabela carregam o que em Humanas precisaria de frase. Medido antes: **378 palavras/aula**, a maior do projeto, com `"Veja o exemplo abaixo."` em 10 das 12 aulas — frase que o próprio prompt prescrevia. Prompt ganhou "O que é enumerável nesta disciplina" (tabela *o que preserva × o que muda* é o formato mais consultado) e "Filler característico". Os 4 capítulos do 3º bim refeitos: **236 pal./aula, 41% de prosa**. |
| 21/07/2026 | **Modelos concluídos do 6º ano à 3ª série.** Os sete capítulos do primeiro bloco do 3º bimestre foram reescritos no formato consolidado: subtópicos numerados, descrição reconstruível das configurações, justificativa antes da fórmula, exemplos resolvidos em todas as aulas, unidades nos resultados e nenhum versículo. Pela regra então vigente, não foram criadas imagens nem arquivos TikZ; descrições verbais e notação substituíram figuras externas. Todos passam no validador de Geometria. |
| 22/07/2026 | **Revogada a proibição geral de imagens em Geometria por decisão do Felipe.** O padrão passa a admitir figuras produzidas em TikZ, com fonte `.tex` editável e PNG incorporado ao Markdown, quando houver função pedagógica. Os sete modelos existentes serão revisados em etapa posterior para definir onde as figuras são necessárias. |
| 22/07/2026 | **Contrato provisório local substituído pelo pipeline definitivo.** Toda a produção passou para `../_tikz/`; um `.tex` multipágina gera vários PNGs a 300 DPI, registrados em manifesto privado. O criador implementa `novo`, `adicionar`, `renderizar`, `aprovar`, `validar`, `publicar` e `indexar`, com simulação de publicação por padrão, envio exclusivo de PNG e verificação por SHA-256. O Markdown usa apenas URLs de `felipeelv/imagens-tikz`. O validador confere URL autorizada, manifesto, fonte, texto alternativo e versão publicada. Testes automatizados e renderização real confirmaram o fluxo. |
| 22/07/2026 | **Repositório público criado:** `https://github.com/felipeelv/imagens-tikz`, branch `main`. O primeiro commit contém somente o README de finalidade e estrutura; nenhuma fonte, manifesto, capítulo ou imagem de teste foi publicada. |
| 22/07/2026 | **Primeiro capítulo ilustrado pelo pipeline definitivo:** `modelos/geometria-6ano-modelo.md` recebeu quatro figuras — elementos/classificação dos quadriláteros, propriedades do paralelogramo, elementos da circunferência e razão `C/d`. Um único `figuras.tex` multipágina e seu manifesto ficam em `../_tikz/geometria/6ano/quadrilateros-e-circunferencia/`; somente os quatro PNGs foram publicados no commit `5b38d1dc1ecb` de `felipeelv/imagens-tikz`. As URLs foram validadas por SHA-256 e a cópia pronta do Google Drive foi sincronizada. |
| 22/07/2026 | **Padrão visual transparente adotado.** O renderizador passou de `pdftoppm` para `pdftocairo -transp`, e o validador agora reprova PNG sem canal alfa. As quatro figuras do 6º ano foram redesenhadas sem cartão externo ou painéis brancos, com composição mais estreita, rótulos maiores e texto redundante removido. Os mesmos quatro caminhos públicos foram atualizados no commit `38da6ac130bb`; Markdown e cópia do Google Drive permaneceram sincronizados. |
| 22/07/2026 | **Escala real de revisão corrigida para 300 px.** Um print do material em duas colunas mostrou que a primeira figura ainda comprimia e aproximava rótulos. Elementos e classificação dos quadriláteros foram reorganizados em uma única árvore vertical, com faixas exclusivas de texto e desenho. `AUTOR.md` e `_tikz/README.md` agora exigem prévia a 300 px sobre branco, `\normalsize` como mínimo e proíbem cruzamento entre rótulo, segmento, seta ou marca. Somente `fig-01-elementos-e-classificacao-dos-quadrilateros.png` mudou no commit público `029a488e7373`. |
| 22/07/2026 | **Elementos e classificação separados em duas imagens.** A figura combinada ainda ocupava altura excessiva no conteúdo. `fig-01-elementos-dos-quadrilateros.png` ficou junto da definição dos elementos, e `fig-05-classificacao-dos-quadrilateros.png`, junto da tabela de famílias. Os cinco PNGs vigentes foram publicados no commit `4f19a7f8cdf9`; o combinado obsoleto foi retirado no commit recuperável `6e82f936ab36`. |
| 22/07/2026 | **Paralelogramos e trapézios separados.** A classificação foi dividida em `fig-05-classificacao-dos-paralelogramos.png`, antes da tabela, e `fig-06-classificacao-dos-trapezios.png`, depois dela. Os seis PNGs vigentes foram publicados no commit `0ce181ae40fd`; a classificação combinada anterior foi retirada no commit recuperável `15da9c288601`. |
| 22/07/2026 | **Padrão e plano mestre consolidados.** `../_tikz/PADRAO-DE-CONSTRUCAO.md` fixa uma pergunta visual por PNG, divisão por trecho do Markdown, transparência e aprovação a 300 px. `PLANO-DE-IMAGENS-TIKZ.md` mapeia 45 novas figuras para os seis capítulos restantes: 15 no Fundamental II e 30 no Ensino Médio. |
| 22/07/2026 | **Produção visual do bloco 1 concluída.** As 45 figuras planejadas foram produzidas por lotes, revisadas no original e a 300 px, aprovadas e publicadas em seis commits no repositório `felipeelv/imagens-tikz`. Somadas às seis do 6º ano, são 51 imagens transparentes. Os sete modelos passam no validador com URLs e SHA-256 públicos confirmados e estão idênticos às cópias do Google Drive. |
| 22/07/2026 | **Auditoria de continuidade da 3ª série.** O blueprint do bloco 1 contém dois capítulos, mas somente Hipérbole havia sido produzido. Foi recuperado o Capítulo 2, *Parábola: definição e equações reduzidas*, pré-requisito explícito do bloco 2. |
| 22/07/2026 | **Produção textual seguinte concluída.** Foram escritos os sete capítulos do bloco 2 e o capítulo ausente da 3ª série: 8 arquivos, 32 aulas, todas entre 150 e 203 palavras e aprovadas pelo validador. As oito cópias no Google Drive foram confirmadas como idênticas aos arquivos privados. |
| 22/07/2026 | **Plano visual do bloco 2 consolidado.** `PLANO-DE-IMAGENS-TIKZ-BLOCO2.md` define 60 figuras, com uma pergunta visual por PNG, pasta privada, ID e ponto de inserção: 25 no Fundamental II, 13 na 1ª série, 10 na 2ª e 12 na 3ª. Nenhuma dessas imagens foi gerada ou publicada nesta etapa. |
| 22/07/2026 | **Conflito residual do autor removido.** O anexo genérico ainda permitia versículo condicional, em oposição à decisão específica de Geometria. A seção VP, o modelo de capítulo e o resumo do anexo agora determinam explicitamente **sem versículo**. A regra visual “uma pergunta por PNG, conceitos independentes separados” também foi incorporada ao corpo e ao checklist do `AUTOR.md`. |
| 22/07/2026 | **Produção visual do 3º bimestre concluída.** As 60 figuras do segundo plano foram produzidas em oito documentos TikZ, revisadas no original e a 300 px sobre branco, aprovadas e publicadas em oito commits. Os 15 capítulos somam 111 PNGs transparentes; todas as URLs, textos alternativos, fontes privadas e versões públicas passaram no validador. As oito cópias novas do Google Drive estão idênticas aos Markdown privados. O repositório público contém somente o README e os 111 PNGs. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Geometria/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra (teto próprio de 240 mantido). Pendência herdada: versículo Mateus 25:40 repetido em 3 séries nos blueprints — decisão do Felipe. |
