# Como instalar e usar as skills — Reorganização 2026 · 2º Semestre

> As skills desta pasta valem para **todas as disciplinas**. É o oposto dos kits: em vez de nove cópias que envelhecem separadamente, uma regra escrita uma vez, disponível em todos os projetos.

---

## 0. Instalação no Claude Code (já feita)

As skills desta pasta estão **instaladas no escopo do projeto**, via symlink:

```
Reorganizacao-2026-2Semestre/
  .claude/skills/
    calibragem-do-aluno -> ../../_skills/calibragem-do-aluno
    validar-capitulo    -> ../../_skills/validar-capitulo
```

**Por que symlink e não cópia:** o motivo desta pasta existir é não ter cópias que envelhecem separadamente (ver abertura deste arquivo). Symlink mantém **um arquivo só**, versionado no git — quem clonar o repo já recebe as skills funcionando, e editar o `SKILL.md` aqui atualiza as duas pontas ao mesmo tempo. Os links são **relativos**, então sobrevivem ao clone em qualquer caminho.

**Escopo de projeto** significa que elas só ficam ativas quando o Claude Code está rodando dentro deste repositório — que é onde fazem sentido. O Claude as invoca sozinho pela `description`; não é preciso chamá-las.

**Ao criar uma skill nova:** crie a pasta em `~/Autores-de-Material/_skills/<nome>/SKILL.md` e acrescente o symlink em `.claude/skills/`. Skills novas são carregadas no **início da sessão** — reinicie o Claude Code para vê-las.

## 1. Instalação no claude.ai

1. Compacte a pasta da skill em **.zip** (a pasta inteira, com o `SKILL.md` dentro):
   ```
   calibragem-do-aluno/
     SKILL.md
   ```
2. No claude.ai, vá em **Customize → Skills → + → Create skill** e envie o .zip.
3. A skill aparece na lista e pode ser ligada/desligada. **O Claude a invoca sozinho** quando a tarefa combina com a `description` — não é preciso chamá-la.
4. Se sua conta for de organização, subir por *organization settings* deixa a skill disponível para todo mundo, sem cada um subir a sua.

**Plano B, se as skills não estiverem disponíveis na sua conta:** suba o `SKILL.md` como arquivo no **conhecimento do projeto** e acrescente uma linha às instruções do projeto (ver §3). Funciona igual — só perde a portabilidade automática entre os nove projetos.

## 2. Skills desta pasta

| Skill | Para quê | Onde funciona |
|---|---|---|
| `calibragem-do-aluno` | ajustar a escrita à série (frase, voz, exemplo), ao nível N2/N3/N4 e à **forma** (prosa × marcadores) | Claude Code e claude.ai |
| `validar-capitulo` | rodar `validar-capitulo.py` e interpretar a saída — mapeia pasta→slug, acha o blueprint, lê o relatório | **só Claude Code** (precisa executar o script) |

*(Planejada: revisão ortográfica.)*

## 3. A linha a acrescentar nas instruções de cada projeto

Na **Parte 1** do `AUTOR.md` da disciplina (o texto colado no campo *Instruções do projeto*), junto das regras inegociáveis:

> Ao escrever cada aula, aplique a skill **calibragem-do-aluno** para ajustar a frase, a voz e o nível (N2/N3/N4) à série pedida. Ela **executa** o que o blueprint definiu — nunca muda o recorte, o nível ou a lista NÃO ANTECIPAR.

## 4. Onde a skill entra na hierarquia

**blueprint → regras editoriais → prompt de produção → instruções do projeto**, e as **skills como auxiliares de execução**.

Uma skill nunca sobrepõe o blueprint. A `calibragem-do-aluno` ajuda a *executar* o nível que o blueprint mandou; jamais a mudá-lo. Se uma skill parecer contradizer o blueprint, o blueprint vence e a skill está errada — corrija a skill.

## 5. Manutenção

Ao editar uma skill: teste antes de subir. O método usado para criar a `calibragem-do-aluno` foi:

1. **Baseline (RED):** peça a um Claude sem a skill para escrever uma aula real de blueprint. Meça o que saiu.
2. **Escreva a skill (GREEN)** atacando só as falhas que apareceram — não as imaginadas.
3. **Rode de novo** com a skill e **meça de novo**. Se corrigiu uma coisa e quebrou outra, ajuste e repita.

Sem baseline, você escreve regra para problema que não existe — e o problema real passa.

---

*jul/2026 · instalação conferida em [support.claude.com](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) (Customize → Skills → Create skill, upload .zip) e [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) (invocação automática pela description).*
