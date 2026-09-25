# Memória do Kit — Química · Produção de Capítulos (Reorganização 2026 · 2º Semestre)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **23/07/2026**.

---

## 1. O que é este kit

Arquivos mestres para produzir capítulos de Química no modelo da reorganização 2026/2S: blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`.

| Arquivo | Papel |
|---|---|
| `AUTOR.md` | Manual consolidado: voz, formato, ortografia, MathJax e regras químicas |
| `validar-capitulo.py` | Validação mecânica de estrutura, extensão, boxes, LaTeX e ortografia |
| `modelos/README.md` | Índice e finalidade dos quatro capítulos-modelo |
| `modelos/quimica-*-modelo.md` | Referências do 9º ano e da 1ª à 3ª série do EM |
| `PADRAO-DE-IMAGENS-TIKZ.md` | Critérios químicos e visuais para gráficos, partículas e processos |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Quimica/blueprints/<série>/<bim>-<bloco>.md` — documento autoritativo de recorte. Séries: 9º ano, 1ª, 2ª e 3ª EM.

## 2. Origem

Kit criado em **19/07/2026** a partir das instruções antigas do projeto Claude.ai de Química (`instruços quimica.rtf`, fluxo antigo por unidades — **absorvido e apagado** após conferência; o que valia foi incorporado aos .md desta pasta).

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Fechamentos abolidos** — a estrutura antiga (Introdução · Aplicações Práticas · "O que a Bíblia diz" · Síntese do Capítulo) não existe mais. Aplicações viram tecido das aulas + boxes 🌍; conexão VP vira versículo + parágrafo curto na aula pertinente (sem "Na prática", sem "Para Conversar"); síntese saiu (blueprints proíbem).
2. **Extensão enxuta aprovada:** preferir 180–210 palavras de conteúdo por aula, com teto firme de 240 e sem mínimo obrigatório. Fórmulas, tabelas e esquemas carregam parte da explicação. Cobriu o recorte, pare.
3. **Exemplo resolvido é conteúdo** (demonstração de cálculo — permitido e incentivado); **exercício proposto ao aluno é proibido** (é do professor).
4. **LaTeX no padrão MathJax** — Felipe usa Auto-LaTeX Equations (Google Docs) com renderizador MathJax. Restrições antigas do CodeCogs (proibir `\text{}`, `\;`, `\,`) **revogadas**.
5. **`\ce{}` (mhchem) está proibido.** O render final exibiu o comando literalmente em 23/07/2026. Equações e espécies químicas usam `\mathrm{}` com subscritos, sobrescritos, `\rightarrow` e `\rightleftharpoons`.
6. **Boxes opcionais:** família própria de Química (💡 Você sabia? · 🔎 Curiosidade · 🌍 Fenômeno · 💭 Pense um pouco · ⏸️ Pare e Pense · ⚠️ Atenção), no máximo 1 por aula, em 1 frase nova. Box que repete definição, tabela ou conclusão deve ser removido.
7. **Abertura de aula:** uma frase com fato observável, contraste entre materiais ou conceito central. Sem história, cena construída ou suspense. Método e experimento entram como descrição objetiva.
8. **Sequência editorial de Química:** fato observável → definição → representação ou fórmula → exemplo/tabela → ressalva. Contexto curto, uma ocorrência reconhecível por conceito e nenhum aquecimento narrativo.
9. **História da ciência:** somente o dado indispensável. O químico-chave aparece uma vez, em frase factual com contribuição e data; não recebe biografia.
10. **Imagens TikZ/PNG:** permitidas quando mostram relações gráficas, espaciais, particuladas ou processuais. ASCII fica restrito a esquemas triviais. Fonte e manifesto permanecem em `_tikz/`; o Markdown recebe somente a URL pública imutável do PNG aprovado.

## 4. Estado e próximos passos

