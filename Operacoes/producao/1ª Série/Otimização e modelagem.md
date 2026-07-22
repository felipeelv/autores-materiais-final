# Capítulo 3 — Otimização e modelagem

> Como usar o vértice para encontrar o maior ou o menor valor?

---

## 1. Problemas de otimização

### 1.1 Extremo pelo vértice

**Otimizar** é encontrar o máximo ou o mínimo de uma grandeza. Quando o modelo é quadrático, a concavidade classifica o extremo e o vértice fornece:

- $$x_v$$ — valor da variável que produz o extremo;
- $$y_v$$ — valor máximo ou mínimo obtido.

### 1.2 Área máxima

**Cercado de área máxima**

Com $$40\,\mathrm{m}$$ de cerca, determine as dimensões do retângulo de maior área.

**Resolução:**

- **Passo 1:** Escrever a restrição do perímetro.

$$2x+2y=40$$

$$y=20-x$$

- **Passo 2:** Modelar a área.

$$A(x)=x(20-x)$$

$$A(x)=-x^2+20x$$

- **Passo 3:** Calcular a abscissa do vértice.

$$x_v=-\frac{20}{2\times(-1)}$$

$$x_v=10$$

- **Passo 4:** Obter o outro lado e a área.

$$y=20-10$$

$$y=10$$

$$A(10)=10\times10$$

$$A(10)=100$$

**Resposta:** O quadrado de lado $$10\,\mathrm{m}$$ tem área máxima de $$100\,\mathrm{m^2}$$.

### 1.3 Receita máxima

**Preço e demanda**

Uma loja vende $$q=60-p$$ unidades ao preço de $$p$$ reais.

**Resolução:**

- **Passo 1:** Registrar o domínio econômico: $$0\leq p\leq60$$.

- **Passo 2:** Modelar a receita.

$$R(p)=p(60-p)$$

$$R(p)=-p^2+60p$$

- **Passo 3:** Calcular o preço do vértice.

$$p_v=-\frac{60}{2\times(-1)}$$

$$p_v=30$$

- **Passo 4:** Calcular a receita máxima.

$$R(30)=30\times30$$

$$R(30)=900$$

**Resposta:** O preço de R$ 30,00 produz receita máxima de R$ 900,00.

> 🔢 **Padrão:**  
> Entre retângulos de mesmo perímetro, o quadrado possui a maior área.

---

## 2. Modelagem com função quadrática

### 2.1 Da condição à função

Um modelo quadrático é construído por quatro decisões:

- escolher a variável independente;
- identificar a grandeza a otimizar;
- traduzir a restrição entre as grandezas;
- eliminar uma variável para obter uma função de uma entrada.

O intervalo admissível da variável deve ser registrado antes da interpretação.

### 2.2 Receita máxima

**Preço que maximiza a receita**

Uma loja vende $$q=100-2p$$ unidades quando cobra $$p$$ reais. Determine o preço e a receita máxima.

**Resolução:**

- **Passo 1:** Registrar o domínio econômico: $$0\leq p\leq50$$.

- **Passo 2:** Multiplicar preço pela quantidade.

$$R(p)=p(100-2p)$$

$$R(p)=-2p^2+100p$$

- **Passo 3:** Calcular o preço do vértice.

$$p_v=-\frac{100}{2\times(-2)}$$

$$p_v=25$$

- **Passo 4:** Calcular a quantidade e a receita.

$$q=100-2\times25$$

$$q=50$$

$$R(25)=25\times50$$

$$R(25)=1\,250$$

**Resposta:** O preço de R$ 25,00 gera receita máxima de R$ 1.250,00.

> ⚠️ **Atenção:**  
> Depois do cálculo, interprete $$x_v$$ e $$y_v$$ com as unidades exigidas pelo problema.

---

## 3. Função quadrática em contextos reais

### 3.1 Trajetória e significado físico

**Galileo Galilei** (1564–1642) demonstrou em *Duas Novas Ciências* (1638) que a trajetória ideal de um projétil é parabólica.

Em um modelo de altura

$$h(t)=at^2+bt+c$$

o coeficiente $$a<0$$ representa a concavidade para baixo, o vértice informa a altura máxima e as raízes indicam os instantes em que a altura é zero.

### 3.2 Altura e alcance temporal

**Altura de uma bola**

Considere $$h(t)=-5t^2+20t$$, com altura em metros e tempo em segundos.

**Resolução:**

- **Passo 1:** Calcular o instante de altura máxima.

$$t_v=-\frac{20}{2\times(-5)}$$

$$t_v=2$$

- **Passo 2:** Calcular a altura máxima.

$$h(2)=-5\times2^2+20\times2$$

$$h(2)=-20+40$$

$$h(2)=20$$

- **Passo 3:** Encontrar quando a bola está no solo.

$$-5t^2+20t=0$$

$$-5t(t-4)=0$$

$$t=0$$

$$t-4=0$$

$$t=4$$

**Resposta:** A bola atinge $$20\,\mathrm{m}$$ aos $$2\,\mathrm{s}$$ e retorna ao solo aos $$4\,\mathrm{s}$$.

Resultados negativos para tempo, comprimento ou preço são descartados quando o contexto não os admite; valores incompatíveis também exigem revisar o modelo.

> ⚠️ **Atenção:**  
> Uma solução algébrica só é válida no problema se respeitar as restrições físicas do contexto.
