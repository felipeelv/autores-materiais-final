# BL1_Capítulo 1 — Medidas de dispersão

> Duas turmas têm a mesma média de notas (7,0). Numa, todos tiraram perto de 7; na outra, há notas 4 e notas 9. Como medir, com um único número, o quanto um conjunto de dados se espalha em torno da média?

---

## 1. Amplitude e desvios

A média localiza o centro do conjunto, mas não informa quanto os valores se afastam dele.

### 1.1 Amplitude total

A **dispersão** descreve o espalhamento dos dados. Sua medida mais simples é a amplitude:

$$AT=x_{\max}-x_{\min}$$

$$x_{\max}$$ é o maior valor, $$x_{\min}$$ o menor e $$AT$$ a amplitude total, na unidade dos dados.

A amplitude tem uma limitação: utiliza apenas os dois extremos. Um único outlier pode alterá-la sem mudar o restante do conjunto.

### 1.2 Desvios em relação à média

O desvio de cada valor é:

$$d_i=x_i-\bar{x}$$

Os desvios positivos e negativos se equilibram:

$$\sum d_i=0$$

Para evitar o cancelamento, o **desvio médio absoluto** usa módulos:

$$DM=\frac{\sum|d_i|}{n}$$

$$x_i$$ é cada valor, $$\bar{x}$$ a média, $$d_i$$ o desvio e $$n$$ a quantidade de dados.

O módulo dificulta certas manipulações algébricas; elevar os desvios ao quadrado conduz à variância.

**Dois conjuntos com média 7**

Considere A = 6, 7, 7, 8 e B = 4, 7, 7, 10.

**Resolução:**

- **Passo 1:** Conferir as médias.

$$\bar{x}_A=\frac{28}{4}=7$$

$$\bar{x}_B=\frac{28}{4}=7$$

- **Passo 2:** Calcular as amplitudes.

$$AT_A=8-6=2$$

$$AT_B=10-4=6$$

- **Passo 3:** Calcular os desvios médios absolutos.

$$DM_A=\frac{1+0+0+1}{4}=0{,}5$$

$$DM_B=\frac{3+0+0+3}{4}=1{,}5$$

**Resposta:** o desvio médio e a amplitude de B são o triplo dos valores de A; a média 7 escondia essa diferença de dispersão.

> ⚠️ **Atenção:**
>
> Média igual não significa distribuição igual — medidas de centro e de dispersão respondem a perguntas diferentes.

---

## 2. Variância e desvio padrão

Elevar os desvios ao quadrado impede o cancelamento e valoriza afastamentos maiores.

### 2.1 População × amostra

Para uma população completa, a variância é:

$$\sigma^2=\frac{\sum(x_i-\mu)^2}{N}$$

Para uma amostra, usa-se a correção de Bessel:

$$s^2=\frac{\sum(x_i-\bar{x})^2}{n-1}$$

Os símbolos distinguem os dois casos:

| População | Amostra | Significado |
|---|---|---|
| $$\mu$$ | $$\bar{x}$$ | média |
| $$N$$ | $$n$$ | quantidade de dados |
| $$\sigma^2$$ | $$s^2$$ | variância |
| $$\sigma$$ | $$s$$ | desvio padrão |

Dividir por $$n-1$$ compensa a tendência de uma amostra subestimar a dispersão da população, pois a média amostral já foi estimada com os próprios dados.

### 2.2 Sequência completa

**Notas de uma amostra**

Considere 4, 6, 7, 8 e 10 como amostra de uma turma maior.

**Resolução:**

- **Passo 1:** Calcular a média.

$$\bar{x}=\frac{4+6+7+8+10}{5}=7$$

- **Passo 2:** Organizar desvios e quadrados.

| $$x_i$$ | $$d_i=x_i-7$$ | $$d_i^2$$ |
|---:|---:|---:|
| 4 | -3 | 9 |
| 6 | -1 | 1 |
| 7 | 0 | 0 |
| 8 | 1 | 1 |
| 10 | 3 | 9 |
| **Soma** | **0** | **20** |

- **Passo 3:** Calcular variância e desvio padrão amostrais.

$$s^2=\frac{20}{5-1}=5$$

$$s=\sqrt{5}\approx2{,}24$$

**Resposta:** o desvio padrão amostral é aproximadamente 2,24 pontos; as notas costumam se afastar da média por cerca de 2 pontos.

Se os cinco valores fossem toda a população, a divisão por 5 daria $$\sigma^2=4$$ e $$\sigma=2$$. Em distribuições aproximadamente normais, cerca de 68% dos dados ficam a até um desvio padrão da média.

Em *Natural Inheritance* (1889), **Francis Galton (1822–1911)** desenvolveu instrumentos para estudar dispersão e correlação, mas também fundou o eugenismo, ideologia discriminatória hoje rejeitada.

> 🔢 **Padrão:**
>
> A variância fica em unidade ao quadrado; a raiz devolve o desvio padrão à unidade original dos dados.

---

## 3. Coeficiente de variação

Um desvio de 5 unidades pode ser pequeno perto de uma média 500 e grande perto de uma média 10.

### 3.1 Dispersão relativa

O **coeficiente de variação** compara o desvio padrão com a média:

$$CV=\frac{s}{\bar{x}}\cdot100\%$$

$$s$$ e $$\bar{x}$$ devem ter a mesma unidade; o resultado $$CV$$ é uma porcentagem sem unidade.

Faixas práticas oferecem uma leitura inicial:

| Coeficiente de variação | Dispersão relativa |
|---|---|
| $$CV\leq15\%$$ | baixa |
| $$15\%<CV\leq30\%$$ | média |
| $$CV>30\%$$ | alta |

Esses limites são referências: cada área pode adotar critérios próprios.

### 3.2 Comparar escalas diferentes

**Dois processos hipotéticos**

O processo A tem média 50 e desvio padrão 5; B tem média 10 e desvio padrão 2.

**Resolução:**

- **Passo 1:** Calcular o CV de A.

$$CV_A=\frac{5}{50}\cdot100\%=10\%$$

- **Passo 2:** Calcular o CV de B.

$$CV_B=\frac{2}{10}\cdot100\%=20\%$$

**Resposta:** embora B tenha menor desvio padrão absoluto, sua dispersão relativa é o dobro da de A.

Em séries de retornos financeiros, o CV pode comparar volatilidade relativa, desde que a média seja positiva e diferente de zero. Ele não resume liquidez, possibilidade de perda, prazo ou outros riscos e, portanto, não determina sozinho uma decisão.

> ⚠️ **Atenção:**
>
> Coeficiente de variação perde sentido quando a média é zero e pode enganar quando ela está muito próxima de zero.
