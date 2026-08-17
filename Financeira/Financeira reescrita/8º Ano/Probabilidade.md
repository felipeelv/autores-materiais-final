# BL1_Capítulo 1 — Probabilidade

> Em 1 dado, qual a probabilidade de NÃO sair 6? Dá para contar direto — ou calcular $$1 - P(6)$$. E em 3 moedas, qual a chance de sair 3 caras seguidas?

---

## 1. Espaço amostral e eventos

Antes de calcular uma chance, construa o mapa: quais resultados o experimento permite.

### 1.1 O universo e suas partes

**Experimento aleatório** — procedimento cujo resultado não se pode prever com certeza, como lançar um dado equilibrado.

O **espaço amostral** ($$\Omega$$) reúne todos os resultados possíveis, e um **evento** é uma parte dele:

$$A \subseteq \Omega$$

No lançamento de um dado, o quadro fica assim:

| Elemento | Conjunto | Classificação |
|---|---|---|
| $$\Omega$$ | $$\{1, 2, 3, 4, 5, 6\}$$ | espaço amostral |
| $$A$$ | $$\{6\}$$ | evento simples — um resultado |
| $$B$$ | $$\{2, 4, 6\}$$ | evento composto — dois ou mais |

### 1.2 Complementares e exclusivos

O **complementar** de $$A$$ reúne o que está em $$\Omega$$ e não está em $$A$$:

$$\bar{A} = \Omega - A = \{1, 2, 3, 4, 5\}$$

$$A \cup \bar{A} = \Omega$$

$$A \cap \bar{A} = \emptyset$$

Eventos **mutuamente exclusivos** não podem ocorrer juntos, mas isso não basta para torná-los complementares.

**Classificando dois eventos do dado**

Considere $$C = $$ "sair 1" e $$D = $$ "sair 2".

**Resolução:**

- **Passo 1:** Verificar se há resultado em comum.

$$C \cap D = \emptyset$$

- **Passo 2:** Verificar se a união cobre o espaço inteiro.

$$C \cup D = \{1, 2\} \neq \Omega$$

**Resposta:** $$C$$ e $$D$$ são mutuamente exclusivos, mas não complementares — quatro resultados ficam de fora da união, e complementares precisam cobrir todo o universo.

Em *Éléments de la théorie des probabilités* (1909), **Émile Borel (1871–1956)** sistematizou a probabilidade moderna. Seu paradoxo do "macaco infinito" mostra que um evento pode ser improvável ao extremo e ainda assim ter probabilidade maior que zero.

> ⚠️ **Atenção:**  
> Eventos complementares sempre são exclusivos, mas eventos exclusivos não precisam completar o espaço amostral.

---

## 2. Cálculo de probabilidades

Com resultados equiprováveis, a chance compara casos favoráveis com o total de casos.

### 2.1 A fórmula e o atalho do complementar

Para um evento $$A$$ em espaço equiprovável:

$$P(A) = \frac{n(A)}{n(\Omega)}$$

$$n(A)$$ é a quantidade de casos favoráveis e $$n(\Omega)$$, o total de resultados possíveis. Somadas, as probabilidades de todos os resultados cobrem o universo inteiro:

$$\sum P_i = 1$$

Daí sai um atalho: contar o contrário costuma ser mais rápido que contar o que se quer.

$$P(\bar{A}) = 1 - P(A)$$

Considere $$S$$ o evento "sair 6". Para "não sair 6" em um dado:

$$P(\bar{S}) = 1 - \frac{1}{6} = \frac{5}{6} \approx 83{,}33\%$$

Cinco das seis faces atendem à condição, e é isso que o resultado significa.

### 2.2 Construir o espaço em etapas

No **princípio multiplicativo**, cada etapa multiplica as possibilidades da anterior:

$$n(\Omega) = n_1 \cdot n_2 \cdots n_k$$

$$n_1, n_2, \ldots, n_k$$ são as quantidades de opções de cada etapa.

**Pelo menos uma cara em três moedas**

Cada lançamento tem duas possibilidades: cara ou coroa.

**Resolução:**

- **Passo 1:** Calcular o tamanho do espaço.

$$n(\Omega) = 2 \cdot 2 \cdot 2 = 8$$

- **Passo 2:** Identificar o complementar — "nenhuma cara" é a única sequência coroa-coroa-coroa.

$$P(\bar{A}) = \frac{1}{8}$$

- **Passo 3:** Subtrair de 1.

$$P(A) = 1 - \frac{1}{8} = \frac{7}{8} = 87{,}50\%$$

**Resposta:** a chance é 87,50% — contar a única sequência sem cara sai mais rápido que listar as sete sequências favoráveis.

O mesmo princípio dá o espaço de dois dados: $$6 \cdot 6 = 36$$ pares. Neles, a soma 7 aparece em 6 pares, ou $$\frac{6}{36}$$, e a soma 2 aparece em apenas 1, ou $$\frac{1}{36}$$ — somas centrais têm mais caminhos que somas extremas.

> 🔢 **Padrão:**  
> Primeiro construa o espaço amostral, depois calcule a chance — o denominador vem antes do numerador.

---

## 3. Probabilidade com múltiplos eventos

Duas ferramentas organizam etapas em sequência sem deixar resultado de fora.

### 3.1 Árvore e tabela de dupla entrada

Para dois lançamentos de moeda, a tabela cruza as duas etapas:

| 1º lançamento \ 2º lançamento | Cara | Coroa |
|---|---|---|
| **Cara** | cara–cara | cara–coroa |
| **Coroa** | coroa–cara | coroa–coroa |

A árvore apresenta o mesmo espaço em ramos: de cada resultado da primeira moeda saem dois novos caminhos, e cada caminho completo é um resultado. As duas mostram os mesmos quatro pares, com ênfases diferentes:

- a **árvore** destaca a ordem em que as etapas acontecem;
- a **tabela** destaca o cruzamento entre as duas etapas.

### 3.2 Eventos independentes

Dois eventos são **independentes** quando o resultado de um não altera a probabilidade do outro. Nesse caso, as probabilidades se multiplicam:

$$P(A \cap B) = P(A) \cdot P(B)$$

**Três caras seguidas**

Considere três lançamentos de uma moeda equilibrada e $$C_i$$ o evento "cara no lançamento $$i$$".

**Resolução:**

- **Passo 1:** Registrar a probabilidade de cara em cada lançamento.

$$P(C_i) = \frac{1}{2}$$

- **Passo 2:** Multiplicar as três probabilidades.

$$P(C_1 \cap C_2 \cap C_3) = \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2}$$

$$P(C_1 \cap C_2 \cap C_3) = \frac{1}{8} = 12{,}50\%$$

**Resposta:** 12,50% — uma das oito sequências possíveis tem três caras, e o resultado confere com o espaço construído pelo princípio multiplicativo.

A moeda não tem memória: depois de várias coroas seguidas, a chance de cara no próximo lançamento continua sendo $$\frac{1}{2}$$, ou 50%. Sorteio com reposição funciona do mesmo modo, porque devolver o item mantém as probabilidades da etapa seguinte.

> ⚠️ **Atenção:**  
> Multiplique as probabilidades somente quando os eventos forem independentes — frequência observada no passado não altera o próximo resultado.
