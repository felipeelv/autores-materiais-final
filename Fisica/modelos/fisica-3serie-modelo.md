# Capítulo 1 — Campo magnético e suas fontes

> Abra a bússola do celular: a agulha aponta para o norte. Como ela “sabe”? E por que aponta para um norte que não é o do mapa — desviando cerca de 21° para oeste em São Paulo? O que é esse campo invisível, e por que a Terra inteira age como um ímã gigante?

---

## 1. Ímãs e campo magnético

Um ímã partido não separa seus polos: cada fragmento volta a apresentar norte e sul.

### 1.1 Polos e linhas de campo

Ímãs possuem polos inseparáveis. Nenhum monopolo magnético foi observado; ao cortar um ímã, formam-se dois dipolos completos.

O vetor $$\vec{B}$$ representa o campo magnético, medido em tesla (T). Suas linhas obedecem a três propriedades:

- saem do polo norte e entram no sul, externamente;
- formam curvas fechadas;
- ficam mais densas onde o campo é mais intenso.

A conversão entre unidades é:

$$1\,\mathrm{T} = 10^4\,\mathrm{G}$$

### 1.2 Intensidades e modelo terrestre

Campos magnéticos variam por muitas ordens de grandeza:

| Fonte | Campo aproximado |
|---|---:|
| Ímã de geladeira | $$5\,\mathrm{mT}$$ |
| Neodímio | $$0{,}2$$ a $$1{,}4\,\mathrm{T}$$ |
| Ressonância magnética | $$1{,}5$$ a $$3\,\mathrm{T}$$ |

Em *De Magnete* (1600), **William Gilbert (1544–1603)** usou uma esfera de magnetita, a *terrella*, para demonstrar que a Terra se comporta como um grande ímã.

> 💡 **Você sabia?**
>
> As linhas representam direção e intensidade do campo; não são trajetórias materiais ao redor do ímã.

---

## 2. Campo magnético da Terra

A bússola se alinha ao campo terrestre, mas seu norte magnético não coincide com o norte do mapa.

### 2.1 Um dipolo inclinado

O campo terrestre se aproxima do campo de um dipolo inclinado cerca de $$11^{\circ}$$ em relação ao eixo de rotação.

Sua intensidade varia conforme a região:

| Região ou referência | Campo aproximado |
|---|---:|
| Superfície terrestre | $$25$$ a $$65\,\mu\mathrm{T}$$ |
| Parte do Brasil | cerca de $$23\,\mu\mathrm{T}$$ |

O valor reduzido no Brasil integra a **Anomalia Magnética do Atlântico Sul**.

### 2.2 Norte, declinação e inclinação

A ponta norte da bússola é atraída por um polo sul magnético próximo ao norte geográfico.

Duas medidas descrevem a orientação local:

- **declinação** — ângulo horizontal entre os nortes geográfico e magnético;
- **inclinação** — ângulo do campo em relação ao plano horizontal.

Em São Paulo, a declinação é aproximadamente $$21^{\circ}$$ para oeste e muda com o tempo. Por volta de 1088, o chinês **Shen Kuo** registrou a primeira descrição conhecida desse desvio.

> ⚡ **Física no Dia a Dia:**
>
> Sistemas de navegação corrigem a declinação para converter o rumo da bússola em direção geográfica.

---

## 3. Campo de um fio retilíneo

Uma corrente elétrica em um fio cria ao redor dele um campo em círculos concêntricos.

### 3.1 Intensidade do campo

Para um fio retilíneo longo, o módulo do campo é:

$$B = \frac{\mu_0 \cdot I}{2\pi \cdot r}$$

Aqui, $$\mu_0=4\pi\times10^{-7}\,\mathrm{T \cdot m/A}$$ é a permeabilidade magnética do vácuo, e $$r$$ é a distância ao fio.

O campo aumenta com a corrente e diminui com a distância.

### 3.2 Sentido e cálculo

A regra da mão direita determina o sentido: polegar acompanha a corrente; dedos curvados indicam $$\vec{B}$$.

📝 **Exemplo:**
Para $$I=5\,\mathrm{A}$$ e $$r=0{,}10\,\mathrm{m}$$:

Dados: $$I=5\,\mathrm{A}$$ e $$r=0{,}10\,\mathrm{m}$$

$$B = \frac{\mu_0 \cdot I}{2\pi \cdot r}$$

$$B = \frac{4\pi\times10^{-7}\cdot 5}{2\pi\cdot 0{,}10}$$

