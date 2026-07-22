---
name: validar-capitulo
description: Use depois de escrever ou editar um capítulo de material didático da Reorganização 2026/2S, antes de dar a entrega por concluída. Roda a verificação mecânica (extensão por aula, seções de fechamento proibidas, boxes, emoji fora de box, ortografia pré-Acordo) e interpreta o resultado. Também quando o usuário pedir para "validar o capítulo", "conferir se está dentro das regras" ou "rodar o validador".
---

# Validar capítulo — verificação mecânica

Roda `validar-capitulo.py` e traduz a saída. Existe para você **não montar bateria de grep** nem conferir contagem à mão: é um comando só, e o resultado é lido, não recontado.

## Quando rodar

**Depois de entregar o capítulo, como passo separado** — nunca no meio da escrita. Rodar durante a produção multiplica o tempo sem melhorar o texto, e persegue contagem em vez de conteúdo.

## O comando

```bash
python3 ~/Autores-de-Material/validar-capitulo.py <capitulo.md> --disciplina <slug>
```

O script é **idêntico nas 9 disciplinas** — rode o de qualquer pasta, o que muda é o slug. A partir da raiz do repo:

```bash
python3 ~/Autores-de-Material/validar-capitulo.py \
  "conteudos-prontos/Biologia/9ano/biologia-9ano-3bim-cap1.md" \
  --disciplina biologia \
```

## Mapeamento pasta → slug

A pasta em `conteudos-prontos/` não é igual ao slug do `--disciplina`:

| Pasta em `conteudos-prontos/` | slug |
|---|---|
| `Biologia` | `biologia` |
| `Ciencias` | `ciencias` |
| `Fisica` | `fisica` |
| `Quimica` | `quimica` |
| `Estudos Sociais` | `estudos-sociais` |
| `Operacoes` | `operacoes` |
| `Geometria` | `geometria` |
| `Financeira` | `financeira` |
| `Portugues` | `portugues` |

**O slug importa:** ele define a família de boxes aceita. Rodar Biologia com `--disciplina quimica` reprova boxes válidos.

## Achar o blueprint


```
conteudos-prontos/<Disc>/<serie>/<disc>-<serie>-<bim>-cap<N>.md
        ↓
disciplinas/<Disc>/blueprints/<serie>/<bim>-bloco1.md
```

`biologia-9ano-3bim-cap1.md` → `disciplinas/Biologia/blueprints/9ano/3bim-bloco1.md`.

Blocos possíveis: `3bim-bloco1` · `3bim-bloco2` · `4bim-bloco1` · `4bim-bloco23`.

## Como ler a saída

Código de saída: **0** se nada falhou, **1** se há falha. `⚠️` são avisos e **não** falham.

| Seção | O que significa |
|---|---|
| `[1] Estrutura` | título `# Capítulo N — Tema` e aulas numeradas em ordem |
| `[2] Extensão` | 220–250 é o alvo · **teto firme 300** · acima de 330 (+10%) **reprova** · abaixo de 180 só avisa |
| `[2b] Prosa × marcadores` | **diagnóstico — nunca reprova.** Referência ~45% de prosa |
| `[3] Fechamento` | seções proibidas (Sua Parte, Simplificando, Para não esquecer…) |
| `[4] Boxes` | família permitida da disciplina · nenhum par consecutivo |
| `[5] Emoji fora de box` | emoji solto no corpo |
| `[6] Ortografia` | formas pré-Acordo e trema indevido |
| `[8] NÃO ANTECIPAR` | imprime a lista do blueprint — **conferir por leitura**, o script não decide |

### O que o `[2b]` quer dizer

Não é um portão e **não deve virar meta**. Percentual alto sozinho não é defeito: aula de cálculo ou de raciocínio encadeado é prosa por natureza. O aviso que se sustenta sozinho é **"sem lista nem tabela"** — aula inteira sem nenhuma estrutura quase sempre tem conteúdo enumerável escondido em parágrafo.

Se for corrigir, corrija pela regra operacional (*máximo 2 frases seguidas antes de uma lista*), nunca perseguindo o número — travar no percentual produz bullet forçado e raciocínio picotado.

## O que ele NÃO faz

Estes ficam para conferência de leitura, sua ou do Felipe:

- se o **recorte do blueprint** foi cumprido;
- se algum item do **NÃO ANTECIPAR** apareceu (o script só imprime a lista);
- **qualidade**, clareza, adequação de nível;
- se o **versículo** tem ligação conceitual ou é trocadilho (aplique o teste do sinônimo).

## Rodar em lote

Para varrer uma disciplina inteira e ver só o que falhou:

```bash
for f in conteudos-prontos/Biologia/*/*.md; do
  python3 ~/Autores-de-Material/validar-capitulo.py "$f" --disciplina biologia >/dev/null 2>&1 \
    || echo "FALHOU: $f"
done
```

## Depois de rodar

Relate ao usuário **o que falhou e o que você fez**, não o relatório inteiro. Se nada falhou, uma linha basta — e não invente aprovação: se o script não rodou, diga que não rodou.
