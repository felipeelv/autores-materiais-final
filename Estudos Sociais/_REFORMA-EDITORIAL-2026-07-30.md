# Reforma editorial de Estudos Sociais — 30/07/2026

> Registro operacional do que foi mudado, por quê e onde. Complementa o `_MEMORIA.md` (decisão 14), que guarda as **decisões**; aqui está a **execução**. Ler junto com o `AUTOR.md` atual antes de produzir qualquer capítulo novo.

---

## 1. Como isso começou

O Felipe leu o **BL1_Capítulo 1 do 8º ano — Independências no Haiti e na América Espanhola** e apontou três coisas:

1. o autor inseriu box "Curiosidade" logo depois do subtítulo, e isso confundia o conteúdo;
2. o box "Esse foi o cara" ficou ruim e deveria sair;
3. sentia falta do "Enquanto isso" e do "Para hoje" do autor antigo (`~/autores-material/autores/autor_estudos-sociais/prompt-autor.md`) — mas **não** como parte corrida do conteúdo, e sim como **anexo**.

O capítulo de referência que ele usou para mostrar o formato antigo foi *Unidade 3 — América Latina e Brasil | 8º Ano*, em `Conteúdos Prontos_2026/Estudos Sociais/8ano/2bim/`.

## 2. O diagnóstico

O problema do box **não era um deslize de um capítulo** — era uma lacuna do manual reproduzida em escala.

O `AUTOR.md` dizia quantos boxes por aula (1–2), proibia boxes consecutivos e definia a formatação interna. **Nunca dizia onde o box podia entrar.** Sem regra de posição, o autor pôs no lugar visualmente mais fácil: logo abaixo do título. Resultado medido:

| Ocorrência | Quantidade |
|---|---|
| Box logo abaixo de um título | **46**, em 29 dos 34 capítulos |
| Box `👤 Esse foi o "cara"` | **34** (exatamente 1 por capítulo) |
| Versículo inline no corpo | 5 |

Piores casos: 9º ano — *Oceania*, *Oriente Médio* e *Potências econômicas asiáticas*, com 4 ocorrências cada.

**O achado mais sério apareceu ao remover o `👤`:** em vários capítulos **o box era todo o conteúdo do subtópico**. Removê-lo deixava a seção vazia ou sem sentido:

| Capítulo | Subtópico | O que sobrou |
|---|---|---|
| Império Romano (6º) | `1.2 Júlio César e a transição` | nada |
| Fim da Monarquia (8º) | `3.2 Deodoro e o Exército` | nada |
| Europa (9º) | `4.2 Schuman e a paz econômica` | uma frase que não citava Schuman |
| A República Velha (5º) | `2.3 Campos Sales` | uma frase que não citava Campos Sales |

Foram **12 subtópicos** nessa condição. Todos reescritos com o **papel histórico** do personagem em prosa — que é o que o blueprint pede —, com a biografia indo para o anexo.

## 3. O que mudou nas regras

Tudo no `AUTOR.md`, Partes 1 e 2:

- **Box nunca abre subtópico** (§6). Antes dele é obrigatório haver parágrafo, lista ou tabela do mesmo subtópico, porque o box comenta o que o aluno já leu. Corolário: **box não carrega o conceito da aula** — se o dado é o núcleo, é prosa.
- **Família de boxes:** 🔎 💭 👤 → **🔎 💭**.
- **Personagem-chave** (§4 item 5): ficha biográfica só no anexo; no capítulo, apenas o papel histórico, quando o recorte pedir. Regra prática: se a informação só identifica a pessoa (nascimento, morte, títulos), é anexo; se explica o processo, é aula.
- **Anexo como arquivo separado** (§2.1, com esqueleto pronto).
- **Versículo fora do capítulo** (§9): a conexão VP vive em "E para hoje…", no anexo.
- **Título:** `# BL{1|2}_Capítulo {N} — {Tema}`, com numeração reiniciando a cada bloco.

## 4. O anexo

Cada capítulo entrega **dois arquivos** na pasta do ano:

```
{Tema}.md            ← o capítulo, só as aulas
{Tema} — Anexo.md    ← Enquanto isso… · E para hoje… · Esse foi o "cara"
```

- **"Enquanto isso…"** é sempre a **trajetória cristã** contemporânea ao tema — igreja, missões, comunidades e debates de fé. Não é sincronia histórica genérica.
- **"E para hoje…"** usa o **versículo-âncora prescrito pelo blueprint**, com um parágrafo de ligação ancorado no conteúdo daquele capítulo.
- **"Esse foi o 'cara'"** traz o personagem-chave do blueprint, com os dados que o próprio blueprint fornece.
- É o único lugar onde emoji aparece fora de box (o 🏛️ do legado).

