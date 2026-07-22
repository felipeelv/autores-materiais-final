# Capítulo 1 — Equilíbrio de Hardy-Weinberg

> Se uma doença genética é recessiva e rara, por que ela não desaparece sozinha das populações ao longo das gerações?

---

## 1. População mendeliana e frequências

Numa lavoura há 36 plantas **AA**, 48 **Aa** e 16 **aa**. Contar indivíduos dá três grupos; contar alelos dá outra coisa.

### 1.1 População mendeliana e pool gênico

**População mendeliana:** conjunto de indivíduos da mesma espécie que ocupam a mesma área e se cruzam entre si.

**Pool gênico:** a soma de todos os alelos presentes nesse grupo.

A mudança de escala é o ponto central da genética de populações:

- o **indivíduo** tem genótipo fixo da fecundação à morte — não evolui;
- a **população** muda, porque a composição do pool gênico muda ao longo das gerações.

### 1.2 Os dois tipos de frequência

| | Frequência genotípica | Frequência alélica |
|---|---|---|
| Mede | proporção de cada genótipo entre os indivíduos | proporção de cada alelo entre todos os alelos do gene |
| Base de contagem | nº de indivíduos | nº de alelos (2 × indivíduos) |
| Símbolos | AA, Aa, aa | $$p$$ (dominante), $$q$$ (recessivo) |

Cada indivíduo diploide carrega dois alelos: 100 indivíduos têm 200 alelos para o gene analisado.

### 1.3 Contando na prática

Genotípicas — divisão direta pelo total:

$$AA = \frac{36}{100} = 0{,}36 \qquad Aa = \frac{48}{100} = 0{,}48 \qquad aa = \frac{16}{100} = 0{,}16$$

Alélicas — cada **AA** contribui com dois alelos **A**; cada heterozigoto, com um:

$$A = (2 \cdot 36) + 48 = 120$$

$$a = (2 \cdot 16) + 48 = 80$$

$$p = \frac{120}{200} = 0{,}60 \qquad q = \frac{80}{200} = 0{,}40$$

Como só há dois alelos, $$p + q = 1$$ sempre.

Leitura: 60% dos alelos são **A**, ainda que só 36% das plantas sejam **AA** — boa parte do alelo dominante está guardada nos heterozigotos.

---

## 2. O princípio e suas condições

Em 1908, um matemático de Cambridge respondeu por carta: se o alelo para dedos curtos é dominante, ele não deveria se espalhar por toda a população?

### 2.1 Hardy e a resposta

**Godfrey Harold Hardy** (1877–1947) mostrou que não: dominância diz respeito a como o alelo **se manifesta**, não à sua **frequência** na população. O princípio saiu no mesmo ano, de forma independente, com o médico alemão **Wilhelm Weinberg**.

**Princípio de Hardy-Weinberg:** na ausência de forças evolutivas, as frequências alélicas e genotípicas **permanecem constantes** de geração em geração.

Duas leituras diretas:

- sozinha, a hereditariedade não muda nada;
- se as frequências mudaram, **alguma força atuou**.

### 2.2 As cinco condições

O princípio só vale se as cinco valerem ao mesmo tempo:

| Condição | O que exige | Fator que a quebra |
|---|---|---|
| Sem mutação | nenhum alelo novo surge | mutação |
| Sem migração | não há entrada nem saída de indivíduos | fluxo gênico |
| População grande | o acaso não altera as proporções | deriva genética |
| Sem seleção | todos os genótipos sobrevivem e se reproduzem igual | seleção natural |
| Cruzamento ao acaso | a escolha do parceiro independe do genótipo | endogamia |

> ⏸️ **Pare e Pense:**  
> Numa população humana real, qual dessas cinco condições parece a mais difícil de cumprir?

### 2.3 Uma linha de base, não um retrato

Nenhuma população natural cumpre as cinco — e é aí que está a utilidade do modelo.

Hardy-Weinberg descreve a população que **não** evolui, e serve como referência de comparação:

- frequências observadas **iguais** às previstas → nenhuma força detectável;
- frequências **diferentes** → há força evolutiva agindo, e o tipo de desvio indica qual.

---

## 3. Aplicações e cálculo

A fenilcetonúria afeta cerca de 1 em cada 10.000 recém-nascidos no Brasil e é detectada no teste do pezinho.

### 3.1 A equação

Se os cruzamentos são ao acaso, as combinações na fecundação seguem:

$$p^2 + 2pq + q^2 = 1$$

Cada termo representa uma proporção:

- $$p^2$$ — homozigotos dominantes (**AA**);
- $$2pq$$ — heterozigotos (**Aa**), multiplicado por dois porque se formam de duas maneiras: **A** do pai com **a** da mãe, ou o inverso;
- $$q^2$$ — homozigotos recessivos (**aa**).

### 3.2 Estimando os portadores

Numa doença recessiva, só os **aa** a manifestam — e é esse o dado conhecido:

$$q^2 = \frac{1}{10000} = 0{,}0001$$

$$q = \sqrt{0{,}0001} = 0{,}01$$

$$p = 1 - 0{,}01 = 0{,}99$$

$$2pq = 2 \cdot 0{,}99 \cdot 0{,}01 = 0{,}0198$$

### 3.3 Lendo o resultado

$$0{,}0198$$ significa cerca de 198 portadores em cada 10.000 pessoas — quase 1 em 50 — contra 1 afetado em 10.000.

**Há cerca de 198 portadores para cada pessoa doente.** Aí está a resposta da pergunta do capítulo: a maioria dos alelos recessivos está em heterozigotos saudáveis, invisível à seleção. Mesmo que nenhum afetado tivesse filhos, o alelo continuaria circulando.

> 📏 **Medidas Interessantes:**  
> Estima-se que cada pessoa seja portadora de alguns alelos recessivos capazes de causar doença grave em homozigose.

O mesmo raciocínio explica o risco em casamentos entre parentes: eles têm maior chance de carregar o mesmo alelo raro de um ancestral comum.

> *"Criou Deus o homem à sua imagem, à imagem de Deus o criou; homem e mulher os criou."*
> — **Gênesis 1:27**

Não existe indivíduo "geneticamente superior": cada um carrega alelos recessivos que, em outra combinação, causariam doença. A **dignidade** não depende do sorteio genético que coube a cada um.
