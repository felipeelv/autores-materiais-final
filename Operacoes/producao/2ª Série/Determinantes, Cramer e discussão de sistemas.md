# BL1_Capítulo 3 — Determinantes, Cramer e discussão de sistemas

> Como resolver e classificar sistemas usando determinantes?

---

## 1. Determinantes aplicados a sistemas

### 1.1 Matrizes associadas

Para $$AX=B$$, a matriz $$A_i$$ é obtida substituindo em $$A$$ apenas a coluna da incógnita $$x_i$$ pela coluna $$B$$.

Se $$\det A\neq0$$, o sistema é SPD. Se $$\det A=0$$, não há solução única e será necessária outra análise.

### 1.2 Construção das matrizes substituídas

**Matrizes de um sistema**

Considere

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Escrever a matriz dos coeficientes.

$$A=\begin{pmatrix}2&3\\1&-1\end{pmatrix}$$

- **Passo 2:** Substituir a coluna de $$x$$.

$$A_x=\begin{pmatrix}8&3\\-1&-1\end{pmatrix}$$

- **Passo 3:** Substituir a coluna de $$y$$.

$$A_y=\begin{pmatrix}2&8\\1&-1\end{pmatrix}$$

- **Passo 4:** Calcular o determinante principal.

$$\det A=2\times(-1)-3\times1$$

$$\det A=-5$$

**Resposta:** Como $$\det A\neq0$$, o sistema é SPD e suas matrizes associadas estão prontas para Cramer.

> ⚠️ **Atenção:**  
> Em $$A_i$$, somente a coluna da incógnita correspondente é substituída.

---

## 2. Regra de Cramer

### 2.1 Fórmula e validade

A **Regra de Cramer** estabelece, para um sistema quadrado com $$\det A\neq0$$,

$$x_i=\frac{\det A_i}{\det A}$$

onde $$A_i$$ substitui a coluna $$i$$ de $$A$$ pela coluna dos termos independentes.

A condição é indispensável: com $$\det A=0$$, a divisão não existe e o sistema não possui solução única.

### 2.2 Aplicação da fórmula

**Valores obtidos pelos determinantes**

Suponha $$\det A=-5$$, $$\det A_x=-5$$ e $$\det A_y=-10$$.

**Resolução:**

- **Passo 1:** Calcular $$x$$.

$$x=\frac{-5}{-5}$$

$$x=1$$

- **Passo 2:** Calcular $$y$$.

$$y=\frac{-10}{-5}$$

$$y=2$$

**Resposta:** A solução é $$(1,2)$$.

**Gabriel Cramer** (1704–1752) publicou a regra em 1750, no apêndice de sua obra sobre curvas algébricas. O método é elegante para sistemas pequenos, mas exige muitos determinantes em ordens elevadas.

> ⚠️ **Atenção:**  
> Cramer é válida somente quando $$\det A\neq0$$.

---

## 3. Cálculo de sistemas por Cramer

### 3.1 Sistema de ordem 2

**Duas incógnitas por Cramer**

Resolva

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante principal.

$$\det A=2\times(-1)-3\times1$$

$$\det A=-5$$

- **Passo 2:** Calcular o determinante de $$A_x$$.

$$\det A_x=8\times(-1)-3\times(-1)$$

$$\det A_x=-5$$

- **Passo 3:** Calcular o determinante de $$A_y$$.

$$\det A_y=2\times(-1)-8\times1$$

$$\det A_y=-10$$

- **Passo 4:** Aplicar Cramer.

$$x=\frac{-5}{-5}$$

$$x=1$$

$$y=\frac{-10}{-5}$$

$$y=2$$

- **Passo 5:** Verificar nas equações originais.

$$2\times1+3\times2=8$$

$$1-2=-1$$

**Resposta:** A solução é $$(1,2)$$ e satisfaz as duas equações.

### 3.2 Sistema de ordem 3

**Três incógnitas por Cramer**

Resolva

$$\begin{cases}x+y+z=6\\x-y+z=2\\x+y-z=0\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante principal por expansão.

$$\det A=1(1-1)-1(-1-1)+1(1+1)$$

$$\det A=4$$

- **Passo 2:** Substituir a primeira coluna e calcular.

$$A_x=\begin{pmatrix}6&1&1\\2&-1&1\\0&1&-1\end{pmatrix}$$

$$\det A_x=6(1-1)-1(-2-0)+1(2-0)$$

$$\det A_x=4$$

- **Passo 3:** Substituir a segunda coluna e calcular.

