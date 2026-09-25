# Capítulo 1 — Transformações geométricas

> Na esteira rolante, tudo em você viaja igual; no espelho, sua mão direita vira esquerda; no relógio, o ponteiro gira sem mudar de tamanho. O que esses três movimentos preservam — e o que cada um muda?

---

## 1. Translação

Numa esteira rolante, todos os pontos de uma mala avançam juntos sem alterar distâncias ou ângulos.

### 1.1 Transformação e vetor

**Transformação geométrica** é uma regra que associa cada ponto da figura original a um ponto de sua imagem. Uma **isometria** preserva comprimentos, ângulos e áreas.

Na **translação**, cada ponto percorre o mesmo vetor $$\vec{v}$$, definido por:

- direção — inclinação do deslocamento;
- sentido — lado para o qual se desloca;
- módulo — comprimento percorrido.

Por isso, os segmentos que ligam pontos correspondentes são paralelos e congruentes.

<!-- tikz:inicio fig-01-translacao-por-vetor -->
![Triângulo ABC e sua imagem A linha B linha C linha ligados por deslocamentos paralelos iguais ao vetor v](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/transformacoes-geometricas/fig-01-translacao-por-vetor.png)
<!-- tikz:fim fig-01-translacao-por-vetor -->

### 1.2 Procedimento de construção

Para transladar o triângulo $$ABC$$ com régua e compasso:

- **Passo 1:** por cada vértice, traça-se uma paralela à direção de $$\vec{v}$$;
- **Passo 2:** marca-se o módulo no sentido indicado, obtendo $$A'$$, $$B'$$ e $$C'$$;
- **Passo 3:** ligam-se os três pontos na mesma ordem.

Num software de geometria dinâmica, cria-se o vetor e aplica-se a ferramenta de translação à figura.

**Placa deslocada**

Um triângulo tem lados de $$3\,\mathrm{cm}$$, $$4\,\mathrm{cm}$$ e $$5\,\mathrm{cm}$$ e é transladado $$6\,\mathrm{cm}$$ para a direita.

**Resolução:**

- **Passo 1:** Aplicar o mesmo vetor aos três vértices.
- **Passo 2:** Usar a conservação de comprimentos da isometria.

$$A'B'=3\,\mathrm{cm}$$

$$B'C'=4\,\mathrm{cm}$$

$$C'A'=5\,\mathrm{cm}$$

**Resposta:** a imagem muda de posição, mas continua com lados de $$3\,\mathrm{cm}$$, $$4\,\mathrm{cm}$$ e $$5\,\mathrm{cm}$$.

> 🔢 **Padrão:**
>
> Na translação, todos os pontos percorrem vetores de mesma direção, sentido e módulo.

---

## 2. Reflexão e rotação

O espelho inverte a orientação; o ponteiro do relógio gira e mantém a ordem dos pontos.

### 2.1 Reflexão pelo eixo

