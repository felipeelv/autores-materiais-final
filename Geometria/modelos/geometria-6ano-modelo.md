# Capítulo 1 — Quadriláteros e circunferência

> O quadrado é também um retângulo? E por que a razão entre o contorno e o diâmetro de QUALQUER objeto redondo — da moeda ao pneu — dá sempre o mesmo número?

---

## 1. Quadriláteros: conceito e classificação

A bandeira reúne um retângulo verde e um losango amarelo: duas formas de quatro lados com propriedades distintas.

### 1.1 Elementos e famílias

**Quadrilátero** é o polígono de quatro lados. Num quadrilátero $$ABCD$$, os elementos são:

- quatro lados e quatro vértices;
- quatro ângulos internos, cuja soma é $$360^{\circ}$$;
- duas diagonais, $$\overline{AC}$$ e $$\overline{BD}$$, que ligam vértices não consecutivos.

<!-- tikz:inicio fig-01-elementos-dos-quadrilateros -->
![Quadrilátero ABCD com quatro lados, quatro vértices e as duas diagonais traçadas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/6ano/quadrilateros-e-circunferencia/fig-01-elementos-dos-quadrilateros.png)
<!-- tikz:fim fig-01-elementos-dos-quadrilateros -->

A quantidade de pares de lados paralelos separa duas famílias:

<!-- tikz:inicio fig-05-classificacao-dos-paralelogramos -->
![Árvore visual mostra retângulos e losangos como paralelogramos e o quadrado pertencendo às duas classes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/6ano/quadrilateros-e-circunferencia/fig-05-classificacao-dos-paralelogramos.png)
<!-- tikz:fim fig-05-classificacao-dos-paralelogramos -->

| Família | Condição | Casos |
|---|---|---|
| Paralelogramos | dois pares paralelos | retângulo, losango, quadrado |
| Trapézios | exatamente um par paralelo | retângulo, isósceles, escaleno |

<!-- tikz:inicio fig-06-classificacao-dos-trapezios -->
![Trapézio com setas indicando seu único par de lados paralelos](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/6ano/quadrilateros-e-circunferencia/fig-06-classificacao-dos-trapezios.png)
<!-- tikz:fim fig-06-classificacao-dos-trapezios -->

Trapézio retângulo tem dois ângulos retos; o isósceles, lados não paralelos congruentes; o escaleno não reúne essas condições.

### 1.2 Inclusão de classes

Cada nome acrescenta uma condição: retângulo tem quatro ângulos retos; losango, quatro lados congruentes; quadrado reúne as duas propriedades.

**Classificação de uma placa quadrada**

Uma placa tem quatro lados congruentes e quatro ângulos retos. Como ela pode ser classificada?

**Resolução:**

- **Passo 1:** Os quatro ângulos retos atendem à definição de retângulo.
- **Passo 2:** Os quatro lados congruentes atendem à definição de losango.
- **Passo 3:** As duas condições juntas atendem à definição de quadrado.

**Resposta:** a placa é quadrado, retângulo, losango e paralelogramo; pertencer a classes mais amplas não apaga sua classificação mais específica.

Em *Éléments de Géométrie* (1794), **Adrien-Marie Legendre (1752–1833)** sistematizou a classificação usada no ensino por mais de um século.

> ⚠️ **Atenção:**
>
> Neste material, trapézio tem exatamente um par de lados paralelos e, portanto, não é paralelogramo.

---

## 2. Propriedades dos paralelogramos

Uma moldura inclinada pode perder os ângulos retos e ainda conservar os dois pares de lados opostos paralelos.

### 2.1 Lados e ângulos

Num paralelogramo $$ABCD$$, lados e ângulos opostos são congruentes:

<!-- tikz:inicio fig-02-propriedades-do-paralelogramo -->
![Paralelogramo ABCD com lados e ângulos opostos congruentes e diagonais cruzando-se no ponto médio M](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/6ano/quadrilateros-e-circunferencia/fig-02-propriedades-do-paralelogramo.png)
<!-- tikz:fim fig-02-propriedades-do-paralelogramo -->

$$\overline{AB}\cong\overline{CD}$$

$$\overline{BC}\cong\overline{AD}$$

