# Capítulo 1 — Trigonometria no triângulo retângulo

> Por que toda rampa de acessibilidade no shopping tem o mesmo “jeito” de subida — e como medir a altura de um prédio sem subir nele, só com uma fita métrica e um aparelho de medir ângulos?

---

## 1. Razões trigonométricas

Rampas de comprimentos diferentes podem manter a mesma inclinação quando seus triângulos têm o mesmo ângulo agudo.

### 1.1 Os lados dependem do ângulo

No triângulo $$ABC$$, retângulo em $$A$$, tome $$\theta=\angle B$$. A hipotenusa é $$\overline{BC}$$; em relação a $$\theta$$:

- $$\overline{AC}$$ é o cateto oposto;
- $$\overline{AB}$$ é o cateto adjacente.

<!-- tikz:inicio fig-01-lados-em-relacao-ao-angulo -->
![Triângulo ABC retângulo em A com hipotenusa, cateto oposto e cateto adjacente identificados em relação ao ângulo teta em B](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/trigonometria-no-triangulo-retangulo/fig-01-lados-em-relacao-ao-angulo.png)
<!-- tikz:fim fig-01-lados-em-relacao-ao-angulo -->

Triângulos retângulos com o mesmo $$\theta$$ são semelhantes pelo caso AA. Portanto, as razões entre lados correspondentes não dependem do tamanho.

<!-- tikz:inicio fig-02-triangulos-semelhantes-mesmo-angulo -->
![Dois triângulos retângulos de tamanhos diferentes compartilham o mesmo ângulo teta e têm lados correspondentes proporcionais](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/trigonometria-no-triangulo-retangulo/fig-02-triangulos-semelhantes-mesmo-angulo.png)
<!-- tikz:fim fig-02-triangulos-semelhantes-mesmo-angulo -->

### 1.2 Seno, cosseno e tangente

As três razões são:

$$\mathrm{sen}\,\theta=\frac{\mathrm{cateto\ oposto}}{\mathrm{hipotenusa}}$$

$$\cos\theta=\frac{\mathrm{cateto\ adjacente}}{\mathrm{hipotenusa}}$$

$$\mathrm{tg}\,\theta=\frac{\mathrm{cateto\ oposto}}{\mathrm{cateto\ adjacente}}$$

Dividir seno por cosseno elimina a hipotenusa:

$$\mathrm{tg}\,\theta=\frac{\mathrm{sen}\,\theta}{\cos\theta}$$

**Triângulo de lados 3, 4 e 5**

No triângulo descrito, $$AB=3\,\mathrm{cm}$$, $$AC=4\,\mathrm{cm}$$ e $$BC=5\,\mathrm{cm}$$. Calcule as razões de $$\angle B$$.

**Resolução:**

- **Passo 1:** Calcular o seno.

$$\mathrm{sen}\,B=\frac{4}{5}$$

$$\mathrm{sen}\,B=0{,}8$$

- **Passo 2:** Calcular o cosseno.

$$\cos B=\frac{3}{5}$$

$$\cos B=0{,}6$$

- **Passo 3:** Calcular a tangente.

$$\mathrm{tg}\,B=\frac{4}{3}$$

**Resposta:** $$\mathrm{sen}\,B=0{,}8$$, $$\cos B=0{,}6$$ e $$\mathrm{tg}\,B=\frac{4}{3}$$; as razões não têm unidade.

**Hiparco de Niceia (c. 190–c. 120 a.C.)** construiu uma tabela de cordas associadas a ângulos e ficou conhecido como pai da trigonometria.

> ⚠️ **Atenção:**
>
> Ao trocar o ângulo de referência, os catetos oposto e adjacente também trocam de papel.

---

## 2. Valores notáveis

Os esquadros de desenho usam $$30^{\circ}$$, $$45^{\circ}$$ e $$60^{\circ}$$ porque suas razões trigonométricas têm valores exatos.

### 2.1 Dois triângulos de origem

Uma altura divide um triângulo equilátero de lado 2 em dois triângulos retângulos com hipotenusa 2, cateto 1 e outro cateto $$\sqrt{3}$$. Eles produzem os valores de $$30^{\circ}$$ e $$60^{\circ}$$.

<!-- tikz:inicio fig-03-triangulo-de-trinta-e-sessenta -->
![Triângulo equilátero de lado 2 dividido pela altura em triângulos retângulos com catetos 1 e raiz de 3 e ângulos de 30 e 60 graus](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/trigonometria-no-triangulo-retangulo/fig-03-triangulo-de-trinta-e-sessenta.png)
<!-- tikz:fim fig-03-triangulo-de-trinta-e-sessenta -->

Um triângulo retângulo isósceles com catetos 1 tem hipotenusa:

$$h^{2}=1^{2}+1^{2}$$

$$h=\sqrt{2}$$

