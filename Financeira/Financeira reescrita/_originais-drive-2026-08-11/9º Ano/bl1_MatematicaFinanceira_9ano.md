# Financeira — 9º Ano · Bloco 1

> **3º Bimestre — Educação financeira e probabilidade** · Bloco 1 (05/08–25/08)

**Capítulos deste bloco**

1. **Juros, inflação e investimentos** (3 aulas)

---

# BL1_Capítulo 1 — Juros, inflação e investimentos

> R$ 1.000,00 a 1% ao mês: em 12 meses, juros simples dão R$ 1.120,00 e compostos R$ 1.126,83 — quase igual. Em 30 anos, simples dão R$ 4.600,00 e compostos R$ 35.949,64 — quase 8 vezes mais. O que muda quando o tempo muda? E a poupança “rendendo 8% ao ano” está mesmo ganhando 8% ao ano?

---

## 1. Juros simples e compostos

Uma taxa de 1% ao mês pode incidir sempre sobre o capital inicial ou sobre o saldo acumulado.

### 1.1 Dois regimes de crescimento

Nos **juros simples**, o acréscimo por período é constante:

$$M=C(1+i\cdot t)$$

Nos **juros compostos**, cada período incorpora os juros ao saldo:

$$M=C(1+i)^t$$

Nessas expressões, os elementos são:

- $$M$$ — montante final;
- $$C$$ — capital inicial;
- $$i$$ — taxa decimal por período;
- $$t$$ — quantidade de períodos.

| Regime | Base dos juros | Crescimento |
|---|---|---|
| Simples | capital inicial | linear |
| Composto | saldo acumulado | exponencial |

Problemas de capitalização composta já apareciam no *Liber Abaci* (1202), de Fibonacci. Séculos depois, Jacob Bernoulli relacionou capitalizações cada vez mais frequentes ao número $$e\approx2{,}718$$.

**O efeito do tempo**

Considere R$ 1.000,00 a 1% ao mês durante 360 meses.

**Resolução:**

- **Passo 1:** Registrar os dados.

$$C=1000 \qquad i=0{,}01 \qquad t=360$$

- **Passo 2:** Calcular o montante simples.

$$M_s=1000(1+0{,}01\cdot360)$$

$$M_s=\mathrm{R\$}\,4\,600{,}00$$

- **Passo 3:** Calcular o montante composto.

$$M_c=1000(1+0{,}01)^{360}$$

$$M_c\approx\mathrm{R\$}\,35\,949{,}64$$

**Resposta:** após 30 anos, o composto é cerca de 7,8 vezes o simples; a diferença cresce porque cada juro passa a integrar a base do período seguinte.

A evolução evidencia quando os regimes se afastam:

| Prazo | Juros simples | Juros compostos |
|---|---:|---:|
| 12 meses | R$ 1.120,00 | R$ 1.126,83 |
| 24 meses | R$ 1.240,00 | R$ 1.269,73 |
| 360 meses | R$ 4.600,00 | R$ 35.949,64 |

No início, a diferença é pequena; em prazos longos, o crescimento exponencial domina o linear.

### 1.2 Tempo e capital inicial

Para descobrir quanto seria necessário hoje, isola-se o capital:

$$C=\frac{M}{(1+i)^t}$$

A **regra de 72** estima em quantos períodos uma taxa dobra um valor:

$$t\approx\frac{72}{i\cdot100}$$

Com 1% ao mês, a estimativa é 72 meses. É uma aproximação, não uma promessa de resultado.

> ⚠️ **Atenção:**
>
> Taxa e tempo precisam usar o mesmo período: taxa mensal combina com quantidade de meses.

---

## 2. Inflação e poder de compra

Um saldo pode aumentar no extrato e, mesmo assim, comprar menos produtos e serviços.

### 2.1 O que os índices medem

**Inflação** — aumento geral dos preços, medido pela variação de uma cesta de consumo.

Dois índices brasileiros têm finalidades diferentes:

| Índice | Instituição | Uso de referência |
|---|---|---|
| IPCA | IBGE | inflação oficial ao consumidor |
| IGP-M | FGV | contratos, inclusive alguns aluguéis |

O IPCA acumulou 4,64% nos 12 meses encerrados em junho de 2026, segundo o IBGE. Isso não significa que cada preço subiu 4,64%: os itens variam de modo diferente e recebem pesos conforme a cesta.

### 2.2 Rendimento nominal × real

O rendimento **nominal** é o percentual exibido; o **real** desconta a perda do poder de compra. Uma aproximação prática é:

$$r_r\approx r_n-i_{inf}$$

$$r_r$$ é a taxa real, $$r_n$$ a nominal e $$i_{inf}$$ a inflação, todas no mesmo período.

A relação exata de Fisher é:

$$1+r_r=\frac{1+r_n}{1+i_{inf}}$$

**Ganho aparente de 8%**

Suponha uma aplicação hipotética com rendimento de 8% ao ano no período em que a inflação foi 4,64%.

**Resolução:**

- **Passo 1:** Aplicar a aproximação.

$$r_r\approx8\%-4{,}64\%$$

$$r_r\approx3{,}36\%$$

- **Passo 2:** Conferir pela relação exata.

$$r_r=\frac{1+0{,}08}{1+0{,}0464}-1$$

$$r_r\approx3{,}21\%$$

**Resposta:** o saldo cresceu 8% nominalmente, mas o ganho real foi aproximadamente 3,21%; a subtração forneceu a estimativa próxima de 3,36%.

> ⚠️ **Atenção:**
>
> Comparar rendimento e inflação exige o mesmo intervalo, como 12 meses com 12 meses.

---

## 3. Noções de investimentos

Rentabilidade, risco e liquidez descrevem aspectos diferentes; nenhum número isolado determina uma decisão responsável.

### 3.1 Mecanismos e riscos

As categorias diferem pela forma de remuneração e pela possibilidade de oscilação:

| Categoria | Exemplos | Característica principal |
|---|---|---|
| Renda fixa | poupança, CDB, título público | regra de remuneração definida |
| Renda variável | ações, fundos imobiliários | preço e retorno oscilam |

**Liquidez** indica a facilidade de transformar o ativo em dinheiro. **Risco** inclui possibilidade de perda, atraso ou oscilação de preço; maior retorno potencial costuma vir acompanhado de maior incerteza.

Em 2026, o FGC informava garantia ordinária de até R$ 250.000,00 por CPF ou CNPJ e por instituição ou conglomerado para depósitos cobertos, com regras e limites próprios. Títulos públicos seguem outro regime e também podem oscilar antes do vencimento.

### 3.2 Diversificação e concentração

Diversificar reduz a dependência de um único resultado, mas não elimina perdas.

**Dois ativos hipotéticos**

Suponha R$ 500,00 em A, que caiu 10%, e R$ 500,00 em B, que subiu 4%.

**Resolução:**

- **Passo 1:** Atualizar os dois valores.

$$A=500(1-0{,}10)=\mathrm{R\$}\,450{,}00$$

$$B=500(1+0{,}04)=\mathrm{R\$}\,520{,}00$$

- **Passo 2:** Somar e comparar com o capital inicial.

$$M=450+520=\mathrm{R\$}\,970{,}00$$

$$\frac{970-1000}{1000}\cdot100=-3\%$$

**Resposta:** a carteira perdeu 3%, menos que a queda de 10% de A; B reduziu a concentração do prejuízo, sem impedir resultado negativo.

O investidor americano **Warren Buffett (1930–)** destacou, em cartas anuais da Berkshire Hathaway, o efeito da capitalização mantida por décadas. Seu histórico ilustra o papel do tempo, mas retorno passado não garante retorno futuro.

> ⚠️ **Atenção:**
>
> Comparar produtos exige observar prazo, tributação, liquidez, risco e regras vigentes, sem transformar uma taxa isolada em recomendação.
