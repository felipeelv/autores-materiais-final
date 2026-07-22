# Capítulo 3 — Problemas e modelagem com sistemas

> Como transformar um problema com duas incógnitas em sistema?

---

## 1. Da situação ao sistema

### 1.1 Nomear as incógnitas

O primeiro passo é identificar as quantidades desconhecidas. Na fazenda, definimos:

- $$g$$ — quantidade de galinhas;
- $$c$$ — quantidade de coelhos.

### 1.2 Traduzir as condições

Cada informação independente gera uma equação. As 50 cabeças produzem:

$$g+c=50$$

As 140 patas, considerando 2 por galinha e 4 por coelho, produzem:

$$2g+4c=140$$

O modelo completo é:

$$\begin{cases}g+c=50\\2g+4c=140\end{cases}$$

Duas incógnitas e duas condições independentes indicam um sistema 2×2.

**Preços na cantina**

Duas bebidas e um lanche custam R$ 14,00; uma bebida e um lanche custam R$ 10,00. Modele a situação.

**Resolução:**

- **Passo 1:** Nomear os preços.

Usaremos $$b$$ para o preço da bebida e $$l$$ para o preço do lanche.

- **Passo 2:** Traduzir cada compra.

$$2b+l=14$$

$$b+l=10$$

**Resposta:** o modelo é $$\begin{cases}2b+l=14\\b+l=10\end{cases}$$.

> 🔢 **Padrão:**  
> Um sistema 2×2 precisa de duas condições independentes para determinar um único par.

**Sharaf al-Dīn al-Ṭūsī** (c. 1135–1213) estudou equações e sistemas no século XII.

---

## 2. Resolução de problemas

### 2.1 Fluxo completo

O procedimento reúne cinco decisões:

- definir as variáveis;
- escrever as duas equações;
- escolher substituição ou adição;
- resolver sem pular etapas;
- verificar e interpretar.

### 2.2 Cabeças e patas

**Animais da fazenda**

Resolva o sistema modelado na aula anterior.

**Resolução:**

- **Passo 1:** Multiplicar a primeira equação por $$-2$$.

$$-2g-2c=-100$$

- **Passo 2:** Somar com a segunda equação.

$$-2g+2g-2c+4c=-100+140$$

$$2c=40$$

$$c=20$$

- **Passo 3:** Retornar à primeira equação.

$$g+20=50$$

$$g=30$$

- **Passo 4:** Verificar as patas: $$2\times30+4\times20$$.

$$2\times30+4\times20=60+80$$

$$60+80=140$$

**Resposta:** há 30 galinhas e 20 coelhos.

**Cadernos e canetas**

Três cadernos e duas canetas custam R$ 26,00; um caderno e quatro canetas custam R$ 22,00.

**Resolução:**

- **Passo 1:** Modelar, com $$d$$ para o preço do caderno e $$n$$ para o preço da caneta.

$$\begin{cases}3d+2n=26\\d+4n=22\end{cases}$$

- **Passo 2:** Isolar $$d$$ na segunda equação.

$$d=22-4n$$

- **Passo 3:** Substituir na primeira.

$$3(22-4n)+2n=26$$

$$66-12n+2n=26$$

$$-10n=-40$$

$$n=4$$

- **Passo 4:** Calcular $$d$$.

$$d=22-4\times4$$

$$d=6$$

**Resposta:** o caderno custa R$ 6,00 e a caneta, R$ 4,00.

> ⚠️ **Atenção:**  
> A resposta final deve nomear as grandezas; o par $$(30,20)$$ sozinho não informa qual número pertence a cada espécie.

---

## 3. Interpretação das soluções

### 3.1 Unidades e restrições

Cada valor retorna à variável que representa, acompanhado da unidade. Três restrições comuns ajudam a validar o resultado:

- quantidades de objetos ou pessoas são inteiras e não negativas;
- idades e medidas não são negativas;
- preços não são negativos.

Um valor incompatível pode indicar erro de cálculo, tradução incorreta ou dados insuficientes.

### 3.2 Fechar o ciclo

**Compra conferida**

Três cadernos de R$ 6,00 e duas canetas de R$ 4,00 devem totalizar R$ 26,00.

**Resolução:**

- **Passo 1:** Calcular o valor dos cadernos.

$$3\times6=18$$

- **Passo 2:** Calcular o valor das canetas.

$$2\times4=8$$

- **Passo 3:** Somar os valores.

$$18+8=26$$

**Resposta:** os preços satisfazem a condição de R$ 26,00.

> 🔢 **Padrão:**  
> Modelar, resolver, interpretar e verificar formam um único ciclo.

Confira o par nas equações e nas unidades do contexto.

---

## 4. Estruturas do cotidiano

### 4.1 Situações recorrentes

Quatro estruturas aparecem com frequência:

- compras ou misturas relacionam quantidades, valores unitários e total;
- idades relacionam duas pessoas no mesmo instante;
- encontros relacionam posições ou distâncias;
- divisões repartem um total sob uma segunda condição.

O contexto muda, mas o procedimento permanece: situação, sistema, resolução, interpretação e validação.

### 4.2 Relação entre idades

**Pai e filho**

A soma das idades é 48 anos, e o pai tem o triplo da idade do filho.

**Resolução:**

- **Passo 1:** Modelar, com $$p$$ para pai e $$f$$ para filho.

$$\begin{cases}p+f=48\\p=3f\end{cases}$$

- **Passo 2:** Substituir.

$$3f+f=48$$

$$4f=48$$

$$f=12$$

- **Passo 3:** Calcular $$p$$.

$$p=3\times12$$

$$p=36$$

**Resposta:** o filho tem 12 anos e o pai, 36 anos.

O enunciado “dois números somam 48 e um é o triplo do outro” gera o mesmo sistema e as mesmas soluções, mas muda o significado da resposta.

> ⚠️ **Atenção:**  
> Uma mesma expressão algébrica pode modelar situações diferentes, mas a resposta deve respeitar o significado das variáveis.
