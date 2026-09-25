# BL1_Capítulo 1 — Medidas de tendência central

> Seu boletim diz: prova 1 vale 2, prova 2 vale 3, trabalho vale 1, prova final vale 4. Você tirou 8, 7, 9 e 5. Sua nota final é a média simples (7,25) — ou outro número?

---

## 1. Média simples e média ponderada

Quatro notas com pesos diferentes: somar e dividir por quatro dá um número que o boletim não usa.

### 1.1 A média simples e suas duas conferências

A **média aritmética simples** distribui o total igualmente entre os valores:

$$\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

Nessa expressão, $$x_1, x_2, \ldots, x_n$$ são os valores observados, $$n$$ a quantidade deles e $$\bar{x}$$ a média. Com as notas 8, 7, 9 e 5:

$$\bar{x} = \frac{8 + 7 + 9 + 5}{4} = \frac{29}{4} = 7{,}25$$

Duas propriedades conferem qualquer média calculada:

- ela fica entre o menor e o maior valor — 7,25 está entre 5 e 9;
- a soma dos desvios em relação a ela é zero.

$$(8 - 7{,}25) + (7 - 7{,}25) + (9 - 7{,}25) + (5 - 7{,}25) = 0$$

$$0{,}75 - 0{,}25 + 1{,}75 - 2{,}25 = 0$$

Em *Theoria Motus* (1809), **Carl Friedrich Gauss (1777–1855)** mostrou que erros de medição se distribuem em torno da média. Aos 24 anos, ele usou a média das observações para reencontrar o asteroide Ceres, que a astronomia europeia tinha dado por perdido.

### 1.2 Quando os pesos mudam

A **média ponderada** multiplica cada valor pela sua importância antes de somar:

$$\bar{x}_p = \frac{\sum (x_i \cdot p_i)}{\sum p_i}$$

$$p_i$$ é o peso de cada valor e $$\bar{x}_p$$, a média ponderada. Com todos os pesos iguais, a fórmula devolve a média simples.

**Nota final do boletim**

As notas 8, 7, 9 e 5 têm pesos 2, 3, 1 e 4.

**Resolução:**

- **Passo 1:** Multiplicar cada nota pelo seu peso.

| Nota | Peso | Produto |
|---:|---:|---:|
| 8 | 2 | 16 |
| 7 | 3 | 21 |
| 9 | 1 | 9 |
| 5 | 4 | 20 |

- **Passo 2:** Somar os produtos e somar os pesos.

$$16 + 21 + 9 + 20 = 66$$

$$2 + 3 + 1 + 4 = 10$$

- **Passo 3:** Dividir um total pelo outro.

$$\bar{x}_p = \frac{66}{10} = 6{,}6$$

**Resposta:** a nota final é 6,6 — a prova final, de peso 4, puxa o resultado para baixo com mais força do que o trabalho, de peso 1, consegue puxar para cima.

> ⚠️ **Atenção:**  
> A média simples 7,25 ignora os pesos e não é a nota do boletim: peso maior significa maior influência no resultado.

---

## 2. Moda e mediana

Uma renda muito alta no meio de quatro rendas comuns muda a média sem mudar o centro do grupo.

### 2.1 Moda: o valor que mais se repete

A **moda** ($$\mathrm{Mo}$$) é o valor de maior frequência. É a única das três medidas que serve também para dados qualitativos nominais, como cor preferida.

A quantidade de valores mais frequentes classifica o conjunto:

| Classificação | Situação |
|---|---|
| Unimodal | uma moda |
| Bimodal | duas modas |
| Multimodal | três ou mais modas |
| Amodal | nenhuma repetição |

### 2.2 Mediana: o valor da posição central

A **mediana** ($$\mathrm{Md}$$) é o valor que ocupa o centro depois de ordenar os dados. Ordenar vem sempre primeiro.

A posição depende da quantidade de dados:

- $$n$$ ímpar — posição $$\frac{n+1}{2}$$;
- $$n$$ par — média dos dois valores centrais.

**Cinco rendas hipotéticas**

Considere R$ 2.000,00; R$ 2.100,00; R$ 2.100,00; R$ 2.300,00 e R$ 8.000,00, já em ordem.

**Resolução:**

- **Passo 1:** Localizar a posição central.

$$\frac{5+1}{2} = 3$$

- **Passo 2:** Identificar moda e mediana.

$$\mathrm{Mo} = \mathrm{R\$}\,2\,100{,}00$$

$$\mathrm{Md} = \mathrm{R\$}\,2\,100{,}00$$

- **Passo 3:** Calcular a média para comparar.

$$\bar{x} = \frac{2000 + 2100 + 2100 + 2300 + 8000}{5}$$

$$\bar{x} = \mathrm{R\$}\,3\,300{,}00$$

**Resposta:** moda e mediana ficam em R$ 2.100,00 e a média sobe para R$ 3.300,00 — a renda de R$ 8.000,00 puxa a média para a direita, mas não desloca o centro posicional, que continua na terceira posição.

> 🔢 **Padrão:**  
> A média se desloca com o valor extremo; a mediana permanece no centro, porque depende da posição e não da soma.

---

## 3. Amplitude e escolha da medida

Duas turmas podem ter média 7 e distribuições que não se parecem em nada.

### 3.1 O alcance dos dados

A **amplitude total** mede a distância entre os extremos:

$$AT = x_{\max} - x_{\min}$$

$$x_{\max}$$ é o maior valor, $$x_{\min}$$ o menor e $$AT$$ a amplitude, na unidade dos dados.

**Duas turmas com média 7**

Considere os conjuntos hipotéticos A = 7, 7, 7, 7, 7 e B = 0, 5, 7, 9, 14.

**Resolução:**

- **Passo 1:** Conferir as duas médias.

$$\bar{x}_A = \frac{35}{5} = 7$$

$$\bar{x}_B = \frac{35}{5} = 7$$

- **Passo 2:** Calcular as amplitudes.

$$AT_A = 7 - 7 = 0$$

$$AT_B = 14 - 0 = 14$$

**Resposta:** as médias são idênticas, mas A não varia e B se espalha por 14 pontos — o centro e o espalhamento respondem a perguntas diferentes, e a média sozinha não separa as duas turmas.

### 3.2 Qual medida usar

O **outlier** é o valor muito afastado dos demais, como o 14 do conjunto B. Ele altera média e amplitude, e pode ser tanto erro de registro quanto caso real importante: investigue antes de excluir, nunca apague automaticamente.

O tipo de dado e a pergunta feita orientam a escolha:

| Situação | Medida |
|---|---|
| Categoria nominal | moda |
| Escala ordinal | mediana ou moda |
| Valores simétricos | média |
| Valores com extremos | mediana |
| Comparar o alcance | amplitude |

Resumir bem é escolher a medida que responde à pergunta feita, e não a mais conhecida delas.

> ⚠️ **Atenção:**  
> A amplitude usa apenas dois valores do conjunto e pode mudar por completo por causa de um único outlier.
