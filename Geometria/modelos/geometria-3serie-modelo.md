# Capítulo 1 — Hipérbole

> Antes do GPS, navios cruzaram o Atlântico por 70 anos usando o sistema LORAN — puramente hipérboles. Como uma curva de “duas folhas separadas” substituía 24 satélites?

---

## 1. Definição e elementos

Duas torres transmissoras podem definir uma curva pelos pontos cuja diferença de distâncias até elas permanece constante.

### 1.1 Lugar geométrico

A **hipérbole** é o lugar geométrico dos pontos $$P$$ para os quais a diferença em módulo das distâncias a dois focos é constante:

$$|PF_1-PF_2|=2a$$

Os focos são $$F_1$$ e $$F_2$$, separados por $$2c$$, com $$2a<2c$$. Diferentemente da elipse, que usa soma, a hipérbole tem duas folhas abertas e usa diferença.

### 1.2 Eixos e relação fundamental

Seus elementos são:

- centro — ponto médio dos focos;
- eixo real ou transverso — mede $$2a$$ e contém os dois vértices;
- eixo imaginário ou conjugado — mede $$2b$$;
- distância focal — mede $$2c$$.

A relação fundamental é:

$$c^{2}=a^{2}+b^{2}$$

**Elementos de uma hipérbole**

Uma hipérbole tem $$a=3$$ e $$c=5$$. Determine $$b$$ e as medidas dos eixos.

**Resolução:**

- **Passo 1:** Substituir na relação fundamental.

$$5^{2}=3^{2}+b^{2}$$

- **Passo 2:** Isolar $$b^{2}$$.

$$b^{2}=16$$

$$b=4$$

- **Passo 3:** Dobrar os parâmetros.

$$2a=6$$

$$2b=8$$

$$2c=10$$

**Resposta:** $$b=4$$; os eixos real e imaginário medem 6 e 8 unidades, e a distância focal mede 10 unidades.

**Ibrahim ibn Sinan (909–946)** desenvolveu construções de tangentes a cônicas em tratados escritos por volta de 940, combinando rigor geométrico e clareza demonstrativa.

> ⚠️ **Atenção:**
>
> Na hipérbole, $$c^{2}=a^{2}+b^{2}$$; na elipse, a posição desses parâmetros na relação é diferente.

---

## 2. Equações reduzidas e assíntotas

O termo positivo da equação indica a direção em que as duas folhas da hipérbole se abrem.

### 2.1 Orientação do eixo real

Com centro na origem, as formas reduzidas são:

| Eixo real | Equação | Assíntotas |
|---|---|---|
| horizontal | $$\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$$ | $$y=\pm\frac{b}{a}x$$ |
| vertical | $$\frac{y^{2}}{a^{2}}-\frac{x^{2}}{b^{2}}=1$$ | $$y=\pm\frac{a}{b}x$$ |

O denominador do termo positivo contém $$a^{2}$$ e determina os vértices. O outro contém $$b^{2}$$.

### 2.2 Retângulo fundamental

As retas que passam pelo centro e pelas diagonais do retângulo de lados $$2a$$ e $$2b$$ são assíntotas: as folhas se aproximam delas sem tocá-las.

**Leitura de uma equação**

Considere:

$$\frac{x^{2}}{9}-\frac{y^{2}}{4}=1$$

**Resolução:**

- **Passo 1:** Identificar os parâmetros.

$$a=3$$

$$b=2$$

- **Passo 2:** Calcular a distância focal.

$$c=\sqrt{3^{2}+2^{2}}$$

$$c=\sqrt{13}$$

- **Passo 3:** Escrever as assíntotas.

$$y=\pm\frac{2}{3}x$$

**Resposta:** a hipérbole abre horizontalmente, tem vértices $$(\pm3,0)$$, focos $$(\pm\sqrt{13},0)$$ e assíntotas $$y=\pm2x/3$$.

