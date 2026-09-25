# Modelos de Português por ano/série

> Estes capítulos são referências de linguagem, ritmo e organização visual. O conteúdo sempre vem do blueprint; o modelo não autoriza copiar recortes, exemplos ou dados para outro capítulo. Se houver divergência, prevalecem o blueprint e o `AUTOR.md` atual.
>
> Padrão de concisão: cada ideia aparece uma vez; conceito novo segue definição curta → exemplo → uma observação; aplicação não redefine o princípio. Não há meta ou mínimo de palavras, apenas teto de 300 por aula.

| Ano/série | Arquivo | Capítulo de referência |
|---|---|---|
| 4º ano | `portugues-4ano-modelo.md` | Pronomes pessoais: caso reto e caso oblíquo |
| 5º ano | `portugues-5ano-modelo.md` | Sujeito |
| 6º ano | `portugues-6ano-modelo.md` | Pronomes: classes e emprego |
| 7º ano | `portugues-7ano-modelo.md` | Formas nominais do verbo |
| 8º ano | `portugues-8ano-modelo.md` | Sujeito |
| 9º ano | `portugues-9ano-modelo.md` | Concordância verbal |
| 1ª série EM | `portugues-1serie-modelo.md` | Pronomes |
| 2ª série EM | `portugues-2serie-modelo.md` | Próclise |
| 3ª série EM | `portugues-3serie-modelo.md` | Relações de sentido entre palavras |

## Validar os modelos

Na pasta `Portugues/`:

```bash
python3 validar-capitulo.py modelos/portugues-6ano-modelo.md --disciplina portugues
```

Para validar todos os modelos disponíveis, execute `python3 validar-modelos.py` na raiz do projeto.
