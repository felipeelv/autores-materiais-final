# BL1_Capítulo 1 — Medidas de dispersão

> Duas turmas têm a mesma média de notas (7,0). Numa, todos tiraram perto de 7; na outra, há notas 4 e notas 9. Como medir, com um único número, o quanto um conjunto de dados se espalha em torno da média?

---

## 1. Amplitude e desvios

Dois conjuntos podem ter a mesma média 7 e espalhamentos que não se parecem.

### 1.1 Amplitude total

A **dispersão** descreve o espalhamento dos dados em torno do centro. Sua medida mais simples é a amplitude:

$$AT = x_{\max} - x_{\min}$$

$$x_{\max}$$ é o maior valor, $$x_{\min}$$ o menor e $$AT$$ a amplitude, na unidade dos dados.

Nos conjuntos hipotéticos A = 6, 7, 7, 7, 8 e B = 4, 6, 7, 9, 9, ambos com média 7:

$$AT_A = 8 - 6 = 2$$

$$AT_B = 9 - 4 = 5$$

A conta é rápida, mas usa somente os extremos — tudo o que acontece entre eles fica invisível.

### 1.2 Desvios em relação à média

O **desvio** de cada valor mede sua distância até a média:

$$d_i = x_i - \bar{x}$$

Os desvios dos dois conjuntos mostram por que a soma deles não serve como medida:

| Conjunto | Desvios | $$\sum d_i$$ |
|---|---|---:|
| A | −1, 0, 0, 0, 1 | 0 |
| B | −3, −1, 0, 2, 2 | 0 |

Os sinais se cancelam sempre. O **desvio médio absoluto** contorna o cancelamento usando módulos:

$$DM = \frac{\sum |d_i|}{n}$$

$$x_i$$ é cada valor, $$\bar{x}$$ a média, $$d_i$$ o desvio e $$n$$ a quantidade de dados.

**Dois conjuntos com média 7**

Considere A = 6, 7, 7, 7, 8 e B = 4, 6, 7, 9, 9.

**Resolução:**

- **Passo 1:** Somar os módulos dos desvios de cada conjunto.

$$A: \; 1 + 0 + 0 + 0 + 1 = 2$$

$$B: \; 3 + 1 + 0 + 2 + 2 = 8$$

- **Passo 2:** Dividir pela quantidade de dados.

$$DM_A = \frac{2}{5} = 0{,}4$$

$$DM_B = \frac{8}{5} = 1{,}6$$

**Resposta:** o desvio médio de B é quatro vezes o de A, e a amplitude é mais que o dobro — a mesma média 7 escondia conjuntos com espalhamentos muito diferentes.

O módulo dificulta manipulações algébricas posteriores. Elevar os desvios ao quadrado resolve o cancelamento sem esse inconveniente, e é o caminho que leva à variância.

> ⚠️ **Atenção:**  
> Média igual não significa distribuição igual: centro e dispersão respondem a perguntas diferentes.

---

## 2. Variância e desvio padrão

Elevar os desvios ao quadrado impede o cancelamento e dá peso maior aos afastamentos grandes.

### 2.1 População × amostra

A escolha do divisor depende de o conjunto ser o todo ou uma parte dele:

$$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$

$$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$$

Os símbolos distinguem os dois casos:

| População | Amostra | Significado |
|---|---|---|
| $$\mu$$ | $$\bar{x}$$ | média |
| $$N$$ | $$n$$ | quantidade de dados |
| $$\sigma^2$$ | $$s^2$$ | variância |
| $$\sigma$$ | $$s$$ | desvio padrão |

Dividir por $$n-1$$ é a **correção de Bessel**: a amostra estima a dispersão do todo e tende a subestimá-la, porque a própria média usada no cálculo saiu daqueles mesmos dados.

### 2.2 A sequência completa

O cálculo segue sete etapas fixas: valores, média, desvios, quadrados, soma, variância e desvio padrão.

**Cinco valores hipotéticos**

Considere os dados 5, 7, 7, 7 e 9.

**Resolução:**

