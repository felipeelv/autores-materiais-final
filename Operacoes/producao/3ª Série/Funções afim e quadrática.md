# Capítulo 1 — Funções afim e quadrática

> Como os coeficientes determinam retas e parábolas?

---

## 1. Função afim: definição e gráfico

### 1.1 Coeficientes e interseções

**Função afim** é a função definida por:

$$f(x)=ax+b$$

Os coeficientes controlam elementos distintos:

- $$a$$ é a taxa de variação e determina a inclinação;
- $$b$$ é o valor inicial e determina o ponto $$(0,b)$$;
- se $$a>0$$, a função é crescente; se $$a<0$$, é decrescente;
- para $$a\neq0$$, a raiz é o ponto em que a reta cruza o eixo horizontal.

$$x=-\frac{b}{a}$$

### 1.2 Taxa de variação constante

Entre dois pontos com $$x_1\neq x_2$$, a taxa é:

$$a=\frac{f(x_2)-f(x_1)}{x_2-x_1}$$

Diferenças iguais em $$x$$ produzem sempre a mesma diferença em $$f(x)$$. Essa constância caracteriza o comportamento afim.

**Tarifa de transporte**

Uma corrida custa R$ 6,00 de bandeirada e R$ 3,00 por quilômetro. Determine a função e o custo de 8 km.

**Resolução:**

- **Passo 1:** Identificar valor inicial e taxa.

$$b=6$$

$$a=3$$

- **Passo 2:** Escrever a função.

$$C(x)=3x+6$$

- **Passo 3:** Substituir 8 km.

$$C(8)=3\times8+6$$

$$C(8)=30$$

**Resposta:** a função é $$C(x)=3x+6$$ e a corrida custa R$ 30,00.

> 🔢 **Padrão:**  
> Diferenças constantes entre imagens consecutivas indicam um modelo afim.

---

## 2. Função afim: aplicações

### 2.1 Modelos lineares

Um custo total combina parcela fixa e parcela por unidade:

$$C(x)=C_f+cx$$

Nos juros simples, o montante também varia de forma afim com o tempo:

$$M(t)=C(1+it)$$

Para reconhecer esse modelo no enunciado, procure taxa constante, acréscimo fixo ou pontos alinhados em uma reta.

### 2.2 Ajuste por dois pontos

Dois pontos distintos determinam uma única reta. Primeiro se calcula $$a$$; depois, substitui-se um ponto em $$f(x)=ax+b$$ para obter $$b$$.

**Produção mensal**

Uma fábrica registrou os pontos $$(1,5)$$ e $$(3,11)$$, em centenas de unidades. Determine a função afim.

**Resolução:**

- **Passo 1:** Calcular a taxa de variação.

$$a=\frac{11-5}{3-1}$$

$$a=3$$

- **Passo 2:** Usar o primeiro ponto para encontrar $$b$$.

$$5=3\times1+b$$

$$b=2$$

- **Passo 3:** Escrever a função.

$$f(x)=3x+2$$

- **Passo 4:** Conferir com o segundo ponto.

$$f(3)=3\times3+2$$

$$f(3)=11$$

**Resposta:** a função ajustada é $$f(x)=3x+2$$.

**Felix Klein** apresentou o Programa de Erlangen em 1872. Sua visão unificadora classificava objetos por estruturas e transformações, ideia útil para comparar famílias de funções sem confundi-las.

> ⚠️ **Atenção:**  
> Crescimento constante indica função afim; razão constante entre valores indica outro tipo de modelo.

---

## 3. Função quadrática: estudo completo

### 3.1 Elementos da parábola

**Função quadrática** tem a forma:

$$f(x)=ax^2+bx+c$$

com $$a\neq0$$. Seus elementos principais são:

- concavidade para cima se $$a>0$$ e para baixo se $$a<0$$;
- raízes dadas pela fórmula resolutiva, quando reais;
- vértice no eixo de simetria;
- interseção com o eixo vertical em $$(0,c)$$.

$$\Delta=b^2-4ac$$

$$x_v=-\frac{b}{2a}$$

$$y_v=-\frac{\Delta}{4a}$$

### 3.2 Sinal, imagem e forma canônica

Com duas raízes, o sinal é igual ao de $$a$$ fora delas e oposto entre elas. A forma canônica exibe o vértice:

$$f(x)=a(x-x_v)^2+y_v$$

**Estudo de uma parábola**

Estude $$f(x)=-x^2+6x-5$$.

**Resolução:**

- **Passo 1:** Identificar a concavidade.

$$a=-1<0$$

- **Passo 2:** Calcular o discriminante.

$$\Delta=6^2-4\times(-1)\times(-5)$$

$$\Delta=16$$

- **Passo 3:** Calcular as raízes.

$$x=\frac{-6\pm4}{-2}$$

$$x_1=1$$

$$x_2=5$$

- **Passo 4:** Calcular o vértice.

$$x_v=3$$

$$y_v=4$$

**Resposta:** a parábola abre para baixo, tem raízes 1 e 5, vértice $$(3,4)$$ e imagem $$]-\infty,4]$$.

> 🔢 **Padrão:**  
> A forma canônica mostra diretamente o vértice e preserva a mesma função da forma geral.

---

## 4. Função quadrática: otimização e aplicações

### 4.1 Máximo ou mínimo

O sinal de $$a$$ define a natureza do extremo:

- se $$a>0$$, $$y_v$$ é mínimo;
- se $$a<0$$, $$y_v$$ é máximo.

O valor $$x_v$$ indica onde o extremo ocorre; $$y_v$$ indica quanto ele vale. A interpretação deve respeitar unidades, domínio e limites físicos.

### 4.2 Modelagem pelo vértice

**Receita de uma loja**

A demanda é $$q=100-2p$$, em que $$p$$ é o preço. Determine o preço que maximiza a receita.

**Resolução:**

- **Passo 1:** Escrever a receita como preço vezes quantidade.

$$R(p)=p(100-2p)$$

$$R(p)=-2p^2+100p$$

- **Passo 2:** Calcular a abscissa do vértice.

$$p_v=-\frac{100}{2\times(-2)}$$

$$p_v=25$$

- **Passo 3:** Calcular a receita máxima.

$$R(25)=-2\times25^2+100\times25$$

$$R(25)=1250$$

- **Passo 4:** Conferir a natureza do extremo.

$$a=-2<0$$

**Resposta:** o preço de R$ 25,00 maximiza a receita em R$ 1.250,00.

Áreas com perímetro fixo e trajetórias parabólicas seguem o mesmo roteiro: montar a função, localizar o vértice e validar o resultado no contexto. Medidas negativas ou valores fora do domínio devem ser descartados.

> ⚠️ **Atenção:**  
> Calcular o vértice sem interpretar $$x_v$$ e $$y_v$$ pode produzir uma resposta numericamente certa e contextualmente errada.
