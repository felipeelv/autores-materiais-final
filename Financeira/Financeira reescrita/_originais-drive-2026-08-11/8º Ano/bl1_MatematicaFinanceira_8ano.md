# Financeira — 8º Ano · Bloco 1

> **3º Bimestre — Probabilidade e gráficos estatísticos** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Probabilidade** (3 aulas)

---

# BL1_Capítulo 1 — Probabilidade

> Em 1 dado, qual a probabilidade de NÃO sair 6? Dá para contar direto — ou calcular $$1-P(6)$$. E em 3 moedas, qual a chance de sair 3 caras seguidas?

---

## 1. Espaço amostral e eventos

Antes de calcular uma chance, é preciso listar quais resultados o experimento permite.

### 1.1 O universo de resultados

**Experimento aleatório** — procedimento cujo resultado não pode ser previsto com certeza.

O **espaço amostral** ($$\Omega$$) reúne todos os resultados possíveis. Um **evento** é um subconjunto desse espaço:

$$A \subseteq \Omega$$

No lançamento de um dado, o quadro é:

| Elemento | Conjunto | Classificação |
|---|---|---|
| $$\Omega$$ | $$\{1,2,3,4,5,6\}$$ | espaço amostral |
| $$A$$ | $$\{6\}$$ | evento simples |
| $$B$$ | $$\{2,4,6\}$$ | evento composto |

Evento simples contém um resultado; evento composto contém dois ou mais.

### 1.2 Complementares × exclusivos

O complementar de $$A$$ reúne o que está em $$\Omega$$, mas não em $$A$$:

$$\bar{A}=\Omega\setminus A$$

$$A\cup\bar{A}=\Omega$$

Eventos mutuamente exclusivos não podem ocorrer juntos:

$$A\cap B=\emptyset$$

**Classificando eventos do dado**

Considere $$C=$$ “sair 1” e $$D=$$ “sair 2”.

**Resolução:**

- **Passo 1:** Verificar a interseção.

$$C\cap D=\emptyset$$

- **Passo 2:** Verificar se a união cobre o espaço inteiro.

$$C\cup D=\{1,2\}\neq\Omega$$

**Resposta:** os eventos são mutuamente exclusivos, mas não complementares, porque deixam quatro resultados fora da união.

Em 1909, **Émile Borel (1871–1956)** sistematizou a teoria das probabilidades. Seu “macaco infinito” ilustra que um evento pode ser extremamente improvável sem ter probabilidade zero.

> ⚠️ **Atenção:**
>
> Eventos complementares sempre são exclusivos, mas eventos exclusivos não precisam completar o espaço amostral.

---

## 2. Cálculo de probabilidades

Em resultados equiprováveis, a chance compara casos favoráveis com todos os casos possíveis.

### 2.1 A fórmula e o complementar

Para um evento $$A$$ em espaço equiprovável:

$$P(A)=\frac{n(A)}{n(\Omega)}$$

Nessa expressão, $$n(A)$$ é a quantidade de casos favoráveis e $$n(\Omega)$$, o total de resultados possíveis.

As probabilidades do espaço obedecem a:

$$\sum P_i=1$$

$$P_i$$ representa a probabilidade de cada resultado elementar.

O complementar oferece um atalho:

$$P(\bar{A})=1-P(A)$$

Considere $$S$$ o evento “sair 6”. Para “não sair 6” em um dado:

$$P(\bar{S})=1-\frac{1}{6}=\frac{5}{6}\approx83{,}33\%$$

O resultado significa que cinco das seis faces atendem à condição.

### 2.2 Montar o espaço em etapas

No princípio multiplicativo, cada etapa multiplica as possibilidades:

$$n(\Omega)=n_1\cdot n_2\cdots n_k$$

$$n_1, n_2, \ldots, n_k$$ são as quantidades de opções em cada etapa.

**Pelo menos uma cara**

Três lançamentos de moeda têm duas possibilidades cada.

**Resolução:**

- **Passo 1:** Calcular o tamanho do espaço.

$$n(\Omega)=2\cdot2\cdot2=8$$

- **Passo 2:** Calcular o evento complementar, “nenhuma cara”.

Se $$A$$ representa “pelo menos uma cara”, seu complementar é “nenhuma cara”:

$$P(\bar{A})=\frac{1}{8}$$

- **Passo 3:** Usar o complementar.

$$P(A)=1-\frac{1}{8}=\frac{7}{8}$$

**Resposta:** a chance é $$\frac{7}{8}$$, ou 87,50%; contar a única sequência sem cara é mais rápido que listar as sete favoráveis.

Uma tabela dos dois dados mostra outra comparação: soma 7 ocorre em 6 dos 36 pares; soma 2 ocorre em apenas 1.

> 🔢 **Padrão:**
>
> Em etapas independentes, multiplicar as opções constrói o espaço amostral antes de calcular a probabilidade.

---

## 3. Probabilidade com múltiplos eventos

Uma árvore registra cada escolha por ramos; uma tabela cruza as possibilidades de duas etapas.

### 3.1 Duas ferramentas de enumeração

Para duas moedas, a tabela de dupla entrada evita omissões:

| 1ª moeda \ 2ª moeda | Cara | Coroa |
|---|---|---|
| Cara | cara–cara | cara–coroa |
| Coroa | coroa–cara | coroa–coroa |

A árvore apresenta o mesmo espaço em sequência: de cada primeiro resultado saem dois novos ramos. A tabela favorece cruzamentos; a árvore destaca a ordem das etapas.

### 3.2 Eventos independentes

Dois eventos são **independentes** quando o resultado de um não altera a probabilidade do outro. Nesse caso:

$$P(A\cap B)=P(A)\cdot P(B)$$

**Três caras seguidas**

Considere três lançamentos de uma moeda equilibrada e $$C_i$$ o evento “cara no lançamento $$i$$”.

**Resolução:**

- **Passo 1:** Registrar a probabilidade de cara em cada lançamento.

$$P(C_i)=\frac{1}{2}$$

- **Passo 2:** Multiplicar as três probabilidades.

$$P(C_1\cap C_2\cap C_3)=\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}$$

$$P(C_1\cap C_2\cap C_3)=\frac{1}{8}=12{,}50\%$$

**Resposta:** uma das oito sequências possíveis tem três caras; portanto, a chance é 12,50%.

Em um sorteio com reposição, devolver o item mantém as probabilidades da etapa seguinte. O mesmo raciocínio combina dado e moeda, pois o resultado de um não interfere no outro.

A moeda não “compensa” resultados passados: depois de várias coroas, a chance de cara no próximo lançamento continua igual a 50%.

> ⚠️ **Atenção:**
>
> Frequência observada no passado não altera a probabilidade do próximo resultado em tentativas independentes.
