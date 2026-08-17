# Contrato semântico de Física

O contrato transforma decisões do blueprint em dados verificáveis. Ele não
substitui o blueprint: registra somente o que o auditor precisa para verificar
ordem conceitual e distinguir história essencial de biografia acessória.

## Fluxo

1. Antes da redação, criar `contratos-semanticos/<série>-<bimestre>-cap<n>.json`.
2. Registrar as grandezas já estabelecidas pelos capítulos anteriores.
3. Para cada resultado sensível à ordem, declarar a seção de introdução, os
   padrões que o identificam e suas dependências.
4. Para cada pessoa citada, registrar onde sua contribuição é essencial e quais
   padrões indicam biografia acessória.
5. Produzir o capítulo, rodar o validador mecânico e depois:

   ```bash
   python3 Fisica/auditar-fisica.py capitulo.md \
     --contrato Fisica/contratos-semanticos/contrato.json \
     --saida Fisica/relatorios/contrato.json
   ```

6. Corrigir automaticamente os achados de confiança alta e revalidar. Achados
   médios são decididos pelo autor/agente com justificativa no relatório. Só
   conflitos de baixa confiança ou divergências com o blueprint seguem para
   revisão humana.

## Campos

```json
{
  "capitulo": "Identificação legível",
  "blueprint": "caminho do blueprint",
  "grandezas_estabelecidas": [
    {"simbolo": "m", "grandeza": "massa", "unidade": "kg", "origem": "capítulo 1"}
  ],
  "conceitos": [
    {
      "id": "identificador_estavel",
      "introduzido_em": "3.1",
      "depende_de": ["outro_identificador"],
      "padroes": ["expressão regular que identifica o uso"]
    }
  ],
  "historia": {
    "pessoas": [
      {
        "id": "nome_curto",
        "padroes_nome": ["Nome", "Sobrenome"],
        "secoes_inline_essenciais": ["1.2"],
        "padroes_acessorios": ["nasceu", "morreu", "prêmio", "universidade"]
      }
    ]
  }
}
```

## Níveis de decisão

| Confiança | Destino |
|---|---|
| Alta, ≥ 0,90 | corrigir e revalidar sem revisão humana |
| Média, 0,65–0,89 | autor/agente decide e registra justificativa |
| Baixa, < 0,65 | humano apenas quando houver conflito real ou amostra final |

O auditor usa regras locais e transparentes. Ele não afirma compreender toda a
semântica do capítulo: o contrato reduz a ambiguidade antes da escrita e deixa
para o humano somente o que não pôde ser decidido com evidência.
