# BL1_Capítulo 3 — Funções exponencial e logarítmica

> Como exponencial e logaritmo se relacionam?

---

## 1. Função exponencial

### 1.1 Definição e gráfico

**Função exponencial** tem a variável no expoente:

$$f(x)=a^x$$

com $$a>0$$ e $$a\neq1$$. Suas propriedades centrais são:

- domínio ℝ e imagem $$]0,+\infty[$$;
- ponto comum $$(0,1)$$;
- crescimento para $$a>1$$;
- decrescimento para $$0<a<1$$;
- eixo horizontal como assíntota, sem ser tocado.

### 1.2 Crescimento e decaimento

Modelos exponenciais aparecem quando há um fator multiplicativo constante: crescimento populacional, meia-vida e juros compostos.

**Cultura de bactérias**

Uma cultura segue $$P(t)=1000\times2^t$$. Determine a população após 10 horas.

**Resolução:**

- **Passo 1:** Substituir o tempo.

$$P(10)=1000\times2^{10}$$

- **Passo 2:** Calcular a potência.

$$2^{10}=1024$$

- **Passo 3:** Multiplicar.

$$P(10)=1000\times1024$$

$$P(10)=1\,024\,000$$

**Resposta:** haverá 1.024.000 bactérias.

> 🔢 **Padrão:**  
> Razões constantes entre valores consecutivos indicam crescimento ou decaimento exponencial.

---

## 2. Função logarítmica

### 2.1 Definição e comportamento

**Função logarítmica** é definida por:

$$f(x)=\log_a x$$

com $$a>0$$, $$a\neq1$$ e $$x>0$$. Seu domínio é $$]0,+\infty[$$, sua imagem é ℝ e seu gráfico passa por $$(1,0)$$.

Ela é crescente se $$a>1$$ e decrescente se $$0<a<1$$. O eixo vertical é uma assíntota.

### 2.2 Propriedades operatórias

Para $$x>0$$ e $$y>0$$, as propriedades transformam produtos e potências:

$$\log_a(xy)=\log_a x+\log_a y$$

$$\log_a\left(\frac{x}{y}\right)=\log_a x-\log_a y$$

$$\log_a(x^n)=n\log_a x$$

**Logaritmo de um produto**

Calcule $$\log_2 32$$ usando uma decomposição.

**Resolução:**

- **Passo 1:** Escrever 32 como produto conveniente.

$$32=4\times8$$

- **Passo 2:** Aplicar a propriedade do produto.

$$\log_2 32=\log_2 4+\log_2 8$$

- **Passo 3:** Calcular os expoentes.

$$\log_2 32=2+3$$

$$\log_2 32=5$$

**Resposta:** $$\log_2 32=5$$.

**Henri Poincaré** estudou diferentes áreas da Matemática por suas relações e simetrias. Essa visão integrada ajuda a reconhecer exponencial e logarítmica como funções de comportamentos opostos, mas estruturalmente ligadas.

> ⚠️ **Atenção:**  
> Não existe propriedade que separe $$\log_a(x+y)$$ em uma soma de logaritmos.

---

## 3. Exponencial e logarítmica como inversas

### 3.1 Identidades e simetria

Para bases válidas e $$x>0$$:

$$a^{\log_a x}=x$$

Para todo $$x$$ real:

$$\log_a(a^x)=x$$

Os gráficos são simétricos em relação à reta $$y=x$$. O ponto $$(0,1)$$ da exponencial corresponde ao ponto $$(1,0)$$ da logarítmica.

### 3.2 Resolver o expoente

A equivalência fundamental é:

$$a^x=b\iff x=\log_a b$$

com $$b>0$$.

**Tempo de crescimento**

Uma cultura segue $$P(t)=1000\times2^t$$. Em quanto tempo atingirá 8.000 indivíduos?

**Resolução:**

- **Passo 1:** Igualar o modelo ao valor desejado.

$$1000\times2^t=8000$$

- **Passo 2:** Isolar a potência.

$$2^t=8$$

- **Passo 3:** Aplicar logaritmo de base 2.

$$t=\log_2 8$$

$$t=3$$

**Resposta:** a população atingirá 8.000 indivíduos em 3 horas.

> 🔢 **Padrão:**  
> A exponencial produz o valor; o logaritmo recupera o expoente.

---

## 4. Escolha do modelo

### 4.1 Critérios de decisão

Quatro padrões orientam a escolha:

| Comportamento | Modelo |
|---|---|
| acréscimo constante | afim |
| máximo, mínimo ou trajetória parabólica | quadrático |
| fator multiplicativo constante | exponencial |
| descobrir expoente ou trabalhar com escala de ordens de grandeza | logarítmico |

Escalas de pH, magnitude sísmica e decibéis são logarítmicas: aumentos iguais na escala representam multiplicações na grandeza original.

### 4.2 Problema integrado

**Duplicação de um investimento**

Um capital cresce 10% ao ano, segundo $$M(t)=C(1{,}1)^t$$. Determine o tempo de duplicação.

**Resolução:**

- **Passo 1:** Igualar o montante ao dobro do capital.

$$C(1{,}1)^t=2C$$

- **Passo 2:** Dividir por $$C$$, com $$C>0$$.

$$(1{,}1)^t=2$$

- **Passo 3:** Aplicar logaritmo.

$$t=\log_{1{,}1}2$$

- **Passo 4:** Usar mudança de base e aproximar: $$t\approx7{,}27$$.

$$t=\frac{\log 2}{\log 1{,}1}$$

**Resposta:** o capital dobra em aproximadamente 7,27 anos.

> ⚠️ **Atenção:**  
> A função deve ser escolhida pelo padrão de variação, não apenas pelas palavras do contexto.
