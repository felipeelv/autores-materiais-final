# Capítulo 1 — Cilindros

> Por que latas de refrigerante são cilíndricas e não em forma de paralelepípedo? E por que existem latas “slim” e latas “sleek” com o MESMO volume e formatos diferentes?

---

## 1. Definição e elementos

Uma lata pode ser entendida como um retângulo girando ou como um círculo deslocado perpendicularmente ao seu plano.

### 1.1 Duas construções equivalentes

O **cilindro circular reto** admite duas leituras equivalentes:

- **sólido de revolução** — rotação completa de um retângulo em torno de um de seus lados;

<!-- tikz:inicio fig-01-geracao-por-rotacao -->
![Retângulo girando trezentos e sessenta graus em torno de um de seus lados para gerar um cilindro](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-01-geracao-por-rotacao.png)
<!-- tikz:fim fig-01-geracao-por-rotacao -->

- **leitura análoga a um prisma** — translação de um círculo ao longo de uma direção não paralela ao plano da base.

<!-- tikz:inicio fig-02-geracao-por-translacao-da-base -->
![Círculo transladado perpendicularmente ao plano da base por uma distância h para gerar um cilindro](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-02-geracao-por-translacao-da-base.png)
<!-- tikz:fim fig-02-geracao-por-translacao-da-base -->

O geômetra **Apolônio de Perga (c. 262–c. 190 a.C.)** estudou superfícies de revolução em *Cônicas*, escrito por volta de 200 a.C.

### 1.2 Elementos do sólido

As duas bases são círculos congruentes situados em planos paralelos. Os demais elementos são:

- eixo — reta que liga os centros das bases;
- raio $$r$$ — raio de cada base;
- altura $$h$$ — distância perpendicular entre os planos das bases;
- geratriz $$g$$ — segmento da superfície lateral paralelo ao eixo.

<!-- tikz:inicio fig-03-elementos-do-cilindro -->
![Cilindro com as duas bases, o eixo, o raio r, a altura h e uma geratriz g identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-03-elementos-do-cilindro.png)
<!-- tikz:fim fig-03-elementos-do-cilindro -->

**Leitura de uma embalagem**

Uma embalagem cilíndrica reta tem bases de raio $$3\,\mathrm{cm}$$, separadas por $$12\,\mathrm{cm}$$. Identifique altura, eixo e geratriz.

**Resolução:**

- **Passo 1:** A distância perpendicular entre as bases fornece a altura.

$$h=12\,\mathrm{cm}$$

- **Passo 2:** No cilindro reto, eixo e geratrizes são perpendiculares às bases.

$$g=h$$

$$g=12\,\mathrm{cm}$$

**Resposta:** a altura e cada geratriz medem $$12\,\mathrm{cm}$$; o eixo liga os centros e também é perpendicular às bases.

> ⚠️ **Atenção:**
>
> Geratriz fica na superfície lateral; altura é a menor distância entre os planos das bases.

---

## 2. Classificação dos cilindros

Inclinar um cilindro altera a geratriz, mas não a distância perpendicular entre os planos de suas bases.

### 2.1 Reto e oblíquo

| Tipo | Eixo em relação às bases | Relação |
|---|---|---|
| Reto | perpendicular | $$g=h$$ |
| Oblíquo | inclinado | $$g>h$$ |

<!-- tikz:inicio fig-04-cilindro-reto-e-obliquo -->
![Comparação entre cilindro reto, em que geratriz e altura coincidem, e cilindro oblíquo, em que a geratriz é maior](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-04-cilindro-reto-e-obliquo.png)
<!-- tikz:fim fig-04-cilindro-reto-e-obliquo -->

Em ambos, as bases continuam congruentes e paralelas. A altura é sempre perpendicular aos planos, mesmo que não coincida com uma geratriz.

### 2.2 Cilindro equilátero

O **cilindro equilátero** é reto e tem altura igual ao diâmetro:

$$h=2r$$

<!-- tikz:inicio fig-05-cilindro-equilatero -->
![Cilindro equilátero cortado pelo eixo, formando uma secção meridiana quadrada com altura h igual a dois raios](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-05-cilindro-equilatero.png)
<!-- tikz:fim fig-05-cilindro-equilatero -->

Sua secção pelo eixo será um quadrado, pois altura e diâmetro têm a mesma medida.

**Recipiente equilátero**

