# Capítulo 5 — Inequações do 2º grau

> Como encontrar a faixa em que uma expressão quadrática é positiva?

---

## 1. Conceito de inequação quadrática

### 1.1 Significado gráfico

Uma **inequação do 2º grau** apresenta uma das formas

$$ax^2+bx+c>0$$

$$ax^2+bx+c<0$$

ou as versões não estritas, com $$a\neq0$$. Resolver é localizar no domínio os pontos do gráfico que estão acima, abaixo ou sobre o eixo $$x$$.

As raízes são as fronteiras possíveis dos intervalos, pois nelas a função vale zero.

### 1.2 Leitura pelos zeros

**Leitura de uma condição quadrática**

Considere $$f(x)=x^2-5x+6$$ e a condição $$f(x)>0$$.

**Resolução:**

- **Passo 1:** Fatorar para obter as raízes.

$$f(x)=(x-2)(x-3)$$

$$x_1=2$$

$$x_2=3$$

- **Passo 2:** Identificar a concavidade.

$$a=1>0$$

- **Passo 3:** Ler onde o gráfico está acima do eixo: $$x<2\ \text{ou}\ x>3$$.

**Resposta:** A condição vale em $$]-\infty,2[\cup]3,+\infty[$$.

> 🔢 **Padrão:**  
> As raízes dividem a reta nos intervalos em que o sinal da função quadrática é constante.

---

## 2. Resolução de inequações quadráticas

### 2.1 Roteiro por discriminante

O método tem quatro etapas:

- calcular as raízes reais;
- identificar o sinal de $$a$$;
- distribuir os sinais nos intervalos;
- selecionar as regiões pedidas e incluir extremos apenas com $$\geq$$ ou $$\leq$$.

Se $$\Delta=0$$, há uma única fronteira; se $$\Delta<0$$, o sinal é o de $$a$$ em todo ℝ.

### 2.2 Aplicação do roteiro

**Faixa entre duas raízes**

Resolva $$-x^2+5x-6\geq0$$.

**Resolução:**

- **Passo 1:** Encontrar as raízes da igualdade associada.

$$-x^2+5x-6=0$$

$$x^2-5x+6=0$$

$$(x-2)(x-3)=0$$

$$x_1=2$$

$$x_2=3$$

- **Passo 2:** Identificar o sinal entre as raízes.

$$a=-1<0$$

A função é positiva entre 2 e 3.

- **Passo 3:** Incluir as raízes por causa de $$\geq$$.

$$S=[2,3]$$

**Resposta:** A solução é $$[2,3]$$.

> ⚠️ **Atenção:**  
> O símbolo não estrito inclui raízes, mas o símbolo estrito as exclui.

---

## 3. Quadro de sinais aplicado

### 3.1 Lucro positivo

**David Hilbert** (1862–1943) defendeu o tratamento formal das relações matemáticas por regras explícitas. Em inequações, esse rigor aparece na separação de casos e na escrita precisa do conjunto solução.

### 3.2 Interpretação da faixa de lucro

**Faixa de preços lucrativa**

Resolva $$L(x)=-2x^2+40x-150>0$$.

**Resolução:**

- **Passo 1:** Resolver a igualdade associada.

$$-2x^2+40x-150=0$$

$$x^2-20x+75=0$$

$$\Delta=(-20)^2-4\times1\times75$$

$$\Delta=100$$

$$x=\frac{20\pm10}{2}$$

$$x_1=5$$

$$x_2=15$$

- **Passo 2:** Montar o quadro pelo sinal de $$a$$.

| Intervalo | $$]-\infty,5[$$ | $$5$$ | $$]5,15[$$ | $$15$$ | $$]15,+\infty[$$ |
|---|---:|---:|---:|---:|---:|
| Sinal de $$L(x)$$ | − | 0 | + | 0 | − |

- **Passo 3:** Selecionar o sinal positivo.

$$S=]5,15[$$

**Resposta:** O lucro é positivo para preços entre R$ 5,00 e R$ 15,00, sem incluir os extremos.

> 🔢 **Padrão:**  
> Em um quadro de sinais, cada coluna representa um intervalo sem mudança de sinal.