$$B = 1{,}0\times10^{-5}\,\mathrm{T}$$

$$B = 10\,\mu\mathrm{T}$$

Inverter a corrente mantém o módulo e inverte o sentido das linhas circulares.

> 📏 **Medidas Impressionantes:**
>
> Nesse exemplo, o campo do fio tem a mesma ordem de grandeza do campo terrestre.

---

## 4. Espira e solenoide

Enrolar o fio faz os campos de vários trechos se somarem na região central.

### 4.1 Espira circular

No centro de uma espira circular, o campo vale:

$$B = \frac{\mu_0 \cdot I}{2R}$$

A regra da mão direita também se aplica: dedos acompanham a corrente na espira; o polegar indica o campo no eixo.

### 4.2 Solenoide ideal

No interior de um solenoide longo, o campo é aproximadamente uniforme:

$$B = \mu_0 \cdot n \cdot I$$

$$n$$ é a quantidade de espiras por metro:

$$n = \frac{N}{L}$$

Nessa relação, $$N$$ é o número de espiras e $$L$$, o comprimento do solenoide.

📝 **Exemplo:**
Para $$N=1000$$, $$L=0{,}50\,\mathrm{m}$$ e $$I=2\,\mathrm{A}$$:

Dados: $$N=1000$$, $$L=0{,}50\,\mathrm{m}$$ e $$I=2\,\mathrm{A}$$

$$n = \frac{N}{L}$$

$$n = \frac{1000}{0{,}50}$$

$$n = 2000\,\mathrm{m^{-1}}$$

$$B = \mu_0 \cdot n \cdot I$$

$$B = 4\pi\times10^{-7}\cdot 2000\cdot 2$$

$$B \approx 5{,}0\times10^{-3}\,\mathrm{T}$$

$$B \approx 5{,}0\,\mathrm{mT}$$

> 💡 **Você sabia?**
>
> O solenoide ideal concentra linhas quase paralelas no interior e apresenta polos nas extremidades.

---

## 5. Corrente elétrica e magnetismo

Uma agulha de bússola próxima a um fio muda de direção quando a corrente é ligada.

### 5.1 A observação de Ørsted

Em 21 de abril de 1820, **Hans Christian Ørsted** observou em Copenhague que uma corrente desviava uma agulha magnética.

A experiência separa duas situações:

| Estado do circuito | Agulha |
|---|---|
| Sem corrente | alinha-se ao campo terrestre |
| Com corrente | orienta-se pelo campo resultante |

Ao inverter a corrente, o desvio muda de sentido. Isso mostra que o campo criado possui orientação definida.

### 5.2 Uma fonte de campo

A descoberta estabeleceu a primeira ligação experimental direta entre eletricidade e magnetismo: cargas em movimento produzem campo magnético.

Três consequências conceituais aparecem:

- corrente elétrica é fonte de $$\vec{B}$$;
- a geometria do condutor define a forma do campo;
- correntes podem reproduzir o comportamento de ímãs.

O fio retilíneo produz círculos; a espira concentra o campo no centro; o solenoide aproxima o campo de um ímã de barra.

> 💡 **Você sabia?**
>
> O eletromagnetismo começou a se unificar quando um efeito elétrico alterou diretamente um instrumento magnético.

---

## 6. Eletroímãs e aplicações

Uma corrente percorre uma bobina e transforma um núcleo metálico em ímã controlável.

### 6.1 Como intensificar o campo

**Eletroímã** — solenoide cujo campo costuma ser ampliado por um núcleo ferromagnético.

Três mudanças aumentam sua intensidade:

- elevar a corrente elétrica;
- aumentar o número de espiras por metro;
- inserir um núcleo adequado.

Ao desligar a corrente, o campo produzido pela bobina desaparece; essa possibilidade de controle diferencia o eletroímã de um ímã permanente.

### 6.2 Usos e campo variável da Terra

O controle do campo sustenta aplicações distintas:

| Aplicação | Papel do campo |
|---|---|
| Ressonância magnética | orientar núcleos atômicos |
| Relé e trava | mover uma peça metálica |
| Tarja de cartão | registrar padrões magnéticos |

O campo terrestre também varia. O polo norte magnético deriva cerca de $$50\,\mathrm{km}$$ por ano em direção à Sibéria; por isso, o **World Magnetic Model** é atualizado a cada cinco anos.

> ⚡ **Física no Dia a Dia:**
>
> A bússola do celular depende de um modelo atualizado porque o campo terrestre não é fixo.
