# BL1_Capítulo 2 — Interpretação gráfica e classificação de sistemas

> Como os coeficientes mostram se duas retas se cruzam?

---

## 1. Equações como retas

### 1.1 Da equação ao gráfico

Toda equação do 1º grau com duas incógnitas, escrita como $$ax+by=c$$, representa uma **reta** quando $$a$$ e $$b$$ não são ambos zero. Para construí-la, escolhemos valores para uma variável e calculamos a outra.

**Tabela da reta**

Construa pontos de $$x+y=6$$.

**Resolução:**

- **Passo 1:** Isolar $$y$$.

$$y=6-x$$

- **Passo 2:** Calcular três pares.

| $$x$$ | $$y$$ | Par |
|---:|---:|---:|
| 0 | 6 | $$(0,6)$$ |
| 2 | 4 | $$(2,4)$$ |
| 6 | 0 | $$(6,0)$$ |

**Resposta:** os três pontos pertencem à mesma reta.

### 1.2 Duas equações, duas retas

Um sistema 2×2 produz duas retas no mesmo plano. Cada uma reúne os pares de sua equação; a posição entre elas revela quantas soluções são comuns.

> 🔢 **Padrão:**  
> Dois pontos determinam uma reta; um terceiro ponto calculado serve de conferência.

**Johann Heinrich Lambert** (1728–1777) relacionou resultados algébricos e geométricos em obras como *Photometria* (1760), além de provar a irracionalidade de $$\pi$$ em 1761.

---

## 2. Interseção e solução

### 2.1 Duas linguagens

**Interseção** é o encontro das retas e também a solução algébrica do sistema. O gráfico permite estimar o par; a substituição nas equações confirma os valores exatos.

Como desenhos têm precisão limitada, a leitura visual não substitui a verificação algébrica.

### 2.2 Planos de telefonia

**Custos que se igualam**

O plano A custa R$ 40,00 mais R$ 2,00 por hora. O plano B custa R$ 20,00 mais R$ 4,00 por hora.

**Resolução:**

- **Passo 1:** Escrever os custos, onde $$h$$ é o número de horas.

$$A=40+2h$$

$$B=20+4h$$

- **Passo 2:** Igualar os valores.

$$40+2h=20+4h$$

$$20=2h$$

$$h=10$$

- **Passo 3:** Calcular o custo comum.

$$A=40+2\times10$$

$$A=60$$

$$B=20+4\times10$$

$$B=60$$

**Resposta:** as retas se cruzam em $$(10,60)$$; após 10 horas, o plano A passa a custar menos.

> ⚠️ **Atenção:**  
> Um cruzamento lido no gráfico deve ser confirmado nas duas expressões originais.

---

## 3. Classificação dos sistemas

### 3.1 Os três casos

O número de interseções define a classificação:

| Sistema | Posição das retas | Soluções |
|---|---|---:|
| SPD | concorrentes | uma |
| SPI | coincidentes | infinitas |
| SI | paralelas distintas | nenhuma |

No **SPD**, as equações são compatíveis; no **SPI**, equivalentes; no **SI**, contraditórias.

### 3.2 Teste sem divisões

Considere as equações:

$$a_1x+b_1y=c_1$$

$$a_2x+b_2y=c_2$$

Os índices identificam cada equação. Produtos cruzados evitam divisões por coeficientes que podem ser zero:

- se $$a_1b_2\neq a_2b_1$$, o sistema é SPD;
- se $$a_1b_2=a_2b_1$$, com $$a_1c_2=a_2c_1$$ e $$b_1c_2=b_2c_1$$, é SPI;
- se a primeira igualdade ocorre, mas alguma das outras falha, é SI.

**Retas paralelas distintas**

Classifique:

$$\begin{cases}x+y=5\\2x+2y=8\end{cases}$$

**Resolução:**

- **Passo 1:** Comparar os coeficientes das incógnitas.

$$1\times2=1\times2$$

- **Passo 2:** Comparar um coeficiente com os termos independentes: $$1\times8\neq2\times5$$.

**Resposta:** o sistema é SI; as retas são paralelas distintas.

> ⚠️ **Atenção:**  
> Razões entre coeficientes só são seguras quando os denominadores não são zero; produtos cruzados funcionam também nos casos nulos.