- [x] Kit consolidado em `AUTOR.md`, `_MEMORIA.md` e validador local
- [x] Convenção mhchem revogada após falha confirmada no render final — 23/07/2026
- [x] Quatro capítulos-modelo produzidos: 9º ano e 1ª–3ª séries do EM — 23/07/2026
- [x] Os quatro modelos passam no validador de Química
- [x] Química incluída na validação global `validar-modelos.py`
- [x] Padrão direto aplicado aos quatro modelos: 9º ano e 1ª–3ª séries — 23/07/2026
- [x] Modelo da 2ª série reorganizado com marcadores e três figuras TikZ/PNG publicadas — 23/07/2026
- [x] Quatro Capítulos 2 do 3º bimestre produzidos, validados, ilustrados e sincronizados — 23/07/2026
- [x] Doze novas figuras TikZ/PNG publicadas, indexadas e conferidas em contexto — 23/07/2026
- [x] Blueprints dos quatro Capítulos 2 revisados com pesquisa curricular e científica — 23/07/2026
- [x] Quatro modelos formalizados como Capítulos 1 oficiais e sincronizados — 23/07/2026
- [x] 3º bimestre concluído: 8 capítulos · 42 aulas · 15 figuras — 23/07/2026

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
| 23/07/2026 | **Capítulos-modelo concluídos:** Ácidos e bases (9º), Tabela periódica (1ª), Equilíbrio químico (2ª) e Isomeria (3ª), totalizando 21 aulas. Todos passam no validador local. |
| 23/07/2026 | **Precisão científica alinhada aos blueprints:** corrigida a ordem de eletronegatividade para F > O > Cl > N; talidomida passou a registrar a interconversão dos enantiômeros; NH₃(aq) substituiu NH₄OH como espécie principal; força e solubilidade de Mg(OH)₂ foram separadas. |
| 23/07/2026 | **Calibragem editorial aprovada após comparação com Tito & Canto e Atkins:** contexto cotidiano curto + encadeamento conceitual explícito, sem histórias. Após a conferência final do blueprint, o modelo do 9º ano caiu de 713 para 568 palavras nas três aulas pelo método do validador (**−20,3%**), com 180, 185 e 203 palavras por aula, sem perda do recorte. A versão de teste foi promovida a `quimica-9ano-modelo.md`; faixa preferencial 180–210 e teto 240 registrados no autor e no validador. |
| 23/07/2026 | **Modelos do Ensino Médio atualizados no mesmo padrão:** as 18 aulas ficaram entre 180 e 209 palavras. A 1ª série passou de 1.374 para 1.162 palavras (−15,4%); a 2ª, que já estava concisa, foi de 1.145 para 1.131 (−1,2%) com acréscimos conceituais e retirada de boxes repetidos; a 3ª passou de 1.301 para 1.137 (−12,6%). Os três modelos passam no validador e preservam os blueprints. |
| 23/07/2026 | **Segunda revisão da 2ª série:** a explicação de equilíbrio químico foi reorganizada em blocos curtos, marcadores e tabelas, sem cortar o recorte. O capítulo ficou com 1.082 palavras pelo método do validador, 164–199 por aula e 26%–51% de prosa no diagnóstico de forma. O validador local passou a excluir imagens e comentários da contagem e a exibir `[2b] Prosa × marcadores`. |
| 23/07/2026 | **Piloto TikZ de Química concluído:** três PNGs transparentes — gráficos do equilíbrio dinâmico, pressão na síntese da amônia e fluxo Haber–Bosch — foram revisados no original, a 300 px e no capítulo em coluna de 720 px; aprovados; publicados no commit `e637319bb635434380a7a194e2ad18c7e0111dfd`; indexados por URLs imutáveis; e validados por SHA-256. A disciplina foi ativada em `_tikz/config.json`, recebeu estilo próprio e manual específico. |
| 23/07/2026 | **Revisão curricular dos Capítulos 2:** a pesquisa em BNCC, matriz oficial do Enem, OpenStax Chemistry 2e e orientação do Ministério da Saúde fundamentou os cortes e correções. No 9º ano, corrigiu-se a atribuição de `EF09CI02`; na 1ª série, ácidos e bases repetidos foram substituídos por estrutura e propriedades dos materiais; na 2ª, pH e titulação receberam condições e estequiometria gerais; na 3ª, mecanismos e regras especializadas sem função no capítulo foram retirados. Blueprints e cronogramas foram atualizados antes da redação. |
| 23/07/2026 | **Primeira etapa oficial concluída:** produzidos os quatro Capítulos 2 do 3º bimestre — Sais, óxidos e neutralização; Ligações químicas e propriedades dos materiais; Equilíbrio iônico, pH e titulação; Reações orgânicas. Os 21 tópicos passam no validador, foram revisados em coluna de 720 px e receberam 12 figuras TikZ. Os PNGs foram publicados e validados até o commit `04cb6b4853f64c3a51e29fafbe3bcfb4b13dda72`. Os quatro Markdown foram sincronizados em [Segundo Semestre/Química](https://drive.google.com/drive/folders/1d-G9jHSN9oozV2AQdxeh5BQ1PxsbwMfI), com leitura de retorno byte a byte idêntica. |
| 23/07/2026 | **Correção definitiva das fórmulas:** o render final exibiu `\ce` literalmente, apesar do teste anterior no Auto-LaTeX. A convenção mhchem foi revogada; modelos, capítulos oficiais, autor e validador passaram a usar exclusivamente MathJax básico com `\mathrm{}` e setas manuais. |
| 23/07/2026 | **3º bimestre formalizado:** os quatro modelos aprovados foram copiados como Capítulos 1 oficiais. As quatro subpastas do Drive passaram a conter os dois capítulos previstos; os oito Markdown foram validados, renderizados sem erro MathJax e conferidos por leitura de retorno byte a byte idêntica. |

---

## Consolidação Autores-de-Material — 21/07/2026

| Data | O quê |
|---|---|
| 21/07/2026 | **Kit consolidado em `~/Autores-de-Material/Quimica/`** — esta pasta passa a ser a mestra (a cópia em `Reorganizacao-2026-2Semestre/prompts-producao/` é a origem e não deve mais ser editada). Decisão do Felipe: formato novo mantido em todas as disciplinas, **blocos pós-conteúdo abolidos em definitivo**; a herança dos autores antigos (`autores-material/autores/`) entra como proposta de conteúdo, não como estrutura. Validador substituído pela versão estendida (12 disciplinas — inclui sociologia, filosofia e matematica-ef1), idêntica em todas as pastas. **Específico deste kit:** cópia fiel, sem mudança de regra. |
