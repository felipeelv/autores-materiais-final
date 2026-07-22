# Capítulo 2 — Estudo do sinal, forma canônica e gráficos

> Como identificar onde uma função quadrática é positiva ou negativa?

---

## 1. Estudo do sinal

### 1.1 Regra pelos intervalos

**Estudar o sinal** é determinar onde $$f(x)$$ é positiva, negativa ou nula. Com duas raízes reais $$x_1<x_2$$:

- fora das raízes, $$f(x)$$ tem o sinal de $$a$$;
- entre as raízes, tem sinal contrário ao de $$a$$;
- nas raízes, vale zero.

Os seis casos completos são:

| Discriminante | $$a>0$$ | $$a<0$$ |
|---|---|---|
| $$\Delta>0$$ | positiva fora; negativa entre | negativa fora; positiva entre |
| $$\Delta=0$$ | positiva, exceto zero na raiz | negativa, exceto zero na raiz |
| $$\Delta<0$$ | positiva em ℝ | negativa em ℝ |

### 1.2 Aplicação da regra

**Sinal de uma função de duas raízes**

Estude $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Identificar as raízes e o coeficiente quadrático.

$$x_1=1$$

$$x_2=3$$

$$a=1>0$$

- **Passo 2:** Aplicar a regra fora das raízes: $$f(x)>0\ \text{em}\ ]-\infty,1[\cup]3,+\infty[$$.

- **Passo 3:** Aplicar a regra entre as raízes: $$f(x)<0\ \text{em}\ ]1,3[$$.

**Resposta:** A função é positiva fora das raízes, negativa entre elas e nula em 1 e 3.

**Bernhard Riemann** (1826–1866) ampliou o estudo das funções no século XIX. Seu olhar estrutural ajuda a reconhecer que uma mesma regra organiza toda a família das parábolas.

> 🔢 **Padrão:**  
> Sem raízes reais, a função quadrática conserva o sinal de $$a$$ em todo o domínio.

---

## 2. Forma canônica

### 2.1 Completamento de quadrado

A **forma canônica** é

$$f(x)=a(x-x_v)^2+y_v$$

onde $$(x_v,y_v)$$ é o vértice e $$a\neq0$$. Ela é obtida da forma geral por completamento de quadrado.

**Dedução da forma canônica**

Parta de $$f(x)=ax^2+bx+c$$.

**Resolução:**

- **Passo 1:** Colocar $$a$$ em evidência nos termos com $$x$$.

$$f(x)=a\left(x^2+\frac{b}{a}x\right)+c$$

- **Passo 2:** Somar e subtrair o termo que completa o quadrado.

$$f(x)=a\left(x^2+\frac{b}{a}x+\frac{b^2}{4a^2}-\frac{b^2}{4a^2}\right)+c$$

- **Passo 3:** Fatorar o trinômio quadrado perfeito.

$$f(x)=a\left(x+\frac{b}{2a}\right)^2-\frac{b^2}{4a}+c$$

- **Passo 4:** Reunir os termos independentes.

$$f(x)=a\left(x+\frac{b}{2a}\right)^2-\frac{b^2-4ac}{4a}$$

**Resposta:** Como $$x_v=-\frac{b}{2a}$$ e $$y_v=-\frac{\Delta}{4a}$$, resulta $$f(x)=a(x-x_v)^2+y_v$$.

### 2.2 Equivalência das formas

Para $$f(x)=x^2-4x+3$$, a escrita canônica é

$$f(x)=(x-2)^2-1$$

Expandir essa expressão recupera a forma geral; portanto, as duas representam a mesma função.

> ⚠️ **Atenção:**  
> Na expressão $$(x+3)^2$$, a abscissa do vértice é $$-3$$.

---

## 3. Construção de gráficos

### 3.1 Roteiro completo

O gráfico pode ser construído nesta ordem:

- verificar o sinal de $$a$$;
- calcular raízes, quando reais;
- determinar o vértice;
- traçar o eixo $$x=x_v$$;
- marcar o ponto $$(0,c)$$.

Na forma canônica, vértice e concavidade são lidos diretamente.

**Esboço pelos elementos**

Analise $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Determinar a concavidade.

$$a=1>0$$

- **Passo 2:** Registrar raízes e vértice.

$$x_1=1$$

$$x_2=3$$

$$V=(2,-1)$$

- **Passo 3:** Registrar eixo e interseção vertical: $$(0,3)$$.

$$x=2$$

**Resposta:** A parábola abre para cima, corta o eixo $$x$$ em 1 e 3, tem vértice $$(2,-1)$$ e passa por $$(0,3)$$.

### 3.2 Esboço pela forma canônica

**Parábola com vértice explícito**

Analise $$g(x)=2(x-3)^2+1$$.

**Resolução:**

- **Passo 1:** Ler o vértice.

$$V=(3,1)$$

- **Passo 2:** Identificar concavidade e eixo.

$$a=2>0$$

$$x=3$$

- **Passo 3:** Ler a imagem a partir do mínimo.

$$\mathrm{Im}(g)=[1,+\infty[$$

**Resposta:** A parábola abre para cima, tem vértice $$(3,1)$$, eixo $$x=3$$ e não possui raízes reais.

### 3.3 Imagem e monotonicidade

Para $$a>0$$, a função decresce até $$x_v$$, cresce depois e tem imagem $$[y_v,+\infty[$$. Para $$a<0$$, cresce até $$x_v$$, decresce depois e tem imagem $$]-\infty,y_v]$$.

> 🔢 **Padrão:**  
> O vértice separa os dois intervalos de monotonicidade da função quadrática.
