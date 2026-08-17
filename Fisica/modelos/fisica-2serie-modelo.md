# Capítulo 1 — Reflexão e espelhos

> Por que o “1234” do carro de polícia parece “4321” no retrovisor? Por que o farol projeta luz a 100 m à frente, o espelho de maquiagem amplia o rosto e o retrovisor convexo reduz tudo — e o Hubble usa espelhos curvos gigantes em vez de lentes?

---

## 1. Fundamentos da óptica geométrica

Sombras nítidas e feixes estreitos permitem representar a propagação da luz por linhas orientadas.

### 1.1 O modelo de raios

Na **óptica geométrica**, cada raio indica a direção e o sentido da propagação luminosa. O modelo vale quando o comprimento de onda é muito menor que os objetos encontrados:

$$\lambda \ll D$$

Nessa condição, $$\lambda$$ é o comprimento de onda e $$D$$, a dimensão do objeto.

Três princípios organizam o modelo:

- **propagação retilínea** — em meio homogêneo, a luz segue em linha reta;
- **independência** — raios que se cruzam não alteram seus caminhos;
- **reversibilidade** — o percurso pode ser feito no sentido inverso.

### 1.2 Reflexão e imagem

Superfícies produzem dois tipos de reflexão:

| Reflexão | Superfície | Resultado |
|---|---|---|
| Regular | lisa | raios ordenados; forma imagem |
| Difusa | irregular | raios espalhados; permite ver objetos |

Uma imagem é **real** quando os raios convergem e **virtual** quando apenas seus prolongamentos convergem.

Entre 1011 e 1021, **Ibn al-Haytham (965–1040)** escreveu o *Livro da Óptica* e demonstrou que a luz vem dos objetos para os olhos, combinando hipótese, experimento e verificação.

> 💡 **Você sabia?**
>
> O raio é um modelo da direção da luz, não um fio material atravessando o espaço.

---

## 2. Reflexão e espelhos planos

Um espelho plano devolve raios ordenados e produz uma imagem simétrica atrás de sua superfície.

### 2.1 Lei da reflexão

Os ângulos são medidos em relação à **normal**, reta perpendicular à superfície:

$$\hat{i} = \hat{r}$$

Nessa expressão, $$\hat{i}$$ é o ângulo de incidência e $$\hat{r}$$, o de reflexão, ambos medidos em grau.

Raio incidente, normal e raio refletido pertencem ao mesmo plano. Medir o ângulo a partir do espelho, e não da normal, é um erro clássico.

### 2.2 A imagem plana

A imagem no espelho plano possui quatro propriedades:

- virtual;
- direita;
- do mesmo tamanho do objeto;
- simétrica e à mesma distância do espelho.

A simetria em relação ao espelho faz a sequência escrita parecer invertida; por isso “1234” aparece como “4321”.

Dois espelhos formando um ângulo $$\theta$$ produzem, em casos simétricos:

$$N = \frac{360^{\circ}}{\theta} - 1$$

$$N$$ é o número de imagens e $$\theta$$ é o ângulo entre os espelhos.

O campo visual depende do tamanho do espelho e das posições do observador e do objeto.

📝 **Exemplo:**
Para $$\theta=90^{\circ}$$:

$$N = \frac{360^{\circ}}{90^{\circ}} - 1$$

$$N = 3$$

> ⚡ **Física no Dia a Dia:**
>
> Espelhos planos inclinados formam os padrões repetidos de um caleidoscópio.

---

## 3. Espelhos esféricos

Uma colher aproxima ou inverte sua imagem conforme o lado refletor e a distância do rosto.

### 3.1 Côncavo × convexo

Os espelhos esféricos têm comportamentos opostos:

| Espelho | Ação sobre raios paralelos | Foco |
|---|---|---|
| Côncavo | converge | real, à frente |
| Convexo | diverge | virtual, atrás |

Seus elementos geométricos são vértice $$V$$, foco $$F$$, centro de curvatura $$C$$, raio $$R$$ e eixo principal.

### 3.2 Foco e limite do modelo

Para raios próximos ao eixo principal, vale a aproximação paraxial:

$$f = \frac{R}{2}$$

Nessa expressão, $$f$$ é a distância focal e $$R$$, o raio de curvatura.

Raios muito afastados do eixo não convergem exatamente no mesmo ponto. Esse desvio é a **aberração esférica**, limite do modelo ideal.

Espelhos parabólicos evitam esse problema para raios paralelos, concentrando-os em um único foco.

> 💡 **Você sabia?**
>
> No espelho convexo, o foco resulta do encontro dos prolongamentos, não dos raios refletidos.

---

## 4. Formação de imagens

Dois raios notáveis bastam para localizar graficamente a imagem de um ponto do objeto.

### 4.1 Raios notáveis

