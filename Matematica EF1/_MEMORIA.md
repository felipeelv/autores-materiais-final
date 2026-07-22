# Memória do Kit — Matemática EF1 · Produção de Capítulos (Autores-de-Material)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **21/07/2026**.

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
2. **Regras da faixa:** coluna **4º–5º EF** do `_PADROES-DE-ESCRITA.md` §2 (20/07/2026) + regras transversais dos próprios blueprints do EF1 (metodologia **CPA** da Diretriz Matemática Fund 1 §1.2; exemplo antes do conceito sem exceção; 2 exemplos por conceito; N1–N3; sem infantilizar).
3. **Herança do autor antigo de Matemática** (`autores-material/autores/autor_matematica/`): apoio pictórico no Fundamental antes da formalização, formato de exemplo resolvido passo a passo.

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Disciplina única com eixo declarado por tema** — a escrita segue o eixo do tema (números → pictórico; medidas → instrumento/estimativa antes do cálculo; geometria → figura descrita). Não dividir em Operações/Geometria/Financeira no EF1.
2. **Extensão própria da faixa: alvo 180–220, teto 260** (validador: `matematica-ef1: (150, 260)`). Racional: criança de 9–10 anos lê menos texto, e contas/ASCII ficam fora da contagem. **Calibração PROVISÓRIA — ajustar após o capítulo piloto** (mesmo processo que apertou Física para 190 e Geometria para 240).
3. **Boxes 🔢 e ⚠️** (família das matemáticas) — sem box de curiosidade das empíricas.
4. **LaTeX mínimo:** frações e contas quando a notação ajudar; a maior parte dos números em texto normal. A convenção MathJax vale integralmente quando usada.
5. **Infantilização é o erro nº 1 da faixa** — proibição explícita de diminutivos e personagem falante no prompt e nas regras (herdada da experiência de Ciências EF1, 20/07/2026).

## 4. Estado e próximos passos

- [ ] Montar o projeto Claude.ai de Matemática EF1 (ver `_COMO-MONTAR-OS-PROJETOS.md` na raiz)
- [ ] Capítulo piloto (sugestão: Frações equivalentes e comparação · 4º ano · `4ano-3bim-bloco1.md`, Capítulo 1 — 7 aulas, testa CPA + eixo pictórico + NÃO ANTECIPAR de denominadores diferentes)
- [ ] **Calibrar a extensão** (alvo/teto) com o piloto e registrar aqui
- [ ] Após piloto aprovado pelo Felipe: registrar ajustes aqui

## 5. Histórico

| Data | O quê |
|---|---|
| 21/07/2026 | Kit criado na consolidação Autores-de-Material: molde de Operações + coluna 4º–5º EF dos padrões de escrita + regras CPA dos blueprints do EF1 + herança do autor antigo de Matemática. Extensão provisória 180–220 (teto 260). |