Na **reflexão** em relação à reta $$e$$, o eixo é a mediatriz de cada segmento $$\overline{PP'}$$. Portanto:

- $$P$$ e $$P'$$ ficam à mesma distância de $$e$$;
- $$\overline{PP'}\perp e$$;
- comprimentos e ângulos se conservam;
- a orientação da figura se inverte.

<!-- tikz:inicio fig-02-reflexao-por-eixo -->
![Triângulo e sua reflexão em lados opostos do eixo e, com segmentos perpendiculares e distâncias correspondentes iguais](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/transformacoes-geometricas/fig-02-reflexao-por-eixo.png)
<!-- tikz:fim fig-02-reflexao-por-eixo -->

Com compasso, arcos centrados em dois pontos do eixo localizam $$P'$$ no lado oposto.

### 2.2 Rotação pelo centro

Na **rotação**, cada ponto gira ao redor de um centro $$O$$ por um mesmo ângulo $$\alpha$$. As condições são:

$$OP'=OP$$

$$\angle POP'=\alpha$$

<!-- tikz:inicio fig-03-rotacao-por-centro -->
![Triângulo girado em torno do centro O por um ângulo alfa, preservando a distância entre O e pontos correspondentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/transformacoes-geometricas/fig-03-rotacao-por-centro.png)
<!-- tikz:fim fig-03-rotacao-por-centro -->

O sentido anti-horário é positivo. Giros de $$90^{\circ}$$, $$180^{\circ}$$ e $$360^{\circ}$$ são casos frequentes; a rotação preserva a orientação.

Com instrumentos, o compasso conserva $$OP$$ e o transferidor marca $$\alpha$$. No software, informam-se figura, centro, ângulo e sentido.

**Ponteiro do relógio**

Um ponteiro de $$12\,\mathrm{cm}$$ vai de 12h00 a 12h20. Determine o giro e seu comprimento final.

**Resolução:**

- **Passo 1:** Calcular o giro por minuto.

$$\frac{360^{\circ}}{60}=6^{\circ}$$

- **Passo 2:** Calcular o giro em vinte minutos.

$$20\cdot6^{\circ}=120^{\circ}$$

- **Passo 3:** Aplicar a conservação de comprimento.

**Resposta:** o ponteiro gira $$120^{\circ}$$ no sentido horário e continua medindo $$12\,\mathrm{cm}$$.

> ⚠️ **Atenção:**
>
> Reflexão inverte a orientação; translação e rotação a preservam.

---

## 3. Composição de transformações

Pegadas alternadas combinam reflexão e translação: uma transformação atua sobre o resultado da anterior.

### 3.1 Ordem das operações

**Composição** é a aplicação sucessiva de transformações. Compor isometrias produz outra isometria, mas trocar a ordem pode alterar a posição final.

Uma reflexão seguida de translação paralela ao eixo forma uma **reflexão deslizante**, padrão observado em sequências de pegadas.

<!-- tikz:inicio fig-04-ordem-da-composicao -->
![Duas sequências mostram que refletir e depois transladar leva de 1 a 3, enquanto transladar e depois refletir leva de 1 a menos 5](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/transformacoes-geometricas/fig-04-ordem-da-composicao.png)
<!-- tikz:fim fig-04-ordem-da-composicao -->

**Refletir e transladar um ponto**

O ponto $$P$$ está a $$1\,\mathrm{cm}$$ à direita de um eixo vertical. A translação desloca $$4\,\mathrm{cm}$$ para a direita.

**Resolução:**

- **Passo 1:** Refletir $$P$$ e depois transladar sua imagem.

$$4\,\mathrm{cm}-1\,\mathrm{cm}=3\,\mathrm{cm}$$

- **Passo 2:** Transladar $$P$$ e depois refletir o resultado.

$$1\,\mathrm{cm}+4\,\mathrm{cm}=5\,\mathrm{cm}$$

**Resposta:** na primeira ordem, a imagem fica $$3\,\mathrm{cm}$$ à direita do eixo; na segunda, $$5\,\mathrm{cm}$$ à esquerda. A composição não é comutativa em geral.

### 3.2 Tesselações

**Tesselação** recobre o plano com figuras congruentes, sem falhas nem sobreposições. Nos vértices, os ângulos completam uma volta:

<!-- tikz:inicio fig-05-tesselacao-hexagonal -->
![Três hexágonos regulares compartilham um vértice onde três ângulos de 120 graus completam 360 graus sem falha](https://raw.githubusercontent.com/felipeelv/imagens-tikz/main/geometria/8ano/transformacoes-geometricas/fig-05-tesselacao-hexagonal.png)
<!-- tikz:fim fig-05-tesselacao-hexagonal -->

$$360^{\circ}$$

Triângulos equiláteros, quadrados e hexágonos regulares pavimentam o plano sozinhos porque seus ângulos internos dividem essa volta exatamente.

O gravurista holandês **Maurits Cornelis Escher (1898–1972)** combinou translação, reflexão e rotação em obras como *Reptiles* (1943) e *Metamorphosis* (1937–1968), transformando tesselações em arte.

Azulejos portugueses e mosaicos islâmicos também constroem padrões pela repetição dessas isometrias.

> 🔢 **Padrão:**
>
> Numa tesselação, os ângulos reunidos em cada vértice somam $$360^{\circ}$$.
