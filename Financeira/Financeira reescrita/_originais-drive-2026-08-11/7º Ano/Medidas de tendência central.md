# BL1_Capítulo 1 — Medidas de tendência central

> Seu boletim diz: prova 1 vale 2, prova 2 vale 3, trabalho vale 1, prova final vale 4. Você tirou 8, 7, 9 e 5. Sua nota final é a média simples (7,25) — ou outro número?

---

## 1. Média simples e média ponderada

Quatro notas podem ter importâncias diferentes; nesse caso, somá-las e dividir por quatro distorce o resultado.

### 1.1 A média como ponto de equilíbrio

A **média aritmética simples** distribui igualmente o total entre os valores:

$$\bar{x} = \frac{x_1+x_2+\cdots+x_n}{n}$$

Nessa expressão, os elementos são:

- $$x_1, x_2, \ldots, x_n$$ — valores observados;
- $$n$$ — quantidade de valores;
- $$\bar{x}$$ — média aritmética.

Duas propriedades ajudam a conferir o resultado:

- a média fica entre o menor e o maior valor;
- a soma dos desvios em relação à média é zero.

Em 1809, **Carl Friedrich Gauss (1777–1855)** sistematizou métodos que organizavam erros de medição ao redor da média. Anos antes, médias de observações ajudaram a reencontrar o asteroide Ceres.

### 1.2 Pesos diferentes

A **média ponderada** multiplica cada valor por sua importância:

$$\bar{x}_p = \frac{\sum x_i p_i}{\sum p_i}$$

$$p_i$$ representa o peso de cada valor e $$\bar{x}_p$$, a média ponderada.

Quando todos os pesos são iguais, a fórmula devolve a média simples. O IPCA também usa ponderação: cada grupo de consumo participa conforme seu peso no orçamento familiar.

**Nota final do boletim**

As notas 8, 7, 9 e 5 têm pesos 2, 3, 1 e 4.

**Resolução:**

- **Passo 1:** Multiplicar cada nota pelo peso.

| Nota | Peso | Produto |
|---:|---:|---:|
| 8 | 2 | 16 |
| 7 | 3 | 21 |
| 9 | 1 | 9 |
| 5 | 4 | 20 |

- **Passo 2:** Somar os produtos e os pesos.

$$16+21+9+20=66$$

$$2+3+1+4=10$$

- **Passo 3:** Dividir os totais.

$$\bar{x}_p=\frac{66}{10}=6{,}6$$

**Resposta:** a nota final é 6,6; a prova final, com peso 4, influencia mais o resultado do que o trabalho, com peso 1.

> ⚠️ **Atenção:**
>
> Somar as notas sem considerar os pesos produziria 7,25, uma resposta incompatível com a regra do boletim.

---

## 2. Moda e mediana

Um valor extremo pode elevar muito a média sem alterar o centro ocupado pela maioria dos dados.

### 2.1 Moda e seus tipos

A **moda** ($$\mathrm{Mo}$$) é o valor de maior frequência e pode resumir até dados qualitativos.

O número de valores mais frequentes define quatro casos:

| Classificação | Situação |
|---|---|
| Unimodal | uma moda |
| Bimodal | duas modas |
| Multimodal | três ou mais modas |
| Amodal | nenhuma repetição |

Uma pesquisa de cor preferida, por exemplo, não admite média ou mediana, mas admite moda.

### 2.2 Mediana e valores extremos

A **mediana** ($$\mathrm{Md}$$) é o valor central depois que os dados são ordenados.

Sua posição depende da quantidade de dados:

| Quantidade | Procedimento |
|---|---|
| Ímpar | posição $$\frac{n+1}{2}$$ |
| Par | média dos dois valores centrais |

**Cinco rendas hipotéticas**

Considere R$ 2.000,00; R$ 2.100,00; R$ 2.100,00; R$ 2.300,00 e R$ 8.000,00.

**Resolução:**

- **Passo 1:** Localizar a posição mediana.

$$\frac{5+1}{2}=3$$

- **Passo 2:** Identificar moda e mediana.

$$\mathrm{Mo}=\mathrm{R\$}\,2\,100{,}00$$

$$\mathrm{Md}=\mathrm{R\$}\,2\,100{,}00$$

- **Passo 3:** Calcular a média para comparar.

$$\bar{x}=\frac{2000+2100+2100+2300+8000}{5}$$

$$\bar{x}=\mathrm{R\$}\,3\,300{,}00$$

**Resposta:** moda e mediana são R$ 2.100,00, enquanto a média sobe para R$ 3.300,00 por causa do valor extremo de R$ 8.000,00.

> 🔢 **Padrão:**
>
> A mediana resiste a extremos porque depende da posição dos dados, não da soma de seus valores.

---

## 3. Amplitude e escolha da medida

Duas turmas podem ter média 7 e, ainda assim, apresentar distribuições completamente diferentes.

### 3.1 O alcance dos dados

A **amplitude total** mede a distância entre os extremos:

$$AT=x_{\max}-x_{\min}$$

$$x_{\max}$$ é o maior valor, $$x_{\min}$$ o menor e $$AT$$ a amplitude total, todos na unidade dos dados.

**Duas turmas com média 7**

Considere os conjuntos hipotéticos A = 7, 7, 7, 7, 7 e B = 0, 5, 7, 9, 14.

**Resolução:**

- **Passo 1:** Conferir as médias.

$$\bar{x}_A=\frac{35}{5}=7$$

$$\bar{x}_B=\frac{35}{5}=7$$

- **Passo 2:** Calcular as amplitudes.

$$AT_A=7-7=0$$

$$AT_B=14-0=14$$

**Resposta:** as médias coincidem, mas A não varia e B se espalha por 14 pontos; a média sozinha esconde essa diferença.

### 3.2 Qual medida usar

O tipo e a forma dos dados orientam a escolha:

| Situação | Medida mais informativa |
|---|---|
| Categoria nominal | moda |
| Escala ordinal | mediana ou moda |
| Valores simétricos | média |
| Valores com extremos | mediana |
| Comparar alcance | amplitude |

Um **outlier** é um valor muito afastado dos demais. Ele pode ser erro de registro, mas também pode revelar um caso real importante; por isso, deve ser investigado antes de qualquer exclusão.

> ⚠️ **Atenção:**
>
> A amplitude usa apenas dois valores e pode mudar completamente por causa de um único outlier.
