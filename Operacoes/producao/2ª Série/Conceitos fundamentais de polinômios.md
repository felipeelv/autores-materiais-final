# BL2_Capítulo 1 — Conceitos fundamentais de polinômios

> O que define um polinômio e quando um valor é sua raiz?

---

## 1. Polinômio e função polinomial

### 1.1 Definição formal

Um **polinômio** real na variável $$x$$ tem a forma

$$P(x)=a_nx^n+a_{n-1}x^{n-1}+\timess+a_1x+a_0$$

onde os coeficientes $$a_k$$ são reais e os expoentes são inteiros não negativos.

A expressão formal registra termos e coeficientes. A **função polinomial** associada usa essa expressão como regra para relacionar cada $$x\in\mathbb{R}$$ ao valor $$P(x)$$.

### 1.2 Reconhecimento da estrutura

**Reconhecimento de uma expressão**

Analise $$P(x)=3x^4-2x+7$$.

**Resolução:**

- **Passo 1:** Verificar a quantidade de termos.

A soma possui três termos, portanto é finita.

- **Passo 2:** Verificar os expoentes: $$4,1,0$$.

- **Passo 3:** Verificar os coeficientes: $$3,-2,7\in\mathbb{R}$$.

**Resposta:** A expressão é um polinômio real em $$x$$.

**Jean le Rond d'Alembert** (1717–1783), coeditor da *Encyclopédie*, estudou equações polinomiais e formulou uma versão inicial do Teorema Fundamental da Álgebra.

> ⚠️ **Atenção:**  
> Expoente negativo, fracionário ou variável impede que a expressão seja um polinômio em $$x$$.

---

## 2. Grau e coeficientes

### 2.1 Elementos principais

Em um polinômio não nulo:

- o **grau** é o maior expoente com coeficiente não nulo;
- o **coeficiente líder** acompanha o termo de maior grau;
- o **termo independente** é $$a_0$$.

Alguns graus recebem nomes usuais:

| Grau | Nome |
|---:|---|
| 0 | constante não nulo |
| 1 | linear |
| 2 | quadrático |
| 3 | cúbico |

### 2.2 Leitura dos elementos

**Leitura dos elementos**

Analise $$P(x)=-2x^4+5x-7$$.

**Resolução:**

- **Passo 1:** Identificar o maior expoente: $$4$$.

- **Passo 2:** Ler o coeficiente desse termo.

$$a_4=-2$$

- **Passo 3:** Ler o termo sem variável.

$$a_0=-7$$

**Resposta:** O polinômio tem grau 4, coeficiente líder $$-2$$ e termo independente $$-7$$.

Os coeficientes das potências ausentes são zero; no exemplo, $$a_3=0$$ e $$a_2=0$$.

> 🔢 **Padrão:**  
> O grau depende do maior expoente com coeficiente não nulo, não da quantidade de termos escritos.

---

## 3. Valor numérico

### 3.1 Substituição organizada

O **valor numérico** $$P(a)$$ é obtido substituindo $$x$$ por $$a$$. Para reduzir erros:

- coloque entradas negativas entre parênteses;
- calcule potências antes de produtos;
- respeite os sinais de cada termo.

### 3.2 Avaliação em entrada negativa

**Valor em uma entrada negativa**

Calcule $$P(-2)$$ para $$P(x)=x^3-3x+1$$.

**Resolução:**

- **Passo 1:** Substituir a variável.

$$P(-2)=(-2)^3-3\times(-2)+1$$

- **Passo 2:** Calcular a potência.

$$P(-2)=-8-3\times(-2)+1$$

- **Passo 3:** Calcular o produto.

$$P(-2)=-8+6+1$$

- **Passo 4:** Somar.

$$P(-2)=-1$$

**Resposta:** O valor numérico é $$-1$$.

> ⚠️ **Atenção:**  
> Em $$(-2)^2$$ o resultado é positivo; em $$-2^2$$, a potência é calculada antes do sinal.

---

## 4. Raiz de um polinômio

### 4.1 Zero e grau

Um número $$a$$ é **raiz** de $$P$$ quando

$$P(a)=0$$

Para um polinômio não nulo de grau $$n$$, há no máximo $$n$$ raízes reais distintas. O Teorema Fundamental da Álgebra afirma, sem demonstração neste recorte, a existência de $$n$$ raízes complexas quando se contam as multiplicidades.

A raiz $$a$$ também se relaciona ao fator $$x-a$$, ideia que sustenta testes de divisibilidade.

### 4.2 Teste de raiz

**Teste direto de uma raiz**

Verifique se 2 é raiz de $$P(x)=x^3-6x^2+11x-6$$.

**Resolução:**

- **Passo 1:** Substituir $$x$$ por 2.

$$P(2)=2^3-6\times2^2+11\times2-6$$

- **Passo 2:** Calcular as potências.

$$P(2)=8-6\times4+22-6$$

- **Passo 3:** Calcular o produto.

$$P(2)=8-24+22-6$$

- **Passo 4:** Somar os termos.

$$P(2)=0$$

**Resposta:** O número 2 é uma raiz de $$P$$.

> 🔢 **Padrão:**  
> Toda raiz real produz um ponto $$(a,0)$$ no gráfico da função polinomial.

---

## 5. Polinômio nulo

### 5.1 Nulo e identicamente nulo

O **polinômio nulo** possui todos os coeficientes iguais a zero. A função associada é **identicamente nula**:

$$P(x)=0$$

para todo $$x\in\mathbb{R}$$. Sobre ℝ, as definições coincidem; seu grau não é definido.

### 5.2 Determinação dos coeficientes

**Coeficientes que anulam o polinômio**

Determine $$a$$, $$b$$ e $$c$$ para que

$$P(x)=(a-1)x^2+(b+2)x+c$$

seja nulo.

**Resolução:**

- **Passo 1:** Igualar o coeficiente quadrático a zero.

$$a-1=0$$

$$a=1$$

- **Passo 2:** Igualar o coeficiente linear a zero.

$$b+2=0$$

$$b=-2$$

- **Passo 3:** Igualar o termo independente a zero.

$$c=0$$

**Resposta:** O polinômio é nulo quando $$a=1$$, $$b=-2$$ e $$c=0$$.

> ⚠️ **Atenção:**  
> Ter uma raiz não torna um polinômio identicamente nulo; todos os coeficientes precisam ser zero.

---

## 6. Igualdade de polinômios

### 6.1 Identidade polinomial

Dois polinômios são **iguais** se, e somente se, possuem o mesmo coeficiente em cada potência de $$x$$. Esse princípio permite determinar parâmetros em identidades.

### 6.2 Comparação de coeficientes

**Coeficientes a determinar**

Encontre $$a$$ e $$b$$ para que

$$(a+1)x^2+(b-2)x+3=4x^2+x+3$$

para todo $$x$$ real.

**Resolução:**

- **Passo 1:** Comparar os coeficientes de $$x^2$$.

$$a+1=4$$

$$a=3$$

- **Passo 2:** Comparar os coeficientes de $$x$$.

$$b-2=1$$

$$b=3$$

- **Passo 3:** Conferir os termos independentes.

$$3=3$$

**Resposta:** A identidade vale para $$a=3$$ e $$b=3$$.

Termos ausentes devem ser escritos mentalmente com coeficiente zero antes da comparação.

Em decomposições ou ajustes de expressões, introduzem-se coeficientes desconhecidos e comparam-se as potências correspondentes pelo mesmo método.

> 🔢 **Padrão:**  
> Uma identidade polinomial transforma a igualdade de expressões em igualdades entre coeficientes.
