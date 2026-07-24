# Modelos de Física por série

> Estes capítulos são referências de linguagem, ritmo, notação e organização visual. O conteúdo sempre vem do blueprint; o modelo não autoriza copiar recortes, exemplos ou dados para outro capítulo. Se houver divergência, prevalecem o blueprint e o `AUTOR.md` atual. Os sete modelos foram revisados em 23/07/2026 após a adoção da passada específica de exatas.

| Série | Arquivo | Situação |
|---|---|---|
| 6º ano | `fisica-6ano-modelo.md` | Disponível para validação |
| 7º ano | `fisica-7ano-modelo.md` | Disponível para validação |
| 8º ano | `fisica-8ano-modelo.md` | Disponível para validação |
| 9º ano | `fisica-9ano-modelo.md` | Disponível para validação |
| 1ª série EM | `fisica-1serie-modelo.md` | Disponível para validação |
| 2ª série EM | `fisica-2serie-modelo.md` | Disponível para validação |
| 3ª série EM | `fisica-3serie-modelo.md` | Disponível para validação |

## Validar os modelos

Na pasta `Fisica/`:

```bash
python3 validar-capitulo.py modelos/fisica-6ano-modelo.md --disciplina fisica
```

Para validar todos os modelos disponíveis, execute `python3 validar-modelos.py` na raiz do repositório.

A auditoria semântica exige um contrato do capítulo e roda separadamente com `auditar-fisica.py`; não se reutiliza o contrato de um modelo para outro conteúdo.
