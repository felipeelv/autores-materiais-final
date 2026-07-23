# Capítulo 1 — Circunferência

> Dois torcedores em pontos diferentes da arquibancada do Maracanã veem o gol com o MESMO ângulo de visão — desde que estejam no mesmo arco. Por que a circunferência trata todos os observadores com a mesma medida?

---

## 1. Definição, elementos e posição de ponto

O contorno de uma pista circular é uma linha; a superfície delimitada por ele é uma região.

### 1.1 Circunferência e círculo

**Circunferência** é o conjunto dos pontos do plano à distância fixa $$r$$ de um centro $$O$$; **círculo** é a região interna com sua borda.

Seus elementos incluem:

- raio, diâmetro e corda;
- arco e flecha, segmento entre o ponto médio da corda e o arco;
- centro, que determina a equidistância.

<!-- tikz:inicio fig-01-elementos-da-circunferencia -->
![Circunferência com raio, diâmetro, corda, arco e flecha identificados](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-01-elementos-da-circunferencia.png)
<!-- tikz:fim fig-01-elementos-da-circunferencia -->

### 1.2 Critério algébrico

A distância $$\overline{OP}$$ classifica um ponto $$P$$:

| Condição | Posição |
|---|---|
| $$\overline{OP}<r$$ | interna |
| $$\overline{OP}=r$$ | na circunferência |
| $$\overline{OP}>r$$ | externa |

<!-- tikz:inicio fig-02-posicoes-de-um-ponto -->
![Comparação visual das posições interna, pertencente e externa de um ponto em relação à circunferência](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-02-posicoes-de-um-ponto.png)
<!-- tikz:fim fig-02-posicoes-de-um-ponto -->

**Sensor próximo à pista**

Uma pista tem centro $$O$$ e raio $$12\,\mathrm{m}$$. Os sensores $$P$$, $$Q$$ e $$R$$ estão, respectivamente, a $$9\,\mathrm{m}$$, $$12\,\mathrm{m}$$ e $$15\,\mathrm{m}$$ do centro.

**Resolução:**

- **Passo 1:** Comparar cada distância com o raio.

$$9\,\mathrm{m}<12\,\mathrm{m}$$

$$12\,\mathrm{m}=12\,\mathrm{m}$$

$$15\,\mathrm{m}>12\,\mathrm{m}$$

**Resposta:** $$P$$ é interno, $$Q$$ pertence à circunferência e $$R$$ é externo; a classificação depende apenas da distância ao centro.

> ⚠️ **Atenção:**
>
> Circunferência é uma linha, enquanto círculo é uma região bidimensional.

---

## 2. Posições relativas

Uma rua pode atravessar, tangenciar ou evitar uma praça circular conforme sua distância ao centro.

### 2.1 Reta e circunferência

Para uma reta $$s$$, compara-se a distância perpendicular $$d(O,s)$$ com o raio:

| Condição | Posição | Interseções |
|---|---|---:|
| $$d(O,s)>r$$ | externa | 0 |
| $$d(O,s)=r$$ | tangente | 1 |
| $$d(O,s)<r$$ | secante | 2 |

<!-- tikz:inicio fig-03-posicoes-de-uma-reta -->
![Comparação entre reta externa sem interseções, tangente com uma interseção e secante com duas interseções](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-03-posicoes-de-uma-reta.png)
<!-- tikz:fim fig-03-posicoes-de-uma-reta -->

No ponto de tangência $$T$$, o raio é perpendicular à reta:

$$\overline{OT}\perp s$$

### 2.2 Duas circunferências

Se $$D=\overline{O_1O_2}$$, compara-se a distância entre centros com a soma e a diferença dos raios:

| Condição | Posição |
|---|---|
| $$D>r_1+r_2$$ | externas |
| $$D=r_1+r_2$$ | tangentes externas |
| $$|r_1-r_2|<D<r_1+r_2$$ | secantes |

<!-- tikz:inicio fig-04-circunferencias-externas -->
![Comparação entre duas circunferências externas, tangentes externas e secantes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-04-circunferencias-externas.png)
<!-- tikz:fim fig-04-circunferencias-externas -->

| Condição | Posição |
|---|---|
| $$D=|r_1-r_2|$$ | tangentes internas |
| $$0<D<|r_1-r_2|$$ | internas |
| $$D=0$$ | concêntricas |

<!-- tikz:inicio fig-05-circunferencias-internas -->
![Comparação entre duas circunferências tangentes internas, internas sem contato e concêntricas](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-05-circunferencias-internas.png)
<!-- tikz:fim fig-05-circunferencias-internas -->

**Rua tangente à praça**

Uma praça tem raio $$20\,\mathrm{m}$$ e a distância perpendicular do centro à rua é $$20\,\mathrm{m}$$.

**Resolução:**

