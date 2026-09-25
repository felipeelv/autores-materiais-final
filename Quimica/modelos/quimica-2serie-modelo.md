# Capítulo 1 — Equilíbrio químico

> Se as concentrações ficam constantes no equilíbrio, a reação parou — e como o controle de um equilíbrio químico permite produzir amônia em escala industrial?

---

## 1. Reações reversíveis e equilíbrio dinâmico

No sistema NO₂/N₂O₄, a cor indica mudanças na proporção entre as duas espécies.

### 1.1 Dois sentidos simultâneos

**Reação reversível é aquela em que produtos formam reagentes enquanto reagentes formam produtos.**

$$\mathrm{N_2O_4(g)} \rightleftharpoons 2\mathrm{NO_2(g)}$$

A seta dupla indica dois processos:

- **sentido direto:** N₂O₄ origina NO₂;
- **sentido inverso:** NO₂ volta a formar N₂O₄.

Em um sistema inicialmente rico em N₂O₄:

- a velocidade direta começa maior;
- a formação de NO₂ acelera a reação inversa;
- o equilíbrio é atingido quando as velocidades se igualam;
- o sistema deve ser fechado para a matéria, mas pode trocar energia com o ambiente.

### 1.2 Constante no visível, ativo no microscópico

**Equilíbrio dinâmico é o estado em que as velocidades direta e inversa são iguais.**

$$v_{\mathrm{direta}} = v_{\mathrm{inversa}}$$

No equilíbrio:

- as velocidades direta e inversa são iguais;
- as concentrações ficam constantes, mas não precisam ser iguais;
- as reações continuam nos dois sentidos;
- cor, pressão e outras propriedades macroscópicas permanecem estáveis se temperatura e volume não mudarem.

