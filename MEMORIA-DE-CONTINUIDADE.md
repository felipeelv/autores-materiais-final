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

## Geometria

Modelos disponíveis do **6º ao 9º ano e da 1ª à 3ª série do Ensino Médio**, em `Geometria/modelos/`.

Regras calibradas:

- manter 170–210 palavras por aula, com teto de 240 e sem mínimo obrigatório;
- descrever toda configuração com pontos, posições relativas, medidas, dados e incógnitas suficientes para reconstruí-la;
- não usar imagens: diagramas simples podem ser representados em ASCII quando forem indispensáveis;
- apresentar justificativa geométrica antes da fórmula e uma operação por linha nos exemplos;
- escrever construções com instrumentos ou software como procedimentos descritos, nunca como atividades;
- manter unidade em todo resultado de comprimento, área, volume ou ângulo;
- não inserir versículos, mesmo quando o blueprint trouxer conexão VP.

Os sete modelos passam no validador da disciplina e foram conferidos quanto a fórmulas, unidades e descrição das configurações.

### Decisão pendente para 22/07/2026 — imagens em Geometria

O `Geometria/AUTOR.md` consolidado determina atualmente **“sem imagens”**: as figuras devem ser reconstruíveis por descrição verbal, notação geométrica e, quando indispensável, ASCII. Por essa razão, os sete modelos foram produzidos sem TikZ e sem PNG.

O fluxo especializado de produção de Geometria também oferece a possibilidade de gerar **fontes TikZ editáveis e imagens PNG incorporadas ao Markdown**. Felipe decidirá em **22/07/2026** se esse recurso deve passar a fazer parte do padrão oficial da disciplina.

Quando o assunto for retomado, seguir esta ordem:

1. decidir entre **manter o padrão textual atual** ou **adotar TikZ + PNG**;
2. se TikZ + PNG for aprovado, reajustar primeiro o `Geometria/AUTOR.md` — instruções do projeto, regras de figuras, proibições, estrutura da aula e checklist;
3. registrar a nova decisão em `Geometria/_MEMORIA.md`;
4. somente depois revisar os sete modelos e definir quais conceitos realmente exigem figura;
5. criar fontes `.tex`, renderizar PNGs e validar os links apenas para as figuras pedagogicamente necessárias.

**Gatilho de retomada:** se Felipe mencionar “imagens”, “TikZ”, “PNG” ou “figuras de Geometria”, reler esta pendência antes de alterar o autor ou gerar arquivos.

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

Existem **36 capítulos-modelo**:

- 4 de Biologia;
- 5 de Ciências;
- 6 de Estudos Sociais;
- 7 de Física;
- 7 de Matemática Financeira;
- 7 de Geometria.

Todos passam em `python3 validar-modelos.py`. Isso confirma a estrutura mecânica; a aprovação editorial final continua sendo feita pelo Felipe.

## GitHub

- Repositório definitivo: `felipeelv/autores-materiais-final`
- Visibilidade: privada
- Branch principal: `main`
- Branch de trabalho atual: `agent/consolida-modelos-curriculares`
- Os arquivos ficam diretamente na raiz do repositório.

O repositório antigo `autores-material` não deve ser usado como fonte desta versão final. A separação permite higienizar os arquivos antigos sem afetar os autores consolidados.

### Estado da publicação em 21/07/2026

- A branch de trabalho reúne os modelos de Estudos Sociais, Física, Matemática Financeira e Geometria.
- O PR rascunho [#1](https://github.com/felipeelv/autores-materiais-final/pull/1) está aberto contra a `main` com esse conjunto consolidado.
- A decisão sobre adotar TikZ e PNG em Geometria permanece pendente para 22/07/2026; os modelos publicados seguem a regra textual atualmente vigente.

## Como continuar de casa

```bash
git clone https://github.com/felipeelv/autores-materiais-final.git
cd autores-materiais-final
python3 sincronizar.py --check
python3 validar-modelos.py
```

Enquanto o PR #1 estiver aberto, retome pela branch de trabalho:

```bash
git fetch origin
git switch agent/consolida-modelos-curriculares
git pull --ff-only
```

## Próximos passos

1. Em 22/07/2026, decidir se Geometria continuará sem imagens ou adotará fontes TikZ editáveis e PNGs renderizados; se mudar, reajustar o `Geometria/AUTOR.md` antes dos modelos.
2. Validar visualmente os modelos de Biologia, Ciências, Estudos Sociais, Física, Matemática Financeira e Geometria.
3. Registrar novos ajustes no `AUTOR.md` e no `_MEMORIA.md` da disciplina correspondente.
4. Aplicar o mesmo processo às demais disciplinas, uma por vez.
5. Manter o repositório final atualizado até a aprovação de todas as disciplinas.
