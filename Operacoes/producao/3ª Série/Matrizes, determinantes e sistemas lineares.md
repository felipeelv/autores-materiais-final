# Capítulo 4 — Matrizes, determinantes e sistemas lineares

> Como matrizes, determinantes e sistemas se conectam?

---

## 1. Matrizes: tipos

### 1.1 Ordem e elementos

**Matriz** é uma organização retangular de elementos. Em uma matriz de ordem $$m\times n$$, o elemento $$a_{ij}$$ ocupa a linha $$i$$ e a coluna $$j$$.

Os tipos principais são:

- linha: uma linha;
- coluna: uma coluna;
- quadrada: mesmo número de linhas e colunas;
- nula: todos os elementos iguais a zero;
- identidade: diagonal principal igual a 1 e demais elementos iguais a zero;
- transposta: linhas e colunas trocam de posição;
- simétrica: matriz quadrada igual à própria transposta.

### 1.2 Igualdade e sistemas

Duas matrizes são iguais quando têm a mesma ordem e elementos correspondentes iguais. A matriz dos coeficientes registra um sistema mantendo cada incógnita em uma coluna fixa.

**Leitura de uma matriz**

Considere:

$$A=\begin{pmatrix}2&-1&0\\4&3&5\end{pmatrix}$$

Determine a ordem, $$a_{23}$$ e a transposta.

**Resolução:**

- **Passo 1:** Contar linhas e colunas: $$A\text{ tem ordem }2\times3$$.

- **Passo 2:** Ler linha 2, coluna 3.

$$a_{23}=5$$

- **Passo 3:** Trocar linhas por colunas.

$$A^T=\begin{pmatrix}2&4\\-1&3\\0&5\end{pmatrix}$$

**Resposta:** a ordem é 2×3, $$a_{23}=5$$ e a transposta é a matriz apresentada.

> ⚠️ **Atenção:**  
> A posição $$a_{ij}$$ é lida como linha $$i$$ e coluna $$j$$, nessa ordem.

---

## 2. Matrizes: operações

### 2.1 Operações básicas

Adição e subtração exigem matrizes de mesma ordem e operam elementos correspondentes. Multiplicar por um escalar multiplica cada elemento.

No produto $$AB$$, o número de colunas de $$A$$ deve igualar o número de linhas de $$B$$. Cada elemento resulta do produto de uma linha por uma coluna. Em geral:

$$AB\neq BA$$

### 2.2 Produto e inversa

**Produto linha por coluna**

Considere:

$$A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$$

$$B=\begin{pmatrix}2&0\\1&5\end{pmatrix}$$

Calcule $$AB$$.

**Resolução:**

- **Passo 1:** Calcular o elemento da linha 1, coluna 1.

$$c_{11}=1\times2+2\times1$$

$$c_{11}=4$$

- **Passo 2:** Calcular o elemento da linha 1, coluna 2.

$$c_{12}=1\times0+2\times5$$

$$c_{12}=10$$

- **Passo 3:** Calcular os elementos da segunda linha.

$$c_{21}=3\times2+4\times1$$

$$c_{21}=10$$

$$c_{22}=3\times0+4\times5$$

$$c_{22}=20$$

- **Passo 4:** Montar o produto.

$$AB=\begin{pmatrix}4&10\\10&20\end{pmatrix}$$

**Resposta:** o produto é a matriz apresentada.

A inversa de uma matriz quadrada $$A$$ satisfaz $$AA^{-1}=I$$. Ela existe somente quando $$\det A\neq0$$ e permite escrever a solução de $$AX=B$$ como $$X=A^{-1}B$$.

> 🔢 **Padrão:**  
> A ordem do produto é linhas da primeira matriz por colunas da segunda.

---

## 3. Determinantes: cálculo

### 3.1 Segunda e terceira ordens

Para uma matriz 2×2:

$$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$

$$\det A=ad-bc$$

Na ordem 3, a regra de Sarrus soma os três produtos das diagonais descendentes e subtrai os três produtos das diagonais ascendentes.

### 3.2 Cofatores e Laplace

O menor complementar $$M_{ij}$$ é o determinante obtido ao retirar a linha $$i$$ e a coluna $$j$$. O cofator é:

$$C_{ij}=(-1)^{i+j}M_{ij}$$

A expansão de Laplace calcula o determinante pela soma dos elementos de uma linha ou coluna multiplicados por seus cofatores.

**Determinante de ordem 3**

Calcule:

$$A=\begin{pmatrix}1&2&0\\3&1&2\\0&4&1\end{pmatrix}$$

**Resolução:**

- **Passo 1:** Aplicar Sarrus.

