# Capítulo 2 — Função modular, composta e inversa

> Como interpretar módulo, composição e função inversa?

---

## 1. Função modular: definição e gráfico

### 1.1 Módulo e definição por partes

**Módulo** é a distância de um número real até zero:

$$|x|=\sqrt{x^2}$$

$$|x|=\begin{cases}x, & x\geq0\\-x, & x<0\end{cases}$$

O domínio de $$f(x)=|x|$$ é ℝ, e sua imagem é $$[0,+\infty[$$. O gráfico tem formato de V, com vértice na origem.

### 1.2 Módulo de outra função

Em $$y=|g(x)|$$, os pontos de $$g$$ que já estão acima do eixo horizontal permanecem. Os pontos abaixo dele são refletidos para cima.

**Imagem de uma parábola modular**

Descreva a transformação de $$g(x)=x^2-4$$ para $$f(x)=|x^2-4|$$.

**Resolução:**

- **Passo 1:** Encontrar onde a parábola corta o eixo horizontal.

$$x^2-4=0$$

$$x=-2$$

$$x=2$$

- **Passo 2:** Identificar o trecho negativo: $$-2<x<2$$.

- **Passo 3:** Refletir esse trecho.

$$f(x)=\begin{cases}x^2-4, & x\leq-2\\4-x^2, & -2<x<2\\x^2-4, & x\geq2\end{cases}$$

**Resposta:** o trecho entre −2 e 2 é refletido para cima; os demais permanecem.

**Karl Weierstrass** consolidou o rigor moderno na análise matemática. O cuidado com definições precisas sustenta o uso de módulo, composição e inversão sem ambiguidades.

> 🔢 **Padrão:**  
> Aplicar módulo à imagem preserva a parte não negativa e reflete a parte negativa.

---

## 2. Equações e inequações modulares

### 2.1 Equações com módulo

Para $$a>0$$, a equação se divide em dois casos:

$$|f(x)|=a$$

$$f(x)=a$$

$$f(x)=-a$$

Se $$a=0$$, resolve-se apenas $$f(x)=0$$. Se $$a<0$$, não existe solução real.

**Duas posições possíveis**

Resolva $$|2x-6|=4$$.

**Resolução:**

- **Passo 1:** Abrir o caso positivo.

$$2x-6=4$$

$$x=5$$

- **Passo 2:** Abrir o caso negativo.

$$2x-6=-4$$

$$x=1$$

**Resposta:** $$x=1$$ ou $$x=5$$.

### 2.2 Inequações e intervalos

Para $$a>0$$, valem as equivalências:

$$|x|<a\iff -a<x<a$$

$$|x|>a\iff x<-a\text{ ou }x>a$$

A primeira solução é uma interseção no intervalo central. A segunda é uma união de dois intervalos externos:

$$|x|>3\iff x\in]-\infty,-3[\cup]3,+\infty[$$

> ⚠️ **Atenção:**  
> As equivalências usuais de inequações modulares exigem $$a>0$$; sem essa condição, os casos mudam.

---

## 3. Função composta

### 3.1 Composição e ordem

**Função composta** aplica primeiro a função interna e depois a externa:

$$(f\circ g)(x)=f(g(x))$$

Em geral, a composição não é comutativa:

$$f\circ g\neq g\circ f$$

### 3.2 Cálculo e domínio

**Duas ordens de composição**

Dadas $$f(x)=2x+1$$ e $$g(x)=x^2$$, determine as duas composições.

**Resolução:**

- **Passo 1:** Aplicar $$g$$ dentro de $$f$$.

$$(f\circ g)(x)=f(x^2)$$

$$(f\circ g)(x)=2x^2+1$$

- **Passo 2:** Aplicar $$f$$ dentro de $$g$$.

$$(g\circ f)(x)=g(2x+1)$$

$$(g\circ f)(x)=(2x+1)^2$$

$$(g\circ f)(x)=4x^2+4x+1$$

**Resposta:** as composições são $$2x^2+1$$ e $$4x^2+4x+1$$, portanto são diferentes.

Para que $$f(g(x))$$ exista, $$x$$ deve pertencer ao domínio de $$g$$ e $$g(x)$$ deve pertencer ao domínio de $$f$$. Se $$f(x)=\sqrt{x}$$ e $$g(x)=x-4$$, então:

$$x-4\geq0$$

$$x\geq4$$

> 🔢 **Padrão:**  
> Na composição, a função mais próxima de $$x$$ é aplicada primeiro.

---

## 4. Função inversa

### 4.1 Existência e obtenção

**Função inversa** desfaz a função original. Ela existe quando a função é bijetora entre o domínio e o contradomínio considerados.

$$(f\circ f^{-1})(x)=x$$

$$(f^{-1}\circ f)(x)=x$$

O procedimento troca $$x$$ e $$y$$ e depois isola $$y$$.

**Inversa de uma função afim**

Determine a inversa de $$f(x)=2x+1$$.

**Resolução:**

- **Passo 1:** Escrever a função com $$y$$.

$$y=2x+1$$

- **Passo 2:** Trocar as variáveis.

$$x=2y+1$$

- **Passo 3:** Isolar $$y$$.

$$2y=x-1$$

$$y=\frac{x-1}{2}$$

**Resposta:** $$f^{-1}(x)=\dfrac{x-1}{2}$$.

### 4.2 Simetria dos gráficos

Se $$(a,b)$$ pertence ao gráfico de $$f$$, então $$(b,a)$$ pertence ao gráfico de $$f^{-1}$$. Os gráficos são reflexos em relação à reta $$y=x$$.

Domínio e imagem também trocam de papel. A função $$f(x)=x^2$$ em ℝ não é injetora, pois 3 e −3 têm a mesma imagem; ela só admite inversa após uma restrição adequada do domínio.

> ⚠️ **Atenção:**  
> O expoente −1 em $$f^{-1}$$ indica inversa, não o recíproco $$1/f(x)$$.
