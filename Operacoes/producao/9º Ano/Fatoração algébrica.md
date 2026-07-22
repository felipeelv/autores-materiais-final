# Capítulo 3 — Fatoração algébrica

> Quando a fatoração resolve uma equação quadrática?

---

## 1. Fator comum e diferença de quadrados

### 1.1 Fator comum

O fator comum reúne o maior divisor compartilhado pelos coeficientes e a menor potência comum da variável:

$$6x^2+9x=3x(2x+3)$$

Essa escrita permite aplicar o produto nulo quando a expressão está igualada a zero.

### 1.2 Diferença de quadrados

A identidade é:

$$a^2-b^2=(a+b)(a-b)$$

Ela exige dois quadrados separados por subtração. Para números reais, lembre:

$$\sqrt{x^2}=|x|$$

Assim, por exemplo:

$$\sqrt{4a^2}=2|a|$$

**Diferença reconhecida**

Fatore $$x^2-16$$.

**Resolução:**

- **Passo 1:** Identificar os quadrados.

$$x^2=(x)^2$$

$$16=4^2$$

- **Passo 2:** Aplicar a identidade.

$$x^2-16=(x+4)(x-4)$$

**Resposta:** a forma fatorada é $$(x+4)(x-4)$$.

> ⚠️ **Atenção:**  
> A soma $$a^2+b^2$$ não se fatora dessa maneira sobre os números reais.

**Girolamo Cardano** (1501–1576) usou fatorações sistematicamente no *Ars Magna* (1545) para reduzir equações a casos resolvíveis.

---

## 2. Trinômios

### 2.1 Trinômio quadrado perfeito

As identidades fundamentais são:

$$(a+b)^2=a^2+2ab+b^2$$

$$(a-b)^2=a^2-2ab+b^2$$

Para reconhecer um **trinômio quadrado perfeito**, verificamos se o termo central é duas vezes o produto das bases dos quadrados extremos.

**Quadrado de uma soma**

Fatore $$x^2+6x+9$$.

**Resolução:**

- **Passo 1:** Identificar as bases algébricas dos quadrados extremos.

$$x^2=(x)^2$$

$$9=3^2$$

- **Passo 2:** Conferir o termo central algebricamente.

$$2\times x\times3=6x$$

- **Passo 3:** Escrever o quadrado.

$$x^2+6x+9=(x+3)^2$$

**Resposta:** a forma fatorada é $$(x+3)^2$$.

A raiz principal satisfaz $$\sqrt{x^2}=|x|$$; no reconhecimento da identidade, porém, usamos a base algébrica $$x$$ cujo quadrado é $$x^2$$.

### 2.2 Trinômio pelas raízes

Se a equação tem raízes reais $$x_1$$ e $$x_2$$, então:

$$ax^2+bx+c=a(x-x_1)(x-x_2)$$

onde $$a\neq0$$. O sinal das raízes aparece invertido dentro dos fatores.

**Trinômio pelas raízes**

Fatore $$x^2-5x+6$$.

**Resolução:**

- **Passo 1:** Calcular o discriminante.

$$\Delta=(-5)^2-4\times1\times6$$

$$\Delta=1$$

- **Passo 2:** Calcular as raízes.

$$x=\frac{5\pm\sqrt{1}}{2}$$

$$x_1=3$$

$$x_2=2$$

- **Passo 3:** Escrever a forma fatorada.

$$x^2-5x+6=(x-3)(x-2)$$

**Resposta:** a forma fatorada é $$(x-3)(x-2)$$.

> ⚠️ **Atenção:**  
> $$(a+b)^2$$ contém o termo $$2ab$$; não é igual a $$a^2+b^2$$.

---

## 3. Fatoração na resolução

### 3.1 Fatorar e anular

O princípio do produto nulo fornece:

$$(x-r_1)(x-r_2)=0$$

$$x=r_1\text{ ou }x=r_2$$

onde $$r_1$$ e $$r_2$$ são as raízes. Fatoração é preferível quando há fator comum, diferença de quadrados ou trinômio quadrado perfeito; sem padrão visível, a fórmula geral é mais segura.

### 3.2 Atalho conferido

**Raízes de uma diferença**

Resolva $$x^2-16=0$$.

**Resolução:**

- **Passo 1:** Fatorar.

$$(x+4)(x-4)=0$$

- **Passo 2:** Anular o primeiro fator.

$$x+4=0$$

$$x=-4$$

- **Passo 3:** Anular o segundo fator.

$$x-4=0$$

$$x=4$$

**Resposta:** $$x=-4$$ ou $$x=4$$.

> 🔢 **Padrão:**  
> A fatoração é um atalho quando a estrutura é reconhecível e também uma forma de verificar raízes obtidas por outro método.