- **Passo 1:** Calcular a média.

$$\bar{x} = \frac{5 + 7 + 7 + 7 + 9}{5} = 7$$

- **Passo 2:** Organizar desvios e quadrados.

| $$x_i$$ | $$d_i$$ | $$d_i^2$$ |
|---:|---:|---:|
| 5 | −2 | 4 |
| 7 | 0 | 0 |
| 7 | 0 | 0 |
| 7 | 0 | 0 |
| 9 | 2 | 4 |
| **Soma** | **0** | **8** |

- **Passo 3:** Calcular variância e desvio padrão tratando os dados como população.

$$\sigma^2 = \frac{8}{5} = 1{,}6$$

$$\sigma = \sqrt{1{,}6} \approx 1{,}26$$

- **Passo 4:** Refazer o cálculo tratando os dados como amostra.

$$s^2 = \frac{8}{4} = 2$$

$$s = \sqrt{2} \approx 1{,}41$$

**Resposta:** os mesmos cinco dados dão desvio padrão 1,26 se forem a população inteira e 1,41 se forem uma amostra — os valores se afastam da média pouco mais de um ponto, e o divisor $$n-1$$ produz a estimativa maior, mais prudente.

Em distribuições aproximadamente normais, cerca de 68% dos dados ficam entre $$\mu - \sigma$$ e $$\mu + \sigma$$.

Em *Natural Inheritance* (1889), **Francis Galton (1822–1911)** cunhou os termos regressão à média e correlação e inventou a caixa de Galton — e também fundou o eugenismo, ideologia discriminatória hoje rejeitada.

> 🔢 **Padrão:**  
> A variância sai em unidade ao quadrado; só o desvio padrão devolve o resultado à unidade original dos dados.

---

## 3. Coeficiente de variação

Um desvio de R$ 50,00 é pequeno perto de uma média de R$ 1.000,00 e grande perto de uma média de R$ 200,00.

### 3.1 Dispersão relativa

O **coeficiente de variação** divide o desvio padrão pela média e expressa o resultado em porcentagem:

$$CV = \frac{\sigma}{\bar{x}} \cdot 100\%$$

$$\sigma$$ e $$\bar{x}$$ precisam estar na mesma unidade, porque o quociente entre elas é o que cancela a unidade. Daí as três características da medida:

- **relativa** — mede o espalhamento em proporção ao próprio centro;
- **adimensional** — reais sobre reais, pontos sobre pontos;
- **em porcentagem** — leitura direta, comparável entre escalas diferentes.

**Duas séries de valores hipotéticas**

A série A tem média R$ 1.000,00 e desvio padrão R$ 50,00; a série B tem média R$ 200,00 e desvio padrão R$ 20,00.

**Resolução:**

- **Passo 1:** Calcular o coeficiente da série A.

$$CV_A = \frac{50}{1000} \cdot 100\% = 5\%$$

- **Passo 2:** Calcular o coeficiente da série B.

$$CV_B = \frac{20}{200} \cdot 100\% = 10\%$$

**Resposta:** B tem desvio padrão absoluto menor, R$ 20,00 contra R$ 50,00, e ainda assim varia o dobro em relação à própria média — o desvio padrão é absoluto, o coeficiente de variação é relativo, e comparar séries de escalas diferentes exige o segundo.

### 3.2 Ler o resultado

Faixas de referência didática orientam a primeira leitura:

| Coeficiente de variação | Dispersão relativa |
|---|---|
| $$CV \leq 15\%$$ | baixa |
| $$15\% < CV \leq 30\%$$ | média |
| $$CV > 30\%$$ | alta |

Os limites dependem do contexto, e cada área adota critérios próprios.

Em séries de retornos financeiros, o coeficiente compara a variação relativa de aplicações diferentes — mas não resume liquidez, prazo nem possibilidade de perda. Uma medida apoia a análise; não decide sozinha.

> ⚠️ **Atenção:**  
> Média zero ou próxima de zero torna o coeficiente de variação inadequado, porque o divisor faz o resultado disparar.