<!-- tikz:inicio fig-01-equilibrio-dinamico-graficos -->
![Gráficos qualitativos em que as velocidades direta e inversa convergem para o mesmo valor enquanto as concentrações atingem patamares constantes diferentes](https://raw.githubusercontent.com/felipeelv/imagens-tikz/e637319bb635434380a7a194e2ad18c7e0111dfd/quimica/2serie/equilibrio-quimico/fig-01-equilibrio-dinamico-graficos.png)
<!-- tikz:fim fig-01-equilibrio-dinamico-graficos -->

---

## 2. Constante Kc e quociente Q

A composição de equilíbrio pode favorecer reagentes ou produtos, mesmo quando as duas reações continuam ocorrendo.

### 2.1 Lei da ação das massas

**Kc é a razão entre concentrações de equilíbrio, elevadas aos respectivos coeficientes estequiométricos.**

Para a reação geral:

$$a\mathrm{A(aq)} + b\mathrm{B(aq)} \rightleftharpoons c\mathrm{C(aq)} + d\mathrm{D(aq)}$$

$$K_c = \frac{[\mathrm{C}]^c[\mathrm{D}]^d}{[\mathrm{A}]^a[\mathrm{B}]^b}$$

Cato Guldberg e Peter Waage formularam a lei da ação das massas em 1864. Na expressão escolar de Kc:

- entram espécies aquosas e gasosas;
- sólidos e líquidos puros são omitidos porque suas concentrações constantes já estão incorporadas a Kc;
- os valores são tomados no equilíbrio;
- Kc depende da temperatura.

A leitura de Kc é direta:

- **Kc ≫ 1:** predominam produtos;
- **Kc ≪ 1:** predominam reagentes;
- **Kc não mede velocidade:** informa a composição do equilíbrio.

### 2.2 Comparar Q com Kc

O **quociente de reação Q** usa a mesma expressão de Kc, mas com concentrações de qualquer instante.

Para $$\mathrm{H_2(g)} + \mathrm{I_2(g)} \rightleftharpoons 2\mathrm{HI(g)}$$, considere:

- $K_c = 16$;
- $[\mathrm{H_2}] = 0{,}20\,\mathrm{mol/L}$;
- $[\mathrm{I_2}] = 0{,}20\,\mathrm{mol/L}$;
- $[\mathrm{HI}] = 0{,}40\,\mathrm{mol/L}$.

$$Q = \frac{[\mathrm{HI}]^2}{[\mathrm{H_2}][\mathrm{I_2}]}$$

$$Q = \frac{(0{,}40)^2}{(0{,}20)(0{,}20)}$$

$$Q = 4$$

Como Q < Kc, o sistema avança para a direita até Q alcançar 16.

| Comparação | Ajuste espontâneo |
|---|---|
| Q < Kc | forma mais produtos |
| Q > Kc | forma mais reagentes |
| Q = Kc | já está em equilíbrio |

---

## 3. Constante em função das pressões

Em misturas gasosas, cada componente exerce uma parcela da pressão total.

### 3.1 A expressão de Kp

**Kp é a constante de equilíbrio escrita com as pressões parciais dos gases.**

Para:

$$a\mathrm{A(g)} + b\mathrm{B(g)} \rightleftharpoons c\mathrm{C(g)} + d\mathrm{D(g)}$$

$$K_p = \frac{(P_{\mathrm{C}})^c(P_{\mathrm{D}})^d}{(P_{\mathrm{A}})^a(P_{\mathrm{B}})^b}$$

Na expressão de Kp:

- entram somente substâncias gasosas;
- os coeficientes tornam-se expoentes;
- usam-se pressões parciais no equilíbrio;
- a pressão total não aparece diretamente.

Para a síntese de amônia:

$$\mathrm{N_2(g)} + 3\mathrm{H_2(g)} \rightleftharpoons 2\mathrm{NH_3(g)}$$

$$K_p = \frac{(P_{\mathrm{NH_3}})^2}{P_{\mathrm{N_2}}(P_{\mathrm{H_2}})^3}$$

### 3.2 Relação entre Kp e Kc

Para gases com comportamento ideal:

$$K_p = K_c(RT)^{\Delta n}$$

$$\Delta n = n_{\mathrm{produtos\ gasosos}} - n_{\mathrm{reagentes\ gasosos}}$$

Na reação de formação da amônia:

$$\Delta n = 2-(1+3)$$

$$\Delta n = -2$$

$$K_p = K_c(RT)^{-2}$$

$$K_p = \frac{K_c}{(RT)^2}$$

Se Kc = 0,50 a 500 K e R = 0,082 L·atm·mol⁻¹·K⁻¹:

$$RT = 0{,}082 \cdot 500$$

$$RT = 41$$

$$K_p = \frac{0{,}50}{41^2}$$

$$K_p \approx 2{,}97 \times 10^{-4}$$

Interpretação do resultado:

- Kp pequeno indica uma razão pequena, não ausência de produtos;
- o valor corresponde à equação balanceada e à temperatura informada.

Quando há o mesmo total de mols gasosos nos dois lados, $\Delta n = 0$ e $K_p = K_c$. Exemplo:

$$\mathrm{CO(g)} + \mathrm{H_2O(g)} \rightleftharpoons \mathrm{CO_2(g)} + \mathrm{H_2(g)}$$

No cálculo:

- use R compatível com as unidades de pressão e volume;
- expresse a temperatura em kelvin;
- aplique a relação ao modelo de gases ideais.

---

## 4. Deslocamento por concentração e pressão

Alterar um sistema em equilíbrio produz um ajuste previsível em sua composição.

### 4.1 Princípio de Le Chatelier

Em 1884, **Henry Le Chatelier** formulou: um sistema em equilíbrio responde a uma perturbação minimizando seu efeito.

Para $$\mathrm{N_2(g)} + 3\mathrm{H_2(g)} \rightleftharpoons 2\mathrm{NH_3(g)}$$:

| Perturbação | Resposta predominante |
|---|---|
| adicionar N₂ ou H₂ | deslocamento para a direita |
| retirar N₂ ou H₂ | deslocamento para a esquerda |
| adicionar NH₃ | deslocamento para a esquerda |
| retirar NH₃ | deslocamento para a direita |

O ajuste consome parte do que foi adicionado ou repõe parte do que foi retirado. Ele não elimina completamente a perturbação.

### 4.2 Pressão e volume

Em equilíbrios gasosos, reduzir o volume aumenta a pressão e favorece o lado com menor número de mols de gás.

Na síntese da amônia, a compressão favorece os produtos:

<!-- tikz:inicio fig-02-pressao-na-sintese-da-amonia -->
![Comparação estequiométrica entre quatro mols gasosos nos reagentes e dois nos produtos mostrando por que maior pressão favorece a formação de amônia](https://raw.githubusercontent.com/felipeelv/imagens-tikz/e637319bb635434380a7a194e2ad18c7e0111dfd/quimica/2serie/equilibrio-quimico/fig-02-pressao-na-sintese-da-amonia.png)
<!-- tikz:fim fig-02-pressao-na-sintese-da-amonia -->

Regras de aplicação:

- aumento da pressão favorece o lado com menos mols gasosos;
- redução da pressão favorece o lado com mais mols gasosos;
- números iguais de mols gasosos nos dois lados não produzem deslocamento;
- sólidos e líquidos não entram na contagem;
- a composição muda até o mesmo K ser restabelecido, se a temperatura permanecer constante.

No sistema NO₂/N₂O₄, a compressão muda as proporções e a cor da mistura.

---

## 5. Temperatura, catalisador e grau de equilíbrio

A temperatura é a perturbação que modifica o valor da constante de equilíbrio.

### 5.1 Calor como participante

Na síntese da amônia, o sentido direto é exotérmico:

$$\mathrm{N_2(g)} + 3\mathrm{H_2(g)} \rightleftharpoons 2\mathrm{NH_3(g)} \qquad \Delta H \approx -92\,\mathrm{kJ}$$

O efeito térmico pode ser previsto:

- aumentar a temperatura favorece o sentido endotérmico, para a esquerda;
- diminuir a temperatura favorece o sentido exotérmico, para a direita;
- ao mudar a temperatura, mudam Kc e Kp.

Um **catalisador**:

- reduz a energia de ativação nos dois sentidos;
- acelera a chegada ao equilíbrio;
- não altera K;
- não altera a composição final.

### 5.2 Quanto a reação avançou

**Grau de equilíbrio, α, é a fração da quantidade inicial de um reagente que foi consumida até o equilíbrio.**

$$\alpha = \frac{n_{\mathrm{reagido}}}{n_{\mathrm{inicial}}}$$

Leitura de α:

- $0 \leq \alpha \leq 1$;
- em porcentagem, varia de 0% a 100%;
- $\alpha = 0$: nenhum consumo;
- $\alpha = 1$: consumo total do reagente de referência.

Se havia 2,0 mol de um reagente e 0,80 mol reagiu:

$$\alpha = \frac{0{,}80}{2{,}0}$$

$$\alpha = 0{,}40$$

$$\alpha = 40\%$$

α e K têm funções diferentes:

- **α:** quanto a reação avançou para um reagente e uma mistura específicos;
- **K:** composição característica do equilíbrio em determinada temperatura.

---

## 6. Aplicações industriais e naturais

Controlar equilíbrios permite aumentar rendimento sem ignorar velocidade, custo, segurança e consumo energético.

### 6.1 Amônia e ácido sulfúrico

No processo Haber-Bosch, nitrogênio e hidrogênio formam amônia:

$$\mathrm{N_2(g)} + 3\mathrm{H_2(g)} \rightleftharpoons 2\mathrm{NH_3(g)}$$

Fritz Haber desenvolveu a rota química; Carl Bosch a adaptou à escala industrial.

A indústria combina:

- pressão elevada, que favorece o lado com menos gás;
- temperatura moderadamente alta, compromisso entre rendimento e velocidade;
- catalisador à base de ferro, que acelera a chegada ao equilíbrio;
- retirada contínua de NH₃, que favorece nova formação do produto.

<!-- tikz:inicio fig-03-fluxo-haber-bosch -->
![Fluxo do processo Haber-Bosch com compressão, reator catalítico, resfriamento, retirada de amônia e recirculação de nitrogênio e hidrogênio](https://raw.githubusercontent.com/felipeelv/imagens-tikz/e637319bb635434380a7a194e2ad18c7e0111dfd/quimica/2serie/equilibrio-quimico/fig-03-fluxo-haber-bosch.png)
<!-- tikz:fim fig-03-fluxo-haber-bosch -->

A amônia é matéria-prima de fertilizantes nitrogenados. O processo de contato aplica raciocínio semelhante à produção de ácido sulfúrico:

$$2\mathrm{SO_2(g)} + \mathrm{O_2(g)} \rightleftharpoons 2\mathrm{SO_3(g)}$$

Essa etapa é exotérmica e utiliza catalisador, frequentemente baseado em V₂O₅.

### 6.2 Equilíbrios em sistemas vivos e ambientais

Dois exemplos:

- **oceanos:** CO₂ dissolvido participa de equilíbrios entre dióxido de carbono, ácido carbônico e íons carbonato; alterar o CO₂ muda essas proporções e afeta organismos com estruturas calcárias;
- **sangue:** a hemoglobina liga-se reversivelmente ao oxigênio:

  $$\mathrm{Hb} + \mathrm{O_2} \rightleftharpoons \mathrm{HbO_2}$$

  - **pulmões:** mais O₂ favorece a oxigenação da hemoglobina;
  - **tecidos:** o consumo de O₂ favorece sua liberação.
