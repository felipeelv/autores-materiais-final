# Financeira — 2ª Série · Bloco 1

> **3º Bimestre — Probabilidade condicional e crédito** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Probabilidade (aprofundamento)** (3 aulas)

---

# BL1_Capítulo 1 — Probabilidade: aprofundamento

> Um teste de COVID acerta 95% dos casos. Você testa positivo numa cidade onde só 1% tem a doença. Sua chance real de estar doente é… cerca de 16%. Como a matemática explica um resultado tão contraintuitivo?

---

## 1. Extensão dos conceitos

Operações entre eventos evitam contar duas vezes resultados que pertencem a mais de um conjunto.

### 1.1 Espaço, complementar e união

Em um espaço equiprovável, a probabilidade de $$E$$ é:

$$P(E)=\frac{n(E)}{n(\Omega)}$$

$$n(E)$$ é a quantidade de casos favoráveis e $$n(\Omega)$$, o total de resultados possíveis.

O complementar resolve eventos do tipo “pelo menos um”:

$$P(E')=1-P(E)$$

Para dois eventos quaisquer, a regra da união desconta a interseção contada duas vezes:

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$

Se $$A\cap B=\emptyset$$, os eventos são mutuamente exclusivos e o último termo é zero.

### 1.2 Aplicar a regra da união

**Eventos em um dado**

Considere $$A=$$ “resultado par” e $$B=$$ “resultado maior que 4”.

| Evento | Resultados | Probabilidade |
|---|---|---:|
| $$A$$ | 2, 4, 6 | $$\frac{3}{6}$$ |
| $$B$$ | 5, 6 | $$\frac{2}{6}$$ |
| $$A\cap B$$ | 6 | $$\frac{1}{6}$$ |

**Resolução:**

- **Passo 1:** Substituir na regra da união.

$$P(A\cup B)=\frac{3}{6}+\frac{2}{6}-\frac{1}{6}$$

- **Passo 2:** Simplificar.

$$P(A\cup B)=\frac{4}{6}=\frac{2}{3}$$

**Resposta:** quatro das seis faces são pares ou maiores que 4; a face 6 pertence aos dois eventos e deve ser contada uma única vez.

Em espaços grandes, a combinatória fornece o denominador. Uma aposta simples da Mega-Sena corresponde a uma entre:

$$C(60,6)=50\,063\,860$$

Logo, a probabilidade é $$\frac{1}{50\,063\,860}$$; o número mostra por que ganhos não podem ser tratados como expectativa financeira.

> ⚠️ **Atenção:**
>
> Somar probabilidades sem descontar a interseção conta duas vezes os resultados compartilhados.

---

## 2. Probabilidade condicional

A expressão “dado que” reduz o universo: só permanecem os resultados compatíveis com a informação recebida.

### 2.1 Reduzir o espaço

A probabilidade de $$A$$ dado $$B$$ é:

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}$$

$$P(A\mid B)$$ mede a chance de $$A$$ dentro do novo universo $$B$$.

A regra geral da multiplicação decorre dessa definição:

$$P(A\cap B)=P(A)\cdot P(B\mid A)$$

Uma árvore representa o processo por ramos; a probabilidade de cada caminho é o produto de suas etapas.

### 2.2 Dependência e independência

**Duas retiradas sem reposição**

Uma urna hipotética contém 3 bolas vermelhas e 2 azuis. Qual a chance de retirar duas vermelhas?

| Etapa | Casos vermelhos | Probabilidade |
|---|---:|---:|
| Primeira retirada | 3 em 5 | $$\frac{3}{5}$$ |
| Segunda, após vermelha | 2 em 4 | $$\frac{2}{4}$$ |

**Resolução:**

- **Passo 1:** Calcular a chance da primeira vermelha.

$$P(V_1)=\frac{3}{5}$$

- **Passo 2:** Atualizar o espaço depois da retirada.

$$P(V_2\mid V_1)=\frac{2}{4}$$

- **Passo 3:** Multiplicar as etapas.

$$P(V_1\cap V_2)=\frac{3}{5}\cdot\frac{2}{4}$$

$$P(V_1\cap V_2)=\frac{3}{10}=30\%$$

**Resposta:** a chance é 30%; sem reposição, a primeira retirada altera a composição e a probabilidade seguinte.

Eventos independentes satisfazem $$P(A\mid B)=P(A)$$ e, portanto, $$P(A\cap B)=P(A)P(B)$$. Eles não são sinônimo de mutuamente exclusivos: eventos disjuntos e possíveis não ocorrem juntos, então conhecer um altera a chance do outro para zero.

> 🔢 **Padrão:**
>
> Sem reposição, o denominador e possivelmente o numerador mudam a cada etapa da árvore.

---

## 3. Probabilidade total e teorema de Bayes

Um resultado positivo depende tanto da qualidade do teste quanto da frequência anterior da condição na população.

### 3.1 Atualizar uma probabilidade

Se $$B_1,B_2,\ldots,B_k$$ formam uma partição do espaço, a probabilidade total de $$A$$ é:

$$P(A)=\sum_i P(A\mid B_i)P(B_i)$$

O teorema de Bayes inverte a condição:

$$P(B_i\mid A)=\frac{P(A\mid B_i)P(B_i)}{P(A)}$$

$$P(B_i)$$ é a probabilidade *a priori*; $$P(A\mid B_i)$$, a verossimilhança; e $$P(B_i\mid A)$$, a probabilidade atualizada após a evidência.

O pastor e matemático **Thomas Bayes (c. 1701–1761)** apresentou a base desse raciocínio em um ensaio publicado postumamente em 1763 por Richard Price.

### 3.2 Um teste hipotético

Suponha 10.000 pessoas, prevalência de 1%, sensibilidade de 95% e especificidade de 95%.

| Grupo | Pessoas | Positivos |
|---|---:|---:|
| Com a condição | 100 | 95 verdadeiros |
| Sem a condição | 9.900 | 495 falsos |
| **Total** | **10.000** | **590** |

**Resolução:**

- **Passo 1:** Identificar todos os resultados positivos.

$$95+495=590$$

- **Passo 2:** Calcular a fração de verdadeiros positivos.

Considere $$D$$ o evento “ter a condição” e $$+$$ o resultado positivo.

$$P(D\mid +)=\frac{95}{590}$$

$$P(D\mid +)\approx16{,}10\%$$

**Resposta:** entre os positivos, cerca de 16% têm a condição; como ela é rara, os falsos positivos superam os verdadeiros mesmo com um teste de 95%.

Filtros de spam usam atualização semelhante. A **falácia do promotor** surge ao confundir a chance de uma evidência se a pessoa for culpada com a chance de culpa dada a evidência.

> ⚠️ **Atenção:**
>
> Sensibilidade, especificidade e probabilidade após um positivo respondem a perguntas diferentes.
