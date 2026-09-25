# Autores de Material — Colégio Eleve

> **Fonte única dos autores de material didático.** Cada disciplina mantém um kit editorial autossuficiente. A produção técnica compartilhada de figuras fica isolada em `_tikz/`, sem espalhar fontes ou imagens pelas pastas das disciplinas. Formato único da Reorganização 2026 · 2º Semestre — **sem blocos pós-conteúdo**.

---

## 1. Como está organizado

```
Autores-de-Material/
├── PADRAO-GERAL-DE-ESCRITA.md ← fonte oficial comum, visível para consulta
├── <Disciplina>/            ← pasta autônoma, funciona sozinha
│   ├── AUTOR.md             ← TUDO da disciplina (manual + referência)
│   ├── _MEMORIA.md          ← decisões e histórico (não sobe no projeto)
│   ├── modelos/             ← um capítulo de referência por ano/série
│   └── validar-capitulo.py  ← conferência mecânica (roda no terminal)
├── _fontes/                 ← convenções comuns + espelho do padrão antigo
├── _skills/                 ← skills do Claude Code
├── _tikz/                   ← única área privada de produção de figuras TikZ
├── sincronizar.py           ← replica os anexos comuns nas 12 pastas
└── validar-capitulo.py      ← validador mestre
```

**O `AUTOR.md` tem três partes:**

| Parte | O que é | Uso |
|---|---|---|
| **1 — Instruções do projeto** | texto curto com as regras inegociáveis | colar no campo *Instruções do projeto* do claude.ai |
| **2 — Manual de produção** | escopo, estrutura, forma, construção da aula, voz, boxes, notação, proibições, integrações, checklist | o manual da disciplina |
| **3 — Referência** | Anexo A (nível × faixa + esqueleto do capítulo) · Anexo B (ortografia) · Anexo C (LaTeX, onde há fórmula) | consulta; igual em todas as disciplinas |

O arquivo `PADRAO-GERAL-DE-ESCRITA.md`, na raiz, é a **fonte oficial e mais simples de consultar** para nível N1–N4, linguagem por faixa e estrutura comum. O Anexo A de cada `AUTOR.md` é uma cópia integral gerada dele, preservada para que o kit editorial da disciplina continue funcionando sozinho. Quando houver figura autorizada, a produção e a rastreabilidade ficam centralizadas em `_tikz/`.

**O único insumo externo é o blueprint** — o conteúdo a desenvolver, que vive em `Reorganizacao-2026-2Semestre/disciplinas/<D>/blueprints/`.

| Kit | Escopo | Situação |
|---|---|---|
| `Portugues/` | Português 1 · 4º ano EF1 → 3ª EM | ✅ validado em produção *(EF1 sem piloto)* |
| `Matematica EF1/` | Matemática única · 4º–5º ano | ✅ 3º bimestre concluído: 18 capítulos · 96 aulas |
| `Operacoes/` | Matemática 1 · 6º → 3ª EM | ✅ validado em produção |
| `Geometria/` | Matemática 2 · 6º → 3ª EM | ✅ validado em produção |
| `Financeira/` | Matemática 3 · 6º → 3ª EM | ✅ 3º bimestre concluído: 14 capítulos · 42 aulas · Bloco 1 alinhado às páginas-resumo (11/08) |
| `Ciencias/` | 4º → 8º ano | ✅ validado em produção |
| `Biologia/` | 9º ano → 3ª EM | ✅ validado em produção |
| `Fisica/` | 6º ano → 3ª EM | ✅ validado em produção |
| `Quimica/` | 9º ano → 3ª EM | ✅ 3º bimestre concluído: 8 capítulos · 42 aulas · 15 figuras TikZ |
| `Estudos Sociais/` | 4º → 9º ano | ✅ validado em produção |
| `Geografia/` | 1ª → 3ª EM | ✅ 3º bimestre concluído: 12 capítulos · 54 aulas |
| `Historia/` | 1ª → 3ª EM | ✅ 3º bimestre concluído: 12 capítulos · 54 aulas |
| `Sociologia/` | 1ª → 3ª EM | ✅ 3º bimestre concluído: 6 capítulos · 18 aulas |
| `Filosofia/` | 1ª → 3ª EM | ✅ 3º bimestre concluído: 6 capítulos · 18 aulas |

