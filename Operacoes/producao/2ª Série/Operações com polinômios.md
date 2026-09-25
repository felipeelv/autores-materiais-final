# BL2_Capítulo 2 — Operações com polinômios

> Como operar e dividir polinômios com segurança?

---

## 1. Adição e subtração

### 1.1 Termos semelhantes

Na **adição**, agrupam-se coeficientes correspondentes. Na **subtração**, distribui-se primeiro o sinal negativo por todos os termos do segundo polinômio.

Organizar as expressões em grau decrescente e preencher mentalmente potências ausentes com coeficiente zero reduz erros. Cancelamentos podem fazer o grau do resultado ficar menor que o maior grau inicial.

### 1.2 Subtração termo a termo

**Diferença entre dois polinômios**

Calcule $$P(x)-Q(x)$$, sendo

$$P(x)=3x^2+2x-1$$

$$Q(x)=x^2-5x+4$$

**Resolução:**

- **Passo 1:** Distribuir o sinal da subtração.

$$P(x)-Q(x)=3x^2+2x-1-x^2+5x-4$$

- **Passo 2:** Agrupar termos semelhantes.

$$P(x)-Q(x)=(3x^2-x^2)+(2x+5x)+(-1-4)$$

- **Passo 3:** Operar os coeficientes.

$$P(x)-Q(x)=2x^2+7x-5$$

**Resposta:** A diferença é $$2x^2+7x-5$$.

> ⚠️ **Atenção:**  
> Na subtração, o sinal negativo altera todos os termos do polinômio subtraído.

---

## 2. Multiplicação

### 2.1 Distributiva e grau

O procedimento segue três ações:

- multiplicar coeficientes;
- somar expoentes de bases iguais;
- reunir termos semelhantes.

Para polinômios não nulos, o grau do produto é a soma dos graus. Produtos notáveis são casos particulares dessa distributiva.

### 2.2 Aplicação da distributiva

**Produto termo a termo**

Calcule $$(2x-3)(x^2+x+4)$$.

**Resolução:**

- **Passo 1:** Distribuir $$2x$$.

$$2x(x^2+x+4)=2x^3+2x^2+8x$$

- **Passo 2:** Distribuir $$-3$$.

$$-3(x^2+x+4)=-3x^2-3x-12$$

- **Passo 3:** Somar os resultados: $$2x^3+2x^2+8x-3x^2-3x-12$$.

- **Passo 4:** Reduzir termos semelhantes: $$2x^3-x^2+5x-12$$.

**Resposta:** O produto é $$2x^3-x^2+5x-12$$, de grau 3.

> 🔢 **Padrão:**  
> O grau do produto de polinômios não nulos é a soma dos graus dos fatores.

---

## 3. Divisão pelo método da chave

### 3.1 Divisão euclidiana

Para $$D(x)\neq0$$, existem quociente $$Q(x)$$ e resto $$R(x)$$ tais que

$$P(x)=D(x)Q(x)+R(x)$$

com $$R(x)=0$$ ou grau de $$R$$ menor que o grau de $$D$$. O método da chave funciona para qualquer divisor polinomial não nulo.

### 3.2 Algoritmo da chave

**Divisão exata pela chave**

Divida $$x^3-7x+6$$ por $$x-1$$.

**Resolução:**

- **Passo 1:** Ordenar e incluir a potência ausente.

$$P(x)=x^3+0x^2-7x+6$$

- **Passo 2:** Dividir os termos líderes.

$$\frac{x^3}{x}=x^2$$

$$x^2(x-1)=x^3-x^2$$

A subtração deixa $$x^2-7x+6$$.

- **Passo 3:** Repetir com o novo termo líder.

$$\frac{x^2}{x}=x$$

$$x(x-1)=x^2-x$$

A subtração deixa $$-6x+6$$.

- **Passo 4:** Obter o último termo.

$$\frac{-6x}{x}=-6$$

$$-6(x-1)=-6x+6$$

O resto é zero.

**Resposta:** O quociente é $$x^2+x-6$$ e o resto é 0.

> ⚠️ **Atenção:**  
> Ordene os polinômios e registre coeficiente zero nas potências ausentes antes da divisão.

---

## 4. Dispositivo de Briot–Ruffini

### 4.1 Procedimento sintético

No **dispositivo de Briot–Ruffini**, use $$a$$ do divisor $$x-a$$. Baixe, multiplique e some: o último resultado é o resto; os demais formam o quociente.

### 4.2 Aplicação do dispositivo

**Divisão sintética**

Divida $$2x^3-3x^2+5$$ por $$x-2$$.

**Resolução:**

- **Passo 1:** Registrar os coeficientes, incluindo o termo ausente: $$2,-3,0,5$$.

- **Passo 2:** Baixar o primeiro coeficiente e multiplicar por 2.

$$2\times2=4$$

- **Passo 3:** Somar à coluna seguinte.

$$-3+4=1$$

- **Passo 4:** Repetir as operações.

$$1\times2=2$$

$$0+2=2$$

$$2\times2=4$$

$$5+4=9$$

- **Passo 5:** Interpretar os coeficientes finais.

$$Q(x)=2x^2+x+2$$

$$R=9$$

**Resposta:** O quociente é $$2x^2+x+2$$ e o resto é 9.

**Paolo Ruffini** (1765–1822) desenvolveu o dispositivo como forma econômica de dividir por fatores lineares.

> 🔢 **Padrão:**  
> No divisor $$x-a$$, o número usado no dispositivo é $$a$$ com o sinal já invertido em relação ao termo escrito.
