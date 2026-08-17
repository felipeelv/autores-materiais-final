# BL2_Capítulo 2 — Vértice e eixo de simetria

> Como calcular o vértice e o eixo de simetria?

---

## 1. O vértice

### 1.1 Ponto de virada

O **vértice** é o ponto de mudança de direção da parábola:

$$V(x_v,y_v)$$

Se $$a>0$$, ele é o ponto mais baixo; se $$a<0$$, é o ponto mais alto. Pontos situados à mesma distância horizontal do vértice têm a mesma coordenada vertical.

### 1.2 Vértice não é raiz

Raiz é uma entrada para a qual $$f(x)=0$$. Vértice é o extremo da curva e pode estar acima, abaixo ou sobre o eixo $$x$$.

**Parábola com duas raízes**

Considere uma função com raízes 2 e 6.

**Resolução:**

- **Passo 1:** Localizar o ponto médio horizontal.

$$x_v=\frac{2+6}{2}$$

$$x_v=4$$

**Resposta:** a coordenada horizontal do vértice é 4; isso não significa que 4 seja raiz.

> ⚠️ **Atenção:**  
> Raiz indica cruzamento com o eixo $$x$$; vértice indica o extremo da parábola.

**Pappus de Alexandria** (c. 290–c. 350) organizou propriedades das cônicas na *Coleção Matemática*.

---

## 2. Coordenadas do vértice

### 2.1 Coordenada horizontal

Com duas raízes reais, o vértice fica no ponto médio:

$$x_1+x_2=-\frac{b}{a}$$

temos:

$$x_v=\frac{x_1+x_2}{2}$$

$$x_v=-\frac{b}{2a}$$

A coordenada vertical é:

$$y_v=f(x_v)$$

ou:

$$y_v=-\frac{\Delta}{4a}$$

onde $$\Delta=b^2-4ac$$.

### 2.2 Altura máxima

**Trajetória de uma bola**

Considere $$h(t)=-5t^2+20t+1$$, com $$t$$ em segundos e $$h$$ em metros.

**Resolução:**

- **Passo 1:** Calcular o instante do vértice.

$$t_v=-\frac{20}{2\times(-5)}$$

$$t_v=2$$

- **Passo 2:** Substituir na função.

$$h(2)=-5\times2^2+20\times2+1$$

$$h(2)=-20+40+1$$

$$h(2)=21$$

**Resposta:** o vértice é $$(2,21)$$; a bola atinge $$21\,\mathrm{m}$$ após $$2\,\mathrm{s}$$.

> ⚠️ **Atenção:**  
> Na fórmula de $$x_v$$, o denominador é $$2a$$.

---

## 3. Eixo de simetria

### 3.1 A reta central

O **eixo de simetria** tem equação:

$$x=x_v$$

Se dois valores de $$x$$ estão à mesma distância de $$x_v$$, suas imagens são iguais. Essa propriedade permite obter um ponto de um lado a partir do correspondente do outro.

Pelo sinal de $$a$$, classificamos o extremo:

- $$a>0$$: vértice de mínimo;
- $$a<0$$: vértice de máximo.

### 3.2 Pontos espelhados

**Simetria de uma função**

Para $$f(x)=x^2-4x+3$$, compare $$f(1)$$ e $$f(3)$$.

**Resolução:**

- **Passo 1:** Calcular o eixo.

$$x_v=-\frac{-4}{2\times1}$$

$$x_v=2$$

- **Passo 2:** Calcular a primeira imagem.

$$f(1)=1^2-4\times1+3$$

$$f(1)=0$$

- **Passo 3:** Calcular a segunda.

$$f(3)=3^2-4\times3+3$$

$$f(3)=0$$

**Resposta:** $$(1,0)$$ e $$(3,0)$$ são simétricos em relação à reta $$x=2$$.

> 🔢 **Padrão:**  
> Pontos equidistantes do eixo de simetria têm a mesma imagem.
