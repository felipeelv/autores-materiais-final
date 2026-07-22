# Capítulo 1 — Conceito e classificação de sistemas lineares

> Como classificar um sistema pela quantidade de soluções?

---

## 1. Equações e sistemas lineares

### 1.1 Estrutura linear

Uma **equação linear** em $$n$$ incógnitas tem a forma

$$a_1x_1+a_2x_2+\timess+a_nx_n=b$$

onde $$a_i$$ são coeficientes reais, $$x_i$$ são incógnitas e $$b$$ é o termo independente. As incógnitas aparecem apenas na primeira potência e não são multiplicadas entre si.

Um **sistema linear** $$m\times n$$ reúne $$m$$ equações e $$n$$ incógnitas que devem ser satisfeitas simultaneamente. Sua forma matricial é

$$AX=B$$

onde $$A$$ é a matriz dos coeficientes, $$X$$ é a coluna das incógnitas e $$B$$ é a coluna dos termos independentes.

### 1.2 Tradução de uma situação

**Produção de dois itens**

Uma fábrica produz itens $$x$$ e $$y$$. O total é 50 e o item $$x$$ usa duas unidades de matéria-prima, contra uma de $$y$$, totalizando 70.

**Resolução:**

- **Passo 1:** Traduzir a quantidade total.

$$x+y=50$$

- **Passo 2:** Traduzir o consumo.

$$2x+y=70$$

- **Passo 3:** Reunir as condições.

$$\begin{cases}x+y=50\\2x+y=70\end{cases}$$

**Resposta:** A situação produz um sistema $$2\times2$$.

> 🔢 **Padrão:**  
> Incógnita ausente em uma equação ocupa sua coluna com coeficiente zero.

---

## 2. Solução e sistemas equivalentes

### 2.1 Solução ordenada

A **solução** de um sistema com $$n$$ incógnitas é a n-upla ordenada que satisfaz simultaneamente as $$m$$ equações. A ordem dos valores acompanha a ordem das incógnitas.

**Sistemas equivalentes** possuem exatamente o mesmo conjunto solução. Três transformações preservam essa equivalência:

- trocar duas equações de posição;
- multiplicar uma equação inteira por constante não nula;
- somar a uma equação um múltiplo de outra.

### 2.2 Verificação da solução

**Verificação de um terno**

Verifique $$(1,2,3)$$ em

$$\begin{cases}x+y+z=6\\2x-y+z=3\\x+2y-z=2\end{cases}$$

**Resolução:**

- **Passo 1:** Testar a primeira equação.

$$1+2+3=6$$

- **Passo 2:** Testar a segunda equação.

$$2\times1-2+3=3$$

- **Passo 3:** Testar a terceira equação.

$$1+2\times2-3=2$$

**Resposta:** Como as três igualdades são verdadeiras, $$(1,2,3)$$ é solução.

> ⚠️ **Atenção:**  
> Satisfazer apenas parte das equações não torna uma n-upla solução do sistema.

---

## 3. Classificação de sistemas

### 3.1 As três classes

A classificação usa três siglas:

| Classe | Significado | Quantidade de soluções |
|---|---|---:|
| SPD | possível e determinado | uma |
| SPI | possível e indeterminado | infinitas |
| SI | impossível | nenhuma |

Em um sistema quadrado, $$\det A\neq0$$ garante SPD. Quando $$\det A=0$$, o determinante sozinho apenas mostra que não há solução única; distinguir SPI de SI exige comparar as equações ou escalonar o sistema.

### 3.2 Critério e sistemas homogêneos

**Classificação imediata**

Classifique

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Registrar a matriz dos coeficientes.

$$A=\begin{pmatrix}2&3\\1&-1\end{pmatrix}$$

- **Passo 2:** Calcular o determinante.

$$\det A=2\times(-1)-3\times1$$

$$\det A=-5$$

- **Passo 3:** Aplicar o critério suficiente: $$\det A\neq0$$.

**Resposta:** O sistema é SPD.

Um sistema **homogêneo**, com $$B=0$$, sempre tem a solução trivial. Se for quadrado e $$\det A=0$$, também possui soluções não triviais.

**Eugène Rouché** (1832–1910) publicou em 1875 a base da classificação geral por postos, completada por Alfredo Capelli em 1892.

> ⚠️ **Atenção:**  
> Em sistemas gerais, $$\det A=0$$ não autoriza concluir SPI sem análise adicional.
