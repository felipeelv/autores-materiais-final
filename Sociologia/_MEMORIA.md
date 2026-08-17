# Memória do Kit — Sociologia · Produção de Capítulos (Autores-de-Material)

> Registro de origem, decisões e estado deste kit. Ler antes de alterar qualquer arquivo da pasta. Última atualização: **17/08/2026**.

---

## 1. O que é este kit

Arquivos que o projeto **Claude.ai de Sociologia** consome para produzir capítulos no modelo da reorganização 2026/2S (blueprint → capítulo · 1 tema = 1 capítulo · 1 aula = 1 tópico `## N.`). Criado na **consolidação Autores-de-Material (21/07/2026)** — era um dos kits faltantes registrados no README de `prompts-producao/`.

| Arquivo | Papel |
|---|---|
| `AUTOR.md` | Instruções do projeto, voz, rigor sociológico e padrão editorial |
| `modelos/` | Um capítulo-modelo validado para cada série do Ensino Médio |
| `validar-capitulo.py` | Verificação automática exclusiva da disciplina |
| `Acompanhamento de produção.md` | Estado dos modelos e da produção oficial |

**Insumo por capítulo (fora desta pasta):** blueprint do bloco em `~/Reorganizacao-2026-2Semestre/disciplinas/Sociologia/blueprints/<série>/<bim>-<bloco>.md` (12 blueprints prontos desde 19/07/2026). Sem arquivo de LaTeX — a disciplina não usa fórmulas.

## 2. Origem — dupla

1. **Formato:** molde dos kits validados em produção (Estudos Sociais/Ciências — família humanas), com todas as decisões vigentes: sem blocos pós-conteúdo, prosa curta com organizadores visuais e VP condicional com teste do sinônimo.
2. **DNA editorial:** autor antigo de Filosofia e Sociologia (`autores-material/autores/autor_sociologia/` — prompt-autor.md + CLAUDE.md), de onde vieram: família de boxes (💭 ⏸️ 💡 🔍 Conexão), abordagem dialógica (partir de pergunta/fenômeno), teorias conectadas a fenômenos observáveis com dados, adaptação por série (1ª fundantes → 2ª correntes/debates → 3ª síntese/ENEM) e a **regra inviolável de ancoragem cristã** (§4.1 do autor antigo, preservada integralmente).

## 3. Decisões registradas (não reabrir sem o Felipe)

1. **Blocos pós-conteúdo do autor antigo ABOLIDOS** (decisão do Felipe, 21/07/2026 — vale para todas as disciplinas): Ampliando o Olhar, No Fio da História, O Que a Fé Diz, Pensador em Destaque, Você já pensou nisso?, Simplificando, Para não esquecer. Funções dissolvidas nas aulas: contexto histórico vira narrativa curta na aula pertinente; problematização vira parte da análise e dos boxes; pensador vira referência integrada ao texto (2–3 linhas, sem box); conexão bíblica vira versículo condicional inline; resumos saíram.
2. **Estrutura antiga de "exatamente 4 tópicos numerados" NÃO se aplica** — o número de tópicos agora é o número de aulas do blueprint (1 aula = 1 tópico).
3. **Ancoragem cristã preservada como inviolável** — Escritura como referencial, distinção fé/teoria, comparações morais explícitas, fidelidade intelectual antes da avaliação.
4. **Box `🔍 Conexão:` mantido** (era a marca do autor antigo) no lugar de boxes de outras famílias.
5. **Extensão própria de Sociologia:** preferir 175–195 palavras por aula; teto firme de 200. A carga de uma aula semanal justifica maior densidade, mas o teto não é meta.
6. **Meta antiga de 1.300–1.600 palavras por capítulo REVOGADA** — a extensão agora é por aula, no padrão de todas as disciplinas.
7. **Organização visual obrigatória:** pelo menos duas subseções de cada aula contêm lista ou tabela. Definições paralelas, classificações, marcos e consequências ficam em tópicos rotulados; a prosa curta explica apenas causas, relações e limites. Quando o recorte reúne três núcleos, os subtópicos separam contexto ou fenômeno, conceito e leitura sociológica.
8. **Boxes:** exatamente um por aula, em uma linha e uma frase, da família 💭/⏸️/💡/🔍. Referências a pensadores permanecem integradas ao corpo.
9. **Respiro do capítulo:** usar, em geral, um ou dois blockquotes simples por capítulo. Os três modelos vigentes usam dois.
10. **Fidelidade conceitual antes da avaliação:** apresentar autores, movimentos e conflitos em seus próprios termos; a ancoragem cristã distingue análise sociológica, juízo moral e aplicação bíblica.

## 4. Estado e próximos passos

