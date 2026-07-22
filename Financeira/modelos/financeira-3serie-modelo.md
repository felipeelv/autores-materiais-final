# Capítulo 1 — Estatística

> Duas escolas têm média 580 no ENEM. Numa, o desvio padrão é 80; na outra, 30. São escolas iguais? E quando uma manchete grita “aumento de 200%!”, que perguntas separam o alarme real do pânico estatístico?

---

## 1. Estatística descritiva

Antes de resumir um conjunto, é preciso reconhecer o tipo de variável e a pergunta que os dados podem responder.

### 1.1 Variáveis e representações

As variáveis se organizam em quatro tipos:

| Família | Tipo | Exemplo |
|---|---|---|
| Qualitativa | nominal | cidade de nascimento |
| Qualitativa | ordinal | nível de satisfação |
| Quantitativa | discreta | número de faltas |
| Quantitativa | contínua | tempo de deslocamento |

O tipo orienta a representação:

| Objetivo | Gráfico adequado |
|---|---|
| Comparar categorias | barras |
| Mostrar evolução temporal | linha |
| Exibir partes de um total | setores |
| Distribuir variável contínua | histograma |
| Resumir quartis e outliers | box-plot |

Tabelas de frequência preservam os valores absolutos, relativos e acumulados; o gráfico destaca a forma do conjunto.

### 1.2 Escolher a medida de centro

Cada medida responde melhor a uma estrutura:

| Situação | Medida preferencial |
|---|---|
| Distribuição simétrica | média |
| Assimetria ou outlier | mediana |
| Categoria qualitativa | moda |
| Importâncias diferentes | média ponderada |

A média ponderada é:

$$\bar{x}_p=\frac{\sum x_iw_i}{\sum w_i}$$

$$x_i$$ são os valores, $$w_i$$ os pesos e $$\bar{x}_p$$ a média ponderada.

**Indicador composto hipotético**

Considere 600 com peso 2, 550 com peso 1 e 700 com peso 3.

**Resolução:**

- **Passo 1:** Somar os produtos.

$$600\cdot2+550\cdot1+700\cdot3=3850$$

- **Passo 2:** Somar os pesos e dividir.

$$\bar{x}_p=\frac{3850}{6}\approx641{,}67$$

**Resposta:** o indicador é aproximadamente 641,67; o valor 700 influencia mais o resultado porque recebeu o maior peso.

> ⚠️ **Atenção:**
>
> Nenhuma medida é “a melhor” sem considerar o tipo de variável, a distribuição e a pergunta investigada.

---

## 2. Análise crítica de dados

Uma porcentagem correta pode produzir uma conclusão enganosa quando omite a base, a escala ou o período.

### 2.1 Gráficos e percentuais

Quatro sinais pedem verificação imediata:

- eixo vertical truncado ou com intervalos desiguais;
- ausência de fonte, período ou tamanho da amostra;
- comparação de valores sem a mesma unidade;
- percentual divulgado sem a magnitude absoluta.

**Aumento de 200%**

Suponha que uma ocorrência passe de 1 caso para 3 casos.

**Resolução:**

- **Passo 1:** Calcular a variação absoluta.

$$3-1=2$$

A variação absoluta é de 2 casos.

- **Passo 2:** Calcular a variação relativa.

$$\frac{3-1}{1}\cdot100\%=200\%$$

**Resposta:** o aumento de 200% está matematicamente correto, mas representa apenas 2 casos adicionais; os dois números são necessários para dimensionar o fato.

### 2.2 Causalidade, vieses e amostra

O coeficiente de Pearson apresenta a força da correlação linear:

$$-1\leq r\leq1$$

Correlação não demonstra causalidade: duas variáveis podem acompanhar uma terceira ou coincidir por acaso.

Três vieses mudam a conclusão sem alterar as contas:

- **seleção** — a amostra exclui parte relevante da população;
- **sobrevivência** — só os casos que permaneceram são observados;
- **confirmação** — procura-se apenas evidência favorável à hipótese.

Em 1943, **Abraham Wald** mostrou o viés de sobrevivência ao estudar, nos aviões que retornavam, as áreas sem marcas de tiros.

Como ordem de grandeza, a margem de erro de uma proporção pode ser estimada por:

$$ME\approx\frac{1}{\sqrt{n}}$$

$$n$$ é o tamanho da amostra; o cálculo completo exige outros parâmetros.

Primeiro chefe do Departamento de Estatística de Harvard, em 1957, **Frederick Mosteller (1916–2006)** defendeu uma estatística aplicada e acessível ao cidadão comum.

> ⚠️ **Atenção:**
>
> Uma amostra grande continua enviesada se o método de seleção excluir sistematicamente parte da população.

---

## 3. Dispersão e comparação

Duas médias iguais não tornam duas distribuições equivalentes; o espalhamento também precisa ser medido.

### 3.1 Desvio padrão e CV

A variância amostral e o desvio padrão usam todos os desvios:

$$s^2=\frac{1}{n-1}\sum(x_i-\bar{x})^2$$

$$s=\sqrt{s^2}$$

O coeficiente de variação mede a dispersão relativa:

$$CV=\frac{s}{\bar{x}}\cdot100\%$$

$$n$$ é o tamanho da amostra, $$\bar{x}$$ a média, $$s^2$$ a variância, $$s$$ o desvio padrão e $$CV$$ uma porcentagem sem unidade.

As medidas destacam aspectos diferentes:

| Medida | O que compara | Sensibilidade a extremos |
|---|---|---|
| Amplitude | maior e menor valor | alta |
| Desvio padrão | afastamentos da média | alta |
| CV | dispersão relativa | depende da média |
| IQR | metade central dos dados | baixa |

### 3.2 Quartis e comparação

Os quartis dividem os dados ordenados em quatro partes. A amplitude interquartil é:

$$IQR=Q_3-Q_1$$

Um box-plot considera possíveis outliers fora do intervalo:

$$[Q_1-1{,}5\cdot IQR;\ Q_3+1{,}5\cdot IQR]$$

**Duas escolas hipotéticas**

Ambas têm média 580; A tem desvio padrão 80 e B, 30.

**Resolução:**

- **Passo 1:** Calcular o CV de A.

$$CV_A=\frac{80}{580}\cdot100\%\approx13{,}79\%$$

- **Passo 2:** Calcular o CV de B.

$$CV_B=\frac{30}{580}\cdot100\%\approx5{,}17\%$$

**Resposta:** a dispersão relativa de A corresponde a cerca de 2,7 vezes a de B; a média 580 não mostra que seus resultados são muito menos homogêneos.

> 🔢 **Padrão:**
>
> Comparar distribuições exige observar centro, dispersão, formato, tamanho da amostra e possíveis outliers.
