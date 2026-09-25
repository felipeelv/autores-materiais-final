# BL1_Capítulo 1 — Probabilidade: aprofundamento

> Um filtro de spam sinaliza 90% das mensagens de spam e sinaliza por engano 5% das mensagens legítimas. Uma mensagem acabou de ser sinalizada. A chance de ela ser mesmo spam é… cerca de 67%, não 90%. Como a matemática explica a diferença?

---

## 1. União, interseção e complemento

Contar certo vem antes de calcular: resultados que pertencem a dois eventos não podem entrar duas vezes.

### 1.1 A regra da união

Em um espaço equiprovável, a probabilidade de $$E$$ é:

$$P(E) = \frac{n(E)}{n(\Omega)}$$

$$n(E)$$ é a quantidade de casos favoráveis e $$n(\Omega)$$, o total de resultados possíveis.

Para dois eventos quaisquer, a união desconta a interseção que foi contada duas vezes:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Quando $$A \cap B = \emptyset$$, os eventos são **mutuamente exclusivos** e o último termo é zero. O **complementar** resolve os casos de "pelo menos um":

$$P(E') = 1 - P(E)$$

"Pelo menos um" é o contrário de "nenhum", e contar "nenhum" costuma ser bem mais rápido.

**Copas e figuras num baralho**

Num baralho de 52 cartas, considere $$A = $$ "carta de copas" e $$B = $$ "figura", isto é, valete, dama ou rei.

**Resolução:**

- **Passo 1:** Contar cada evento e a interseção entre eles.

| Evento | Cartas | Probabilidade |
|---|---:|---:|
| $$A$$ — copas | 13 | $$\frac{13}{52}$$ |
| $$B$$ — figuras | 12 | $$\frac{12}{52}$$ |
| $$A \cap B$$ — figuras de copas | 3 | $$\frac{3}{52}$$ |

- **Passo 2:** Substituir na regra da união.

$$P(A \cup B) = \frac{13}{52} + \frac{12}{52} - \frac{3}{52}$$

- **Passo 3:** Somar e simplificar.

$$P(A \cup B) = \frac{22}{52} = \frac{11}{26}$$

**Resposta:** 22 cartas são de copas ou figuras — 10 apenas copas, 9 apenas figuras e 3 que são as duas coisas ao mesmo tempo. Somar 13 e 12 daria 25 e contaria as três figuras de copas duas vezes.

### 1.2 Espaços grandes

Quando listar os casos é inviável, a combinatória fornece o denominador. A escolha entre as duas fórmulas depende de a ordem importar ou não:

| | Combinação | Arranjo |
|---|---|---|
| Fórmula | $$C(n,p) = \frac{n!}{p!(n-p)!}$$ | $$A(n,p) = \frac{n!}{(n-p)!}$$ |
| O que faz | escolher $$p$$ entre $$n$$ sem ordem | escolher $$p$$ entre $$n$$ com ordem |

Em ambas, $$n$$ é o total de elementos disponíveis e $$p$$, a quantidade escolhida. Uma aposta simples da Mega-Sena, por exemplo, é uma entre $$C(60,6) = 50\,063\,860$$ combinações possíveis — número que explica por que um prêmio de loteria não entra em planejamento financeiro.

> ⚠️ **Atenção:**  
> Somar probabilidades sem descontar a interseção conta duas vezes os resultados que pertencem aos dois eventos.

---

## 2. Probabilidade condicional

"Dado que" reduz o universo: continuam valendo apenas os resultados compatíveis com a informação recebida.

### 2.1 O universo que encolhe

A probabilidade de $$A$$ dado $$B$$ é:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

$$P(A \mid B)$$ mede a chance de $$A$$ dentro do novo universo, que passou a ser $$B$$.

Da definição sai a **regra da multiplicação**:

$$P(A \cap B) = P(A) \cdot P(B \mid A)$$

Numa árvore de probabilidades, cada caminho completo é o produto das etapas que o compõem.

### 2.2 Retiradas sem reposição

**Duas fichas de um saco**

Um saco hipotético tem 5 fichas azuis e 3 laranjas, num total de 8, e as retiradas são feitas sem reposição. Qual a chance de sair azul e depois laranja?

**Resolução:**

- **Passo 1:** Calcular a chance de a primeira ficha ser azul.

$$P(A_1) = \frac{5}{8}$$

- **Passo 2:** Atualizar o saco — restam 7 fichas, 3 delas laranjas.

$$P(L_2 \mid A_1) = \frac{3}{7}$$

- **Passo 3:** Multiplicar as duas etapas.

$$P(A_1 \cap L_2) = \frac{5}{8} \cdot \frac{3}{7} = \frac{15}{56}$$

**Resposta:** a chance é $$\frac{15}{56}$$, ou cerca de 26,79% — sem reposição, a primeira retirada muda o total e a composição do saco, e por isso o denominador da segunda etapa cai de 8 para 7.

A árvore completa mostra como cada primeira retirada altera a etapa seguinte:

| Primeira retirada | Depois dela, azul | Depois dela, laranja |
|---|---:|---:|
| Azul — $$\frac{5}{8}$$ | $$\frac{4}{7}$$ | $$\frac{3}{7}$$ |
| Laranja — $$\frac{3}{8}$$ | $$\frac{5}{7}$$ | $$\frac{2}{7}$$ |

Três relações entre eventos não podem ser confundidas:

- **dependentes** — a primeira retirada altera a probabilidade da segunda;
- **independentes** — $$P(A \mid B) = P(A)$$ e, portanto, $$P(A \cap B) = P(A) \cdot P(B)$$;
- **exclusivos** — não acontecem juntos, e por isso eventos exclusivos e não vazios são sempre dependentes.

> 🔢 **Padrão:**  
> Condicionar é recalcular dentro da informação já conhecida — sem reposição, o denominador muda a cada etapa.

---

## 3. Probabilidade total e teorema de Bayes

Uma mensagem sinalizada pelo filtro pode ser spam ou falso alarme, e a proporção entre os dois depende de quanto spam existe.

### 3.1 Somar todos os caminhos

Se $$B_1, B_2, \ldots, B_k$$ formam uma partição do espaço, a **probabilidade total** de $$A$$ soma o que vem de cada parte:

$$P(A) = \sum_i P(A \mid B_i) P(B_i)$$

O **teorema de Bayes** inverte a condição, indo da evidência para a causa:

$$P(B_i \mid A) = \frac{P(A \mid B_i) P(B_i)}{P(A)}$$

Os três termos da fórmula têm nomes próprios:

- $$P(B_i)$$ — probabilidade **a priori**, antes da evidência;
- $$P(A \mid B_i)$$ — **verossimilhança**, a chance da evidência dada a causa;
- $$P(B_i \mid A)$$ — probabilidade **a posteriori**, atualizada pela evidência.

O pastor e matemático **Thomas Bayes (c. 1701–1761)** apresentou a base desse raciocínio em ensaio publicado postumamente em 1763 por Richard Price. Hoje ele sustenta desde filtros de spam até diagnóstico médico.

### 3.2 O filtro de spam

**Mil mensagens hipotéticas**

Suponha $$S$$ = "a mensagem é spam" e $$F$$ = "a mensagem foi sinalizada", com $$P(S) = 10\%$$, $$P(F \mid S) = 90\%$$ e $$P(F \mid S') = 5\%$$.

**Resolução:**

- **Passo 1:** Distribuir as 1.000 mensagens e contar as sinalizadas de cada grupo.

| Grupo | Mensagens | Sinalizadas |
|---|---:|---:|
| $$S$$ — spam | 100 | 90 |
| $$S'$$ — legítimas | 900 | 45 |
| **Total** | **1.000** | **135** |

- **Passo 2:** Calcular a probabilidade total de uma mensagem ser sinalizada.

$$P(F) = 0{,}90 \cdot 0{,}10 + 0{,}05 \cdot 0{,}90 = 0{,}135$$

- **Passo 3:** Aplicar o teorema de Bayes.

$$P(S \mid F) = \frac{0{,}90 \cdot 0{,}10}{0{,}135} = \frac{2}{3} \approx 66{,}7\%$$

**Resposta:** entre as mensagens sinalizadas, cerca de 66,7% são spam — bem menos que os 90% de acerto do filtro, porque as 900 mensagens legítimas são tantas que seus 5% de falsos alarmes chegam a 45, metade dos 90 acertos.

Confundir $$P(S \mid F)$$ com $$P(F \mid S)$$ é o erro conhecido como **falácia do promotor**: trocar a chance da evidência dada a causa pela chance da causa dada a evidência. O mesmo cálculo explica por que um teste médico muito preciso ainda produz muitos falsos positivos quando a condição procurada é rara.

> ⚠️ **Atenção:**  
> Bayes atualiza a probabilidade inicial à luz da evidência — não a substitui pela verossimilhança.
