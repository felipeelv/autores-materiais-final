# Modelos de Matemática EF1

Estes capítulos calibram linguagem, concisão, CPA e apresentação dos cálculos. O blueprint continua sendo a fonte do conteúdo.

| Ano | Arquivo | Conteúdo | Figuras |
|---|---|---|---:|
| 4º ano | `matematica-ef1-4ano-modelo.md` | Frações equivalentes e comparação | 6 |
| 5º ano | `matematica-ef1-5ano-modelo.md` | Igualdade e equivalência entre expressões | 4 |

## Padrão validado

- situação concreta → representação pictórica → procedimento → regra;
- sem alvo e sem mínimo de palavras, com teto de segurança de 160;
- contas, tabelas, ASCII, figuras e textos alternativos fora da contagem;
- um exemplo claro por ideia; segundo exemplo apenas quando necessário;
- palavras comuns, frases curtas e tom de professor próximo;
- nenhuma biografia ou curiosidade histórica;
- uma etapa por linha;
- nenhuma atividade proposta.

As figuras TikZ/PNG mostram partições, equivalências, comparações e balanças. Elas usam URLs imutáveis do commit publicado e foram revisadas no original, a 300 px e na coluna de 720 px.

## Google Drive

Os dois modelos foram formalizados como Capítulos 1 do 3º bimestre. O conjunto completo está em `Segundo Semestre/Matemática EF1`, na pasta [Matemática EF1](https://drive.google.com/drive/folders/1GrYCV9-QXcOczHZ6smQfQvDfbuv_29w-), separado em `4º Ano` e `5º Ano`.

Cada série possui nove capítulos oficiais. O registro completo está em `Matematica EF1/Acompanhamento de produção.md`.

## Validar

Na raiz do projeto:

```bash
python3 "Matematica EF1/validar-capitulo.py" "Matematica EF1/modelos/matematica-ef1-4ano-modelo.md" --disciplina matematica-ef1
python3 "Matematica EF1/validar-capitulo.py" "Matematica EF1/modelos/matematica-ef1-5ano-modelo.md" --disciplina matematica-ef1
```
