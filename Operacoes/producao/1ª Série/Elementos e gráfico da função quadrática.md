# Capítulo 1 — Elementos e gráfico da função quadrática

> Como os coeficientes controlam o gráfico de uma função quadrática?

---

## 1. Definição e elementos

### 1.1 Forma geral

**Função quadrática** é a função definida por

$$f(x)=ax^2+bx+c$$

onde $$a$$, $$b$$ e $$c$$ são reais e $$a\neq 0$$. Seu domínio é ℝ.

Os coeficientes cumprem papéis distintos:

- $$a$$ garante o grau 2 e determina concavidade e abertura;
- $$b$$ participa da posição do eixo e do vértice;
- $$c$$ é o valor de $$f(0)$$ e marca a interseção com o eixo vertical.

Uma **equação do 2º grau** pede os valores que tornam uma igualdade verdadeira; a função associa cada entrada $$x$$ a uma imagem $$f(x)$$.

### 1.2 Cálculo do valor numérico

**Valor da função em uma entrada**

Calcule $$f(2)$$ para $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Substituir $$x$$ por 2.

$$f(2)=2^2-4\times 2+3$$

- **Passo 2:** Efetuar a potência.

$$f(2)=4-4\times 2+3$$

- **Passo 3:** Efetuar a multiplicação.

$$f(2)=4-8+3$$

- **Passo 4:** Somar os termos.

$$f(2)=-1$$

**Resposta:** A imagem de 2 é $$-1$$.

**Augustin-Louis Cauchy** (1789–1857) consolidou a definição rigorosa de função no *Cours d'analyse* (1821), tratando-a como objeto matemático preciso.

> ⚠️ **Atenção:**  
> Se $$a=0$$, a expressão deixa de definir uma função quadrática.

---

## 2. Parábola e concavidade

### 2.1 Forma do gráfico

O gráfico é uma **parábola**, e o sinal de $$a$$ determina sua concavidade:

- $$a>0$$: concavidade para cima;
- $$a<0$$: concavidade para baixo.

O valor absoluto de $$a$$ também influencia a abertura: quanto maior $$|a|$$, mais fechada é a curva.

### 2.2 Interseção com o eixo vertical

No eixo $$y$$, a abscissa vale zero. Portanto,

$$f(0)=c$$

e a parábola passa pelo ponto $$(0,c)$$.

**Leitura dos coeficientes de uma trajetória**

Considere $$h(t)=-5t^2+8t+2$$.

**Resolução:**

- **Passo 1:** Identificar o coeficiente quadrático.

$$a=-5<0$$

- **Passo 2:** Determinar a concavidade.

A parábola tem concavidade para baixo.

- **Passo 3:** Calcular a altura inicial.

$$h(0)=2$$

**Resposta:** A trajetória é parabólica, abre para baixo e começa no ponto $$(0,2)$$; os demais coeficientes participam da posição do vértice e das raízes.

> 🔢 **Padrão:**  
> O ponto $$(0,c)$$ pertence ao gráfico de toda função $$f(x)=ax^2+bx+c$$.

---

## 3. Raízes da função

### 3.1 Zeros e discriminante

**Raízes** ou **zeros** são os valores de $$x$$ para os quais $$f(x)=0$$. Para calculá-los, usa-se

$$\Delta=b^2-4ac$$

$$x=\frac{-b\pm\sqrt{\Delta}}{2a}$$

onde $$a$$, $$b$$ e $$c$$ são os coeficientes e $$a\neq 0$$.

O discriminante determina o número de raízes reais:

| Condição | Raízes reais | Encontro com o eixo $$x$$ |
|---|---:|---|
| $$\Delta>0$$ | duas distintas | corta em dois pontos |
| $$\Delta=0$$ | uma dupla | toca em um ponto |
| $$\Delta<0$$ | nenhuma | não encontra |

### 3.2 Cálculo e leitura geométrica

**Zeros de uma parábola**

Determine as raízes de $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Calcular o discriminante.

$$\Delta=(-4)^2-4\times 1\times 3$$

$$\Delta=4$$

- **Passo 2:** Aplicar a fórmula.

$$x=\frac{4\pm\sqrt{4}}{2}$$

$$x=\frac{4\pm 2}{2}$$

- **Passo 3:** Separar os resultados.

$$x_1=1$$

$$x_2=3$$

**Resposta:** As raízes são 1 e 3, abscissas onde a parábola corta o eixo $$x$$.

