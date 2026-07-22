# _fontes — convenções comuns e espelho de compatibilidade

> **Não é insumo de produção.** Cada disciplina já tem tudo embutido no seu `AUTOR.md` (Parte 3 — Anexos A, B e C), porque a pasta da disciplina precisa funcionar sozinha. O padrão geral de escrita agora fica visível na raiz; esta pasta mantém as convenções e o caminho antigo por compatibilidade.

| Arquivo | Vira, nos `AUTOR.md` |
|---|---|
| `_PADROES-DE-ESCRITA.md` | Espelho automático de `../PADRAO-GERAL-DE-ESCRITA.md` — **não editar aqui** |
| `_CONVENCOES.md` | **Anexo B** (ortografia) e **Anexo C** (LaTeX/MathJax base) |

## Como mudar uma regra comum

1. Para nível × faixa e estrutura, edite `../PADRAO-GERAL-DE-ESCRITA.md`. Para ortografia ou LaTeX, edite `_CONVENCOES.md` aqui.
2. Rode `python3 sincronizar.py` na raiz — ele atualiza o espelho e reescreve a Parte 3 dos 12 `AUTOR.md`. Os validadores permanecem independentes por disciplina.
3. Suba de novo, nos Claude Projects afetados, os `AUTOR.md` que mudaram.

**Nunca edite a Parte 3 de um `AUTOR.md` diretamente** — a próxima sincronização sobrescreve. Regra que vale só para uma disciplina vai na Parte 2 (o manual), não no anexo.