- **Passo 1:** Comparar distância e raio.

$$d(O,s)=r$$

- **Passo 2:** Aplicar a propriedade do ponto de contato.

$$\overline{OT}\perp s$$

**Resposta:** a rua é tangente à praça em um único ponto $$T$$, e o raio $$OT$$ forma $$90^{\circ}$$ com a rua.

> 🔢 **Padrão:**
>
> Toda tangente é perpendicular ao raio traçado até o ponto de tangência.

---

## 3. Ângulo central e ângulo inscrito

Um mesmo arco pode ser observado a partir do centro ou de um ponto da própria circunferência.

### 3.1 Dois vértices possíveis

O **ângulo central** tem vértice no centro e lados formados por raios; sua medida coincide com a do arco abrangido.

O **ângulo inscrito** tem vértice na circunferência e lados formados por cordas. Para o mesmo arco $$AB$$:

$$\angle AOB=2\angle APB$$

<!-- tikz:inicio fig-06-angulo-central-e-inscrito -->
![Mesmo arco AB determina um ângulo central de medida dois alfa e um ângulo inscrito de medida alfa](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-06-angulo-central-e-inscrito.png)
<!-- tikz:fim fig-06-angulo-central-e-inscrito -->

Logo, o inscrito mede metade do central.

### 3.2 Leitura pelo arco

**Visão de uma corda**

Os pontos $$A$$ e $$B$$ limitam um arco de $$120^{\circ}$$. O centro é $$O$$ e $$P$$ está no arco oposto a $$AB$$. Determine $$\angle AOB$$ e $$\angle APB$$.

**Resolução:**

- **Passo 1:** Igualar ângulo central e arco.

$$\angle AOB=120^{\circ}$$

- **Passo 2:** Calcular a metade para o ângulo inscrito.

$$\angle APB=\frac{120^{\circ}}{2}$$

$$\angle APB=60^{\circ}$$

**Resposta:** o ângulo central mede $$120^{\circ}$$ e o inscrito mede $$60^{\circ}$$.

Todos os vértices situados no mesmo arco oposto enxergam a corda $$AB$$ sob esse mesmo ângulo inscrito.

> 🔢 **Padrão:**
>
> Para o mesmo arco, o ângulo central mede o dobro do ângulo inscrito.

---

## 4. Relação 2:1 e ângulo de segmento

Na arquibancada circular, lugares do mesmo arco mantêm o mesmo ângulo de visão de uma abertura fixa.

### 4.1 Por que surge a metade

Ligando o centro $$O$$ ao vértice inscrito $$P$$, formam-se triângulos isósceles, pois todos os raios são congruentes. Quando $$O$$ fica dentro de $$\angle APB$$, tome $$x=\angle APO$$ e $$y=\angle OPB$$. Então:

$$\angle AOP=180^{\circ}-2x$$

$$\angle POB=180^{\circ}-2y$$

O ângulo central menor completa a volta e mede $$2(x+y)$$, enquanto $$\angle APB=x+y$$. Assim:

$$\angle APB=\frac{\angle AOB}{2}$$

Quando o centro fica sobre ou fora do ângulo, a mesma relação dos triângulos isósceles é aplicada por soma ou diferença.

Duas consequências são diretas:

- ângulos inscritos no mesmo arco são congruentes;
- o ângulo inscrito numa semicircunferência mede $$90^{\circ}$$.

### 4.2 Corda e tangente

O **ângulo de segmento** tem vértice na circunferência e lados formados por uma corda e uma tangente. Ele também mede metade do arco correspondente.

<!-- tikz:inicio fig-07-angulo-de-segmento -->
![Ângulo de segmento formado por uma tangente e uma corda com o arco correspondente destacado](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-07-angulo-de-segmento.png)
<!-- tikz:fim fig-07-angulo-de-segmento -->

**Ângulo de visão no estádio**

Uma abertura determina um arco de $$80^{\circ}$$. Calcule o ângulo visto por um observador situado no arco oposto.

**Resolução:**

- **Passo 1:** Aplicar a relação do ângulo inscrito.

$$\alpha=\frac{80^{\circ}}{2}$$

$$\alpha=40^{\circ}$$

**Resposta:** o observador vê a abertura sob $$40^{\circ}$$; qualquer lugar no mesmo arco oposto produz a mesma medida.

> ⚠️ **Atenção:**
>
> A relação de metade exige que os ângulos central e inscrito abranjam exatamente o mesmo arco.

---

## 5. Ângulos excêntricos

Duas cordas podem cruzar-se dentro da circunferência, enquanto secantes e tangentes também podem encontrar-se fora dela.

### 5.1 Vértice interior

No **ângulo excêntrico interior**, duas cordas se cruzam dentro da circunferência. A medida é a semissoma dos arcos opostos:

$$\gamma_{int}=\frac{\alpha_1+\alpha_2}{2}$$