Um recipiente cilíndrico reto tem altura de $$14\,\mathrm{cm}$$ e é equilátero. Determine o raio e a geratriz.

**Resolução:**

- **Passo 1:** Usar a relação do cilindro equilátero.

$$14=2r$$

- **Passo 2:** Isolar o raio.

$$r=7\,\mathrm{cm}$$

- **Passo 3:** Usar a condição de cilindro reto.

$$g=h$$

$$g=14\,\mathrm{cm}$$

**Resposta:** o recipiente tem raio de $$7\,\mathrm{cm}$$ e geratriz de $$14\,\mathrm{cm}$$.

> 🔢 **Padrão:**
>
> Todo cilindro equilátero é reto, mas nem todo cilindro reto é equilátero.

---

## 3. Área lateral

Ao cortar verticalmente o rótulo de uma lata e abri-lo, a superfície lateral transforma-se em um retângulo.

### 3.1 O desenrolamento

No cilindro reto, o retângulo obtido tem:

- base igual ao comprimento da circunferência, $$2\pi r$$;
- altura igual à geratriz, que coincide com $$h$$.

<!-- tikz:inicio fig-06-desenrolamento-da-area-lateral -->
![Superfície lateral de um cilindro sendo aberta em um retângulo de comprimento dois pi r e altura h](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-06-desenrolamento-da-area-lateral.png)
<!-- tikz:fim fig-06-desenrolamento-da-area-lateral -->

Por isso, sua área lateral é:

$$A_L=2\pi rh$$

O fator $$2\pi r$$ mede comprimento; já $$\pi r^{2}$$ mede a área de uma base.

### 3.2 Material do rótulo

**Rótulo de uma lata**

Uma lata cilíndrica reta tem raio $$3{,}3\,\mathrm{cm}$$ e altura $$12{,}2\,\mathrm{cm}$$. Calcule a área do rótulo usando $$\pi\approx3{,}14$$.

**Resolução:**

- **Passo 1:** Aplicar a fórmula da área lateral.

$$A_L=2\pi rh$$

- **Passo 2:** Substituir as medidas.

$$A_L\approx2\cdot3{,}14\cdot3{,}3\cdot12{,}2$$

- **Passo 3:** Calcular o produto.

$$A_L\approx252{,}83\,\mathrm{cm^2}$$

**Resposta:** o rótulo ocupa aproximadamente $$252{,}83\,\mathrm{cm^2}$$, desconsiderando a sobreposição necessária para colagem.

> ⚠️ **Atenção:**
>
> O comprimento $$2\pi r$$ contorna a base; ele não é a área $$\pi r^{2}$$ do círculo.

---

## 4. Área total

Uma lata fechada usa material na superfície lateral e também nos dois círculos das extremidades.

### 4.1 Somar as superfícies

Cada base tem área:

$$A_B=\pi r^{2}$$

Somando a área lateral e duas bases:

$$A_T=A_L+2A_B$$

<!-- tikz:inicio fig-07-planificacao-da-area-total -->
![Planificação de um cilindro fechado com o retângulo lateral e duas bases circulares de raio r separados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-07-planificacao-da-area-total.png)
<!-- tikz:fim fig-07-planificacao-da-area-total -->

$$A_T=2\pi rh+2\pi r^{2}$$

Fatorando o termo comum:

$$A_T=2\pi r(h+r)$$

No cilindro equilátero, $$h=2r$$, então $$A_L=4\pi r^{2}$$ e $$A_T=6\pi r^{2}$$.

### 4.2 Embalagem fechada

**Área de uma embalagem**

Um cilindro fechado tem raio $$3\,\mathrm{cm}$$ e altura $$8\,\mathrm{cm}$$. Determine a área total.

**Resolução:**

- **Passo 1:** Substituir na forma fatorada.

$$A_T=2\pi\cdot3\cdot(8+3)$$

- **Passo 2:** Simplificar.

$$A_T=66\pi\,\mathrm{cm^2}$$

- **Passo 3:** Aproximar com $$\pi\approx3{,}14$$.

$$A_T\approx207{,}24\,\mathrm{cm^2}$$

**Resposta:** a embalagem exige $$66\pi\,\mathrm{cm^2}$$, ou aproximadamente $$207{,}24\,\mathrm{cm^2}$$, sem considerar perdas e emendas.

> 🔢 **Padrão:**
>
> Cilindro fechado possui duas bases; um recipiente aberto perde uma delas no cálculo do material.

---

## 5. Volume

