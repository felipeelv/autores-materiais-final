# Capítulo 6 — Discriminante e construção de gráficos

> Como o discriminante orienta o esboço da parábola?

---

## 1. Discriminante positivo

### 1.1 Dois cruzamentos

Para a função quadrática:

$$f(x)=ax^2+bx+c$$

calculamos:

$$\Delta=b^2-4ac$$

Se $$\Delta>0$$, a equação $$f(x)=0$$ tem duas raízes reais distintas. Portanto, a parábola atravessa o eixo $$x$$ em dois pontos, $$(x_1,0)$$ e $$(x_2,0)$$.

### 1.2 Localizar as raízes

**Dois pontos no eixo**

Analise $$f(x)=x^2-5x+6$$.

**Resolução:**

- **Passo 1:** Calcular o discriminante.

$$\Delta=(-5)^2-4\times1\times6$$

$$\Delta=25-24$$

$$\Delta=1$$

- **Passo 2:** Calcular as raízes.

$$x=\frac{5\pm\sqrt{1}}{2}$$

$$x_1=2$$

$$x_2=3$$

**Resposta:** a parábola cruza o eixo $$x$$ em $$(2,0)$$ e $$(3,0)$$.

> 🔢 **Padrão:**  
> Discriminante positivo corresponde a dois cruzamentos distintos com o eixo $$x$$.

**Yang Hui** (c. 1238–c. 1298) sistematizou métodos para raízes simples e duplas.

---

## 2. Discriminante nulo ou negativo

### 2.1 Raiz dupla

Se $$\Delta=0$$, a fórmula produz uma única raiz real, repetida. A parábola **tangencia** o eixo $$x$$: toca-o no vértice e retorna para o mesmo lado.

**Toque único**

Analise $$f(x)=x^2-4x+4$$.

**Resolução:**

- **Passo 1:** Calcular $$\Delta$$.

$$\Delta=(-4)^2-4\times1\times4$$

$$\Delta=16-16$$

$$\Delta=0$$

- **Passo 2:** Calcular a raiz dupla.

$$x=-\frac{-4}{2\times1}$$

$$x=2$$

**Resposta:** a parábola tangencia o eixo $$x$$ em $$(2,0)$$.

### 2.2 Nenhum cruzamento

Se $$\Delta<0$$, não existem raízes reais. A parábola não toca o eixo $$x$$: fica toda acima dele quando $$a>0$$ ou toda abaixo quando $$a<0$$.

> ⚠️ **Atenção:**  
> Ausência de raízes reais não significa ausência de gráfico; domínio, parábola e vértice continuam definidos.

---

## 3. Seis configurações

### 3.1 Quadro completo

Os seis casos são:

| Sinal de $$a$$ | Sinal de $$\Delta$$ | Configuração |
|---|---|---|
| positivo | positivo | abre para cima e cruza duas vezes |
| positivo | zero | abre para cima e tangencia |
| positivo | negativo | abre para cima e fica acima do eixo |
| negativo | positivo | abre para baixo e cruza duas vezes |
| negativo | zero | abre para baixo e tangencia |
| negativo | negativo | abre para baixo e fica abaixo do eixo |

### 3.2 Leitura em mão dupla

Do gráfico para a álgebra:

- a abertura revela o sinal de $$a$$;
- a quantidade de encontros com o eixo $$x$$ revela o sinal de $$\Delta$$;
- quando existem duas raízes, o eixo de simetria passa pelo ponto médio entre elas.

**Gráfico descrito**

Uma parábola abre para baixo e não toca o eixo $$x$$.

**Resolução:**

- **Passo 1:** Ler a concavidade: $$a<0$$.

- **Passo 2:** Ler os cruzamentos: $$\Delta<0$$.

**Resposta:** o coeficiente quadrático e o discriminante são negativos.

> 🔢 **Padrão:**  
> O sinal de $$a$$ controla a abertura; o sinal de $$\Delta$$ controla os encontros com o eixo $$x$$.

---

## 4. Construção de gráficos

### 4.1 Roteiro

A construção segue seis etapas:

- identificar $$a$$, $$b$$ e $$c$$;
- decidir a concavidade pelo sinal de $$a$$;
- marcar $$(0,c)$$;
- calcular $$\Delta$$ e as raízes reais;
- calcular o vértice;
- completar o traçado usando a simetria.

### 4.2 Três casos de discriminante

**Esboços pelos pontos essenciais**

Analise $$f(x)=x^2-1$$, $$g(x)=x^2-2x+1$$ e $$h(x)=x^2+1$$.

**Resolução:**

- **Passo 1:** Para $$f$$, calcular o discriminante.

$$\Delta_f=0^2-4\times1\times(-1)$$

$$\Delta_f=4$$

$$x_1=-1$$

$$x_2=1$$

$$V_f=(0,-1)$$

- **Passo 2:** Para $$g$$, calcular o discriminante.

$$\Delta_g=(-2)^2-4\times1\times1$$

$$\Delta_g=0$$

$$x=1$$

$$V_g=(1,0)$$

- **Passo 3:** Para $$h$$, calcular o discriminante.

$$\Delta_h=0^2-4\times1\times1$$

$$\Delta_h=-4$$

$$V_h=(0,1)$$

**Resposta:** as três parábolas abrem para cima; $$f$$ passa por $$(0,-1)$$ e cruza o eixo $$x$$ em $$-1$$ e 1; $$g$$ passa por $$(0,1)$$ e tangencia em $$(1,0)$$; $$h$$ passa por $$(0,1)$$ e não toca o eixo $$x$$.

> ⚠️ **Atenção:**  
> Um esboço confiável depende dos pontos calculados e da simetria, não de desenhar a curva antes das contas.
