# BL1_Capítulo 2 — Métodos de resolução: substituição, adição e escalonamento

> Como escolher e aplicar substituição, adição ou escalonamento?

---

## 1. Método da substituição

### 1.1 Fluxo do método

O **método da substituição** segue quatro ações:

- isolar uma incógnita;
- substituir a expressão na outra equação;
- resolver a equação resultante;
- voltar e calcular a variável restante.

### 1.2 Aplicação e verificação

**Sistema com variável de coeficiente 1**

Resolva

$$\begin{cases}2x+3y=8\\x-y=-1\end{cases}$$

**Resolução:**

- **Passo 1:** Isolar $$x$$ na segunda equação.

$$x=y-1$$

- **Passo 2:** Substituir na primeira.

$$2(y-1)+3y=8$$

$$2y-2+3y=8$$

$$5y=10$$

$$y=2$$

- **Passo 3:** Voltar à expressão isolada.

$$x=2-1$$

$$x=1$$

- **Passo 4:** Verificar na primeira equação original.

$$2\times1+3\times2=8$$

**Resposta:** A solução é $$(1,2)$$.

> ⚠️ **Atenção:**  
> A verificação final deve usar as equações originais, não apenas as transformadas.

---

## 2. Método da adição

### 2.1 Eliminação organizada

No **método da adição**, multiplicam-se equações inteiras por constantes para obter coeficientes opostos. Em seguida, somam-se os membros correspondentes.

### 2.2 Eliminação aplicada

**Eliminação de uma variável**

Resolva

$$\begin{cases}3x+2y=12\\2x-3y=-5\end{cases}$$

**Resolução:**

- **Passo 1:** Multiplicar a primeira equação por 3.

$$9x+6y=36$$

- **Passo 2:** Multiplicar a segunda por 2.

$$4x-6y=-10$$

- **Passo 3:** Somar as equações.

$$13x=26$$

$$x=2$$

- **Passo 4:** Substituir na primeira equação original.

$$3\times2+2y=12$$

$$2y=6$$

$$y=3$$

**Resposta:** A solução é $$(2,3)$$.

Escalonar é somar a uma equação um múltiplo de outra.

> ⚠️ **Atenção:**  
> Ao multiplicar uma equação, multiplique todos os termos, inclusive o membro direito.

---

## 3. Escalonamento: conceito

### 3.1 Operações e forma triangular

**Escalonar** é aplicar operações elementares até obter uma forma triangular. As operações permitidas são:

- trocar linhas;
- multiplicar uma linha por constante não nula;
- somar a uma linha um múltiplo de outra.

Na forma escalonada, cada linha começa depois da anterior; os primeiros coeficientes não nulos são os **pivôs**.

### 3.2 Aplicação e forma reduzida

**Primeira etapa de escalonamento**

Considere

$$\begin{cases}x+y=5\\2x-y=1\end{cases}$$

**Resolução:**

- **Passo 1:** Subtrair duas vezes a primeira equação da segunda.

$$-3y=-9$$

- **Passo 2:** Escrever o sistema triangular equivalente.

$$\begin{cases}x+y=5\\-3y=-9\end{cases}$$

**Resposta:** O sistema foi escalonado e a última equação já fornece $$y$$ diretamente.

**Wilhelm Jordan** (1842–1899) estendeu a eliminação de Gauss no *Handbuch der Vermessungskunde* (1873–1888). Na forma reduzida de Gauss-Jordan, também se anulam os coeficientes acima dos pivôs.

> 🔢 **Padrão:**  
> Cada pivô organiza a eliminação dos coeficientes abaixo dele.

---

## 4. Escalonamento: aplicação

### 4.1 Resolução completa

**Sistema de três incógnitas**

Resolva

$$\begin{cases}x+y+z=6\\2x-y+z=3\\x+2y-z=2\end{cases}$$

**Resolução:**

- **Passo 1:** Eliminar $$x$$ da segunda equação.

$$-3y-z=-9$$

- **Passo 2:** Eliminar $$x$$ da terceira equação.

$$y-2z=-4$$

- **Passo 3:** Eliminar $$y$$ da terceira equação transformada.

$$3(y-2z)+(-3y-z)=3\times(-4)+(-9)$$

$$-7z=-21$$

$$z=3$$

- **Passo 4:** Fazer a substituição reversa na segunda equação.

$$-3y-3=-9$$

$$-3y=-6$$

$$y=2$$

- **Passo 5:** Voltar à primeira equação.

$$x+2+3=6$$

$$x=1$$

**Resposta:** A solução é $$(1,2,3)$$.

### 4.2 Organização e classificação

O alinhamento das incógnitas em colunas evita misturar coeficientes. Na forma escalonada, uma linha $$0=0$$ indica informação redundante; uma linha $$0=k$$, com $$k\neq0$$, indica contradição.

> ⚠️ **Atenção:**  
> Substituição reversa começa na última equação não nula do sistema escalonado.