- [x] Autor e validador recalibrados para o padrão conciso e visual — 24/07/2026.
- [x] Três capítulos-modelo criados em `modelos/` — um por série, com 9 aulas.
- [x] Modelos reorganizados e validados: aulas entre 175 e 195 palavras, média de 186,3.
- [x] Conteúdo conferido contra ordem, itens obrigatórios e `NÃO ANTECIPAR` dos blueprints.
- [x] Modelos aprovados e formalizados como os três Capítulos 1.
- [x] Três Capítulos 2 produzidos, validados e salvos no Drive.
- [x] 3º bimestre concluído: 6 capítulos · 18 aulas, entre 175 e 195 palavras, média de 188,6.
- [x] 2ª série reorganizada para o segundo semestre: 4 capítulos · 11 aulas — 17/08/2026.
- [x] Quatro blueprints da 2ª série reescritos com códigos BNCC corrigidos e recortes sem sobreposição.
- [x] Quatro capítulos da 2ª série produzidos, validados e publicados no Drive.

### Modelos atuais

| Série | Tema | Aulas | Faixa |
|---|---|---:|---:|
| 1ª série | O trabalho como atividade social | 3 | 175–189 |
| 2ª série | Estado, poder e dominação | 3 | 179–192 |
| 3ª série | Clássicos da Sociologia | 3 | 189–195 |

Na reorganização da 2ª série, foram preservadas as formulações juridicamente atuais: Lei de Cotas alterada em 2023, feminicídio convertido em crime autônomo em 2024 e decisões do STF sobre união estável homoafetiva, homofobia e transfobia descritas com seus limites. O vínculo no trabalho por plataformas permanece apresentado como questão jurídica em disputa, e o impacto da IA como transformação de tarefas e ocupações.

A pasta oficial [Segundo Semestre/Sociologia](https://drive.google.com/drive/folders/19srtjGKY0f9VA_G00ZupP5xhHvAPuIPV) contém as três subpastas de série. Na [2ª Série](https://drive.google.com/drive/folders/1v0qgIjgqttdDrEJwdavvRuq_8cYK4v8O), os quatro arquivos vigentes por bloco foram conferidos após o envio; os dois arquivos anteriores nomeados por tema permanecem como histórico.

## 5. Histórico

| Data | O quê |
|---|---|
| 21/07/2026 | Kit criado na consolidação Autores-de-Material: formato dos kits validados + DNA do autor antigo de Filosofia e Sociologia. Blocos pós-conteúdo abolidos por decisão do Felipe. |
| 24/07/2026 | Autor e validador recalibrados; três modelos concisos e visuais criados e validados. |
| 24/07/2026 | Modelos aprofundados para a carga semanal de Sociologia: três movimentos curtos por aula e faixa preferencial ajustada para 175–195 palavras. |
| 24/07/2026 | Conteúdo redistribuído em tópicos pedagógicos; duas subseções visuais por aula passaram a ser exigidas pelo autor e pelo validador. |
| 24/07/2026 | Modelos formalizados como Capítulos 1; Capítulos 2 produzidos; 3º bimestre concluído e conferido no Drive. |
| 17/08/2026 | 2ª série reorganizada: Estado/poder e democracia/cidadania no 3º bimestre; movimentos/redes e capitalismo/globalização/trabalho no 4º. Quatro blueprints e quatro capítulos concluídos, validados e publicados na pasta oficial. |

## 6. Checkpoint de retomada

- **Última etapa concluída:** reorganização integral e publicação oficial da 2ª série — 4 capítulos · 11 aulas.
- **Fonte local vigente da 2ª série:** `~/Reorganizacao-2026-2Semestre/conteudos-prontos/Sociologia/2serie/`.
- **Fonte oficial vigente:** [Segundo Semestre/Sociologia/2ª Série](https://drive.google.com/drive/folders/1v0qgIjgqttdDrEJwdavvRuq_8cYK4v8O); os quatro arquivos por bloco foram conferidos por leitura de retorno. Os dois arquivos antigos nomeados por tema foram preservados como histórico.
- **Referências editoriais locais:** `AUTOR.md`, `modelos/` e `validar-capitulo.py`.
- **Próxima etapa:** sincronização do documento curricular e produção do 4º bimestre da 1ª e da 3ª séries.
- **Blueprints vigentes da 2ª série:** `2serie/3bim-bloco1.md`, `2serie/3bim-bloco2.md`, `2serie/4bim-bloco1.md` e `2serie/4bim-bloco23.md`.
- **Regra de continuidade:** manter 175–195 palavras por aula, três subtópicos curtos, organizadores visuais em pelo menos duas subseções, um box por aula e dois blockquotes simples por capítulo.