Isso **reverte parcialmente** a decisão de 21/07/2026 que aboliu os blocos pós-conteúdo — mas só em Estudos Sociais, e só fora do capítulo. Nada disso pode voltar ao corpo.

## 5. O que foi executado

| Frente | Resultado |
|---|---|
| `AUTOR.md` | Partes 1 e 2 reescritas nos pontos afetados |
| `validar-capitulo.py` | aceita/exige prefixo `BL`; detecta box abrindo subtópico; família sem 👤 |
| 34 capítulos no Drive | 46 boxes reposicionados · 34 `👤` removidos · 12 subtópicos reescritos · 5 versículos retirados |
| 34 anexos | criados, todos com as 3 seções (4 sem "E para hoje…" — ver §7) |
| 6 modelos | regenerados dos capítulos revisados, agora com anexo (12 arquivos) |
| `PADRAO-GERAL-DE-ESCRITA.md` | regra do box + notas de Estudos Sociais · `sincronizar.py` rodado |
| Documentação | `_MEMORIA.md` (decisão 14), `Acompanhamento de produção.md`, `README.md` |

**Validação final: 0 falhas nos 34 capítulos.**

### Detalhe importante sobre o validador

O commit `12e9cfb` introduziu os prefixos `BL1_`/`BL2_` nos títulos, mas **o validador não foi atualizado junto** — ele exigia `# Capítulo N — Tema` e por isso **acusava falha nos 34 capítulos** desde então. Isso mascarava os problemas reais. Corrigido: agora o prefixo é obrigatório em Estudos Sociais e opcional nas demais disciplinas (`cfg["prefixo_bloco"]`).

## 6. Verificação dos fatos históricos

Todos os "Enquanto isso…" foram checados via Perplexity **antes** de escrever, conforme a regra da casa de nunca inventar data. Confirmados: jesuítas em 1549 com Nóbrega · Anchieta em 1553 e gramática do tupi em 1595 · abolicionismo britânico (1783, 1787, 1789, 1807, 1833) · Missão Artística Francesa em 1816 · Decreto 119-A de 07/01/1890 · Canudos 1896-1897 · Villa-Lobos no Canto Orfeônico em 1932 · Questão Religiosa 1872-1875 com Dom Vital e Dom Macedo Costa · Concílio de Trento 1545-1563 · franciscanos 1209 e dominicanos 1216 · Manuscritos do Mar Morto em 1947 · Cântico das Criaturas em 1224 · edito de Ciro em 538 a.C. e Segundo Templo em 516 a.C. · Pompeu em Jerusalém em 63 a.C. · Editos de Milão (313) e Tessalônica (380) · CEBs nos anos 1960 · Pastoral das Favelas em 1976 · Rádio Aparecida em 08/09/1951 · Madre Teresa (1950, Nobel 1979) · Matteo Ricci em 1583 · Wangari Maathai no Kennedy Airlift em 1960 · Desmond Tutu (Nobel 1984, Comissão da Verdade 1995) · Tratado de Waitangi e Henry Williams em 04/02/1840.

## 7. Pendências

1. **4 anexos sem "E para hoje…"** — Europa, Ásia: quadro natural e humano, Potências econômicas asiáticas e Oriente Médio, todos do **9º ano bloco 1**. Os blueprints desses quatro capítulos **não trazem Conexão VP**. A ausência está registrada dentro de cada anexo. Inventar a ligação contrariaria a regra editorial; se os versículos forem desejados, a correção é **no blueprint**, em `~/Reorganizacao-2026-2Semestre/disciplinas/Estudos Sociais/blueprints/9ano/3bim-bloco1.md`.

2. **Repetição de versículo-âncora dentro do mesmo ano.** Os blueprints do 7º, 8º e 9º ano repetem a mesma âncora em capítulos diferentes, porque a unidade VP é a mesma no bloco. Isso vem da fonte e não é erro de produção — o que varia é o parágrafo de ligação. Registrado como revisão da decisão 7 do `_MEMORIA.md`.

3. **Nada foi commitado.** As alterações do kit estão no working tree do repositório, prontas para revisão.

## 8. Como reverter

Backup dos 34 capítulos originais, anterior a qualquer alteração:

```
~/Desktop/Estudos Sociais — backup antes do ajuste/
```

Os anexos são arquivos novos — apagá-los não afeta os capítulos. As mudanças do kit editorial estão todas em git e podem ser revertidas com `git checkout`.

---

*Registro criado em 30/07/2026, ao fim da reforma. Se uma regra deste arquivo divergir do `AUTOR.md`, o `AUTOR.md` prevalece — este documento explica o porquê das decisões, não as substitui.*
