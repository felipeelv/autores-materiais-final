# Memória de continuidade — Autores de Material

Atualizado em **21/07/2026**.

## Objetivo

Organizar os autores de material didático por disciplina, com regras editoriais claras, um capítulo-modelo por ano/série e validadores independentes.

O **blueprint define o conteúdo**. O modelo de cada ano define apenas a forma, o ritmo e o nível de escrita.

## Decisões gerais

- A pasta principal é `Autores-de-Material/`.
- Cada disciplina possui `AUTOR.md`, `_MEMORIA.md`, `validar-capitulo.py` e, quando já calibrada, a pasta `modelos/`.
- A pasta antiga `conteudos/` foi apagada. Os capítulos de referência ficam junto do autor, em `Disciplina/modelos/`.
- Existe um modelo para cada ano ou série já trabalhado.
- Profundidade não significa mais texto: séries mais altas recebem conceitos mais densos dentro de volume semelhante.
- Parágrafos devem ser curtos, com uma ideia principal.
- Marcadores organizam enumerações, causas, consequências, etapas, grupos e contrastes reais.
- Blockquote simples (`>`) cria respiro visual para contraste, ressalva, exceção ou síntese.
- O padrão geral está em `PADRAO-GERAL-DE-ESCRITA.md`, espelhado em `_fontes/_PADROES-DE-ESCRITA.md`.
- `sincronizar.py` mantém os padrões comuns alinhados, sem sobrescrever os validadores específicos.

## Biologia

Modelos disponíveis:

- 9º ano;
- 1ª série do Ensino Médio;
- 2ª série do Ensino Médio;
- 3ª série do Ensino Médio.

Os quatro modelos ficam em `Biologia/modelos/` e passam no validador da disciplina.

## Ciências

Modelos disponíveis do **4º ao 8º ano**, em `Ciencias/modelos/`.

Regras calibradas:

- preferir 180–220 palavras por aula, com teto de 300 e sem mínimo obrigatório;
- manter volume e ritmo semelhantes em todos os anos;
- não deixar três parágrafos consecutivos sem lista, tabela, box ou blockquote;
- não deixar dois subtópicos `###` consecutivos sem lista de marcadores;
- subtópicos com marcadores podem aparecer em sequência;
- não criar listas artificiais apenas para cumprir a forma.

O validador de Ciências verifica automaticamente o ritmo da prosa e a alternância dos subtópicos.

## Física

Modelos disponíveis do **6º ao 9º ano e da 1ª à 3ª série do Ensino Médio**, em `Fisica/modelos/`.

Regras calibradas:

- manter 130–170 palavras por aula, com teto de 190 e sem aumento de volume nas séries mais altas;
- usar fórmula, tabela de grandezas e exemplo resolvido para carregar o formalismo;
- numerar os subtópicos como `N.1`, `N.2` e `N.3`;
- manter a progressão fenômeno → conceito ou lei → modelo idealizado → expressão matemática;
- não inserir versículos, mesmo quando o blueprint trouxer conexão VP;
- conferir cálculos, símbolos, notação vetorial e unidades SI antes da entrega.

Os sete modelos passam no validador da disciplina.

## Matemática Financeira

Modelos disponíveis do **6º ao 9º ano e da 1ª à 3ª série do Ensino Médio**, em `Financeira/modelos/`.

Regras calibradas:

- manter as aulas preferencialmente entre 220–250 palavras, com teto de 300 e sem mínimo obrigatório;
- organizar dados em tabelas Markdown e declarar quando um conjunto é hipotético;
- apresentar exemplos resolvidos passo a passo e interpretar todo resultado numérico;
- escrever valores monetários com duas casas e associar toda taxa ao seu período;
- distinguir mecanismos, riscos e consequências sem recomendar produtos ou prometer rentabilidade;
- explicitar população e amostra, além de conferir fórmulas, símbolos, percentuais e arredondamentos.

Os sete modelos passam no validador da disciplina. No capítulo de 9º ano, os dados reais de inflação e de garantia do FGC foram conferidos em fontes oficiais.

## Estudos Sociais

Modelos disponíveis do **4º ao 9º ano**, em `Estudos Sociais/modelos/`.

Foram aplicadas as mesmas regras visuais de Ciências:

- não deixar três parágrafos consecutivos sem quebra visual;
- não deixar dois subtópicos consecutivos sem marcadores;
- usar blockquote para ressalvas históricas, distinção entre fontes, contrastes e sínteses;
- usar marcadores apenas quando o conteúdo já apresentar elementos paralelos;
- manter parágrafos enxutos e aulas preferencialmente entre 180–220 palavras;
- manter de 1 a 2 boxes por aula, sem contar os blockquotes simples de respiro visual.

Os seis modelos totalizam **31 aulas e 31 boxes**: 14 🔎 Curiosidades, 11 💭 reflexões e 6 👤 personagens. Cada aula possui exatamente um box; informações que já estavam no corpo foram convertidas, em vez de duplicadas.

O validador de Estudos Sociais verifica automaticamente o ritmo da prosa e a alternância dos subtópicos.

A quantidade de boxes ainda exige conferência separada: o validador atual verifica a família permitida e impede boxes consecutivos, mas não reprova uma aula sem box.

## Estado da validação

Existem **29 capítulos-modelo**:

- 4 de Biologia;
- 5 de Ciências;
- 6 de Estudos Sociais;
- 7 de Física;
- 7 de Matemática Financeira.

Todos passam em `python3 validar-modelos.py`. Isso confirma a estrutura mecânica; a aprovação editorial final continua sendo feita pelo Felipe.

## GitHub

- Repositório definitivo: `felipeelv/autores-materiais-final`
- Visibilidade: privada
- Branch principal: `main`
- Os arquivos ficam diretamente na raiz do repositório.

O repositório antigo `autores-material` não deve ser usado como fonte desta versão final. A separação permite higienizar os arquivos antigos sem afetar os autores consolidados.

## Como continuar de casa

```bash
git clone https://github.com/felipeelv/autores-materiais-final.git
cd autores-materiais-final
python3 sincronizar.py --check
python3 validar-modelos.py
```

Se o repositório já estiver clonado:

```bash
git fetch origin
git switch main
git pull origin main
```

## Próximos passos

1. Validar visualmente os modelos de Biologia, Ciências, Estudos Sociais, Física e Matemática Financeira.
2. Registrar novos ajustes no `AUTOR.md` e no `_MEMORIA.md` da disciplina correspondente.
3. Aplicar o mesmo processo às demais disciplinas, uma por vez.
4. Manter o repositório final atualizado até a aprovação de todas as disciplinas.
