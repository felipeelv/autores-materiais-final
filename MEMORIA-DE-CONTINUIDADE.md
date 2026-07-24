# Memória de continuidade — Autores de Material

Atualizado em **23/07/2026**.

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

## Matemática EF1

### Produção do 3º bimestre — concluída em 23/07/2026

- Os **18 capítulos previstos**, totalizando **96 aulas**, foram produzidos: nove do 4º ano e nove do 5º.
- Os dois modelos foram formalizados como Capítulos 1; os outros 16 capítulos somam 84 aulas novas.
- O padrão definitivo ficou **sem alvo e sem mínimo de palavras**, com teto de segurança de 160 por aula.
- A voz foi simplificada para crianças de 9–10 anos: palavras comuns, frases curtas, um exemplo claro por ideia e nenhuma biografia ou curiosidade histórica.
- Os cálculos usam `\times` para multiplicação e reúnem etapas relacionadas em um único bloco `aligned`.
- As **58 figuras TikZ/PNG** foram aprovadas, publicadas por URLs imutáveis, indexadas, validadas por SHA-256 e revisadas no original, a 300 px e em contexto de 720 px.
- Os arquivos estão em `Segundo Semestre/Matemática EF1`, na pasta oficial [Matemática EF1 — Google Drive](https://drive.google.com/drive/folders/1GrYCV9-QXcOczHZ6smQfQvDfbuv_29w-).
- A estrutura oficial é [4º Ano](https://drive.google.com/drive/folders/1Dvr5rFC6mb3a-t515D7V7qRa888-o3X0) e [5º Ano](https://drive.google.com/drive/folders/1RcU6FXM5c7sBWgIIRpPQ_gSdYGB2TkDy), com exatamente nove arquivos em cada pasta. Após a revisão editorial, a leitura de retorno confirmou igualdade integral dos 18 arquivos com a produção local validada.
- A pasta anterior `Segundo Semestre/MATEMÁTICA EDITANDO` ficou vazia após a migração e **não é mais um destino válido**.
- O controle detalhado está em `Matematica EF1/Acompanhamento de produção.md`.

O 4º bimestre permanece pendente: **18 capítulos e 80 aulas**.

### Ponto de retomada de Matemática EF1

- Não há trabalho pendente no 3º bimestre.
- Os capítulos finais ficam apenas no Drive; os modelos e as fontes TikZ permanecem locais.
- Salvar toda nova produção do 4º ano em `Matemática EF1/4º Ano` e toda nova produção do 5º ano em `Matemática EF1/5º Ano`.
- O padrão vigente está em `Matematica EF1/AUTOR.md`: linguagem direta para crianças, sem mínimo de palavras, teto 160, um exemplo claro por ideia e nenhuma referência histórica.
- A próxima produção é o 4º bimestre. Antes de iniciar, usar `Matematica EF1/Acompanhamento de produção.md` e os blueprints como fontes de estado.

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
- usar figuras produzidas em TikZ e renderizadas em PNG quando a configuração visual favorecer a compreensão;
- concentrar fonte `.tex`, manifesto, ferramentas e renderizações temporárias exclusivamente em `_tikz/`;
- publicar somente o PNG aprovado em `felipeelv/imagens-tikz` e indexar sua URL absoluta no Markdown;
- usar ASCII simples quando ele for suficiente, sem duplicar uma figura TikZ/PNG equivalente;
- apresentar justificativa geométrica antes da fórmula e uma operação por linha nos exemplos;
- escrever construções com instrumentos ou software como procedimentos descritos, nunca como atividades;
- manter unidade em todo resultado de comprimento, área, volume ou ângulo;
- não inserir versículos, mesmo quando o blueprint trouxer conexão VP.

Os sete modelos passam no validador da disciplina e foram conferidos quanto a fórmulas, unidades e descrição das configurações.

### Decisão de 22/07/2026 — imagens em Geometria

Felipe aprovou o uso de **fontes TikZ editáveis e imagens PNG incorporadas ao Markdown**. A proibição geral de imagens em Geometria foi revogada no `Geometria/AUTOR.md` e em `Geometria/_MEMORIA.md`.

O padrão oficial passa a ser:

1. usar figura apenas quando a configuração visual tiver função pedagógica;
2. preservar a fonte `.tex` e o manifesto privado em `_tikz/` e renderizar uma versão `.png` transparente a 300 DPI, sem cartão externo ou painéis brancos;
3. publicar somente o PNG aprovado em `felipeelv/imagens-tikz` e indexar sua URL absoluta no Markdown com texto alternativo descritivo;
4. informar no texto as medidas, relações e incógnitas necessárias para interpretar a figura;
5. usar ASCII apenas quando for suficiente e não duplicar uma figura TikZ/PNG equivalente;
6. impedir referências vagas, imagens inexistentes e links quebrados.

O criador definitivo está em `_tikz/`: fonte multipágina, manifesto por documento, estilo visual, renderização transparente, aprovação, publicação protegida e indexação idempotente. O validador confere canal alfa, URL do repositório autorizado, manifesto e fonte privados, texto alternativo, SHA-256 e registro da versão publicada. As figuras são planejadas e revisadas na largura efetiva mínima de 300 px sobre fundo branco, com composição vertical ou quase quadrada, `\normalsize` como tamanho mínimo, faixas exclusivas para texto e desenho e nenhum cruzamento entre rótulo, segmento, seta ou marca. Capítulos sem figura continuam válidos. O contrato visual definitivo foi registrado em `_tikz/PADRAO-DE-CONSTRUCAO.md`: uma pergunta pedagógica por PNG, separação obrigatória de conceitos independentes, fundo transparente e revisão na largura real de leitura.

Os sete modelos inicialmente produzidos foram analisados e ilustrados. Eles possuem **51 figuras publicadas** — 6 no 6º ano, 5 no 7º, 5 no 8º, 5 no 9º, 12 na 1ª série, 10 na 2ª e 8 na 3ª — com fontes e manifestos privados, PNGs transparentes e pontos de inserção registrados em `Geometria/PLANO-DE-IMAGENS-TIKZ.md`. Todos os hashes públicos foram confirmados e os sete Markdown estão sincronizados no Google Drive.

**Correção curricular de 22/07/2026:** a auditoria dos blueprints revelou que o bloco 1 da 3ª série tinha um segundo capítulo, **Parábola: definição e equações reduzidas**, que ainda não havia sido produzido. Ele foi escrito como pré-requisito antes do Capítulo 3.

**Nova produção concluída:** os sete capítulos do bloco 2 e o capítulo ausente da 3ª série foram produzidos e validados: 8 arquivos, 32 aulas, todas entre 150 e 203 palavras. Suas **60 figuras** — 56 do bloco 2 e 4 do pré-requisito — foram produzidas em oito documentos TikZ, revisadas no original e a 300 px sobre branco, publicadas, indexadas e validadas. As oito cópias em `Segundo Semestre/Geometria/` foram conferidas como idênticas. O controle completo está em `Geometria/Acompanhamento de produção.md`.

O repositório público exclusivo está em `https://github.com/felipeelv/imagens-tikz`, na branch `main`. Ele contém o README e **111 PNGs transparentes aprovados**; nenhuma fonte, manifesto, capítulo ou imagem de teste foi publicada. Os 15 Markdown privados e suas cópias em `Segundo Semestre/Geometria/` estão idênticos e validados. As fontes, manifestos e renderizações permanecem exclusivamente em `_tikz/`. O checkpoint da etapa termina no commit `2fdcd844d6a909e73c4204a99445dd7d55535447`; os oito commits do bloco 2 estão registrados em `Geometria/PLANO-DE-IMAGENS-TIKZ-BLOCO2.md`.

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
- Em 22/07/2026, os sete capítulos inicialmente ilustrados de Geometria foram concluídos com 51 figuras TikZ/PNG publicadas, indexadas e sincronizadas no Google Drive.
- Na mesma data, os sete capítulos do bloco 2 e o capítulo de parábola ausente da 3ª série foram produzidos, validados e ilustrados com outras 60 imagens; o 3º bimestre foi fechado com 15 capítulos, 60 aulas e 111 PNGs sincronizados no Drive.

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

1. Estudos Sociais do 3º bimestre está concluído; usar `Estudos Sociais/Acompanhamento de produção.md` como registro final.
2. Ao iniciar outro bimestre ou disciplina, repetir o fluxo: blueprint → capítulo → validação → pasta oficial → acompanhamento.
3. Registrar qualquer nova calibragem no `AUTOR.md` e no `_MEMORIA.md` da disciplina correspondente.
4. Geometria do 3º bimestre está concluída; usar `Geometria/Acompanhamento de produção.md` como registro final e manter o mesmo pipeline nos próximos bimestres.