Dois reservatórios com a mesma área de base e a mesma altura armazenam o mesmo volume, mesmo que um seja inclinado.

### 5.1 Base vezes altura

O Princípio de Cavalieri compara secções paralelas de sólidos com a mesma altura. Como o cilindro tem secções transversais congruentes à base:

$$V=A_Bh$$

$$V=\pi r^{2}h$$

<!-- tikz:inicio fig-08-cavalieri-e-volume -->
![Cilindros reto e oblíquo com a mesma área de base, a mesma altura e secções paralelas correspondentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-08-cavalieri-e-volume.png)
<!-- tikz:fim fig-08-cavalieri-e-volume -->

A fórmula vale para cilindros retos e oblíquos com mesma base e mesma altura.

Para conservar o volume, o produto $$r^{2}h$$ deve permanecer constante: aumentar o raio exige reduzir a altura. A escolha de uma lata também considera material, resistência e armazenamento.

### 5.2 Capacidade de um reservatório

**Caixa-d'água cilíndrica**

Uma caixa cilíndrica tem raio $$0{,}5\,\mathrm{m}$$ e altura $$1{,}5\,\mathrm{m}$$. Calcule a capacidade usando $$\pi\approx3{,}14$$ e $$1\,\mathrm{m^3}=1000\,\mathrm{L}$$.

**Resolução:**

- **Passo 1:** Calcular o volume em metros cúbicos.

$$V\approx3{,}14\cdot(0{,}5)^{2}\cdot1{,}5$$

$$V\approx1{,}1775\,\mathrm{m^3}$$

- **Passo 2:** Converter para litros.

$$1{,}1775\cdot1000=1177{,}5\,\mathrm{L}$$

- **Passo 3:** Comparar com um consumo hipotético de $$150\,\mathrm{L}$$ por pessoa ao dia.

$$\frac{1177{,}5}{150}\approx7{,}85\,\mathrm{dias}$$

**Resposta:** a capacidade geométrica é aproximadamente $$1177{,}5\,\mathrm{L}$$, equivalente a cerca de $$7{,}85$$ dias nesse consumo hipotético; a capacidade útil pode ser menor.

> ⚠️ **Atenção:**
>
> O volume usa a altura perpendicular entre as bases, não a geratriz inclinada.

---

## 6. Secções do cilindro

Cortar um cilindro por planos diferentes produz figuras planas que revelam suas dimensões.

### 6.1 Secção meridiana

No cilindro reto, o plano que contém o eixo produz uma **secção meridiana** retangular, com lados:

$$2r$$

$$h$$

<!-- tikz:inicio fig-09-seccao-meridiana -->
![Plano que contém o eixo de um cilindro reto produzindo uma secção meridiana retangular de lados dois r e h](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-09-seccao-meridiana.png)
<!-- tikz:fim fig-09-seccao-meridiana -->

No cilindro equilátero, $$h=2r$$, e esse retângulo torna-se quadrado.

### 6.2 Secção transversal

Um plano paralelo às bases produz um círculo congruente a elas, em qualquer altura. A secção preserva o raio $$r$$ e permite ler a área da base.

<!-- tikz:inicio fig-10-seccao-transversal -->
![Plano paralelo às bases cortando o cilindro e produzindo uma secção circular de raio r](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/2serie/cilindros/fig-10-seccao-transversal.png)
<!-- tikz:fim fig-10-seccao-transversal -->

**Dimensões pela secção**

A secção meridiana de um cilindro reto é um retângulo de $$10\,\mathrm{cm}$$ por $$12\,\mathrm{cm}$$. O lado de $$10\,\mathrm{cm}$$ é o diâmetro da base.

**Resolução:**

- **Passo 1:** Obter o raio pelo diâmetro.

$$r=\frac{10}{2}$$

$$r=5\,\mathrm{cm}$$

- **Passo 2:** Identificar a altura pelo outro lado.

$$h=12\,\mathrm{cm}$$

- **Passo 3:** Comparar altura e diâmetro.

$$12\,\mathrm{cm}\neq10\,\mathrm{cm}$$

**Resposta:** o cilindro tem raio $$5\,\mathrm{cm}$$ e altura $$12\,\mathrm{cm}$$; não é equilátero porque sua secção meridiana não é quadrada.

> 🔢 **Padrão:**
>
> Secção transversal paralela às bases conserva o círculo; secção meridiana revela diâmetro e altura.