$$A_y=\begin{pmatrix}1&6&1\\1&2&1\\1&0&-1\end{pmatrix}$$

$$\det A_y=1(-2-0)-6(-1-1)+1(0-2)$$

$$\det A_y=8$$

- **Passo 4:** Substituir a terceira coluna e calcular.

$$A_z=\begin{pmatrix}1&1&6\\1&-1&2\\1&1&0\end{pmatrix}$$

$$\det A_z=1(0-2)-1(0-2)+6(1+1)$$

$$\det A_z=12$$

- **Passo 5:** Calcular as incógnitas.

$$x=\frac{4}{4}$$

$$x=1$$

$$y=\frac{8}{4}$$

$$y=2$$

$$z=\frac{12}{4}$$

$$z=3$$

**Resposta:** A solução é $$(1,2,3)$$.

Para ordens maiores, o escalonamento costuma exigir menos operações.

> 🔢 **Padrão:**  
> Um sistema de ordem $$n$$ exige $$n+1$$ determinantes na aplicação direta de Cramer.

---

## 4. Discussão de sistemas

### 4.1 Critérios seguros

Para sistemas quadrados:

- $$\det A\neq0$$ garante SPD;
- $$\det A=0$$ e algum $$\det A_i\neq0$$ garantem SI;
- $$\det A=0$$ e todos os $$\det A_i=0$$ não bastam, em geral, para concluir SPI.

No último caso, o escalonamento ou a comparação de postos decide corretamente, sobretudo em ordem 3 ou maior.

### 4.2 Discussão com parâmetro

**Sistema com parâmetro**

Discuta

$$\begin{cases}mx+y=1\\x+my=1\end{cases}$$

**Resolução:**

- **Passo 1:** Calcular o determinante principal.

$$\det A=m\times m-1\times1$$

$$\det A=m^2-1$$

- **Passo 2:** Identificar os valores que garantem SPD: $$m^2-1\neq0$$; $$m\neq-1\ \text{e}\ m\neq1$$.

- **Passo 3:** Analisar $$m=1$$.

$$\begin{cases}x+y=1\\x+y=1\end{cases}$$

As equações coincidem, portanto há infinitas soluções.

- **Passo 4:** Analisar $$m=-1$$.

$$\begin{cases}-x+y=1\\x-y=1\end{cases}$$

Multiplicar a segunda equação por $$-1$$ produz

$$-x+y=-1$$

que contradiz a primeira.

**Resposta:** O sistema é SPD para $$m\neq-1$$ e $$m\neq1$$, SPI para $$m=1$$ e SI para $$m=-1$$.

> ⚠️ **Atenção:**  
> Determinantes substituídos todos nulos não substituem a análise de posto em sistemas gerais.

---

## 5. Teorema de Rouché–Capelli

### 5.1 Postos das matrizes

O **posto** é o número de linhas não nulas após o escalonamento. O Teorema de Rouché–Capelli afirma:

$$\mathrm{posto}(A)=\mathrm{posto}([A|B])$$

se, e somente se, o sistema é compatível. Sendo $$n$$ o número de incógnitas:

| Condição | Classe |
|---|---|
| $$\mathrm{posto}(A)=\mathrm{posto}([A|B])=n$$ | SPD |
| $$\mathrm{posto}(A)=\mathrm{posto}([A|B])<n$$ | SPI |
| $$\mathrm{posto}(A)<\mathrm{posto}([A|B])$$ | SI |

### 5.2 Classificação pelo escalonamento

**Classificação por posto**

Classifique

$$\begin{cases}x+y+z=3\\2x+2y+2z=6\end{cases}$$

**Resolução:**

- **Passo 1:** Escrever a matriz ampliada.

$$[A|B]=\begin{pmatrix}1&1&1&3\\2&2&2&6\end{pmatrix}$$

- **Passo 2:** Subtrair duas vezes a primeira linha da segunda: $$\begin{pmatrix}1&1&1&3\\0&0&0&0\end{pmatrix}$$.

- **Passo 3:** Comparar os postos com o número de incógnitas.

$$\mathrm{posto}(A)=1$$

$$\mathrm{posto}([A|B])=1$$

$$n=3$$

**Resposta:** O sistema é SPI, pois os postos são iguais e menores que o número de incógnitas.

As três ações formam um fluxo único:

- classificar pela comparação dos postos;
- resolver por um método equivalente adequado;
- discutir parâmetros repetindo a classificação nos casos críticos.

> 🔢 **Padrão:**  
> Igualdade dos postos garante compatibilidade; compará-los com $$n$$ decide entre SPD e SPI.
