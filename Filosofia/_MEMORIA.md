# Memória do Kit — Filosofia · Produção de Capítulos (Autores-de-Material)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **24/07/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Filosofia** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Criado na **consolidação Autores-de-Material (21/07/2026)** — era um dos kits faltantes registrados no README de `prompts-producao/`.

| Arquivo | Papel |
|---|---|
| `AUTOR.md` | Instruções, manual editorial e referências comuns |
| `modelos/` | Um capítulo-modelo por série do Ensino Médio |
| `validar-capitulo.py` | Validação de estrutura, extensão, ritmo e boxes |
| `Acompanhamento de produção.md` | Estado dos modelos e da produção oficial |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Filosofia/blueprints/<série>/<bim>-<bloco>.md` (12 blueprints prontos desde 19/07/2026). Sem arquivo de LaTeX — a disciplina não usa fórmulas.

## 2. Origem — dupla

1. **Formato:** molde dos kits validados da família de Humanas, recalibrado para prosa concisa, marcadores seletivos, respiro visual e VP condicional com teste do sinônimo.
2. **DNA editorial:** autor antigo de Filosofia e Sociologia (`autores-material/autores/autor_filosofia/` — prompt-autor.md + CLAUDE.md), de onde vieram: família de boxes (💭 ⏸️ 💡 🔍 Conexão), o método "partir de perguntas, não de respostas prontas", argumento + contra-argumento como estrutura, adaptação por série (1ª fundantes → 2ª correntes/debates → 3ª síntese/ENEM) e a **regra inviolável de ancoragem cristã** (§4.1 do autor antigo, preservada integralmente).

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Blocos pós-conteúdo do autor antigo ABOLIDOS** (decisão do Felipe, 21/07/2026 — vale para todas as disciplinas): Ampliando o Olhar, No Fio da História, O Que a Fé Diz, Pensador em Destaque, Você já pensou nisso?, Simplificando, Para não esquecer. Funções dissolvidas nas aulas: contexto histórico vira narrativa curta na aula pertinente; problematização vira a própria estrutura argumento → objeção e os boxes; filósofo vira referência integrada ao texto (2–3 linhas, sem box); conexão bíblica vira versículo condicional inline; resumos saíram.
2. **Estrutura antiga de "exatamente 4 tópicos numerados" NÃO se aplica** — o número de tópicos agora é o número de aulas do blueprint (1 aula = 1 tópico).
3. **Ancoragem cristã preservada como inviolável** — Escritura como referencial, distinção fé/filosofia na mesma frase, comparações morais explícitas, fidelidade intelectual antes da avaliação.
4. **Box `🔍 Conexão:` mantido** (era a marca do autor antigo) no lugar de boxes de outras famílias.
5. **Extensão recalibrada** em 24/07/2026: preferir 155–185 palavras por aula, admitir até 190 em recortes densos e nunca ultrapassar 200.
6. **Meta antiga de 1.300–1.600 palavras por capítulo REVOGADA** — a extensão agora é por aula, no padrão de todas as disciplinas.
7. **Pergunta-problema pode ficar em aberto** quando o próprio problema filosófico for a entrega da aula — desde que o aberto seja explícito e deliberado (particularidade desta disciplina).
8. **Ritmo visual:** parágrafos de uma ou duas frases, sem três blocos corridos; toda aula possui ao menos uma lista ou tabela ligada ao raciocínio central; um ou dois blockquotes simples por capítulo.
9. **Boxes:** exatamente um por aula, em uma frase curta, apenas da família 💭/⏸️/💡/🔍.

## 4. Estado e próximos passos

- [x] Kit completo (prompt + regras + instruções + CLAUDE + esta memória + validador) — 21/07/2026
- [x] Autor e validador recalibrados no padrão conciso — 24/07/2026
- [x] Três capítulos-modelo produzidos e validados — 24/07/2026
- [x] Modelos aprovados e formalizados como Capítulos 1 — 24/07/2026
- [x] Três Capítulos 2 produzidos, validados e salvos no Drive — 24/07/2026
- [ ] Montar o projeto Claude.ai de Filosofia (ver `_COMO-MONTAR-OS-PROJETOS.md` na raiz)

Os modelos são `Aristóteles — metafísica e ética`, `Nietzsche e a morte de Deus` e `Filosofia antiga e medieval`. Eles permanecem em `modelos/` como referência editorial e foram formalizados como os três Capítulos 1.

O 3º bimestre está concluído com **6 capítulos e 18 aulas**. As aulas ficaram entre **158 e 185 palavras**, com média de **178,8**. Cada aula possui ao menos uma lista ou tabela e exatamente um box; cada capítulo usa dois blockquotes simples. Todos passam no validador e respeitam os itens `NÃO ANTECIPAR`.

A pasta oficial é [Segundo Semestre/Filosofia](https://drive.google.com/drive/folders/1X-rhNe1FWP-Y_QIhdaNRSdWOIzZVHChZ), com subpastas [1ª Série](https://drive.google.com/drive/folders/1TemmeBfXEN3CCMoxxZ6h0eSpN4Ka-hhf), [2ª Série](https://drive.google.com/drive/folders/1PdVDd9fKz78xsVtV4D1-p4WRJ9xGSkZ3) e [3ª Série](https://drive.google.com/drive/folders/1d0ZC75_GYrzormk3WiYkrfVjTiowqOl6). Cada subpasta contém dois arquivos Markdown; a leitura de retorno confirmou igualdade integral com as versões validadas.

A revisão factual adotou formulações cautelosas para tradições biográficas: peripatéticos ligados ao passeio do Liceu; colapso de Nietzsche sem apresentar como fato o episódio não documentado do cavalo; “só sei que nada sei” identificado como fórmula tradicional.

## 5. Histórico

| Data | O quê |
|---|---|
| 21/07/2026 | Kit criado na consolidação Autores-de-Material: formato dos kits validados + DNA do autor antigo de Filosofia e Sociologia. Blocos pós-conteúdo abolidos por decisão do Felipe. |
| 24/07/2026 | Autor e validador recalibrados; três modelos produzidos com 9 aulas, um box por aula e dois blockquotes simples por capítulo. |
| 24/07/2026 | Modelos reorganizados visualmente; listas, linhas do tempo e quadros comparativos passaram a estruturar todas as aulas. |
| 24/07/2026 | Modelos aprovados e formalizados; três Capítulos 2 produzidos. O 3º bimestre foi concluído, validado e salvo na pasta oficial. |