> ⚠️ **Atenção:**  
> Se $$\Delta<0$$, a função não tem raízes reais.

---

## 4. Vértice da parábola

### 4.1 Coordenadas

O **vértice** é o ponto de retorno da parábola. Suas coordenadas são

$$x_v=-\frac{b}{2a}$$

$$y_v=-\frac{\Delta}{4a}$$

onde $$a$$ e $$b$$ são coeficientes da função e $$\Delta=b^2-4ac$$. Também é possível obter $$y_v$$ calculando $$f(x_v)$$.

### 4.2 Relação com as raízes

Quando as raízes reais $$x_1$$ e $$x_2$$ existem, a simetria fornece

$$x_v=\frac{x_1+x_2}{2}$$

**Vértice calculado por duas coordenadas**

Determine o vértice de $$f(x)=x^2-4x+3$$.

**Resolução:**

- **Passo 1:** Calcular a abscissa.

$$x_v=-\frac{-4}{2\times 1}$$

$$x_v=2$$

- **Passo 2:** Usar $$\Delta=4$$ para calcular a ordenada.

$$y_v=-\frac{4}{4\times 1}$$

$$y_v=-1$$

- **Passo 3:** Conferir pela média das raízes 1 e 3.

$$x_v=\frac{1+3}{2}$$

$$x_v=2$$

**Resposta:** O vértice é $$(2,-1)$$.

> ⚠️ **Atenção:**  
> O sinal negativo faz parte da fórmula de $$x_v$$ e deve ser aplicado ao valor de $$b$$.

---

## 5. Eixo de simetria

### 5.1 Reta de simetria

O **eixo de simetria** é a reta vertical que passa pelo vértice:

$$x=x_v$$

Para qualquer distância real $$d$$, os pontos simétricos satisfazem

$$f(x_v-d)=f(x_v+d)$$

Calcule um lado da curva e reflita os pontos.

### 5.2 Esboço por reflexão

Um procedimento econômico usa quatro dados:

- calcular o vértice;
- traçar o eixo de simetria;
- obter pontos de um lado;
- refletir cada ponto à mesma distância no outro lado.

**Pares simétricos**

Em $$f(x)=x^2-4x+3$$, o eixo é $$x=2$$. Verifique os pontos com abscissas 0 e 4.

**Resolução:**

- **Passo 1:** Calcular a primeira imagem.

$$f(0)=3$$

- **Passo 2:** Calcular a segunda imagem.

$$f(4)=4^2-4\times 4+3$$

$$f(4)=16-16+3$$

$$f(4)=3$$

- **Passo 3:** Comparar as distâncias ao eixo.

$$2-0=2$$

$$4-2=2$$

**Resposta:** Os pontos $$(0,3)$$ e $$(4,3)$$ são simétricos em relação a $$x=2$$.

> 🔢 **Padrão:**  
> A média das abscissas de dois pontos simétricos é $$x_v$$.

---

## 6. Máximo, mínimo e imagem

### 6.1 Valor extremo

A concavidade determina o tipo de extremo:

| Condição | Extremo | Imagem |
|---|---|---|
| $$a>0$$ | mínimo $$y_v$$ | $$[y_v,+\infty[$$ |
| $$a<0$$ | máximo $$y_v$$ | $$]-\infty,y_v]$$ |

A coordenada $$x_v$$ indica onde o extremo ocorre; $$y_v$$ indica seu valor.

### 6.2 Altura máxima

**Lançamento de uma bola**

Para $$h(t)=-5t^2+8t+2$$, determine o instante e a altura máxima.

**Resolução:**

- **Passo 1:** Calcular o instante do vértice.

$$t_v=-\frac{8}{2\times(-5)}$$

$$t_v=0{,}8$$

- **Passo 2:** Calcular a altura nesse instante.

$$h(0{,}8)=-5\times(0{,}8)^2+8\times0{,}8+2$$

$$h(0{,}8)=-5\times0{,}64+6{,}4+2$$

$$h(0{,}8)=-3{,}2+6{,}4+2$$

$$h(0{,}8)=5{,}2$$

**Resposta:** A bola atinge a altura máxima de $$5{,}2\,\mathrm{m}$$ em $$0{,}8\,\mathrm{s}$$.

> ⚠️ **Atenção:**  
> Não confunda a entrada do extremo, $$x_v$$, com o valor extremo, $$y_v$$.