**Estudos Sociais** mantém `instrucoes-geografia-historia-EM.md` apenas como registro legado. História usa exclusivamente `Historia/AUTOR.md`. **Português** mantém `referencia-exemplos-linguagem.md` e o capítulo-modelo aprovado.

## 2. O formato (decisão fechada)

**Não existem mais blocos pós-conteúdo** (decisão do Felipe, 21/07/2026): sem "Sua Parte", "O que a Bíblia diz", "Simplificando", "Para não esquecer", "Ampliando o Olhar", "Pensador em Destaque". Tudo vive **dentro das aulas**: `1 tema = 1 capítulo · 1 aula = 1 tópico ## N. · prosa curta + marcadores · Bíblia condicional inline (teste do sinônimo)`. O que sobreviveu dos autores antigos é a **proposta de conteúdo**: voz, famílias de boxes, adaptação por série e as regras invioláveis de cada disciplina.

> **Exceção — Estudos Sociais (30/07/2026).** A disciplina entrega **dois arquivos por capítulo**: o capítulo e um `{Tema} — Anexo.md`, com "Enquanto isso…", "E para hoje…" e "Esse foi o 'cara'". Não é volta do fechamento antigo: nada disso entra no corpo do capítulo, e por isso o **versículo saiu do fluxo da aula** nessa disciplina. Estudos Sociais também não tem mais box `👤`, e nela **o box nunca abre um subtópico** — esta última regra vale para todas as disciplinas (Anexo A §7 item 7).

**Hierarquia de autoridade:** **blueprint** (o quê e até onde) → **Anexo A** (como escrever no nível × faixa) → **Parte 2 do `AUTOR.md`** (voz e formato) → Parte 1 (instruções do projeto).

**Extensão por aula varia por disciplina:** padrão 220–250 (teto 300) · Ciências 140–200 (teto 220) · Estudos Sociais 180–220 (teto 300) · Geografia e História 145–175 (teto de segurança 200) · Filosofia 155–185 (teto de segurança 200) · Sociologia 175–195 (teto 200) · Física 130–170 (teto 190) · Química 180–210 (teto 240) · Geometria 170–210 (teto 240) · Matemática EF1 sem alvo nem mínimo (teto 160). O teto nunca é meta.

## 3. Montar um Claude Project

1. Crie o projeto no claude.ai com o nome da disciplina.
2. **Instruções:** copie a **Parte 1** do `AUTOR.md` e cole no campo *Instruções do projeto*.
3. **Conhecimento:** suba o `AUTOR.md` e, quando existir, **somente o modelo do ano/série em produção** (+ `referencia-exemplos-linguagem.md` em Português).
4. **Blueprints:** cópia fiel de `Reorganizacao-2026-2Semestre/disciplinas/<D>/blueprints/`, **renomeados com a série no nome** (`7ano-3bim-bloco1.md`) — no repositório todos se chamam `3bim-bloco1.md` e colidiriam. Em Estudos Sociais, prefixe a disciplina (`geografia-2serie-…`).
5. **Não suba** `_MEMORIA.md` nem `validar-capitulo.py` (um `.py` no claude.ai é lido como texto, não executa).
6. Se a janela encher: suba só os blueprints do bimestre em produção. Nunca suba capítulos prontos como conhecimento.

Um projeto por kit editorial ativo — **14 projetos**. As matemáticas não se juntam: as regras conflitam e os blueprints estourariam a janela.

## 4. Manutenção

