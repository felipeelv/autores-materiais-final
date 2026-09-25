# Modelos de Geometria por série

> Estes capítulos são referências de linguagem, ritmo, notação, descrição de figuras e organização visual. O conteúdo sempre vem do blueprint; o modelo não autoriza copiar recortes ou exemplos para outro capítulo. Se houver divergência, prevalecem o blueprint e o `AUTOR.md` atual.

| Série | Arquivo | Situação |
|---|---|---|
| 6º ano | `geometria-6ano-modelo.md` | Validado com 6 figuras TikZ/PNG publicadas |
| 7º ano | `geometria-7ano-modelo.md` | Validado com 5 figuras TikZ/PNG publicadas |
| 8º ano | `geometria-8ano-modelo.md` | Validado com 5 figuras TikZ/PNG publicadas |
| 9º ano | `geometria-9ano-modelo.md` | Validado com 5 figuras TikZ/PNG publicadas |
| 1ª série EM | `geometria-1serie-modelo.md` | Validado com 12 figuras TikZ/PNG publicadas |
| 2ª série EM | `geometria-2serie-modelo.md` | Validado com 10 figuras TikZ/PNG publicadas |
| 3ª série EM | `geometria-3serie-modelo.md` | Validado com 8 figuras TikZ/PNG publicadas |

O contrato visual definitivo está em `../../_tikz/PADRAO-DE-CONSTRUCAO.md`. O conteúdo de cada figura, a ordem dos lotes e o ponto exato de inserção no Markdown dos modelos estão em `../PLANO-DE-IMAGENS-TIKZ.md`.

O 3º bimestre completo está registrado em `../Acompanhamento de produção.md`: 15 capítulos, 60 aulas e 111 PNGs publicados. As 60 figuras dos oito capítulos seguintes, com seus commits públicos, estão documentadas em `../PLANO-DE-IMAGENS-TIKZ-BLOCO2.md`.

## Validar os modelos

Na pasta `Geometria/`:

```bash
python3 validar-capitulo.py modelos/geometria-6ano-modelo.md --disciplina geometria
```

Para validar todos os modelos disponíveis, execute `python3 validar-modelos.py` na raiz do repositório.
