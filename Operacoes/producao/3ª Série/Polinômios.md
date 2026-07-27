# BL2_Capítulo 2 — Polinômios

> Como operar, dividir e decompor polinômios?

---

## 1. Polinômios: operações

### 1.1 Operações e grau

Adição e subtração agrupam termos de mesmo grau. A multiplicação aplica a distributividade e soma os expoentes das potências de mesma base.

Se os coeficientes líderes não se anularem:

- o grau do produto é a soma dos graus;
- o grau da soma não supera o maior grau das parcelas;
- na divisão, o grau do resto é menor que o grau do divisor.

A divisão euclidiana é expressa por:

$$P(x)=D(x)Q(x)+R(x)$$

### 1.2 Chave e Briot–Ruffini

A chave funciona para qualquer divisor polinomial. Briot–Ruffini abrevia a divisão quando o divisor tem a forma $$x-r$$.

**Divisão por um binômio**

Divida $$P(x)=x^3-6x^2+11x-6$$ por $$x-1$$ usando Ruffini.

**Resolução:**

- **Passo 1:** Registrar a raiz do divisor e os coeficientes: $$1,-6,11,-6$$.

$$r=1$$

- **Passo 2:** Baixar o primeiro coeficiente e efetuar as multiplicações e somas sucessivas: $$1$$.

$$-6+1=-5$$

$$11+(-5)=6$$

$$-6+6=0$$

- **Passo 3:** Ler quociente e resto.

$$Q(x)=x^2-5x+6$$

$$R(x)=0$$

**Resposta:** $$P(x)=(x-1)(x^2-5x+6)$$.

**Charles Hermite** provou, em 1873, que $$e$$ não é raiz de polinômio inteiro não nulo.

> ⚠️ **Atenção:**  
> Termos ausentes devem entrar na divisão com coeficiente zero para preservar as posições.

---

## 2. Polinômios: teoremas e raízes

### 2.1 Resto, D'Alembert e raízes racionais

O Teorema do Resto afirma que o resto da divisão de $$P(x)$$ por $$x-r$$ é $$P(r)$$. Portanto:

$$P(r)=0\iff (x-r)\mid P(x)$$

Esse é o Teorema de D'Alembert. Candidatos racionais usam divisores do termo independente sobre divisores do coeficiente líder.

### 2.2 Fatoração, Girard e multiplicidade

**Fatoração completa**

Fatore $$P(x)=x^3-6x^2+11x-6$$.

**Resolução:**

- **Passo 1:** Testar o candidato 1.

$$P(1)=1-6+11-6$$

$$P(1)=0$$

- **Passo 2:** Usar o quociente da divisão por $$x-1$$.

$$Q(x)=x^2-5x+6$$

- **Passo 3:** Fatorar o trinômio.

$$Q(x)=(x-2)(x-3)$$

- **Passo 4:** Escrever a decomposição.

$$P(x)=(x-1)(x-2)(x-3)$$

**Resposta:** as raízes são 1, 2 e 3, todas de multiplicidade 1.

Girard relaciona coeficientes a somas e produtos das raízes. Pelo Teorema Fundamental da Álgebra, grau $$n$$ implica $$n$$ raízes complexas, contadas com multiplicidade.

> 🔢 **Padrão:**  
> Uma raiz de multiplicidade $$k$$ produz o fator $$(x-r)^k$$.