- **Regra de uma disciplina só** → edite a **Parte 2** do `AUTOR.md`, registre no `_MEMORIA.md`, suba de novo no projeto.
- **Regra comum de escrita** (nível × faixa e estrutura) → edite `PADRAO-GERAL-DE-ESCRITA.md`, na raiz.
- **Ortografia ou LaTeX comum** → edite `_fontes/_CONVENCOES.md`.
- Depois de qualquer alteração comum, rode `python3 sincronizar.py`. Ele atualiza o espelho antigo e reescreve a Parte 3 das 12 pastas. `python3 sincronizar.py --check` mostra o que está fora de sincronia sem alterar nada.
- **Validadores são independentes:** ajuste e teste um por disciplina. A sincronização dos padrões não substitui nenhum `validar-capitulo.py`.
- **Nunca edite a Parte 3 direto numa disciplina** — a próxima sincronização sobrescreve.
- Conferência de um capítulo: `python3 <Disciplina>/validar-capitulo.py <cap.md> --disciplina <nome>`.
- Conferência de todos os modelos existentes: `python3 validar-modelos.py`.

## 5. O que fica fora daqui

- **Blueprints** — fonte única em `~/Reorganizacao-2026-2Semestre/disciplinas/<D>/blueprints/` (280 prontos).
- **Capítulos concluídos** — salvar diretamente na pasta oficial da disciplina em `Google Drive/Conteudos - Colégio Eleve/Segundo Semestre/`.
- Se a pasta da disciplina ou do ano/série ainda não existir no Drive, **crie-a e salve o capítulo nela**. A ausência da pasta não é motivo para usar outro destino.
- Não manter cópia final em `~/Reorganizacao-2026-2Semestre/conteudos-prontos/` nem em outra área intermediária; o Google Drive é o repositório único dos conteúdos concluídos.
- **Matemática EF1** — usar exclusivamente [Segundo Semestre/Matemática EF1](https://drive.google.com/drive/folders/1GrYCV9-QXcOczHZ6smQfQvDfbuv_29w-), com os arquivos separados nas pastas `4º Ano` e `5º Ano`.
- **Pastas antigas, não editar mais:** `~/autores-material/` (autores do pipeline por unidades — arquivo histórico, fonte da herança editorial) e `~/Reorganizacao-2026-2Semestre/prompts-producao/` (origem dos kits — **esta pasta é a mestra agora**).

## 6. Próximos passos

- [x] **Revisar os capítulos já prontos contra o teto vigente.** Ciências foi integralmente recalibrada para 140–200 palavras por aula, com teto de 220; Estudos Sociais também consta como concluído no controle geral.
- [ ] Revisar cada `AUTOR.md` com o Felipe, um por um.
- [x] Recalibrar o autor, criar os modelos e concluir no Drive os 6 capítulos do 3º bimestre de Sociologia.
- [ ] Piloto de Português EF1 (4º–5º).
- [x] Calibrar a extensão de Matemática EF1 com os modelos do 4º e do 5º ano.
- [x] Produzir, ilustrar e salvar no Drive os 18 capítulos do 3º bimestre de Matemática EF1.
- [x] Criar o autor exclusivo e concluir no Drive os 12 capítulos do 3º bimestre de Geografia.
- [x] Criar o autor exclusivo e os três modelos de História do Ensino Médio.
- [x] Produzir e salvar no Drive os 12 capítulos do 3º bimestre de História.
- [x] Recalibrar o autor, criar os modelos e concluir no Drive os 6 capítulos do 3º bimestre de Filosofia.
- [x] Capítulos-modelo por ano/série concluídos em Biologia (9º + EM), Ciências (4º–8º), Estudos Sociais (4º–9º), Física (6º–9º + EM), Matemática Financeira (6º–9º + EM) e Geometria (6º–9º + EM).
- [ ] Decisão pendente: versículo Mateus 25:40 repetido em 3 séries nos blueprints de Geometria.
- [ ] Decisão pendente: formato da Conexão VP — os kits praticam versículo condicional inline, mas o Anexo A §5 ainda marca como "em aberto". Física e Geometria já decidiram **não levar versículo**; **Estudos Sociais fechou em 30/07/2026**: versículo no arquivo de anexo, em "E para hoje…".
- [x] Reforma editorial de Estudos Sociais (30/07/2026): box nunca abre subtópico · fim do box 👤 · anexo como arquivo separado · convenção de título `BL1_`/`BL2_` oficializada no validador. 34 capítulos revisados e 34 anexos criados.
- [ ] Pendência aberta em Estudos Sociais: os 4 capítulos do **9º ano bloco 1** não têm Conexão VP no blueprint, e seus anexos saíram sem "E para hoje…". Corrigir no blueprint se o versículo for desejado.
- [x] Alinhar os 6 capítulos de Bloco 1 de Matemática Financeira aos exemplos das páginas-resumo aprovadas e republicar no Drive (11/08/2026).
- [ ] **Conferir a mesma divergência nas demais disciplinas.** Descoberto em Financeira: o `gerador-de-imagens` consome os **blueprints**, não os capítulos — o blueprint define o recorte, mas não os números, então autor de texto e autor de imagem inventam exemplos diferentes. Em Financeira, 7 das 18 páginas do Bloco 1 divergiam do capítulo. Vale auditar antes de imprimir qualquer disciplina que já tenha imagem aprovada.
- [ ] Decisão pendente: notação do coeficiente de variação — a página-resumo da 1ª série de Financeira traz `CV = σ/x̄` e o `AUTOR.md` traz `CV = s/x̄`. Ajustar o kit ou regerar a imagem.
- [x] **Validadores ressincronizados (11/08/2026).** Há 15 arquivos `validar-capitulo.py`; 2 são shims (`Historia/` e `Geografia/` executam o de Estudos Sociais via `runpy`), restando 13 implementações reais — o mestre da raiz e 12 cópias por disciplina. As duas lacunas de comportamento foram fechadas nos 13:
  - **Prefixo `BL1_`/`BL2_`** existia em 1 de 13. As outras 12 exigiam `# Capítulo N — Tema` e **reprovavam todos os capítulos em produção** — verificado: as 12 disciplinas usam o prefixo no Drive. Portada a lógica de Estudos Sociais: o prefixo é **aceito em qualquer disciplina** e **obrigatório só onde `prefixo_bloco=True`** no `DISC` (hoje, apenas `estudos-sociais`). Para exigir em outra disciplina, basta acrescentar a chave.
  - **`[2b] Prosa × marcadores`** existia em 2 de 13 (Biologia e Química). Portado para os outros 11, na versão de Química — que descarta imagem Markdown e comentário HTML antes de medir. Segue **diagnóstico, nunca reprova**. Ciências, Estudos Sociais e Filosofia já estavam renumeradas para `[2c]` esperando o bloco que nunca chegou; Filosofia estava incoerente (comentário `2c`, print `[2b]`). Índice do docstring corrigido nos 11.
  - Não eram divergências: a função `contar_conteudo()` tem 4 variantes de texto, mas só 2 comportamentos — descartar ou não imagem Markdown e comentário HTML antes de contar —, e o corte segue as disciplinas que embutem figura TikZ (mestre, Física, Geometria, Química, Matemática EF1). O limite 140–220 de Ciências é escolha da disciplina, que cobre 4º–8º ano. Ambos ficaram como estavam.
- [ ] Os 13 validadores continuam sendo **13 arquivos separados** — o patch igualou o comportamento, não a manutenção. Vale avaliar transformar as cópias em shims do mestre, como já fazem `Historia/` e `Geografia/`.
- [ ] A entrada `"estudos-sociais"` no `DISC` das 12 cópias ainda lista o box `👤`, removido na reforma de 30/07. Não afeta ninguém (Estudos Sociais roda pelo próprio validador), mas está desatualizada.
