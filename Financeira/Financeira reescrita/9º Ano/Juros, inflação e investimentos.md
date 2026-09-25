# BL1_Capítulo 1 — Juros, inflação e investimentos

> R$ 1.000,00 a 1% ao mês: em 12 meses, juros simples dão R$ 1.120,00 e compostos R$ 1.126,83 — quase igual. Em 30 anos, simples dão R$ 4.600,00 e compostos R$ 35.949,64 — quase 8 vezes mais. O que muda quando o tempo muda? E a poupança "rendendo 8% ao ano" está mesmo ganhando 8% ao ano?

---

## 1. Juros simples e compostos

Uma taxa de 1% ao mês pode incidir sempre sobre o valor aplicado ou sobre o saldo que ele foi acumulando.

### 1.1 Dois regimes, duas curvas

A diferença está na base sobre a qual a taxa incide:

| | Juros simples | Juros compostos |
|---|---|---|
| A taxa incide sobre | o capital inicial | o saldo acumulado |
| Fórmula | $$M = C(1 + i \cdot n)$$ | $$M = C(1 + i)^n$$ |
| Crescimento | linear — em linha reta | exponencial — sobre o saldo |

Nas duas fórmulas, $$M$$ é o montante, $$C$$ o capital inicial, $$i$$ a taxa em decimal e $$n$$ a quantidade de períodos.

Incorporar os juros ao saldo chama-se **capitalização**: no regime composto, cada período começa de uma base maior que a do anterior. Problemas assim já apareciam no *Liber Abaci* (1202), de **Leonardo Fibonacci**.

### 1.2 O que o tempo faz com a diferença

**Aplicação hipotética de R$ 1.000,00 a 1% ao mês**

Compare os dois regimes em 12, 24 e 360 meses.

**Resolução:**

- **Passo 1:** Registrar os dados, com a taxa em decimal.

$$C = 1000 \qquad i = 0{,}01$$

- **Passo 2:** Aplicar as duas fórmulas no prazo mais longo.

$$M_s = 1000(1 + 0{,}01 \cdot 360) = \mathrm{R\$}\,4\,600{,}00$$

$$M_c = 1000(1{,}01)^{360} \approx \mathrm{R\$}\,35\,949{,}64$$

- **Passo 3:** Organizar os três prazos lado a lado.

| Prazo | Juros simples | Juros compostos |
|---|---:|---:|
| 12 meses | R$ 1.120,00 | R$ 1.126,83 |
| 24 meses | R$ 1.240,00 | R$ 1.269,73 |
| 360 meses | R$ 4.600,00 | R$ 35.949,64 |

**Resposta:** em 12 meses a diferença é de R$ 6,83, quase nada; em 360 meses o composto chega a cerca de 7,8 vezes o simples — no início a diferença é pequena, e é no prazo longo que o composto acelera.

A mesma fórmula responde à pergunta inversa, quanto seria preciso hoje para chegar a um valor futuro:

$$C = \frac{M}{(1 + i)^n}$$

> ⚠️ **Atenção:**  
> Taxa e tempo precisam usar o mesmo período — taxa mensal só combina com quantidade de meses.

---

## 2. Inflação e poder de compra

O saldo do extrato aumenta e, no mesmo período, o pão, o ônibus e a luz também sobem.

### 2.1 Preços que sobem, dinheiro que compra menos

**Inflação** — variação geral dos preços de uma cesta de consumo, e não de um produto isolado.

O efeito direto é a perda de **poder de compra**: a mesma quantia passa a comprar menos itens do que comprava antes. Por isso o rendimento de uma aplicação tem duas leituras:

- **rendimento nominal** — o percentual exibido no extrato;
- **rendimento real** — o ganho que sobra depois de descontar a inflação.

### 2.2 Do nominal ao real

A estimativa prática subtrai uma taxa da outra:

$$r_{real} \approx r_{nom} - i_{infl}$$

$$r_{real}$$ é a taxa real, $$r_{nom}$$ a nominal e $$i_{infl}$$ a inflação, todas no mesmo período.

**Ganho aparente de 8% ao ano**

Suponha uma aplicação hipotética que rendeu 8% ao ano, num período em que a inflação foi de 5% ao ano.

**Resolução:**

- **Passo 1:** Registrar as duas taxas no mesmo período.

$$r_{nom} = 8\% \qquad i_{infl} = 5\%$$

- **Passo 2:** Descontar a inflação do rendimento nominal.

$$r_{real} \approx 8\% - 5\% = 3\%$$

**Resposta:** o ganho real é de cerca de 3% ao ano — dos 8% do extrato, aproximadamente 5 pontos apenas repuseram a alta dos preços, e só o que passa disso aumenta o poder de compra.

A relação exata entre as três taxas serve de referência quando os valores são altos:

$$1 + r_{real} = \frac{1 + r_{nom}}{1 + i_{infl}}$$

Foi **Irving Fisher (1867–1947)**, em *The Theory of Interest* (1930), quem formalizou essa ligação. Quando o rendimento fica abaixo da inflação, o extrato mostra ganho e o dinheiro compra menos.

> ⚠️ **Atenção:**  
> Rendimento e inflação só podem ser comparados no mesmo intervalo — ganho no extrato não garante ganho real.

---

## 3. Noções de investimentos

Retorno, risco e liquidez respondem a perguntas diferentes, e nenhum número decide sozinho.

### 3.1 Os três critérios e as duas categorias

Toda aplicação é descrita por três características independentes entre si:

- **rentabilidade** — quanto o valor cresce ou diminui;
- **risco** — possibilidade de perda ou de oscilação;
- **liquidez** — facilidade de transformar o ativo em dinheiro.

As aplicações se dividem em duas categorias pela forma de remuneração:

| | Renda fixa | Renda variável |
|---|---|---|
| Regra de remuneração | definida na aplicação | preço e retorno podem oscilar |
| Previsibilidade | alta | nenhuma |
| Exemplos | poupança, CDB, título público | ações, fundos imobiliários |

### 3.2 Concentrar ou dividir

**Diversificar** é distribuir os recursos entre aplicações de comportamentos diferentes, para que um resultado ruim não determine o conjunto.

**Dois ativos hipotéticos**

Suponha R$ 500,00 em A, que caiu 10%, e R$ 500,00 em B, que subiu 4%.

**Resolução:**

- **Passo 1:** Atualizar cada valor.

$$A = 500(1 - 0{,}10) = \mathrm{R\$}\,450{,}00$$

$$B = 500(1 + 0{,}04) = \mathrm{R\$}\,520{,}00$$

- **Passo 2:** Somar e comparar com o valor inicial.

$$450 + 520 = \mathrm{R\$}\,970{,}00$$

$$\frac{970 - 1000}{1000} \cdot 100 = -3\%$$

**Resposta:** a carteira perdeu 3% — concentrada só em A, a perda seria de 10%; dividida entre A e B, a queda de um foi parcialmente compensada pela alta do outro. Diversificar reduz a concentração, mas não elimina perdas.

O investidor americano **Warren Buffett (1930–)**, à frente da Berkshire Hathaway desde 1965, transformou US$ 1 em cerca de US$ 30.000 em aproximadamente 60 anos, com taxa média em torno de 20% ao ano. O que sustenta esse resultado é a duração, não uma tacada isolada — e retorno passado não garante retorno futuro.

Comparar produtos exige olhar prazo, tributação, liquidez, risco e regras vigentes ao mesmo tempo, porque cada um responde a uma parte diferente da decisão.

> ⚠️ **Atenção:**  
> Entender o mecanismo de uma aplicação não é receber uma recomendação de investimento.