<!-- tikz:inicio fig-08-angulo-excentrico-interior -->
![Duas cordas cruzam-se no interior da circunferência e determinam um ângulo e dois arcos opostos](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-08-angulo-excentrico-interior.png)
<!-- tikz:fim fig-08-angulo-excentrico-interior -->

### 5.2 Vértice exterior

No **ângulo excêntrico exterior**, duas secantes, duas tangentes ou uma de cada encontram-se fora. A medida é a semidiferença entre o arco maior e o menor:

$$\gamma_{ext}=\frac{|\alpha_1-\alpha_2|}{2}$$

<!-- tikz:inicio fig-09-angulo-excentrico-exterior -->
![Duas secantes partem de um ponto exterior e determinam um ângulo entre os arcos maior e menor](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-09-angulo-excentrico-exterior.png)
<!-- tikz:fim fig-09-angulo-excentrico-exterior -->

As cinco relações podem ser comparadas assim:

| Ângulo | Relação com arco |
|---|---|
| central | arco inteiro |
| inscrito ou de segmento | metade de um arco |
| excêntrico interior | semissoma |
| excêntrico exterior | semidiferença |

**Cordas cruzadas**

Duas cordas determinam arcos opostos de $$100^{\circ}$$ e $$60^{\circ}$$. Calcule o ângulo interior.

**Resolução:**

- **Passo 1:** Somar os arcos e dividir por dois.

$$\gamma_{int}=\frac{100^{\circ}+60^{\circ}}{2}$$

$$\gamma_{int}=80^{\circ}$$

**Resposta:** o ângulo excêntrico interior mede $$80^{\circ}$$.

> ⚠️ **Atenção:**
>
> Vértice interior pede soma dos arcos; vértice exterior pede diferença em módulo.

---

## 6. Potência de ponto

De um ponto externo, diferentes secantes produzem o mesmo produto entre as distâncias até suas interseções com a circunferência.

### 6.1 Um invariante

Se $$d=\overline{OP}$$ e o raio é $$r$$, a **potência de $$P$$** é:

$$\mathrm{Pot}(P)=d^{2}-r^{2}$$

O sinal localiza o ponto: positivo fora, zero na circunferência e negativo dentro.

As relações métricas são:

| Configuração | Relação |
|---|---|
| corda × corda | $$PA\cdot PB=PC\cdot PD$$ |

<!-- tikz:inicio fig-10-potencia-entre-cordas -->
![Duas cordas AB e CD cruzam-se no ponto interior P, destacando os quatro segmentos da relação de potência](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-10-potencia-entre-cordas.png)
<!-- tikz:fim fig-10-potencia-entre-cordas -->

| Configuração | Relação |
|---|---|
| secante × secante | $$PA\cdot PB=PC\cdot PD$$ |

<!-- tikz:inicio fig-11-potencia-entre-secantes -->
![Duas secantes PAB e PCD partem do mesmo ponto exterior P e destacam as distâncias da relação de potência](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-11-potencia-entre-secantes.png)
<!-- tikz:fim fig-11-potencia-entre-secantes -->

| Configuração | Relação |
|---|---|
| secante × tangente | $$PA\cdot PB=PT^{2}$$ |

No caso de duas secantes, os ângulos inscritos formados pelos mesmos arcos tornam dois triângulos semelhantes; a proporção entre lados correspondentes gera a igualdade dos produtos.

### 6.2 Produto constante

<!-- tikz:inicio fig-12-potencia-secante-tangente -->
![Do ponto exterior P partem uma secante PAB e uma tangente PT, com o raio perpendicular no ponto T](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/1serie/circunferencia/fig-12-potencia-secante-tangente.png)
<!-- tikz:fim fig-12-potencia-secante-tangente -->

**Tangente a partir de um ponto**

De $$P$$ sai uma secante que encontra a circunferência em $$A$$ e $$B$$, com $$PA=4\,\mathrm{cm}$$ e $$PB=9\,\mathrm{cm}$$. Uma tangente toca a curva em $$T$$.

**Resolução:**

- **Passo 1:** Igualar os produtos.

$$PA\cdot PB=PT^{2}$$

- **Passo 2:** Substituir as medidas.

$$4\cdot9=PT^{2}$$

- **Passo 3:** Extrair a raiz positiva.

$$PT=6\,\mathrm{cm}$$

**Resposta:** o segmento tangente mede $$6\,\mathrm{cm}$$; outra reta por $$P$$ preservaria a mesma potência.

**August Ferdinand Möbius (1790–1868)** apresentou a forma moderna da potência de ponto em *Der barycentrische Calcül* (1827), unificando cordas, secantes e tangentes.

> 🔢 **Padrão:**
>
> A potência depende do ponto e da circunferência, não da reta escolhida para medi-la.
