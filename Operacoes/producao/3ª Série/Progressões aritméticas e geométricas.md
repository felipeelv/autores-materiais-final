# Capítulo 6 — Progressões aritméticas e geométricas

> Como calcular termos e somas de PA e PG?

---

## 1. Progressão aritmética: termo geral

### 1.1 Razão e identificação

**Progressão aritmética (PA)** é a sequência em que a diferença entre termos consecutivos é constante:

$$r=a_{n+1}-a_n$$

Se $$r>0$$, a PA é crescente; se $$r<0$$, decrescente; se $$r=0$$, constante.

### 1.2 Termo geral e função afim

O termo de posição $$n$$ é:

$$a_n=a_1+(n-1)r$$

Cada avanço de posição acrescenta $$r$$; é um modelo afim discreto.

**Arquibancada em fileiras**

Uma arquibancada tem 18 lugares na primeira fileira e ganha 4 lugares por fileira. Determine a 20ª fileira.

**Resolução:**

- **Passo 1:** Identificar os dados.

$$a_1=18$$

$$r=4$$

$$n=20$$

- **Passo 2:** Aplicar o termo geral.

$$a_{20}=18+(20-1)\times4$$

$$a_{20}=18+76$$

$$a_{20}=94$$

**Resposta:** a 20ª fileira tem 94 lugares.

**Abu Bakr al-Karaji**, no *Al-Fakhri* por volta do ano 1000, sistematizou propriedades de progressões e usou raciocínios precursores da indução para fórmulas de somas.

> 🔢 **Padrão:**  
> PA apresenta diferenças constantes e corresponde a um modelo afim discreto.

---

## 2. Soma dos termos de uma PA

### 2.1 Fórmula da soma

Em uma PA finita, o primeiro e o último termo têm a mesma soma que o segundo e o penúltimo. Esse pareamento conduz a:

$$S_n=\frac{n(a_1+a_n)}{2}$$

Gauss usou esse pareamento para somar rapidamente os inteiros de 1 a 100.

### 2.2 Termos equidistantes

Termos equidistantes dos extremos têm soma constante. Em três termos consecutivos, o termo central é a média aritmética dos vizinhos.

**Soma das fileiras**

Calcule o total de lugares nas 20 fileiras da PA com $$a_1=18$$ e $$a_{20}=94$$.

**Resolução:**

- **Passo 1:** Aplicar a fórmula.

$$S_{20}=\frac{20(18+94)}{2}$$

- **Passo 2:** Somar os extremos.

$$S_{20}=\frac{20\times112}{2}$$

- **Passo 3:** Simplificar.

$$S_{20}=10\times112$$

$$S_{20}=1120$$

**Resposta:** as 20 fileiras totalizam 1.120 lugares.

Acúmulos com aumento linear, como depósitos que crescem por uma quantia fixa mensal, são modelados pela soma de uma PA.

> ⚠️ **Atenção:**  
> Na fórmula da soma, $$n$$ é a quantidade de termos, não o valor do último termo.

---

## 3. Progressão geométrica: termo geral

### 3.1 Razão e identificação

**Progressão geométrica (PG)** é a sequência em que o quociente entre termos consecutivos não nulos é constante:

$$q=\frac{a_{n+1}}{a_n}$$

O comportamento depende de $$q$$ e dos sinais dos termos. Com $$a_1>0$$ e $$q>1$$, a PG cresce; com $$0<q<1$$, decresce em direção a zero; com $$q<0$$, alterna sinais.

### 3.2 Termo geral e função exponencial

O termo de posição $$n$$ é:

$$a_n=a_1q^{n-1}$$

A PG é uma função exponencial restrita aos naturais.

**Crescimento de uma cultura**

Uma cultura começa com 500 células e dobra a cada período. Determine o 8º termo.

**Resolução:**

- **Passo 1:** Identificar os dados.

$$a_1=500$$

$$q=2$$

$$n=8$$

- **Passo 2:** Aplicar o termo geral.

$$a_8=500\times2^{8-1}$$

$$a_8=500\times128$$

$$a_8=64\,000$$

**Resposta:** o 8º termo é 64.000 células.

> 🔢 **Padrão:**  
> PG apresenta razões constantes e corresponde a um modelo exponencial discreto.

---

## 4. Soma dos termos de uma PG

### 4.1 Soma finita

Para $$q\neq1$$, a soma dos primeiros $$n$$ termos é:

$$S_n=a_1\frac{q^n-1}{q-1}$$

Se $$q=1$$, todos os termos são iguais e $$S_n=na_1$$.

### 4.2 Soma infinita

Quando $$|q|<1$$, os termos se aproximam de zero e a soma infinita converge para:

$$S_\infty=\frac{a_1}{1-q}$$

**Metades sucessivas**

Calcule:

$$1+\frac12+\frac14+\frac18+\ldots$$

**Resolução:**

- **Passo 1:** Identificar primeiro termo e razão.

$$a_1=1$$

$$q=\frac12$$

- **Passo 2:** Confirmar a condição de convergência: $$|q|<1$$.

- **Passo 3:** Aplicar a fórmula.

$$S_\infty=\frac{1}{1-\frac12}$$

$$S_\infty=2$$

**Resposta:** a soma infinita vale 2.

Juros compostos, decaimentos e prestações da Tabela Price usam estruturas geométricas. A soma infinita é uma ideia informal de limite: os totais parciais se aproximam de um valor fixo.

> ⚠️ **Atenção:**  
> A soma infinita só converge quando $$|q|<1$$; fora dessa condição, a fórmula não se aplica.