$$\det A=1\times1\times1+2\times2\times0+0\times3\times4-0\times1\times0-2\times3\times1-1\times2\times4$$

- **Passo 2:** Calcular os produtos.

$$\det A=1-6-8$$

$$\det A=-13$$

**Resposta:** $$\det A=-13$$.

> ⚠️ **Atenção:**  
> Determinante é definido para matrizes quadradas; matriz retangular não possui determinante.

---

## 4. Determinantes: propriedades

### 4.1 Efeito das operações nas linhas

Três transformações são essenciais:

- linha nula implica determinante zero;
- trocar duas linhas muda o sinal do determinante;
- multiplicar uma linha por $$k$$ multiplica o determinante por $$k$$;
- somar a uma linha um múltiplo de outra preserva o determinante;
- linhas proporcionais implicam determinante zero.

Além disso:

$$\det(AB)=\det A\times\det B$$

Uma matriz quadrada é inversível exatamente quando seu determinante é diferente de zero.

### 4.2 Simplificar antes de calcular

**Determinante por transformação**

Considere:

$$A=\begin{pmatrix}1&2\\3&7\end{pmatrix}$$

Subtraia três vezes a primeira linha da segunda.

**Resolução:**

- **Passo 1:** Efetuar a operação que preserva o determinante: $$L_2\leftarrow L_2-3L_1$$.

- **Passo 2:** Obter a matriz triangular.

$$A'=\begin{pmatrix}1&2\\0&1\end{pmatrix}$$

- **Passo 3:** Multiplicar os elementos da diagonal.

$$\det A=1\times1$$

$$\det A=1$$

**Resposta:** $$\det A=1$$, portanto $$A$$ é inversível.

**Sofya Kovalevskaya** tornou-se, em 1874, a primeira mulher a obter um doutorado em Matemática e depois ocupou uma cátedra em Estocolmo. Sua obra conectou álgebra, equações diferenciais e mecânica.

> 🔢 **Padrão:**  
> Operações que criam zeros sem alterar o determinante tornam o cálculo mais curto.

---

## 5. Sistemas lineares: métodos

### 5.1 Escolha do método

Quatro métodos formam uma caixa integrada:

- substituição: variável isolada ou coeficiente 1;
- adição: coeficientes facilmente opostos;
- escalonamento: sistemas maiores;
- Cramer: sistema quadrado pequeno com determinante não nulo.

### 5.2 Resolução e verificação

**Sistema de duas condições**

Resolva:

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Isolar $$x$$ na segunda equação.

$$x=y-1$$

- **Passo 2:** Substituir na primeira.

$$2(y-1)+3y=8$$

$$5y=10$$

$$y=2$$

- **Passo 3:** Calcular $$x$$.

$$x=2-1$$

$$x=1$$

- **Passo 4:** Verificar nas equações originais.

$$2\times1+3\times2=8$$

$$1-2=-1$$

**Resposta:** a solução é $$(1,2)$$.

No formato matricial, o mesmo problema é $$AX=B$$. Substituição e adição são práticas para sistemas 2×2; escalonamento evita a explosão de determinantes em ordens maiores.

> ⚠️ **Atenção:**  
> A solução deve ser conferida nas equações originais, não apenas nas transformadas.

---

## 6. Sistemas lineares: classificação e discussão

### 6.1 Determinante e posto

Para sistema quadrado, $$\det A\neq0$$ garante uma solução única. Quando $$\det A=0$$, determinantes auxiliares não bastam em toda ordem; a classificação geral usa os postos:

- se $$\mathrm{posto}(A)\neq\mathrm{posto}([A|B])$$, o sistema é impossível;
- se os postos são iguais ao número de incógnitas, é possível e determinado;
- se os postos são iguais e menores que o número de incógnitas, é possível e indeterminado.

### 6.2 Discussão com parâmetro

**Parâmetro no sistema**

Classifique conforme $$m$$:

$$\begin{cases}mx+y=3\\x+y=2\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante dos coeficientes.

$$\det A=m-1$$

- **Passo 2:** Analisar o caso não nulo: $$m\neq1$$.

Nesse caso, o sistema tem solução única.

- **Passo 3:** Substituir $$m=1$$.

$$\begin{cases}x+y=3\\x+y=2\end{cases}$$

As equações se contradizem.

**Resposta:** o sistema é determinado para $$m\neq1$$ e impossível para $$m=1$$.

Sistemas modelam balanceamento químico e relações econômicas, como a matriz de Leontief. Em cada aplicação, as variáveis e unidades completam a interpretação algébrica.

> 🔢 **Padrão:**  
> Determinante não nulo decide a unicidade; determinante zero exige análise de compatibilidade.
