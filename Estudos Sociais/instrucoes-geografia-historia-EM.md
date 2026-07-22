# Instruções do Ensino Médio — Geografia e História · Colégio Eleve

> **Complemento obrigatório do `AUTOR.md`** quando a série for **1ª, 2ª ou 3ª do Ensino Médio**. Use os dois juntos: o `AUTOR.md` define a estrutura do capítulo (aulas, boxes, integrações, proibições) e **este arquivo define o que muda no EM**. Em conflito entre os dois, **este arquivo prevalece**.
>
> Para 4º–9º ano (Estudos Sociais), ignore este arquivo — o `AUTOR.md` basta.

---

## 1. A divisão no Ensino Médio

No Fundamental, Estudos Sociais é matéria única (Geografia + História juntas). **No Ensino Médio elas se separam:**

| Disciplina | Aulas/semana | Blueprints | Escopo |
|---|---|---|---|
| **Geografia** | 3 | `disciplinas/Geografia/blueprints/<série>/` | espaço, economia, geopolítica, ambiente |
| **História** | 3 | `disciplinas/Historia/blueprints/<série>/` | processos históricos, Brasil e mundo |

**Um capítulo pertence a uma disciplina só.** Nunca misturar recorte de Geografia com o de História — a ponte entre elas, quando existir, é feita em meia frase ("o mesmo território que a Geografia estuda como fronteira agrícola"), nunca desenvolvendo o conteúdo da outra.

## 2. O que muda em relação ao Fundamental

| Ponto | 6º–9º (Estudos Sociais) | 1ª–3ª (Geografia / História) |
|---|---|---|
| **Profundidade** | narrar, descrever, comparar (N2–N3) | **N3, com N4 em pontos críticos** — interpretar, relacionar, avaliar |
| **Referência-chave** | personagem histórico (box `👤 Esse foi o "cara"`) | **pensador, economista ou historiador** — desenvolvido **no texto**, sem box (ver §4) |
| **Conceitos** | vocabulário básico com glosa | **densidade conceitual alta** — os termos do balizamento do blueprint são o conteúdo, não enfeite |
| **Dados** | pontuais, para ancorar a narrativa | **dados, séries e casos concretos** são obrigatórios (ver §5) |
| **Leitura crítica** | múltiplas perspectivas | **juízo interpretativo explícito**, com as leituras em disputa (ver §3 e §6) |
| **ENEM/vestibular** | não se aplica | mencionar quando natural, 1 frase (ver §7) |

Tudo o mais do prompt principal continua valendo integralmente: 1 aula = 1 tópico `## N.`, 220–250 palavras por aula (teto 300), abertura concreta, **regra anti-redundância** (nunca prosa + lista repetindo o mesmo), máximo 2 tabelas por capítulo, boxes 🔎/💭 como "drops", sem seções de fechamento, versículo-âncora integrado a uma aula.

## 3. Rigor interpretativo — a marca do EM

- **História = juízo historiográfico.** Não basta narrar o processo: mostrar **como ele é lido** ("para uns, a estabilização salvou o país; para outros, custou décadas de investimento"). As leituras em disputa são conteúdo.
- **Geografia = raciocínio geográfico aplicado.** Relacionar espaço, economia e poder: pauta exportadora ↔ modelo de desenvolvimento, fronteira agrícola ↔ ambiente, fluxo comercial ↔ geopolítica. Nunca descrição mnemônica.
- **Contradição é conteúdo, não problema.** Ex.: "todos os países ricos usaram protecionismo para enriquecer e hoje exigem livre comércio dos pobres" — apontar a tensão é o trabalho da disciplina.
- Escalas articuladas: o caso local dentro do processo global, e vice-versa.

## 4. Referência-chave no EM

- É um **pensador, economista ou historiador** (ou uma figura histórica, quando o blueprint assim definir) — **um por tema**, e **não repetir entre os temas da mesma série**.
- **Desenvolvida dentro do texto**, na aula mais pertinente, em 2–4 linhas: quem foi, o que formulou, obra e ano. **Sem o box `👤`** — no EM a densidade do texto comporta a referência no fluxo, e o box fica reservado ao Fundamental.
- Menções secundárias listadas no blueprint entram só se couberem naturalmente, em meia frase, sem protagonismo.
- Quando o blueprint traz duas visões em confronto (ex.: Smith × Prebisch, Gudin × Simonsen), **as duas aparecem** — o capítulo não escolhe lado.

## 5. Dados, datas e casos concretos

- Os dados do balizamento do blueprint (valores, percentuais, datas, marcos institucionais) **entram no texto** — são o que sustenta a interpretação.
- Todo dado com **fonte de tempo explícita**: "superávit de US$ 99 bilhões (2023)", "OMC, criada em 1995, hoje com 164 membros".
- Nunca inventar número, data ou estatística. Se o blueprint não traz o dado, escreva a ordem de grandeza em palavras ("cerca de um terço das exportações").
- Séries longas e comparações ganham tabela — respeitando o **máximo de 2 tabelas por capítulo** do prompt principal.

## 6. Neutralidade em temas vivos

- Períodos e disputas ainda em curso (governos recentes, polarização, conflitos internacionais) exigem cuidado redobrado: **nem hagiografia nem demonização**.
- Mostrar **conquistas e limites** de cada governo, projeto ou modelo, descrevendo fatos e as leituras historiográficas — sem adjetivação militante e sem linguagem de campanha.
- O aluno deve terminar a aula capaz de reconstruir os dois lados do argumento, não de repetir o do autor.
- Vale igualmente para Geografia: modelos econômicos, políticas ambientais e blocos geopolíticos são apresentados com seus custos e benefícios.

## 7. ENEM e vestibular

- Quando o blueprint marcar recorrência no ENEM, **mencionar em 1 frase**, integrada ao texto ("balança comercial e reprimarização são leitura recorrente no ENEM").
- ❌ **Nunca** criar "caso ENEM", questão comentada, simulado ou box de vestibular — os blueprints proíbem expressamente. Continua valendo: material é só conteúdo.

## 8. Autovalidação adicional do EM

*(Somar aos itens do prompt principal.)*

- [ ] Disciplina correta e única (Geografia **ou** História) — zero recorte da outra
- [ ] Profundidade N3/N4: o capítulo **interpreta e relaciona**, não só narra
- [ ] Conceitos do balizamento do blueprint desenvolvidos, não apenas citados
- [ ] Dados, datas e casos concretos presentes, com referência de tempo — e nenhum número inventado
- [ ] Leituras em disputa apresentadas quando o tema pede; nenhum juízo partidário
- [ ] Referência-chave desenvolvida no texto (2–4 linhas), **sem box 👤**, única no tema
- [ ] Menção ENEM (se houver) em 1 frase; zero questão, caso ou simulado

---

*v1 · jul/2026 · complemento do kit de Estudos Sociais — base: blueprints de Geografia e História EM (regras transversais, balizamento por série, referência-chave) + decisão do Felipe (19/07/2026) de manter Geografia e História no mesmo kit, com instrução específica em vez de kits separados.*