Três trajetórias simplificam a construção:

- raio paralelo ao eixo reflete passando pelo foco;
- raio que passa pelo foco reflete paralelo ao eixo;
- raio que atinge o vértice reflete simetricamente ao eixo.

A interseção dos raios refletidos forma imagem real; a interseção de seus prolongamentos forma imagem virtual.

### 4.2 Casos do espelho côncavo

A posição do objeto determina a imagem:

| Objeto | Imagem |
|---|---|
| Além de $$C$$ | real, invertida, reduzida |
| Em $$C$$ | real, invertida, igual |
| Entre $$C$$ e $$F$$ | real, invertida, ampliada |
| Em $$F$$ | imprópria, no infinito |
| Entre $$F$$ e $$V$$ | virtual, direita, ampliada |

No espelho convexo, há um único caso para objeto real: a imagem é sempre virtual, direita e reduzida.

> ⏸️ **Pare e Pense:**
>
> Se o desenho e as propriedades da tabela discordarem, qual construção precisa ser revista?

---

## 5. Equação de Gauss

O desenho prevê o tipo de imagem; a equação determina numericamente sua posição e seu tamanho.

### 5.1 Posição e aumento

Sob aproximação paraxial, a equação dos espelhos é:

$$\frac{1}{p} + \frac{1}{p'} = \frac{1}{f}$$

O aumento linear é:

$$A = \frac{i}{o} = -\frac{p'}{p}$$

Os símbolos e sinais distinguem posição e natureza da imagem:

- $$p$$ e $$p'$$ — posições do objeto e da imagem;
- $$f$$ — distância focal;
- $$i$$ e $$o$$ — alturas da imagem e do objeto;
- $$A$$ — aumento, sem unidade.

### 5.2 Convenção de sinais

Os sinais codificam a natureza da imagem:

| Grandeza | Positivo | Negativo |
|---|---|---|
| $$p'$$ | imagem real | imagem virtual |
| $$f$$ | espelho côncavo | espelho convexo |
| $$A$$ | imagem direita | imagem invertida |

Para um objeto real, adota-se $$p>0$$.

📝 **Exemplo:**
Espelho côncavo com $$f=0{,}10\,\mathrm{m}$$ e objeto em $$p=0{,}30\,\mathrm{m}$$.

Dados: $$f=0{,}10\,\mathrm{m}$$ e $$p=0{,}30\,\mathrm{m}$$

$$\frac{1}{p} + \frac{1}{p'} = \frac{1}{f}$$

$$\frac{1}{0{,}30} + \frac{1}{p'} = \frac{1}{0{,}10}$$

$$\frac{1}{f}=10\,\mathrm{m^{-1}}$$

$$\frac{1}{p}\approx3{,}33\,\mathrm{m^{-1}}$$

$$\frac{1}{p'} = 10 - 3{,}33$$

$$\frac{1}{p'} = 6{,}67\,\mathrm{m^{-1}}$$

$$p' = 0{,}15\,\mathrm{m}$$

$$A = -\frac{p'}{p}$$

$$A = -\frac{0{,}15}{0{,}30}$$

$$A = -0{,}5$$

A imagem é real, invertida e reduzida. **Carl Friedrich Gauss** formalizou esse tratamento algébrico.

> 📏 **Medidas Impressionantes:**
>
> Construção geométrica e cálculo algébrico devem indicar o mesmo tipo de imagem.

---

## 6. Aplicações dos espelhos curvos

Faróis, retrovisores e telescópios escolhem curvaturas diferentes conforme a imagem ou o feixe desejado.

### 6.1 Concentrar ou ampliar

Espelhos côncavos têm duas aplicações principais:

| Aplicação | Posição do objeto | Resultado |
|---|---|---|
| Farol parabólico | fonte no foco | feixe aproximadamente paralelo |
| Maquiagem | entre foco e vértice | imagem direita e ampliada |
| Telescópio | objeto muito distante | luz concentrada no foco |

O telescópio refletor usa um espelho grande para coletar mais luz. O Observatório do Pico dos Dias opera um instrumento com espelho de $$1{,}6\,\mathrm{m}$$.

### 6.2 Ampliar o campo visual

O espelho convexo produz imagens reduzidas, mas mostra uma região maior. Essa troca favorece retrovisores e espelhos de segurança.

Duas consequências aparecem no uso:

- mais objetos cabem no campo visual;
- as imagens parecem mais distantes do que realmente estão.

O retrovisor responde à pergunta inicial: reduz os veículos para ampliar a área observada. Já o Hubble usa espelhos curvos para concentrar luz fraca de objetos distantes.

> ⚡ **Física no Dia a Dia:**
>
> No retrovisor convexo, “menor” não significa “mais distante”; a curvatura altera a imagem percebida.