Ângulos consecutivos são suplementares porque aparecem entre retas paralelas cortadas por uma transversal:

$$\angle A+\angle B=180^{\circ}$$

### 2.2 Diagonais e medidas

As diagonais $$\overline{AC}$$ e $$\overline{BD}$$ encontram-se em $$M$$, ponto médio de ambas:

$$AM=MC$$

$$BM=MD$$

Essa propriedade permite conferir a moldura e descobrir a diagonal inteira conhecendo apenas uma de suas metades.

**Moldura inclinada**

Num paralelogramo, dois lados vizinhos medem $$8\,\mathrm{cm}$$ e $$5\,\mathrm{cm}$$, e o ângulo $$A$$ mede $$70^{\circ}$$. Determine o perímetro e os demais ângulos.

**Resolução:**

- **Passo 1:** Repetir as medidas nos lados opostos e somá-las.

$$P=8+5+8+5$$

$$P=26\,\mathrm{cm}$$

- **Passo 2:** Calcular o ângulo consecutivo.

$$\angle B=180^{\circ}-70^{\circ}$$

$$\angle B=110^{\circ}$$

- **Passo 3:** Usar a congruência dos ângulos opostos.

$$\angle C=70^{\circ}$$

$$\angle D=110^{\circ}$$

**Resposta:** o perímetro mede $$26\,\mathrm{cm}$$; os ângulos são $$70^{\circ}$$, $$110^{\circ}$$, $$70^{\circ}$$ e $$110^{\circ}$$.

> 🔢 **Padrão:**
>
> Em todo paralelogramo, dois ângulos consecutivos somam $$180^{\circ}$$.

---

## 3. Circunferência e círculo

Uma moeda mostra a borda que a contorna e a face inteira; em Geometria, cada parte recebe um nome.

### 3.1 Linha, região e elementos

**Circunferência** é a linha formada pelos pontos à mesma distância de um centro; **círculo** é essa linha com a região interna.

<!-- tikz:inicio fig-03-elementos-da-circunferencia -->
![Diagrama identifica raio, diâmetro, corda e arco de uma circunferência e compara as retas tangente e secante](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/6ano/quadrilateros-e-circunferencia/fig-03-elementos-da-circunferencia.png)
<!-- tikz:fim fig-03-elementos-da-circunferencia -->

Se o centro é $$O$$, seus elementos são:

- **raio** — segmento do centro à circunferência;
- **corda** — segmento com extremidades na circunferência;
- **diâmetro** — corda que passa pelo centro;
- **arco** — parte da circunferência;
- **tangente** e **secante** — retas que têm, respectivamente, um e dois pontos comuns com a curva.

O diâmetro reúne dois raios alinhados:

$$d=2r$$

### 3.2 A razão constante

Ao dividir o comprimento $$C$$ pelo diâmetro $$d$$ de qualquer circunferência, obtém-se o número $$\pi$$:

<!-- tikz:inicio fig-04-razao-circunferencia-diametro -->
![Circunferência desenrolada mede aproximadamente três vírgula quatorze vezes o diâmetro, ilustrando a razão entre C e d igual a pi](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/6ano/quadrilateros-e-circunferencia/fig-04-razao-circunferencia-diametro.png)
<!-- tikz:fim fig-04-razao-circunferencia-diametro -->

$$\frac{C}{d}=\pi\approx3{,}14$$

Por isso, o comprimento pode ser calculado por:

$$C=\pi d$$

$$C=2\pi r$$

**Contorno de uma tampa**

Uma tampa tem diâmetro de $$20\,\mathrm{cm}$$. Calcule seu contorno usando $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Escolher a fórmula que usa o diâmetro.

$$C=\pi d$$

- **Passo 2:** Substituir os valores.

$$C\approx3{,}14\cdot20$$

$$C\approx62{,}8\,\mathrm{cm}$$

**Resposta:** o contorno da tampa mede aproximadamente $$62{,}8\,\mathrm{cm}$$; objetos redondos maiores mantêm a mesma razão $$C/d$$.

> ⚠️ **Atenção:**
>
> Circunferência é a borda; círculo é a borda junto com toda a região interna.