> 🔢 **Padrão:**
>
> Na equação reduzida, a variável do termo positivo está alinhada ao eixo real.

---

## 3. Excentricidade e hipérbole equilátera

A excentricidade informa quanto as folhas se afastam da forma-limite determinada por suas assíntotas.

### 3.1 Excentricidade

Na hipérbole:

$$e=\frac{c}{a}>1$$

Quanto mais próximo $$e$$ está de 1, mais estreita é a abertura; valores maiores indicam folhas mais abertas. Na elipse, em contraste, $$0<e<1$$.

### 3.2 Caso equilátero

A **hipérbole equilátera** satisfaz $$a=b$$. Com centro na origem e eixo real horizontal, suas propriedades são:

- assíntotas perpendiculares;
- equações das assíntotas $$y=\pm x$$ no caso horizontal;
- excentricidade $$e=\sqrt{2}$$.

**Hipérbole com parâmetros iguais**

Considere $$a=b=4$$. Determine $$c$$ e $$e$$.

**Resolução:**

- **Passo 1:** Aplicar a relação fundamental.

$$c^{2}=4^{2}+4^{2}$$

$$c^{2}=32$$

$$c=4\sqrt{2}$$

- **Passo 2:** Calcular a excentricidade.

$$e=\frac{4\sqrt{2}}{4}$$

$$e=\sqrt{2}$$

**Resposta:** a distância do centro a cada foco é $$4\sqrt{2}$$ unidades e a excentricidade é $$\sqrt{2}$$; trata-se de hipérbole equilátera.

| Elipse | Hipérbole |
|---|---|
| soma de distâncias | diferença em módulo |
| curva fechada | duas folhas abertas |
| quatro vértices | dois vértices |
| $$0<e<1$$ | $$e>1$$ |

> ⚠️ **Atenção:**
>
> “Equilátera” não significa lados iguais: significa parâmetros $$a$$ e $$b$$ iguais e assíntotas perpendiculares.

---

## 4. Aplicações da hipérbole

Sistemas de navegação hiperbólica localizam um receptor comparando o tempo de chegada de sinais enviados por estações conhecidas.

### 4.1 Diferença de tempo e distância

Se dois sinais viajam com velocidade $$v_s$$ e chegam separados por $$\Delta t$$, a diferença entre as distâncias percorridas é:

$$\Delta d=v_s\Delta t$$

Manter $$\Delta d$$ constante define uma hipérbole com as estações nos focos. Uma segunda dupla de estações produz outra hipérbole; a interseção indica a posição.

**Diferença registrada pelo receptor**

Considere $$v_s\approx3\cdot10^{8}\,\mathrm{m/s}$$ e $$\Delta t=20\,\mu\mathrm{s}$$.

**Resolução:**

- **Passo 1:** Converter o intervalo para segundos.

$$20\,\mu\mathrm{s}=20\cdot10^{-6}\,\mathrm{s}$$

- **Passo 2:** Calcular a diferença de distâncias.

$$\Delta d=3\cdot10^{8}\cdot20\cdot10^{-6}$$

$$\Delta d=6000\,\mathrm{m}$$

$$\Delta d=6\,\mathrm{km}$$

**Resposta:** o receptor está num ramo da hipérbole cujos pontos diferem em $$6\,\mathrm{km}$$ nas distâncias às duas estações.

### 4.2 Outros contextos

| Contexto | Papel da hipérbole |
|---|---|
| LORAN e DECCA | localizar por diferenças de tempo |
| cometa C/1980 E1, $$e\approx1{,}05$$ | órbita hiperbólica, não periódica |
| cometa Halley, $$e\approx0{,}967$$ | contraste: órbita elíptica e periódica |
| radar meteorológico | localizar fontes por diferenças de chegada |

> 🔢 **Padrão:**
>
> Uma diferença constante define uma hipérbole; duas hipérboles independentes determinam uma posição possível.
