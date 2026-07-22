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

## Estudos Sociais

Modelos disponíveis do **4º ao 9º ano**, em `Estudos Sociais/modelos/`.

Foram aplicadas as mesmas regras visuais de Ciências:

- não deixar três parágrafos consecutivos sem quebra visual;
- não deixar dois subtópicos consecutivos sem marcadores;
- usar blockquote para ressalvas históricas, distinção entre fontes, contrastes e sínteses;
- usar marcadores apenas quando o conteúdo já apresentar elementos paralelos;
- manter parágrafos enxutos e aulas preferencialmente entre 180–220 palavras.

O validador de Estudos Sociais verifica essas duas regras automaticamente.

## Estado da validação

Existem **15 capítulos-modelo**:

- 4 de Biologia;
- 5 de Ciências;
- 6 de Estudos Sociais.

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

1. Validar visualmente os modelos de Biologia, Ciências e Estudos Sociais.
2. Registrar novos ajustes no `AUTOR.md` e no `_MEMORIA.md` da disciplina correspondente.
3. Aplicar o mesmo processo às demais disciplinas, uma por vez.
4. Manter o repositório final atualizado até a aprovação de todas as disciplinas.
