# Capítulo 2 — Fórmula de Bhaskara e relações entre raízes

> Como resolver uma equação quadrática completa?

---

## 1. Dedução da fórmula

### 1.1 Completamento de quadrado

Partimos de $$ax^2+bx+c=0$$, onde $$a\neq0$$.

**Fórmula construída passo a passo**

**Resolução:**

- **Passo 1:** Dividir por $$a$$ e transpor o termo independente.

$$x^2+\frac{b}{a}x=-\frac{c}{a}$$

- **Passo 2:** Somar o quadrado necessário aos dois membros.

$$x^2+\frac{b}{a}x+\frac{b^2}{4a^2}=-\frac{c}{a}+\frac{b^2}{4a^2}$$

- **Passo 3:** Fatorar e reduzir o segundo membro.

$$\left(x+\frac{b}{2a}\right)^2=\frac{b^2-4ac}{4a^2}$$

- **Passo 4:** Multiplicar por $$4a^2$$.

$$(2ax+b)^2=b^2-4ac$$

- **Passo 5:** Extrair a raiz e isolar $$x$$.

$$2ax+b=\pm\sqrt{b^2-4ac}$$

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

**Resposta:** definindo $$\Delta=b^2-4ac$$, obtemos $$x=\frac{-b\pm\sqrt{\Delta}}{2a}$$.

### 1.2 Cuidado com o módulo

Se a raiz do denominador for extraída separadamente, vale:

$$\sqrt{4a^2}=2|a|$$

e não $$2a$$ para todo real $$a$$. A passagem por $$(2ax+b)^2=\Delta$$ preserva os dois sinais e conduz corretamente à fórmula usual.

**Bhaskara II** (1114–c. 1185) difundiu a regra; “fórmula de Bhaskara” é uma denominação brasileira.

---

## 2. Discriminante

### 2.1 Três possibilidades

O **discriminante** é:

$$\Delta=b^2-4ac$$

onde $$a$$, $$b$$ e $$c$$ são os coeficientes. Seu sinal determina:

| Condição | Raízes reais |
|---|---:|
| $$\Delta>0$$ | duas distintas |
| $$\Delta=0$$ | uma dupla |
| $$\Delta<0$$ | nenhuma |

### 2.2 Atenção ao coeficiente negativo

**Quantidade de raízes prevista**

Analise $$x^2-5x+6=0$$.

**Resolução:**

- **Passo 1:** Identificar os coeficientes.

$$a=1$$

$$b=-5$$

$$c=6$$

- **Passo 2:** Calcular o discriminante.

$$\Delta=(-5)^2-4\times1\times6$$

$$\Delta=25-24$$

$$\Delta=1$$

**Resposta:** como $$\Delta>0$$, existem duas raízes reais distintas.

> ⚠️ **Atenção:**  
> O quadrado inclui o sinal: $$(-5)^2=25$$.

---

## 3. Equações completas

### 3.1 Fluxo de resolução

Quatro etapas evitam erros:

- escrever a equação na forma geral;
- identificar $$a$$, $$b$$ e $$c$$ com os sinais;
- calcular $$\Delta$$;
- aplicar a fórmula e simplificar cada raiz.

### 3.2 Aplicação completa

**Dimensões de um terreno**

Um terreno retangular tem $$600\,\mathrm{m^2}$$, e o comprimento excede a largura em $$10\,\mathrm{m}$$. Chamando a largura de $$x$$, temos $$x^2+10x-600=0$$.

**Resolução:**

- **Passo 1:** Identificar os coeficientes.

$$a=1$$

$$b=10$$

$$c=-600$$

- **Passo 2:** Calcular $$\Delta$$.

$$\Delta=10^2-4\times1\times(-600)$$

$$\Delta=100+2400$$

$$\Delta=2500$$

- **Passo 3:** Aplicar a fórmula.

$$x=\frac{-10\pm\sqrt{2500}}{2\times1}$$

$$x=\frac{-10\pm50}{2}$$

- **Passo 4:** Separar as raízes.

$$x_1=\frac{-10+50}{2}$$

$$x_1=20$$

$$x_2=\frac{-10-50}{2}$$

$$x_2=-30$$

- **Passo 5:** Verificar a raiz válida no contexto.

$$20\times30=600$$

$$30-20=10$$

**Resposta:** a largura é $$20\,\mathrm{m}$$ e o comprimento, $$30\,\mathrm{m}$$; a raiz $$-30$$ não representa uma medida.

> ⚠️ **Atenção:**  
> A fórmula começa com $$-b$$ e seu denominador completo é $$2a$$.

---

## 4. Soma das raízes

### 4.1 Dedução

Somando as duas expressões da fórmula:

$$x_1+x_2=\frac{-b+\sqrt{\Delta}}{2a}+\frac{-b-\sqrt{\Delta}}{2a}$$

$$x_1+x_2=\frac{-2b}{2a}$$

$$x_1+x_2=-\frac{b}{a}$$

Definimos $$S=x_1+x_2$$. Os radicais se cancelam e o sinal de $$b$$ aparece invertido.

### 4.2 Verificação estrutural

**Soma sem Bhaskara**

Determine a soma das raízes de $$2x^2-6x-8=0$$.

**Resolução:**

- **Passo 1:** Identificar $$a$$ e $$b$$.

$$a=2$$

$$b=-6$$

- **Passo 2:** Aplicar a relação.

$$S=-\frac{-6}{2}$$

$$S=3$$

**Resposta:** a soma das raízes é 3.

> 🔢 **Padrão:**  
> A soma das raízes é $$-\frac{b}{a}$$, com o sinal de $$b$$ invertido.

---

## 5. Produto e composição

### 5.1 Dedução do produto

Multiplicando as raízes conjugadas:

$$x_1x_2=\frac{(-b+\sqrt{\Delta})(-b-\sqrt{\Delta})}{4a^2}$$

$$x_1x_2=\frac{b^2-\Delta}{4a^2}$$

$$x_1x_2=\frac{4ac}{4a^2}$$

$$x_1x_2=\frac{c}{a}$$

Definimos $$P=x_1x_2$$. Com raízes conhecidas, uma equação mônica pode ser composta por:

$$x^2-Sx+P=0$$

### 5.2 Caminho inverso

**Equação de raízes 3 e 5**

**Resolução:**

- **Passo 1:** Calcular a soma.

$$S=3+5$$

$$S=8$$

- **Passo 2:** Calcular o produto.

$$P=3\times5$$

$$P=15$$

- **Passo 3:** Compor a equação.

$$x^2-8x+15=0$$

**Resposta:** uma equação com essas raízes é $$x^2-8x+15=0$$.

> ⚠️ **Atenção:**  
> Na composição, a soma entra com sinal trocado e o produto mantém seu sinal.