<!-- tikz:inicio fig-04-triangulo-de-quarenta-e-cinco -->
![Triângulo retângulo isósceles com catetos iguais a 1, hipotenusa raiz de 2 e dois ângulos de 45 graus](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/trigonometria-no-triangulo-retangulo/fig-04-triangulo-de-quarenta-e-cinco.png)
<!-- tikz:fim fig-04-triangulo-de-quarenta-e-cinco -->

Esse triângulo produz os valores de $$45^{\circ}$$.

### 2.2 Tabela exata

| $$\theta$$ | $$\mathrm{sen}\,\theta$$ | $$\cos\theta$$ | $$\mathrm{tg}\,\theta$$ |
|---|---|---|---|
| $$30^{\circ}$$ | $$\frac{1}{2}$$ | $$\frac{\sqrt{3}}{2}$$ | $$\frac{\sqrt{3}}{3}$$ |
| $$45^{\circ}$$ | $$\frac{\sqrt{2}}{2}$$ | $$\frac{\sqrt{2}}{2}$$ | $$1$$ |
| $$60^{\circ}$$ | $$\frac{\sqrt{3}}{2}$$ | $$\frac{1}{2}$$ | $$\sqrt{3}$$ |

A tabela evidencia que $$\mathrm{sen}\,30^{\circ}=\cos60^{\circ}$$, enquanto no ângulo de $$45^{\circ}$$ seno e cosseno coincidem.

**Tangente de 30 graus**

Obtenha a tangente de $$30^{\circ}$$ pelo seno e pelo cosseno.

**Resolução:**

- **Passo 1:** Substituir os valores notáveis.

$$\mathrm{tg}\,30^{\circ}=\frac{1/2}{\sqrt{3}/2}$$

- **Passo 2:** Dividir as frações.

$$\mathrm{tg}\,30^{\circ}=\frac{1}{\sqrt{3}}$$

- **Passo 3:** Racionalizar o denominador.

$$\mathrm{tg}\,30^{\circ}=\frac{\sqrt{3}}{3}$$

**Resposta:** a tangente de $$30^{\circ}$$ é exatamente $$\sqrt{3}/3$$, como indica a tabela.

> 🔢 **Padrão:**
>
> Ângulos agudos complementares trocam entre si os valores de seno e cosseno.

---

## 3. Relação fundamental e resolução de triângulos

Um teodolito mede um ângulo a partir da horizontal; a trigonometria transforma essa leitura em uma altura inacessível.

### 3.1 Uma consequência de Pitágoras

Num triângulo retângulo de hipotenusa 1, os catetos medem $$\mathrm{sen}\,\theta$$ e $$\cos\theta$$. Aplicando Pitágoras:

$$\mathrm{sen}^{2}\theta+\cos^{2}\theta=1$$

Essa é a **relação fundamental**. Como os ângulos agudos são complementares, também vale:

$$\mathrm{sen}\,\theta=\cos(90^{\circ}-\theta)$$

### 3.2 Altura por ângulo de elevação

O **ângulo de elevação** parte da horizontal para cima; o de depressão parte da horizontal para baixo.

<!-- tikz:inicio fig-05-angulo-de-elevacao -->
![Teodolito observa o topo de um prédio pelo ângulo de elevação teta, formando triângulo retângulo com distância horizontal b e altura a](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/9ano/trigonometria-no-triangulo-retangulo/fig-05-angulo-de-elevacao.png)
<!-- tikz:fim fig-05-angulo-de-elevacao -->

Se $$a$$ é o cateto oposto, $$b$$ o adjacente e $$c$$ a hipotenusa, casos diretos usam:

$$a=c\cdot\mathrm{sen}\,\theta$$

$$b=c\cdot\cos\theta$$

$$a=b\cdot\mathrm{tg}\,\theta$$

**Altura de um prédio**

No triângulo $$TQP$$, retângulo em $$Q$$, $$T$$ é o teodolito, $$Q$$ a base e $$P$$ o topo. A distância horizontal $$TQ$$ mede $$50\,\mathrm{m}$$ e $$\angle T=30^{\circ}$$.

**Resolução:**

- **Passo 1:** Relacionar altura e distância pela tangente.

$$\mathrm{tg}\,30^{\circ}=\frac{h}{50}$$

- **Passo 2:** Isolar a altura.

$$h=50\cdot\frac{\sqrt{3}}{3}$$

- **Passo 3:** Aproximar com $$\sqrt{3}\approx1{,}732$$.

$$h\approx\frac{50\cdot1{,}732}{3}$$

$$h\approx28{,}9\,\mathrm{m}$$

**Resposta:** o prédio tem aproximadamente $$28{,}9\,\mathrm{m}$$ de altura acima do nível do teodolito.

> ⚠️ **Atenção:**
>
> Ângulos de elevação e depressão são medidos a partir da horizontal, nunca da vertical.
