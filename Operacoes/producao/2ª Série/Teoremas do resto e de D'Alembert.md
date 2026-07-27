# BL2_Capítulo 3 — Teoremas do resto e de D'Alembert

> Como encontrar restos e fatores sem fazer toda a divisão?

---

## 1. Teorema do resto

### 1.1 Enunciado e demonstração

O **Teorema do Resto** afirma: na divisão de $$P(x)$$ por $$x-a$$, o resto é

$$R=P(a)$$

Pela divisão euclidiana,

$$P(x)=(x-a)Q(x)+R$$

Substituindo $$x=a$$:

$$P(a)=(a-a)Q(a)+R$$

$$P(a)=0\times Q(a)+R$$

$$P(a)=R$$

### 1.2 Cálculo direto do resto

**Resto sem divisão completa**

Determine o resto da divisão de $$P(x)=x^3-4x+1$$ por $$x-2$$.

**Resolução:**

- **Passo 1:** Identificar o valor de $$a$$.

$$a=2$$

- **Passo 2:** Calcular $$P(2)$$.

$$P(2)=2^3-4\times2+1$$

$$P(2)=8-8+1$$

$$P(2)=1$$

**Resposta:** O resto é 1.

**Étienne Bézout** (1730–1783), autor da *Théorie générale des équations algébriques* (1779), é associado na tradição escolar ao pequeno teorema que relaciona esse resto a $$P(a)$$.

> 🔢 **Padrão:**  
> Dividir por $$x-a$$ transforma o cálculo do resto na avaliação de $$P(a)$$.

---

## 2. Teorema de D'Alembert

### 2.1 Equivalência

O **Teorema de D'Alembert** estabelece

$$x-a\ \text{divide}\ P(x)\Longleftrightarrow P(a)=0$$

Se $$x-a$$ divide $$P$$, o resto é zero; pelo Teorema do Resto, $$P(a)=0$$. Reciprocamente, se $$P(a)=0$$, o resto da divisão por $$x-a$$ é zero, logo a divisão é exata.

### 2.2 Teste de divisibilidade

**Teste de divisibilidade por uma raiz**

Verifique se $$x-2$$ divide $$P(x)=x^3-6x^2+11x-6$$.

**Resolução:**

- **Passo 1:** Avaliar o polinômio em 2.

$$P(2)=2^3-6\times2^2+11\times2-6$$

- **Passo 2:** Calcular as potências.

$$P(2)=8-6\times4+22-6$$

- **Passo 3:** Calcular o produto.

$$P(2)=8-24+22-6$$

- **Passo 4:** Somar.

$$P(2)=0$$

**Resposta:** Como $$P(2)=0$$, o número 2 é raiz e $$x-2$$ divide $$P(x)$$ exatamente.

A equivalência testa raízes sem efetuar a divisão.

> ⚠️ **Atenção:**  
> Para divisor $$x+3$$, escreva $$x-(-3)$$ e avalie o polinômio em $$-3$$.
