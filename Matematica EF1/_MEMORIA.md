# Memória do Kit — Matemática EF1 · Produção de Capítulos (Autores-de-Material)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **23/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Matemática EF1** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Criado na **consolidação Autores-de-Material (21/07/2026)** — a disciplina única do 4º–5º ano não tinha kit (só blueprints).

| Arquivo | Papel |
|---|---|
| `prompt-producao-capitulo.md` | Prompt de produção — ESCOPO (4º–5º, disciplina única, eixo por tema); campos `{ }` |
| `regras-editoriais.md` | Voz da faixa, CPA, rigor, eixos, boxes-"drops" |
| `convencao-latex-mathjax.md` | Fórmulas MathJax (cópia do kit de Operações — uso mínimo no EF1) |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (cópia idêntica à das outras disciplinas) |
| `validar-capitulo.py` | Validador compartilhado (`--disciplina matematica-ef1`) |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Matematica EF1/blueprints/<ano>/<bim>-<bloco>.md` (8 blueprints prontos desde 20/07/2026 — muito autossuficientes: já trazem eixo, CPA, NÃO ANTECIPAR e avisos da faixa).

## 2. Origem — tripla

1. **Formato:** molde do kit de **Operações** (família matemáticas), com todas as decisões vigentes: sem seções de fechamento, prosa+marcadores, exemplo resolvido com rótulo-situação e uma etapa por linha, VP condicional com teste do sinônimo, LaTeX MathJax.
2. **Regras da faixa:** coluna **4º–5º EF** do `_PADROES-DE-ESCRITA.md` §2 (20/07/2026) + regras transversais dos próprios blueprints do EF1 (metodologia **CPA** da Diretriz Matemática Fund 1 §1.2; exemplo antes do conceito; 1 exemplo claro por ideia e outro somente quando necessário; N1–N3; linguagem simples sem infantilização).
3. **Herança do autor antigo de Matemática** (`autores-material/autores/autor_matematica/`): apoio pictórico no Fundamental antes da formalização, formato de exemplo resolvido passo a passo.

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Disciplina única com eixo declarado por tema** — a escrita segue o eixo do tema (números → pictórico; medidas → instrumento/estimativa antes do cálculo; geometria → figura descrita). Não dividir em Operações/Geometria/Financeira no EF1.
2. **Extensão própria da faixa: sem alvo e sem mínimo, teto 160** (validador: `matematica-ef1: (0, 160)`). A aula termina quando o recorte foi explicado com clareza. Contas, tabelas, figuras e exemplos podem carregar a explicação sem prosa adicional.
3. **Boxes 🔢 e ⚠️** (família das matemáticas) — sem box de curiosidade das empíricas.
4. **LaTeX mínimo:** frações e contas quando a notação ajudar; a maior parte dos números em texto normal. A convenção MathJax vale integralmente quando usada.
5. **Escrever para crianças de 9–10 anos:** palavras comuns, frases curtas e voz de professor próximo. Evitar linguagem adulta quando houver opção simples. Diminutivos, personagens falantes e animação forçada continuam proibidos.
6. **TikZ/PNG autorizado como apoio pictórico:** usar quando posição, partição, equivalência ou comparação ficarem mais claras visualmente. Fontes e manifestos permanecem em `_tikz/`; o Markdown recebe URL absoluta do commit publicado e texto alternativo. Cada figura é conferida no original, a 300 px sobre branco e na coluna de 720 px.
7. **Multiplicação no EF1 usa `×`:** escrever `\times`, nunca `\cdot` nem a letra `x`. Etapas da mesma resolução ficam em um único bloco `aligned`, uma igualdade por linha, para evitar espaços excessivos e preservar a relação entre os passos.
8. **Referências históricas são pesquisa interna:** matemáticos citados nos blueprints não aparecem no texto do aluno. Biografias, datas, lugares e curiosidades históricas são cortados.

## 4. Estado e próximos passos

- [ ] Montar o projeto Claude.ai de Matemática EF1 (ver `_COMO-MONTAR-OS-PROJETOS.md` na raiz)
- [x] Modelo do 4º ano: Frações equivalentes e comparação · 7 aulas
- [x] Modelo do 5º ano: Igualdade e equivalência entre expressões · 5 aulas
- [x] **Calibrar a extensão:** sem alvo e sem mínimo de palavras, teto 160
- [x] Ilustrar os dois modelos: 10 figuras TikZ/PNG aprovadas, publicadas e validadas
- [x] Salvar os modelos ilustrados na pasta oficial do Google Drive
- [x] Produzir os outros 16 capítulos do 3º bimestre
- [x] Concluir o 3º bimestre: 18 capítulos, 96 aulas e 58 figuras TikZ/PNG
- [x] Salvar os 18 capítulos no Drive e conferir a leitura de retorno
- [ ] Produzir os 18 capítulos do 4º bimestre

### Ponto de retomada após limpeza de contexto

- O **3º bimestre está encerrado**: 18 capítulos, 96 aulas e 58 figuras.
- Os capítulos finais estão **somente no Google Drive**. Não recriar cópias em `conteudos-prontos` ou em pasta intermediária.
- Pasta oficial: [Matemática EF1](https://drive.google.com/drive/folders/1GrYCV9-QXcOczHZ6smQfQvDfbuv_29w-).
- Destinos: [4º Ano](https://drive.google.com/drive/folders/1Dvr5rFC6mb3a-t515D7V7qRa888-o3X0) e [5º Ano](https://drive.google.com/drive/folders/1RcU6FXM5c7sBWgIIRpPQ_gSdYGB2TkDy), com nove arquivos em cada.
- A pasta anterior `Segundo Semestre/MATEMÁTICA EDITANDO` está vazia e não deve voltar a ser usada.
- Os capítulos do 4º bimestre devem ser salvos diretamente na pasta do ano correspondente dentro de `Matemática EF1`.
- Os 18 arquivos do Drive foram conferidos após a última revisão: **18 correspondências exatas** e zero falhas nos dois validadores.
- Os modelos locais em `Matematica EF1/modelos/` já refletem o tom aprovado.
- O `AUTOR.md` e os validadores já estão ajustados para: sem mínimo de palavras, teto 160, linguagem infantil direta e nenhuma biografia.
- Próxima frente autorizável: **4º bimestre**, com 18 capítulos e 80 aulas. Ler os blueprints antes de produzir.

## 5. Histórico

| Data | O quê |
|---|---|
| 21/07/2026 | Kit criado na consolidação Autores-de-Material: molde de Operações + coluna 4º–5º EF dos padrões de escrita + regras CPA dos blueprints do EF1 + herança do autor antigo de Matemática. Extensão provisória 180–220 (teto 260). |
| 23/07/2026 | Modelos do 4º e do 5º ano produzidos e validados. O padrão inicial usava uma faixa de referência; após revisão editorial, Matemática EF1 ficou sem alvo e sem mínimo de palavras, com teto de segurança de 160 por aula. |
| 23/07/2026 | Dez figuras TikZ/PNG adicionadas aos modelos: 6 no 4º ano e 4 no 5º. Todas foram aprovadas, publicadas com URL imutável, validadas por SHA-256, revisadas no original, a 300 px e em coluna de 720 px. Os dois modelos foram salvos no Google Drive. |
| 23/07/2026 | Notação de multiplicação corrigida para `\times` (`×`) no EF1. Cadeias de cálculo reunidas em blocos `aligned`, com uma igualdade por linha, após revisão do modelo renderizado. |
| 23/07/2026 | Os 16 capítulos restantes do 3º bimestre foram produzidos em sequência e validados: 84 aulas novas. O conjunto oficial passou a ter 18 capítulos e 96 aulas, nove arquivos por série. |
| 23/07/2026 | Quarenta e oito novas figuras TikZ/PNG foram aprovadas, publicadas por URLs imutáveis, indexadas e revisadas no original, a 300 px e em contexto de 720 px. Somadas às dez dos modelos, Matemática EF1 possui 58 figuras em 18 documentos. |
| 23/07/2026 | Os 18 capítulos foram salvos no Google Drive. A leitura de retorno confirmou igualdade integral entre os 16 novos arquivos locais validados e suas cópias; cada pasta contém exatamente nove capítulos. |
| 23/07/2026 | Revisão de faixa etária aplicada aos 18 capítulos: linguagem mais simples e próxima, sem alvo ou mínimo de palavras, um exemplo claro por ideia e retirada integral de biografias e curiosidades históricas. Os dois validadores passaram em todos os arquivos, e a leitura de retorno do Drive confirmou 18 correspondências exatas. |
| 23/07/2026 | A pasta oficial foi corrigida para `Segundo Semestre/Matemática EF1`. As pastas `4º Ano` e `5º Ano`, com nove capítulos cada, foram migradas para o novo destino e conferidas após a mudança. A pasta anterior ficou vazia e foi retirada do fluxo de produção. |
