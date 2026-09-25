# Memória de continuidade — Autores de Material

Atualizado em **24/07/2026**.

## Objetivo

Organizar os autores de material didático por disciplina, com regras editoriais claras, um capítulo-modelo por ano/série e validadores independentes.

O **blueprint define o conteúdo**. O modelo de cada ano define apenas a forma, o ritmo e o nível de escrita.

## Decisões gerais

- A pasta principal é `Autores-de-Material/`.
- Cada disciplina possui `AUTOR.md`, `_MEMORIA.md`, `validar-capitulo.py` e, quando já calibrada, a pasta `modelos/`.
- A pasta antiga `conteudos/` foi apagada. Os capítulos de referência ficam junto do autor, em `Disciplina/modelos/`.
- Existe um modelo para cada ano ou série já trabalhado.
- Profundidade não significa mais texto: séries mais altas recebem conceitos mais densos dentro de volume semelhante.
- Parágrafos devem ser curtos, com uma ideia principal.
- Marcadores organizam enumerações, causas, consequências, etapas, grupos e contrastes reais.
- Blockquote simples (`>`) cria respiro visual para contraste, ressalva, exceção ou síntese.
- O padrão geral está em `PADRAO-GERAL-DE-ESCRITA.md`, espelhado em `_fontes/_PADROES-DE-ESCRITA.md`.
- `sincronizar.py` mantém os padrões comuns alinhados, sem sobrescrever os validadores específicos.

## Português

Modelos disponíveis do **4º ao 9º ano e da 1ª à 3ª série do Ensino Médio**, em `Portugues/modelos/`.

- Os nove modelos usam o Capítulo 1 do 3º bimestre, Bloco 1, de cada faixa.
- Juntos, totalizam **58 aulas** e definem o padrão de linguagem, ritmo e organização para a produção oficial.
- As definições gramaticais partem da função em linguagem cotidiana, usam “frase” antes de “oração” e conectam o exemplo por dois-pontos; estruturas como “X é o termo/elemento que…” não entram.
- Português usa somente os boxes 💡 Dica, ⚠️ Atenção e 📌 Aplicação prática; pesquisadores, personagens e curiosidades laterais não entram no material.
- Cada ideia aparece uma vez: conceito novo usa definição curta → exemplo → uma observação; aplicações não redefinem o princípio. Não há meta nem mínimo de palavras, apenas teto 300 e aviso de possível truncamento abaixo de 100.
- Todos passam individualmente no validador de Português.
- Após a revisão de concisão, as 58 aulas ficaram entre 120 e 217 palavras, com média 146,8; o conteúdo obrigatório dos blueprints foi preservado.
- O nome antigo `Portugues/portugues-6ano-3bim-cap1-completo.md` foi mantido por compatibilidade, com conteúdo sincronizado ao modelo vigente do 6º ano.

### Produção do 3º bimestre — concluída em 23/07/2026

