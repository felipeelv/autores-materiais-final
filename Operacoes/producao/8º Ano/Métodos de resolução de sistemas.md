# Capítulo 1 — Métodos de resolução de sistemas

> Como resolver um sistema 2×2 por substituição ou adição?

---

## 1. Sistema 2×2 e solução

### 1.1 Duas condições simultâneas

Chamando de $$b$$ o preço da bebida e de $$l$$ o preço do lanche, as informações formam o sistema:

$$\begin{cases}2b+l=14\\b+l=10\end{cases}$$

**Sistema 2×2** é um par de equações com as mesmas duas incógnitas, exigidas simultaneamente. Cada equação isolada admite infinitos pares; juntas, elas restringem os valores.

### 1.2 O par ordenado

**Solução** é o par ordenado que torna verdadeiras as duas equações. A ordem das coordenadas segue a ordem declarada para as incógnitas.

**Preços da cantina**

Considere $$b=4$$ e $$l=6$$.

**Resolução:**

- **Passo 1:** Conferir a primeira condição: $$2\times4+6$$.

$$2\times4+6=8+6$$

$$8+6=14$$

- **Passo 2:** Conferir a segunda condição: $$4+6$$.

$$4+6=10$$

**Resposta:** o par $$(4,6)$$ é a solução; a bebida custa R$ 4,00 e o lanche, R$ 6,00.

> ⚠️ **Atenção:**  
> Os pares $$(4,6)$$ e $$(6,4)$$ representam valores diferentes porque a ordem das coordenadas importa.

**Isaac Newton** (1643–1727) sistematizou métodos para equações e sistemas, incluindo a substituição, em *Universal Arithmetick* (1707), obra baseada em suas aulas em Cambridge.

---

## 2. Verificação de soluções

### 2.1 O teste completo

**Verificar** significa substituir cada coordenada nas duas equações e confirmar as duas igualdades. Um par que satisfaz apenas uma delas não resolve o sistema.

O procedimento seguro tem três ações:

- substituir a primeira coordenada no lugar da primeira incógnita;
- substituir a segunda coordenada no lugar da segunda incógnita;
- conferir separadamente cada igualdade.

### 2.2 Um contraexemplo

**Par que funciona pela metade**

Verifique $$(7,0)$$ no sistema:

$$\begin{cases}2x+y=14\\x+y=10\end{cases}$$

**Resolução:**

- **Passo 1:** Testar a primeira equação: $$2\times7+0$$.

$$2\times7+0=14$$

- **Passo 2:** Testar a segunda equação: $$7+0$$; $$7\neq10$$.

$$7+0=7$$

**Resposta:** $$(7,0)$$ não é solução, pois falha na segunda equação.

> 🔢 **Padrão:**  
> Uma solução de sistema precisa satisfazer todas as equações, sem exceção.

Verifique ao final para detectar sinais, contas ou coordenadas incorretas.

---

## 3. Método da substituição

### 3.1 O procedimento

O **método da substituição** reduz o sistema a uma equação com uma incógnita. A sequência é fixa:

- isolar uma variável;
- substituir a expressão na outra equação;
- resolver a equação resultante;
- retornar para encontrar a segunda variável;
- verificar o par.

### 3.2 Soma e diferença

**Dois números procurados**

Resolva:

$$\begin{cases}x+y=18\\x-y=4\end{cases}$$

**Resolução:**

- **Passo 1:** Isolar $$x$$ na primeira equação.

$$x=18-y$$

- **Passo 2:** Substituir na segunda.

$$(18-y)-y=4$$

$$18-2y=4$$

$$-2y=-14$$

$$y=7$$

- **Passo 3:** Retornar à expressão isolada.

$$x=18-7$$

$$x=11$$

- **Passo 4:** Verificar.

$$11+7=18$$

$$11-7=4$$

**Resposta:** o par é $$(11,7)$$; os números são 11 e 7.

> 🔢 **Padrão:**  
> A substituição costuma ser mais econômica quando uma variável tem coeficiente 1 ou já está isolada.

---

## 4. Método da adição

### 4.1 Preparar a eliminação

No **método da adição**, multiplicamos uma ou ambas as equações até obter coeficientes opostos. Todos os termos, inclusive o termo à direita da igualdade, recebem o mesmo fator.

Depois, somamos membro a membro, resolvemos a equação restante e voltamos a uma equação original.

### 4.2 Eliminar uma variável

**Duas incógnitas, uma eliminação**

Resolva:

$$\begin{cases}2x+3y=12\\x-y=1\end{cases}$$

**Resolução:**

- **Passo 1:** Multiplicar a segunda equação por 3.

$$3x-3y=3$$

- **Passo 2:** Somar as equações.

$$2x+3x+3y-3y=12+3$$

$$5x=15$$

$$x=3$$

- **Passo 3:** Substituir na segunda equação.

$$3-y=1$$

$$-y=-2$$

$$y=2$$

- **Passo 4:** Verificar na primeira: $$2\times3+3\times2$$.

$$2\times3+3\times2=6+6$$

$$6+6=12$$

**Resposta:** a solução é $$(3,2)$$.

> ⚠️ **Atenção:**  
> Multiplicar apenas alguns termos muda a equação e produz outro sistema.

---

## 5. Escolha do método e frações

### 5.1 Escolha estratégica

Dois critérios reduzem o trabalho:

- variável isolada ou com coeficiente 1 favorece a substituição;
- coeficientes opostos ou facilmente ajustáveis favorecem a adição.

Com frações, eliminamos primeiro os denominadores usando o MMC. Isso transforma o sistema em outro equivalente, com coeficientes inteiros.

### 5.2 Limpar os denominadores

**Sistema com quartos**

Resolva:

$$\begin{cases}\frac{x}{2}+\frac{y}{4}=5\\x+y=12\end{cases}$$

**Resolução:**

- **Passo 1:** Multiplicar a primeira equação por 4.

$$2x+y=20$$

- **Passo 2:** Subtrair a segunda equação.

$$2x-x+y-y=20-12$$

$$x=8$$

- **Passo 3:** Calcular $$y$$.

$$8+y=12$$

$$y=4$$

- **Passo 4:** Verificar na equação fracionária: $$\frac{8}{2}+\frac{4}{4}$$.

$$\frac{8}{2}+\frac{4}{4}=4+1$$

$$4+1=5$$

**Resposta:** a solução é $$(8,4)$$.

> 🔢 **Padrão:**  
> Multiplicar uma equação inteira por uma constante não nula preserva todas as suas soluções.
