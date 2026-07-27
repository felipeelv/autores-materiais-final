# BL2_Capítulo 4 — Modelagem com inequações

> Como traduzir limites reais em inequações e encontrar soluções viáveis?

---

## 1. Modelagem com inequações do 1º grau

### 1.1 Vocabulário e faixa viável

Algumas expressões indicam diretamente o símbolo matemático:

| Expressão | Símbolo |
|---|---|
| no máximo | $$\leq$$ |
| pelo menos | $$\geq$$ |
| menos que | $$<$$ |
| mais que | $$>$$ |

Cruze o intervalo obtido com as restrições do contexto.

### 1.2 Orçamento e restrições reais

**Serviço dentro do orçamento**

Um serviço cobra taxa fixa de R$ 80,00 e R$ 12,00 por hora. Com orçamento máximo de R$ 200,00, determine o tempo viável.

**Resolução:**

- **Passo 1:** Modelar o custo: $$80+12h\leq200$$.

- **Passo 2:** Isolar a parcela variável: $$12h\leq120$$.

- **Passo 3:** Dividir por 12: $$h\leq10$$.

- **Passo 4:** Incluir a condição física: $$h\geq0$$.

**Resposta:** O tempo viável pertence ao intervalo $$[0,10]$$ horas.

**George Dantzig** (1914–2005) criou o método simplex em 1947 e fundou a programação linear, área dedicada a decisões sob restrições. Aqui interessa apenas a ideia de região viável.

> ⚠️ **Atenção:**  
> A solução algébrica deve ser limitada pelas condições reais declaradas no problema.

---

## 2. Modelagem com inequações do 2º grau

### 2.1 Intervalo econômico

O procedimento aplicado conserva quatro etapas:

- definir a variável e sua unidade;
- escrever a função de lucro;
- resolver a condição de lucro ou prejuízo;
- interpretar raízes e intervalos no contexto.

### 2.2 Faixa de viabilidade econômica

**Faixa de preços com lucro**

Uma empresa modela o lucro, em reais, por $$L(x)=-2x^2+40x-150$$, onde $$x$$ é o preço do produto.

**Resolução:**

- **Passo 1:** Exigir lucro positivo: $$-2x^2+40x-150>0$$.

- **Passo 2:** Calcular os preços de equilíbrio.

$$-2x^2+40x-150=0$$

$$x^2-20x+75=0$$

$$(x-5)(x-15)=0$$

$$x_1=5$$

$$x_2=15$$

- **Passo 3:** Usar a concavidade para selecionar a faixa positiva: $$5<x<15$$.

$$a=-2<0$$

**Resposta:** Há lucro para preços entre R$ 5,00 e R$ 15,00; nos extremos, o lucro é zero.

> 🔢 **Padrão:**  
> As raízes de uma função de lucro são pontos de equilíbrio que delimitam faixas de lucro e prejuízo.
