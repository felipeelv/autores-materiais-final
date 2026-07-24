# Acompanhamento de produção — Química

> Controle dos capítulos do 3º bimestre de 2026. Esta pasta guarda o acompanhamento; `Segundo Semestre/Química` recebe somente conteúdos concluídos.

**Última atualização:** 23/07/2026

**Pasta local dos conteúdos:** `~/Reorganizacao-2026-2Semestre/conteudos-prontos/Quimica`

**Pasta oficial:** [Segundo Semestre/Química](https://drive.google.com/drive/folders/1d-G9jHSN9oozV2AQdxeh5BQ1PxsbwMfI)

## Visão geral

| Ano/série | Capítulos previstos | Oficiais | Pendentes | Aulas previstas | Aulas oficiais |
|---|---:|---:|---:|---:|---:|
| 9º ano | 2 | 2 | 0 | 6 | 6 |
| 1ª série | 2 | 2 | 0 | 12 | 12 |
| 2ª série | 2 | 2 | 0 | 12 | 12 |
| 3ª série | 2 | 2 | 0 | 12 | 12 |
| **Total do 3º bimestre** | **8** | **8** | **0** | **42** | **42** |

**Status geral:** produção, validação, revisão das fórmulas e sincronização do 3º bimestre concluídas.

## Capítulos oficiais

- [x] **9º ano — Capítulo 1: Ácidos e bases** — 3 aulas.

- [x] **9º ano — Capítulo 2: Sais, óxidos e neutralização** — 3 aulas.
- [x] **1ª série — Capítulo 1: Tabela periódica** — 6 aulas.
- [x] **1ª série — Capítulo 2: Ligações químicas e propriedades dos materiais** — 6 aulas.
- [x] **2ª série — Capítulo 1: Equilíbrio químico** — 6 aulas.
- [x] **2ª série — Capítulo 2: Equilíbrio iônico, pH e titulação** — 6 aulas.
- [x] **3ª série — Capítulo 1: Isomeria** — 6 aulas.
- [x] **3ª série — Capítulo 2: Reações orgânicas** — 6 aulas.

Os oito arquivos passam no validador de Química. A extensão menor ocorre quando fórmulas, tabelas e figuras realizam parte da explicação, sem perda do recorte.

## Correção das fórmulas

- O render final não carrega a extensão mhchem e exibia `\ce` literalmente.
- Todas as ocorrências foram substituídas por `\mathrm{}`, subscritos, sobrescritos, `\rightarrow` e `\rightleftharpoons`.
- Os oito capítulos foram renderizados com MathJax; nenhum gerou elemento de erro.
- `AUTOR.md` e `validar-capitulo.py` foram atualizados: `\ce{}` agora é proibido e reprova a validação.

## Ajustes curriculares dos blueprints

A revisão foi feita antes da redação, com consulta à BNCC, à matriz oficial do Enem, ao OpenStax Chemistry 2e e à orientação do Ministério da Saúde sobre queimaduras. O registro das fontes e decisões está em `PESQUISA-E-REVISAO-CURRICULAR-3BIM-BLOCO2.md`.

- **9º ano:** corrigida a referência à BNCC; `EF09CI02` trata de proporções em transformações químicas, não de funções inorgânicas.
- **1ª série:** retirada a repetição de ácidos e bases; o capítulo passou a articular ligações, sólidos e propriedades dos materiais.
- **2ª série:** indicadores foram integrados ao estudo de pH e titulação; `pH = 7` e `pH + pOH = 14` ficaram explicitamente restritos a 25 °C; a estequiometria da titulação deixou de usar igualdade de mols como regra geral.
- **3ª série:** mantiveram-se os tipos gerais de reação e as aplicações curriculares; mecanismos e regras especializadas sem função neste capítulo foram retirados.

## Imagens TikZ

- [x] Doze figuras novas produzidas e revisadas no original e a 300 px.
- [x] Figuras publicadas, indexadas por URLs imutáveis e validadas por SHA-256.
- [x] Quatro capítulos revisados em coluna de 720 px, sem sobreposição ou extravasamento.
- [x] Coleção de Química com 15 figuras: 3 do piloto e 12 desta etapa.

**Commit público vigente da coleção:** `04cb6b4853f64c3a51e29fafbe3bcfb4b13dda72`.

## Conferência da sincronização

- A pasta oficial e as quatro subpastas de ano/série foram criadas em `Segundo Semestre/Química`.
- Os quatro Capítulos 1 foram formalizados e enviados em 23/07/2026.
- Os quatro Capítulos 2 foram substituídos pelas versões com fórmulas corrigidas.
- Cada subpasta contém exatamente os dois capítulos previstos para o 3º bimestre.
- A leitura de retorno confirmou os oito arquivos byte a byte idênticos às versões locais.
- Não há capítulo pendente no 3º bimestre.
