# Memória do Kit — Filosofia · Produção de Capítulos (Autores-de-Material)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **21/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Filosofia** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Criado na **consolidação Autores-de-Material (21/07/2026)** — era um dos kits faltantes registrados no README de `prompts-producao/`.

| Arquivo | Papel |
|---|---|
| `prompt-producao-capitulo.md` | Prompt de produção — ESCOPO (1ª–3ª EM); campos `{ }` |
| `regras-editoriais.md` | Voz, rigor filosófico, ancoragem cristã, boxes-"drops" |
| `convencao-ortografica.md` | Acordo Ortográfico 1990 + escolhas da casa (cópia idêntica à das outras disciplinas) |
| `validar-capitulo.py` | Validador compartilhado (`--disciplina filosofia`) |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Filosofia/blueprints/<série>/<bim>-<bloco>.md` (12 blueprints prontos desde 19/07/2026). Sem arquivo de LaTeX — a disciplina não usa fórmulas.

## 2. Origem — dupla

1. **Formato:** molde dos kits validados em produção (Estudos Sociais/Ciências — família humanas), com todas as decisões vigentes: sem blocos pós-conteúdo, teto 300, prosa+marcadores, VP condicional com teste do sinônimo.
2. **DNA editorial:** autor antigo de Filosofia e Sociologia (`autores-material/autores/autor_filosofia/` — prompt-autor.md + CLAUDE.md), de onde vieram: família de boxes (💭 ⏸️ 💡 🔍 Conexão), o método "partir de perguntas, não de respostas prontas", argumento + contra-argumento como estrutura, adaptação por série (1ª fundantes → 2ª correntes/debates → 3ª síntese/ENEM) e a **regra inviolável de ancoragem cristã** (§4.1 do autor antigo, preservada integralmente).

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Blocos pós-conteúdo do autor antigo ABOLIDOS** (decisão do Felipe, 21/07/2026 — vale para todas as disciplinas): Ampliando o Olhar, No Fio da História, O Que a Fé Diz, Pensador em Destaque, Você já pensou nisso?, Simplificando, Para não esquecer. Funções dissolvidas nas aulas: contexto histórico vira narrativa curta na aula pertinente; problematização vira a própria estrutura argumento → objeção e os boxes; filósofo vira referência integrada ao texto (2–3 linhas, sem box); conexão bíblica vira versículo condicional inline; resumos saíram.
2. **Estrutura antiga de "exatamente 4 tópicos numerados" NÃO se aplica** — o número de tópicos agora é o número de aulas do blueprint (1 aula = 1 tópico).
3. **Ancoragem cristã preservada como inviolável** — Escritura como referencial, distinção fé/filosofia na mesma frase, comparações morais explícitas, fidelidade intelectual antes da avaliação.
4. **Box `🔍 Conexão:` mantido** (era a marca do autor antigo) no lugar de boxes de outras famílias.
5. **Extensão padrão da casa** (220–250, teto 300) — sem override no validador.
6. **Meta antiga de 1.300–1.600 palavras por capítulo REVOGADA** — a extensão agora é por aula, no padrão de todas as disciplinas.
7. **Pergunta-problema pode ficar em aberto** quando o próprio problema filosófico for a entrega da aula — desde que o aberto seja explícito e deliberado (particularidade desta disciplina).

## 4. Estado e próximos passos

- [x] Kit completo (prompt + regras + instruções + CLAUDE + esta memória + validador) — 21/07/2026
- [ ] Montar o projeto Claude.ai de Filosofia (ver `_COMO-MONTAR-OS-PROJETOS.md` na raiz)
- [ ] Capítulo piloto (sugestão: um bloco da 2ª série — testa a ancoragem cristã em pensador que desafia a fé, o caso mais sensível da disciplina)
- [ ] Após piloto aprovado pelo Felipe: registrar ajustes aqui

## 5. Histórico

| Data | O quê |
|---|---|
| 21/07/2026 | Kit criado na consolidação Autores-de-Material: formato dos kits validados + DNA do autor antigo de Filosofia e Sociologia. Blocos pós-conteúdo abolidos por decisão do Felipe. |
