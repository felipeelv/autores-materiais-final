# Capítulo 6 — Sistemas de inequações, produto e quociente

> Como combinar desigualdades e analisar produtos e quocientes?

---

## 1. Sistemas de inequações

### 1.1 Interseção das soluções

Um **sistema de inequações** é resolvido em duas etapas:

- resolver cada inequação separadamente;
- calcular a interseção dos conjuntos obtidos.

Sobrepor os intervalos na reta mostra a região comum. Ela pode ser limitada, ilimitada ou vazia.

### 1.2 Sistema misto

**Sistema misto**

Resolva

$$\begin{cases}x>-1\\x^2-4\leq0\end{cases}$$

**Resolução:**

- **Passo 1:** Resolver a condição linear.

$$S_1=]-1,+\infty[$$

- **Passo 2:** Fatorar a condição quadrática: $$x^2-4\leq0$$; $$(x-2)(x+2)\leq0$$.

$$S_2=[-2,2]$$

- **Passo 3:** Interseccionar os intervalos.

$$S=S_1\cap S_2$$

$$S=]-1,2]$$

**Resposta:** O sistema é satisfeito no intervalo $$]-1,2]$$.

> ⚠️ **Atenção:**  
> Em um sistema, unir respostas aceita valores que podem descumprir uma das condições.

---

## 2. Inequações produto

### 2.1 Quadro do produto

Para fatores reais $$f(x)$$ e $$g(x)$$:

- o produto é positivo quando os sinais são iguais;
- o produto é negativo quando os sinais são opostos;
- o produto é zero quando ao menos um fator é zero.

**Thomas Harriot** (1560–1621) introduziu os símbolos $$>$$ e $$<$$ em *Artis Analyticae Praxis* (1631), tornando a comparação algébrica mais direta.

### 2.2 Montagem do quadro

**Produto não negativo**

Resolva $$(x-1)(x+3)\geq0$$.

**Resolução:**

- **Passo 1:** Identificar os zeros dos fatores.

$$x=-3$$

$$x=1$$

- **Passo 2:** Montar o quadro de sinais.

| Intervalo | $$]-\infty,-3[$$ | $$]-3,1[$$ | $$]1,+\infty[$$ |
|---|---:|---:|---:|
| $$x+3$$ | − | + | + |
| $$x-1$$ | − | − | + |
| Produto | + | − | + |

- **Passo 3:** Selecionar o sinal positivo e os zeros.

$$S=]-\infty,-3]\cup[1,+\infty[$$

**Resposta:** A solução é $$]-\infty,-3]\cup[1,+\infty[$$.

> 🔢 **Padrão:**  
> Produto de fatores com sinais iguais é positivo; com sinais opostos, é negativo.

---

## 3. Inequações quociente

### 3.1 Zeros e restrições

Em uma inequação quociente:

- o zero do numerador pode entrar com símbolo não estrito;
- o zero do denominador nunca pertence ao domínio;
- os pontos críticos dividem a reta para o quadro de sinais.

### 3.2 Restrição do denominador

**Quociente não positivo**

Resolva

$$\frac{x-2}{x+1}\leq0$$

**Resolução:**

- **Passo 1:** Identificar os pontos críticos.

$$x=-1$$

$$x=2$$

- **Passo 2:** Registrar a restrição: $$x\neq-1$$.

- **Passo 3:** Determinar os sinais.

| Intervalo | $$]-\infty,-1[$$ | $$]-1,2[$$ | $$]2,+\infty[$$ |
|---|---:|---:|---:|
| Quociente | + | − | + |

- **Passo 4:** Selecionar o negativo e incluir o zero do numerador.

$$S=]-1,2]$$

**Resposta:** A solução é $$]-1,2]$$; o valor $$-1$$ permanece excluído.

> ⚠️ **Atenção:**  
> O zero do denominador é excluído mesmo quando a inequação usa $$\leq$$ ou $$\geq$$.