- Os **64 capítulos previstos**, totalizando **348 aulas**, foram produzidos do 4º ano à 3ª série do Ensino Médio.
- Os nove modelos foram formalizados como Capítulos 1; outros 55 capítulos foram escritos na ordem dos blueprints.
- Todos os 64 arquivos passam no validador de Português. As aulas têm de 55 a 217 palavras, com média de 100,0 e nenhuma acima do teto de 300.
- Os avisos abaixo de 100 palavras foram usados somente para conferir possível truncamento, conforme a regra de concisão aprovada.
- Os arquivos estão somente na pasta oficial [Segundo Semestre/Português](https://drive.google.com/drive/folders/1SnyRi3y8TnxJXJG2Gh8tPeaJc99sMUkJ).
- A pasta possui nove subpastas e 64 arquivos; todos foram comparados por SHA-256, sem divergências.
- Quando uma pasta oficial não existir, ela deve ser criada. O capítulo concluído é salvo diretamente no Google Drive, sem cópia final em `conteudos-prontos`.
- O controle detalhado está em `Portugues/Acompanhamento de produção.md` e a checklist geral em `CONTROLE-DE-PRODUCAO.md`.

## Matemática EF1

### Produção do 3º bimestre — concluída em 23/07/2026

- Os **18 capítulos previstos**, totalizando **96 aulas**, foram produzidos: nove do 4º ano e nove do 5º.
- Os dois modelos foram formalizados como Capítulos 1; os outros 16 capítulos somam 84 aulas novas.
- O padrão definitivo ficou **sem alvo e sem mínimo de palavras**, com teto de segurança de 160 por aula.
- A voz foi simplificada para crianças de 9–10 anos: palavras comuns, frases curtas, um exemplo claro por ideia e nenhuma biografia ou curiosidade histórica.
- Os cálculos usam `\times` para multiplicação e reúnem etapas relacionadas em um único bloco `aligned`.
- As **58 figuras TikZ/PNG** foram aprovadas, publicadas por URLs imutáveis, indexadas, validadas por SHA-256 e revisadas no original, a 300 px e em contexto de 720 px.
- Os arquivos estão em `Segundo Semestre/Matemática EF1`, na pasta oficial [Matemática EF1 — Google Drive](https://drive.google.com/drive/folders/1GrYCV9-QXcOczHZ6smQfQvDfbuv_29w-).
- A estrutura oficial é [4º Ano](https://drive.google.com/drive/folders/1Dvr5rFC6mb3a-t515D7V7qRa888-o3X0) e [5º Ano](https://drive.google.com/drive/folders/1RcU6FXM5c7sBWgIIRpPQ_gSdYGB2TkDy), com exatamente nove arquivos em cada pasta. Após a revisão editorial, a leitura de retorno confirmou igualdade integral dos 18 arquivos com a produção local validada.
- A pasta anterior `Segundo Semestre/MATEMÁTICA EDITANDO` ficou vazia após a migração e **não é mais um destino válido**.
- O controle detalhado está em `Matematica EF1/Acompanhamento de produção.md`.

O 4º bimestre permanece pendente: **18 capítulos e 80 aulas**.

### Ponto de retomada de Matemática EF1

- Não há trabalho pendente no 3º bimestre.
- Os capítulos finais ficam apenas no Drive; os modelos e as fontes TikZ permanecem locais.
- Salvar toda nova produção do 4º ano em `Matemática EF1/4º Ano` e toda nova produção do 5º ano em `Matemática EF1/5º Ano`.
- O padrão vigente está em `Matematica EF1/AUTOR.md`: linguagem direta para crianças, sem mínimo de palavras, teto 160, um exemplo claro por ideia e nenhuma referência histórica.
- A próxima produção é o 4º bimestre. Antes de iniciar, usar `Matematica EF1/Acompanhamento de produção.md` e os blueprints como fontes de estado.

## Biologia

Modelos disponíveis:

- 9º ano;
- 1ª série do Ensino Médio;
- 2ª série do Ensino Médio;
- 3ª série do Ensino Médio.

Os quatro modelos ficam em `Biologia/modelos/` e passam no validador da disciplina.

### Produção do 3º bimestre — concluída em 22/07/2026

- Os **13 capítulos previstos**, totalizando **48 aulas**, foram produzidos e salvos na pasta oficial `/Users/feliperosamini/Library/CloudStorage/GoogleDrive-felipe.rosa@colegioeleve.com.br/Drives compartilhados/Conteudos - Colégio Eleve/Segundo Semestre/Biologia`.
- Após a leitura do Felipe, todos foram revisados para um formato mais enxuto, sem retirar o recorte dos blueprints.
- A calibragem vigente de Biologia é **180–210 palavras por aula, com teto firme de 220**.
- Resultado final: 48 aulas entre 180 e 219 palavras, média de **192,8 palavras por aula**; redução de 21,6% em relação à versão anterior.
- Os 13 capítulos passam no validador de Biologia com seus respectivos blueprints.
- O padrão foi registrado em `Biologia/AUTOR.md`, `Biologia/_MEMORIA.md` e no validador local.
- O controle completo está em `Biologia/Acompanhamento de produção.md`.

## Ciências

O 3º bimestre está concluído:

- **21 capítulos e 90 aulas** produzidos;
- arquivos organizados do 4º ao 8º ano na pasta oficial [Ciências — Segundo Semestre](https://drive.google.com/drive/folders/19WT5IVADLcv_tNPkwI3616p_F40VgdnM);
- zero falhas no validador;
- 21 arquivos conferidos sem divergência de tamanho entre produção e Drive.

Modelos disponíveis do **4º ao 8º ano**, em `Ciencias/modelos/`.

Regras calibradas:

- preferir 140–200 palavras por aula, com teto de 220 e sem mínimo obrigatório;
- manter volume e ritmo semelhantes em todos os anos;
- não deixar três parágrafos consecutivos sem lista, tabela, box ou blockquote;
- não deixar dois subtópicos `###` consecutivos sem lista de marcadores;
- subtópicos com marcadores podem aparecer em sequência;
- não criar listas artificiais apenas para cumprir a forma.

O conjunto final tem média de **160,3 palavras por aula**, com mínimo de 111 e máximo de 207. O validador de Ciências verifica automaticamente extensão, ritmo da prosa e alternância dos subtópicos.

O controle completo está em `Ciencias/Acompanhamento de produção.md`.

## Física

Modelos disponíveis do **6º ao 9º ano e da 1ª à 3ª série do Ensino Médio**, em `Fisica/modelos/`.

Regras calibradas:

- manter 130–170 palavras por aula, com teto de 190 e sem aumento de volume nas séries mais altas;
- usar fórmula, tabela de grandezas e exemplo resolvido para carregar o formalismo;
- numerar os subtópicos como `N.1`, `N.2` e `N.3`;
- manter a progressão fenômeno → conceito ou lei → modelo idealizado → expressão matemática;
- não inserir versículos, mesmo quando o blueprint trouxer conexão VP;
- conferir cálculos, símbolos, notação vetorial e unidades SI antes da entrega;
- declarar a unidade de uma grandeza nova uma única vez e não redeclarar grandezas já estabelecidas no percurso;
- proibir inventários de unidades e valores implícitos em exemplos; usar uma operação por linha;
- manter história essencial junto ao conceito e biografia acessória, quando útil, em um único box 👤 na última aula;
- exigir que boxes acrescentem aplicação, consequência, erro, pergunta ou dado novo e que a prosa não repita tabelas.

Os sete modelos passam no validador da disciplina.

Em 23/07/2026, a revisão passou a ter duas camadas: `validar-capitulo.py` decide as regras determinísticas, enquanto `Fisica/auditar-fisica.py` usa um contrato JSON para sequenciamento, novidade de boxes, repetição tabela–prosa e distinção entre história essencial e biografia acessória. Achados de alta confiança são corrigidos e revalidados; os médios são decididos pelo autor/agente; somente conflitos de baixa confiança seguem para revisão humana. O piloto `Aplicações da dinâmica` possui contrato próprio e passa sem achados. Seis capítulos afetados por correções objetivas foram sincronizados no Google Drive e conferidos por leitura de retorno.

### Produção do 3º bimestre — concluída em 23/07/2026

- Os **17 capítulos previstos**, totalizando **84 aulas**, estão concluídos do 6º ano à 3ª série do Ensino Médio.
- Foram produzidos os oito capítulos que faltavam, com 42 aulas entre 113 e 190 palavras e média de 167,4 palavras por aula.
- Fórmulas, exemplos, unidades, sinais e recortes dos blueprints foram conferidos; os oito arquivos passam no validador de Física.
- Os 17 capítulos estão na pasta oficial `Segundo Semestre/Física`.
- Dois capítulos já produzidos, `Força e movimento.md` e `Forças mecânicas.md`, foram sincronizados porque ainda não apareciam na pasta oficial.
- O controle completo está em `Fisica/Acompanhamento de produção.md`.

### Decisão de 23/07/2026 — imagens TikZ de Física

- `Aplicações da dinâmica`, da 1ª série, foi escolhido como capítulo-piloto por reunir gráfico, DCL, plano inclinado, movimento circular e sistema com polia.
- Oito figuras foram produzidas, publicadas, indexadas e sincronizadas. O commit público de encerramento do piloto é `9934fd2ba023`.
- Prints do capítulo diagramado revelaram proximidade excessiva nas figuras de lombada/vale e do sistema de blocos, embora os PNGs isolados estivessem legíveis a 300 px.
- A regra definitiva passa a exigir duas revisões: PNG isolado a 300 px e capítulo diagramado na largura real.
- Na prévia de 300 px, usar ao menos 8 px entre rótulo e traço não relacionado e 16 px entre casos empilhados.
- Vetores não podem cobrir cordas, superfícies ou trajetórias nem atravessar identificadores como `A` e `B`.
- Os detalhes estão em `Fisica/PADRAO-DE-IMAGENS-TIKZ.md` e `_tikz/PADRAO-DE-CONSTRUCAO.md`.
- Os 16 capítulos restantes foram planejados em `Fisica/PLANO-DE-IMAGENS-TIKZ.md` e receberam 95 figuras: fontes TikZ multipágina, manifestos e PNGs transparentes a 300 DPI.
- As galerias em `Fisica/REVISAO-TIKZ-DEMAIS-CAPITULOS.md` foram aprovadas. Os 95 PNGs foram publicados, indexados e validados por SHA-256.
- Os 16 capítulos foram revisados em coluna de 720 px, passam no validador de Física e foram sincronizados nos mesmos arquivos do Google Drive; a leitura de retorno é byte a byte idêntica.
- A coleção do 3º bimestre está concluída com **103 PNGs de Física**. O commit público vigente é `8a79200b98f7`.

## Química

Modelos disponíveis do **9º ano e da 1ª à 3ª série do Ensino Médio**, em `Quimica/modelos/`.

- Os quatro modelos usam os Capítulos 1 do 3º bimestre, Bloco 1: Ácidos e bases, Tabela periódica, Equilíbrio químico e Isomeria.
- Juntos, totalizam **21 aulas**, com progressão de fenômeno observável → organização eletrônica → físico-química com cálculo → estrutura orgânica tridimensional.
- O padrão direto aprovado prefere **180–210 palavras por aula, com teto de 240 e sem mínimo obrigatório**; fórmulas, tabelas e esquemas carregam parte do conteúdo.
- A cadência de produção é **fato observável → definição → representação ou fórmula → exemplo/tabela → ressalva**. O contexto é curto; histórias, cenas construídas e biografias não entram. Box é opcional, limitado a um por aula e precisa acrescentar informação.
- Equações e espécies químicas usam MathJax básico com `\mathrm{}`, subscritos, sobrescritos e setas manuais. `\ce{}`/mhchem foi proibido depois que o render final exibiu o comando literalmente.
- As conexões VP não foram inseridas porque não passaram no teste de ligação conceitual do manual.
- Os quatro modelos foram atualizados no padrão direto, passam no validador local e Química já integra `validar-modelos.py`. O 9º ano tem 568 palavras, a 1ª série 1.162 e a 3ª série 1.137. A 2ª série recebeu uma segunda revisão e ficou com 1.082 palavras, entre 164 e 199 por aula; não há mínimo obrigatório.
- Na 2ª série, o diagnóstico do validador registra 26%–51% de prosa por aula. A explicação de equilíbrio químico foi reorganizada em blocos curtos, marcadores e tabelas, sem perda do recorte.
- O piloto TikZ de Química foi concluído com três figuras: gráficos de velocidades e concentrações, pressão na síntese da amônia e fluxo Haber–Bosch. Os PNGs transparentes foram revisados no original, a 300 px e no capítulo em coluna de 720 px, publicados no commit `e637319bb635434380a7a194e2ad18c7e0111dfd`, indexados por URLs imutáveis e validados por SHA-256.
- O 9º ano teve redução de **20,3%**; a 1ª série, **15,4%**; e a 3ª, **12,6%**. A 2ª série já estava na faixa aprovada e permaneceu praticamente estável após retirar boxes repetidos e acrescentar precisões conceituais.
- A conferência científica corrigiu nos blueprints: F > O > Cl > N na escala de Pauling; interconversão dos enantiômeros da talidomida; NH₃(aq) como representação principal da amônia em água; separação entre força e solubilidade de Mg(OH)₂.
- A produção oficial avançou para **8 de 17 capítulos e 42 de 77 aulas**. O 3º bimestre está concluído com os quatro Capítulos 1 formalizados a partir dos modelos e os quatro Capítulos 2 produzidos nesta etapa.
- Antes da redação, os quatro blueprints foram revisados com pesquisa na BNCC, na matriz oficial do Enem, no OpenStax Chemistry 2e e em orientação do Ministério da Saúde. A revisão corrigiu a atribuição de `EF09CI02`, retirou a repetição de ácidos e bases na 1ª série, condicionou relações de pH a 25 °C, generalizou a estequiometria de titulação e removeu mecanismos orgânicos especializados sem função no capítulo.
- Os quatro capítulos oficiais passam no validador, foram revisados em coluna de 720 px e receberam **12 novas figuras TikZ**, elevando a coleção de Química a 15 PNGs. O commit público vigente é `04cb6b4853f64c3a51e29fafbe3bcfb4b13dda72`.
- A pasta oficial [Segundo Semestre/Química](https://drive.google.com/drive/folders/1d-G9jHSN9oozV2AQdxeh5BQ1PxsbwMfI) foi criada com subpastas por ano/série. Cada subpasta contém os dois capítulos previstos; os oito arquivos foram conferidos por leitura de retorno e estão byte a byte idênticos às versões locais.
- Após o erro mostrado no render, todas as ocorrências de `\ce{}` foram convertidas para MathJax básico. Os oito capítulos foram renderizados sem erro, e o validador passou a reprovar automaticamente qualquer nova ocorrência de mhchem.
- A correção foi propagada aos autores, memórias e validadores de Biologia e Física, únicas outras disciplinas que autorizavam equações químicas com mhchem.

## Geografia

### Produção do 3º bimestre — concluída em 24/07/2026

- Geografia passou a ter pasta e `AUTOR.md` exclusivos para a 1ª, a 2ª e a 3ª séries do Ensino Médio.
- Há três modelos aprovados em `Geografia/modelos/`, um por série: `Clima`, `Fundamentos e regulação do comércio internacional` e `Política externa e integração regional do Brasil`.
- O padrão prefere 145–175 palavras por aula, admite até 190 em recortes N4 densos e mantém teto de segurança de 200.
- Os **12 capítulos previstos**, totalizando **54 aulas**, foram produzidos e validados: quatro capítulos e 18 aulas por série.
- Após a segunda revisão de concisão, as aulas ficaram entre 141 e 181 palavras, com média de 157,9 — redução de 24,4%.
- Cada aula possui um box de uma frase, com no máximo 18 palavras.
- Foram atualizados dados instáveis dos blueprints em fontes oficiais, incluindo Mercosul–UE, Bolívia no Mercosul, composição de BRICS e G20, IDH, LDCs, pobreza, conectividade, energia, povos indígenas e fronteiras.
- Estatísticas inexatas nas perguntas-problema foram corrigidas sem alterar o eixo de investigação.
- A pasta oficial [Segundo Semestre/Geografia](https://drive.google.com/drive/folders/1bIep9JGBQaZbhNHxYqe-Fp1He_syo26r) contém três subpastas e exatamente quatro arquivos Markdown em cada uma.
- A leitura de retorno confirmou que os 12 arquivos no Drive são idênticos às versões locais validadas.
- O controle detalhado está em `Geografia/Acompanhamento de produção.md`.

O 4º bimestre de Geografia permanece pendente: **11 capítulos e 45 aulas**.

## História

### Produção do 3º bimestre — concluída em 24/07/2026

- História passou a ter pasta, `AUTOR.md` e validador exclusivos para a 1ª, a 2ª e a 3ª séries do Ensino Médio.
- Há três modelos validados em `Historia/modelos/`: `Origens de Roma: Monarquia e República`, `Política e economia cafeeira do Segundo Reinado` e `Governos Dutra, Vargas e JK`.
- O padrão prefere 145–175 palavras por aula, admite até 190 em recortes N4 densos e mantém teto de segurança de 200.
- Os modelos foram formalizados como os três Capítulos 1 oficiais.
- Foram produzidos os outros nove capítulos, com 40 aulas, totalizando **12 capítulos e 54 aulas**.
- O conjunto final ficou entre **146 e 175 palavras por aula**, com média de **166,7**.
- Cada aula possui um box de uma frase da família 🔎/💭; referências historiográficas aparecem integradas ao corpo.
- Cada capítulo usa dois blockquotes simples em subtópicos sem marcadores para separar fonte, interpretação, contraste ou consequência.
- O texto relaciona agentes, condições, conflitos, causas, consequências, mudanças e permanências, distinguindo acontecimento, fonte, tradição, memória e interpretação.
- Os 12 arquivos passaram no validador e foram revisados contra a ordem, os conteúdos e os itens `NÃO ANTECIPAR` dos blueprints.
- A pasta oficial [Segundo Semestre/História](https://drive.google.com/drive/folders/1Na_5uJ539RgBEUJmy1r73SmAy4kGe3M_) contém três subpastas e exatamente quatro arquivos Markdown em cada uma.
- A conferência de retorno confirmou nomes, destinos e tamanhos idênticos às versões locais validadas.
- O controle detalhado está em `Historia/Acompanhamento de produção.md`.

O 4º bimestre de História permanece pendente: **9 capítulos e 45 aulas**.

## Filosofia

### Produção do 3º bimestre — concluída em 24/07/2026

- O autor e o validador foram recalibrados para o padrão conciso: preferência por 155–185 palavras por aula, tolerância até 190 em recortes densos e teto de segurança de 200.
- Há três modelos validados em `Filosofia/modelos/`: `Aristóteles — metafísica e ética`, `Nietzsche e a morte de Deus` e `Filosofia antiga e medieval`.
- Os modelos foram aprovados e formalizados como os três Capítulos 1 oficiais.
- Foram produzidos os três Capítulos 2, completando **6 capítulos e 18 aulas**.
- O conjunto ficou entre **158 e 185 palavras por aula**, com média de **178,8**.
- Toda aula possui ao menos uma lista ou tabela ligada ao raciocínio central, evitando blocos longos de prosa.
- Cada aula possui exatamente um box de uma frase da família 💭/⏸️/💡/🔍; cada capítulo usa dois blockquotes simples.
- A escrita organiza questão, tese, argumento, objeção e avaliação cristã, preservando fidelidade intelectual antes da crítica.
- Os seis arquivos foram revisados contra conteúdo, ordem e itens `NÃO ANTECIPAR` dos blueprints.
- A pasta oficial [Segundo Semestre/Filosofia](https://drive.google.com/drive/folders/1X-rhNe1FWP-Y_QIhdaNRSdWOIzZVHChZ) contém três subpastas e exatamente dois arquivos Markdown em cada uma.
- A leitura de retorno confirmou que os seis arquivos do Drive são integralmente idênticos às versões locais validadas.
- O controle detalhado está em `Filosofia/Acompanhamento de produção.md`.

O 4º bimestre de Filosofia permanece pendente: **6 capítulos e 15 aulas**.

## Sociologia

### Produção do 3º bimestre — concluída em 24/07/2026

- O autor e o validador foram recalibrados para concisão com maior densidade: preferência por 175–195 palavras por aula e teto firme de 200.
- Há três modelos em `Sociologia/modelos/`: `O trabalho como atividade social`, `Movimentos sociais no Brasil` e `Clássicos da Sociologia`.
- Os modelos foram formalizados como os três Capítulos 1 oficiais.
- Foram produzidos os três Capítulos 2, completando **6 capítulos e 18 aulas**.
- O conjunto ficou entre **175 e 195 palavras por aula**, com média de **188,6**.
- Cada aula possui três movimentos curtos — contexto ou fenômeno, conceito e leitura sociológica — e pelo menos duas subseções com lista ou tabela.
- Definições, classificações, marcos e consequências aparecem em tópicos rotulados; a prosa curta explica causas, relações e limites.
- Toda aula possui exatamente um box de uma frase; cada capítulo usa dois blockquotes simples.
- A escrita segue fenômeno → conceito → análise, preserva fidelidade às teorias antes da avaliação e distingue análise sociológica de ancoragem cristã.
- Os seis arquivos foram revisados contra a ordem, os conteúdos e os itens `NÃO ANTECIPAR` dos blueprints.
- A pasta oficial [Segundo Semestre/Sociologia](https://drive.google.com/drive/folders/19srtjGKY0f9VA_G00ZupP5xhHvAPuIPV) contém três subpastas e exatamente dois arquivos Markdown em cada uma.
- Os nomes e tamanhos no Drive coincidem com as versões locais validadas; a leitura de retorno do Capítulo 2 da 1ª série confirmou a integridade do conteúdo.
- O controle detalhado está em `Sociologia/Acompanhamento de produção.md`.

O 4º bimestre de Sociologia permanece pendente: **6 capítulos e 15 aulas**.

**Checkpoint de retomada:** começar pelos blueprints `1serie/4bim-bloco1.md`, `2serie/4bim-bloco1.md` e `3serie/4bim-bloco1.md`. Os capítulos concluídos permanecem exclusivamente no Drive; `Sociologia/modelos/` conserva apenas as três referências editoriais.

## Matemática Financeira

Modelos disponíveis do **6º ao 9º ano e da 1ª à 3ª série do Ensino Médio**, em `Financeira/modelos/`.

Regras calibradas:

- manter as aulas preferencialmente entre 220–250 palavras, com teto de 300 e sem mínimo obrigatório;
- organizar dados em tabelas Markdown e declarar quando um conjunto é hipotético;
- apresentar exemplos resolvidos passo a passo e interpretar todo resultado numérico;
- escrever valores monetários com duas casas e associar toda taxa ao seu período;
- distinguir mecanismos, riscos e consequências sem recomendar produtos ou prometer rentabilidade;
- explicitar população e amostra, além de conferir fórmulas, símbolos, percentuais e arredondamentos.

Os sete modelos passam no validador da disciplina. No capítulo de 9º ano, os dados reais de inflação e de garantia do FGC foram conferidos em fontes oficiais.

### Produção do 3º bimestre — concluída em 22/07/2026

- Os **14 capítulos previstos**, totalizando **42 aulas**, estão concluídos do 6º ano à 3ª série do Ensino Médio.
- Foram produzidos os sete capítulos que faltavam, com 21 aulas, e o acompanhamento foi atualizado após cada validação.
- Todos os exemplos de probabilidade, porcentagem, juros, Price, SAC, rotativo, valor presente e VPL foram recalculados.
- Dados de 2026 foram conferidos em fontes oficiais do Banco Central, IBGE, Tesouro Direto e CONAR; cenários didáticos foram identificados como hipotéticos.
- Cada aula possui exatamente um box da família 🔢/⚠️, sem exercícios propostos, recomendações de produto ou resultados sem interpretação.
- O controle final está em `Financeira/Acompanhamento de produção.md` e os conteúdos em `Segundo Semestre/Matemática Financeira`.

### Alinhamento com as páginas-resumo — 11/08/2026

- Os **6 capítulos do Bloco 1 com página-resumo aprovada** (6º, 7º, 8º, 9º ano, 1ª e 2ª série) foram reescritos para trabalhar os exemplos das imagens e publicados na pasta oficial: 12 arquivos substituídos, contando os consolidados `bl1_`.
- **Causa da divergência — vale para todas as disciplinas:** o `gerador-de-imagens` consome os **blueprints**, não os capítulos. O blueprint define o recorte, não os números, então autor de texto e autor de imagem inventam exemplos diferentes a partir do mesmo briefing. Onde coincidem, é porque o exemplo era óbvio.
- As páginas correspondem **1:1 às aulas** — página 02 → aula 1, e assim por diante. Vale conferir se o mesmo padrão se repete nas outras disciplinas antes de mandar imprimir.
- **Regra nova:** onde houver página-resumo aprovada, ela manda no exemplo; o capítulo é que se ajusta.
- Três decisões com custo editorial, confirmadas pelo Felipe: o IPCA real de 4,64% saiu do 9º ano em favor de 5% hipotético; a abertura da 2ª série foi reescrita para o filtro de spam, divergindo da pergunta-problema do blueprint; a 1ª série adotou `CV = σ/x̄` da imagem, contra `CV = s/x̄` do kit — este último ainda pendente de decisão.
- Reescrita e backup dos 12 originais em `Financeira/Financeira reescrita/`. **Bloco 2 e 3ª série ficaram de fora**, por não terem imagem aprovada.
- ⚠️ A cópia em `Reorganizacao-2026-2Semestre/conteudos-prontos/Financeira/` é de 21/07 e **não é fonte confiável** — já estava atrás da revisão de 27/07 que só existia no Drive.

## Geometria

Modelos disponíveis do **6º ao 9º ano e da 1ª à 3ª série do Ensino Médio**, em `Geometria/modelos/`.

Regras calibradas:

- manter 170–210 palavras por aula, com teto de 240 e sem mínimo obrigatório;
- usar figuras produzidas em TikZ e renderizadas em PNG quando a configuração visual favorecer a compreensão;
- concentrar fonte `.tex`, manifesto, ferramentas e renderizações temporárias exclusivamente em `_tikz/`;
- publicar somente o PNG aprovado em `felipeelv/imagens-tikz` e indexar sua URL absoluta no Markdown;
- usar ASCII simples quando ele for suficiente, sem duplicar uma figura TikZ/PNG equivalente;
- apresentar justificativa geométrica antes da fórmula e uma operação por linha nos exemplos;
- escrever construções com instrumentos ou software como procedimentos descritos, nunca como atividades;
- manter unidade em todo resultado de comprimento, área, volume ou ângulo;
- não inserir versículos, mesmo quando o blueprint trouxer conexão VP.

Os sete modelos passam no validador da disciplina e foram conferidos quanto a fórmulas, unidades e descrição das configurações.

### Decisão de 22/07/2026 — imagens em Geometria

Felipe aprovou o uso de **fontes TikZ editáveis e imagens PNG incorporadas ao Markdown**. A proibição geral de imagens em Geometria foi revogada no `Geometria/AUTOR.md` e em `Geometria/_MEMORIA.md`.

O padrão oficial passa a ser:

1. usar figura apenas quando a configuração visual tiver função pedagógica;
2. preservar a fonte `.tex` e o manifesto privado em `_tikz/` e renderizar uma versão `.png` transparente a 300 DPI, sem cartão externo ou painéis brancos;
3. publicar somente o PNG aprovado em `felipeelv/imagens-tikz` e indexar sua URL absoluta no Markdown com texto alternativo descritivo;
4. informar no texto as medidas, relações e incógnitas necessárias para interpretar a figura;
5. usar ASCII apenas quando for suficiente e não duplicar uma figura TikZ/PNG equivalente;
6. impedir referências vagas, imagens inexistentes e links quebrados.

O criador definitivo está em `_tikz/`: fonte multipágina, manifesto por documento, estilo visual, renderização transparente, aprovação, publicação protegida e indexação idempotente. O validador confere canal alfa, URL do repositório autorizado, manifesto e fonte privados, texto alternativo, SHA-256 e registro da versão publicada. As figuras são planejadas e revisadas na largura efetiva mínima de 300 px sobre fundo branco, com composição vertical ou quase quadrada, `\normalsize` como tamanho mínimo, faixas exclusivas para texto e desenho e nenhum cruzamento entre rótulo, segmento, seta ou marca. Capítulos sem figura continuam válidos. O contrato visual definitivo foi registrado em `_tikz/PADRAO-DE-CONSTRUCAO.md`: uma pergunta pedagógica por PNG, separação obrigatória de conceitos independentes, fundo transparente e revisão na largura real de leitura.

Os sete modelos inicialmente produzidos foram analisados e ilustrados. Eles possuem **51 figuras publicadas** — 6 no 6º ano, 5 no 7º, 5 no 8º, 5 no 9º, 12 na 1ª série, 10 na 2ª e 8 na 3ª — com fontes e manifestos privados, PNGs transparentes e pontos de inserção registrados em `Geometria/PLANO-DE-IMAGENS-TIKZ.md`. Todos os hashes públicos foram confirmados e os sete Markdown estão sincronizados no Google Drive.

**Correção curricular de 22/07/2026:** a auditoria dos blueprints revelou que o bloco 1 da 3ª série tinha um segundo capítulo, **Parábola: definição e equações reduzidas**, que ainda não havia sido produzido. Ele foi escrito como pré-requisito antes do Capítulo 3.

**Nova produção concluída:** os sete capítulos do bloco 2 e o capítulo ausente da 3ª série foram produzidos e validados: 8 arquivos, 32 aulas, todas entre 150 e 203 palavras. Suas **60 figuras** — 56 do bloco 2 e 4 do pré-requisito — foram produzidas em oito documentos TikZ, revisadas no original e a 300 px sobre branco, publicadas, indexadas e validadas. As oito cópias em `Segundo Semestre/Geometria/` foram conferidas como idênticas. O controle completo está em `Geometria/Acompanhamento de produção.md`.

O repositório público exclusivo está em `https://github.com/felipeelv/imagens-tikz`, na branch `main`. Ele contém o README e **111 PNGs transparentes aprovados**; nenhuma fonte, manifesto, capítulo ou imagem de teste foi publicada. Os 15 Markdown privados e suas cópias em `Segundo Semestre/Geometria/` estão idênticos e validados. As fontes, manifestos e renderizações permanecem exclusivamente em `_tikz/`. O checkpoint da etapa termina no commit `2fdcd844d6a909e73c4204a99445dd7d55535447`; os oito commits do bloco 2 estão registrados em `Geometria/PLANO-DE-IMAGENS-TIKZ-BLOCO2.md`.

## Estudos Sociais

Modelos disponíveis do **4º ao 9º ano**, em `Estudos Sociais/modelos/`.

Foram aplicadas as mesmas regras visuais de Ciências:

- não deixar três parágrafos consecutivos sem quebra visual;
- não deixar dois subtópicos consecutivos sem marcadores;
- usar blockquote para ressalvas históricas, distinção entre fontes, contrastes e sínteses;
- usar marcadores apenas quando o conteúdo já apresentar elementos paralelos;
- manter parágrafos enxutos e aulas preferencialmente entre 180–220 palavras;
- manter de 1 a 2 boxes por aula, sem contar os blockquotes simples de respiro visual.

Os seis modelos totalizam **31 aulas e 31 boxes**: 14 🔎 Curiosidades, 11 💭 reflexões e 6 👤 personagens. Cada aula possui exatamente um box; informações que já estavam no corpo foram convertidas, em vez de duplicadas.

O validador de Estudos Sociais verifica automaticamente o ritmo da prosa e a alternância dos subtópicos.

A quantidade de boxes ainda exige conferência separada: o validador atual verifica a família permitida e impede boxes consecutivos, mas não reprova uma aula sem box.

### Produção do 3º bimestre — concluída em 22/07/2026

- Os **34 capítulos previstos**, totalizando **162 aulas**, estão concluídos do 4º ao 9º ano.
- Foram produzidos os 28 capítulos que faltavam, com 131 aulas, sempre um por vez e com atualização do acompanhamento após cada validação.
- Todos os arquivos passaram no validador de Estudos Sociais e foram revisados contra a ordem, os títulos e os recortes dos blueprints dos blocos 1 e 2.
- A redação foi calibrada para ser **mais concisa e direta**, sem retirar conceitos, processos, personagens ou relações exigidas pelos blueprints.
- Todas as aulas possuem de 1 a 2 boxes da família permitida; não há exercícios, fechamentos ou antecipações de conteúdos indicados para capítulos posteriores.
- O controle final está em `Estudos Sociais/Acompanhamento de produção.md`.
- A pasta oficial é `/Users/feliperosamini/Library/CloudStorage/GoogleDrive-felipe.rosa@colegioeleve.com.br/Drives compartilhados/Conteudos - Colégio Eleve/Segundo Semestre/Estudos Sociais`.

## Ressincronização dos validadores — 11/08/2026

Descoberto ao documentar o alinhamento de Financeira: dos 15 `validar-capitulo.py`, 13 são implementações reais (o mestre + 12 cópias; `Historia/` e `Geografia/` são shims que executam o de Estudos Sociais). Duas lacunas de comportamento foram fechadas nos 13.

- **Prefixo `BL1_`/`BL2_` estava em 1 de 13.** As outras 12 exigiam `# Capítulo N — Tema` e **reprovavam todo capítulo em produção** — as 12 disciplinas usam o prefixo no Drive, conferido um a um. A lógica de Estudos Sociais foi portada: prefixo **aceito em qualquer disciplina**, **obrigatório só onde `prefixo_bloco=True`** no `DISC`. Hoje só `estudos-sociais` exige; para outra disciplina passar a exigir, acrescentar a chave.
- **`[2b] Prosa × marcadores` estava em 2 de 13** (Biologia e Química), embora o histórico de 21/07 registrasse que valia para nove disciplinas. Portado para os 11 restantes na versão de Química, que descarta imagem Markdown e comentário HTML antes de medir. Continua **diagnóstico, nunca reprova**.
- Ciências, Estudos Sociais e Filosofia já tinham sido renumeradas para `[2c]` esperando o bloco que nunca foi inserido; Filosofia estava incoerente (comentário `2c`, print `[2b]`). Índice do docstring corrigido nos 11.
- **Não foram mexidos, porque não eram deriva:** as 4 variantes de `contar_conteudo()` colapsam em 2 comportamentos, e o corte acompanha as disciplinas que embutem figura TikZ; o limite 140–220 de Ciências é escolha da disciplina (4º–8º ano).
- Verificação: os 15 compilam, e os 12 validadores rodaram contra um capítulo real da sua disciplina no Drive — **zero falhas**, com o `[2b]` ativo em todos.

⚠️ Continuam sendo 13 arquivos separados. O patch igualou o comportamento, não a manutenção — a próxima divergência nasce do mesmo jeito. Vale avaliar transformar as cópias em shims do mestre.

## Estado da validação

Existem **63 capítulos-modelo**:

- 4 de Biologia;
- 5 de Ciências;
- 6 de Estudos Sociais;
- 3 de Geografia;
- 3 de História;
- 3 de Filosofia;
- 3 de Sociologia;
- 7 de Física;
- 7 de Matemática Financeira;
- 7 de Geometria;
- 2 de Matemática EF1;
- 4 de Química;
- 9 de Português.

Os modelos de História e Sociologia passam individualmente e já estão incluídos em `python3 validar-modelos.py` com seus validadores exclusivos. Na execução global de 24/07/2026, quatro modelos de Biologia ainda retornaram falha; os demais passaram. A validação confirma a estrutura mecânica, e a aprovação editorial final continua sendo feita pelo Felipe.

## GitHub

- Repositório definitivo: `felipeelv/autores-materiais-final`
- Visibilidade: privada
- Branch principal: `main`
- Branch de trabalho atual: `agent/consolida-modelos-curriculares`
- Os arquivos ficam diretamente na raiz do repositório.

O repositório antigo `autores-material` não deve ser usado como fonte desta versão final. A separação permite higienizar os arquivos antigos sem afetar os autores consolidados.

### Estado da publicação em 21/07/2026

- A branch de trabalho reúne os modelos de Estudos Sociais, Física, Matemática Financeira e Geometria.
- O PR rascunho [#1](https://github.com/felipeelv/autores-materiais-final/pull/1) está aberto contra a `main` com esse conjunto consolidado.
- Em 22/07/2026, os sete capítulos inicialmente ilustrados de Geometria foram concluídos com 51 figuras TikZ/PNG publicadas, indexadas e sincronizadas no Google Drive.
- Na mesma data, os sete capítulos do bloco 2 e o capítulo de parábola ausente da 3ª série foram produzidos, validados e ilustrados com outras 60 imagens; o 3º bimestre foi fechado com 15 capítulos, 60 aulas e 111 PNGs sincronizados no Drive.

## Como continuar de casa

```bash
git clone https://github.com/felipeelv/autores-materiais-final.git
cd autores-materiais-final
python3 sincronizar.py --check
python3 validar-modelos.py
```

Enquanto o PR #1 estiver aberto, retome pela branch de trabalho:

```bash
git fetch origin
git switch agent/consolida-modelos-curriculares
git pull --ff-only
```

## Próximos passos

1. Estudos Sociais do 3º bimestre está concluído; usar `Estudos Sociais/Acompanhamento de produção.md` como registro final.
2. Ao iniciar outro bimestre ou disciplina, repetir o fluxo: blueprint → capítulo → validação → pasta oficial → acompanhamento.
3. Registrar qualquer nova calibragem no `AUTOR.md` e no `_MEMORIA.md` da disciplina correspondente.
4. Geometria do 3º bimestre está concluída; usar `Geometria/Acompanhamento de produção.md` como registro final e manter o mesmo pipeline nos próximos bimestres.
5. Sociologia do 3º bimestre está concluída; usar `Sociologia/Acompanhamento de produção.md` como registro final.
6. Física do 3º bimestre está concluída; o padrão editorial de exatas e a auditoria semântica já foram validados no piloto.
7. **Imagens de Física concluídas:** 103 PNGs aprovados, publicados, indexados, revisados em contexto e sincronizados. Nas próximas produções, repetir: original + 300 px → aprovação → publicação → indexação → coluna de 720 px → hashes públicos → leitura de retorno do Drive. Manter os respiros mínimos de 8/16 px, vetores separados de cordas, superfícies e trajetórias e identificadores livres de setas.
8. Português do 3º bimestre está concluído e conferido na pasta oficial; usar `Portugues/Acompanhamento de produção.md` como registro final.
9. Química do 3º bimestre está concluída e conferida na pasta oficial; usar `Quimica/Acompanhamento de produção.md` como registro final e abrir o 4º bimestre na próxima etapa.
10. Ciências do 3º bimestre está concluída e conferida na pasta oficial; usar `Ciencias/Acompanhamento de produção.md` como registro final.
11. Matemática EF1 do 3º bimestre está concluída e conferida na pasta oficial; usar `Matematica EF1/Acompanhamento de produção.md` como registro final.
12. História do 3º bimestre está concluída e conferida na pasta oficial; usar `Historia/Acompanhamento de produção.md` como registro final e abrir o 4º bimestre na próxima etapa.
13. Filosofia do 3º bimestre está concluída e conferida na pasta oficial; usar `Filosofia/Acompanhamento de produção.md` como registro final e abrir o 4º bimestre na próxima etapa.
