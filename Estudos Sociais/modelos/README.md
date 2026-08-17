# Modelos de Estudos Sociais por ano

> Estes capítulos são referências de linguagem, ritmo e organização visual. O conteúdo sempre vem do blueprint; o modelo não autoriza copiar recortes, exemplos ou dados para outro capítulo. Se houver divergência, prevalecem o blueprint e o `AUTOR.md` atual.

Cada ano tem **dois modelos**: o capítulo e o seu anexo. Desde 30/07/2026 a entrega de um capítulo são sempre os dois arquivos.

| Ano | Capítulo | Anexo |
|---|---|---|
| 4º ano | `estudos-sociais-4ano-modelo.md` | `estudos-sociais-4ano-modelo-anexo.md` |
| 5º ano | `estudos-sociais-5ano-modelo.md` | `estudos-sociais-5ano-modelo-anexo.md` |
| 6º ano | `estudos-sociais-6ano-modelo.md` | `estudos-sociais-6ano-modelo-anexo.md` |
| 7º ano | `estudos-sociais-7ano-modelo.md` | `estudos-sociais-7ano-modelo-anexo.md` |
| 8º ano | `estudos-sociais-8ano-modelo.md` | `estudos-sociais-8ano-modelo-anexo.md` |
| 9º ano | `estudos-sociais-9ano-modelo.md` | `estudos-sociais-9ano-modelo-anexo.md` |

Os modelos foram regenerados em 30/07/2026 a partir dos capítulos do 3º bimestre já revisados: box nunca abre subtópico, sem box `👤`, sem versículo no corpo, título com prefixo de bloco (`BL1_`/`BL2_`).

O modelo do 9º ano é o único cujo anexo sai **sem** "E para hoje…" — o blueprint do bloco 1 daquele ano não traz conexão VP. É o exemplo de como registrar a ausência em vez de inventar um versículo.

Geografia e História do Ensino Médio possuem pastas próprias na raiz do projeto.

## Validar os modelos

Na pasta `Estudos Sociais/`:

```bash
python3 validar-capitulo.py modelos/estudos-sociais-6ano-modelo.md --disciplina estudos-sociais
```

Para validar todos os modelos das três disciplinas de uma vez, execute `python3 validar-modelos.py` na raiz de `Autores-de-Material/`.
