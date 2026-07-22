# Acompanhamento de criação — Operações

> Controle dos capítulos do 3º bimestre de 2026. Esta pasta registra o trabalho; `Segundo Semestre/Operações` recebe somente capítulos revisados e aprovados.

**Última atualização:** 22/07/2026

## Regra atual de extensão e forma

A primeira revisão adotou 150–190 palavras por aula, com teto de 220. Após a leitura do conjunto completo, esse padrão ainda produzia prosa demais para uma disciplina operacional.

A revisão de concisão substitui esse padrão por:

- preferir **90–130 palavras visíveis por aula**;
- **teto firme de 170 palavras**;
- não há mínimo obrigatório;
- blocos MathJax e esquemas ASCII não entram na contagem;
- enunciados, passos, respostas, boxes e texto de tabelas entram na contagem;
- cada aula começa diretamente em `### N.1`, sem repetir o título em outro parágrafo;
- usar uma frase por parágrafo sempre que possível, nunca mais de duas;
- o recorte do blueprint nunca é retirado para reduzir texto;
- o procedimento deve aparecer em passos, com **uma operação por linha**.
- toda explicação deve ser **direta e concisa**: uma frase para a decisão, sem repetir em prosa o que a conta já mostra.

O `AUTOR.md`, o `_MEMORIA.md` e o `validar-capitulo.py` da disciplina já foram atualizados com essa regra.

## Visão geral

| Situação | Capítulos | Aulas |
|---|---:|---:|
| Prontos na pasta oficial | 43 | 168 |
| Existentes no acervo antigo, aguardando revisão | 0 | 0 |
| Pendentes de criação | 0 | 0 |
| **Total do 3º bimestre** | **43** | **168** |

**Pasta dos arquivos antigos:** `Reorganizacao-2026-2Semestre/conteudos-prontos/Operacoes`.

**Pasta oficial:** `Segundo Semestre/Operações`. Ela contém somente os 43 capítulos revisados e aprovados.

## Plano executado

A produção foi dividida em quatro frentes independentes, sempre em ordem de capítulo dentro de cada faixa:

| Frente | Escopo | Capítulos | Aulas | Responsabilidade |
|---|---|---:|---:|---|
| 1 | 6º e 7º anos | 11 | 48 | agente de produção |
| 2 | 8º e 9º anos | 13 | 48 | agente de produção |
| 3 | 1ª e 2ª séries | 13 | 48 | agente de produção |
| 4 | 3ª série | 6 | 24 | agente principal |
| **Total** | **6º ano à 3ª série** | **43** | **168** | — |

Durante a produção, nenhum validador, contador ou auditoria mecânica foi executado. A validação ocorreu somente depois que os 43 capítulos estavam escritos, nesta ordem:

1. conferir quantidade, títulos, numeração e correspondência com os blueprints;
2. validar estrutura editorial e extensão de todas as aulas;
3. verificar MathJax, condições de validade e uma operação por linha;
4. recalcular exemplos e conferir resultados simplificados;
5. corrigir todas as falhas e repetir a bateria completa;
6. publicar apenas o conjunto integralmente aprovado na pasta oficial.

Todas as etapas foram concluídas em 22/07/2026.

## Resultado da validação final da revisão enxuta

- **43 de 43 capítulos aprovados** pelo validador local;
- **168 de 168 aulas** presentes e numeradas conforme os blueprints;
- **0 aulas acima do teto firme de 170 palavras**;
- média de **121,1 palavras visíveis por aula**, com faixa de 60 a 170;
- redução de **17,3 palavras por aula**, em média, em relação à primeira versão aprovada;
- **2.287 expressões MathJax** verificadas, sem delimitadores, chaves, porcentagens ou comandos incompatíveis;
- **185 exemplos completos** localizados, com resolução e resposta;
- correspondência de títulos, quantidade de aulas, tópicos e restrições `NÃO ANTECIPAR` conferida por série;
- cópia oficial conferida como idêntica ao conjunto validado.

A faixa preferencial de 90–130 palavras não é mínimo obrigatório. Aulas abaixo dela foram mantidas quando o procedimento, o exemplo e todo o recorte do blueprint já estavam completos.

## Padrão de notação e resolução vertical

**Capítulo piloto:** 7º ano, Capítulo 2 — Operações com frações.

**Situação:** aprovado pelo Felipe e aplicado aos 43 capítulos.

- multiplicação escrita com `\times` → $$\times$$, nunca `\cdot` → $$\cdot$$;
- a fração ou expressão trabalhada aparece no texto do passo;
- abaixo do passo ficam somente as operações necessárias, uma por linha;
- a fração obtida volta ao texto ou à resposta, sem linha solta apenas com o resultado;
- nenhuma resolução compactada em uma cadeia de igualdades;
- explicações curtas, diretas e restritas à decisão de cada passo.

## Resultado da reorganização global

- **43 de 43 capítulos aprovados** pelo validador local;
- **168 de 168 aulas** preservadas conforme os blueprints;
- **185 exemplos** com resolução e resposta;
- **2.404 expressões MathJax** conferidas;
- média de **121,9 palavras visíveis por aula**, com faixa de 60 a 170;
- **0 aulas acima do teto firme de 170 palavras**;
- **0 usos de `\cdot`**, **0 cálculos iniciados por `=`** e **0 cadeias de igualdades nas resoluções**;
- respostas finais preservadas em relação ao conjunto matematicamente aprovado;
- conjunto validado publicado em `Segundo Semestre/Operações`.

## Diagnóstico inicial dos 19 capítulos existentes

### Extensão

- 84 aulas analisadas;
- média anterior de **238,2 palavras de conteúdo por aula**;
- faixa anterior de **140 a 377 palavras**;
- **49 aulas** excedem o teto firme de 220;
- **69 aulas** ultrapassam a faixa preferencial de 190;
- os 19 capítulos reprovavam o validador com a nova regra.

### Fórmulas e operações

A conferência estática encontrou **1.283 expressões MathJax**:

- todos os delimitadores `$$...$$` estão pareados;
- todas as chaves estão balanceadas;
- nenhum `%` sem escape foi encontrado dentro de fórmula;
- nenhum acento incompatível foi encontrado em `\text{}`;
- os **65 exemplos resolvidos** tiveram seus resultados aritméticos e algébricos recalculados.

Os cálculos finais dos exemplos estavam corretos, mas a apresentação e algumas afirmações matemáticas precisavam ser revistas. Todos os pontos abaixo foram corrigidos na versão final:

- 32 blocos usam `\quad` ou `\qquad` para justapor expressões;
- 144 blocos concentram duas ou mais igualdades, candidatos a desdobramento;
- 18 frações numéricas usam barra simples em vez de `\frac{}{}`;
- os 65 exemplos usam a frase “Veja o exemplo abaixo.”, incompatível com o modelo atual, e precisam receber um nome de situação em negrito;
- **7º ano, Capítulo 1:** trocar “forma irredutível positiva” por “forma irredutível com denominador positivo”;
- **7º ano, Capítulo 2:** restringir as afirmações sobre aumentar ou diminuir ao multiplicar a valores positivos e fatores entre 0 e 1 ou maiores que 1;
- **8º ano, Capítulo 2:** o teste por razões precisa prever coeficientes nulos ou ser escrito por proporcionalidade/produtos cruzados;
- **9º ano, Capítulo 1:** substituir “quadrado dá positivo” por “quadrado é não negativo”;
- **9º ano, Capítulo 2:** explicitar o cuidado com `\sqrt{4a^2}=2|a|` na dedução, preservando a fórmula final de Bhaskara;
- **9º ano, Capítulo 3:** corrigir `\sqrt{x^2}=x` para `\sqrt{x^2}=|x|` nas duas ocorrências;
- **2ª série, Capítulos 1 e 3:** o critério `\det A=0` com todos os `\det A_i=0` não basta, em geral, para classificar sistemas de ordem 3 ou maior; restringir o teste ou usar posto/Rouché-Capelli;
- **3ª série, Capítulo 1:** declarar `x_1 \neq x_2` na fórmula da taxa de variação;
- **3ª série, Capítulo 2:** declarar `a>0` nas equivalências de inequações modulares;
- **3ª série, Capítulo 3:** declarar `x>0` e `y>0` nas propriedades dos logaritmos.

### Cobertura dos blueprints

Os 19 capítulos existentes cobriam as aulas e os tópicos previstos no Bloco 1. A revisão preservou essa cobertura e corrigiu concisão, notação, rigor e formato dos exemplos.

## Critérios para marcar um capítulo como concluído

- [x] Todas as aulas e todos os itens do blueprint estão cobertos.
- [x] Nenhum item da lista NÃO ANTECIPAR aparece.
- [x] Cada aula prefere 90–130 palavras e não ultrapassa 170.
- [x] A explicação é curta; o procedimento está em passos numerados.
- [x] A explicação é direta e concisa, sem repetir a operação em prosa.
- [x] Cada operação do exemplo resolvido ocupa sua própria linha.
- [x] Todas as contas foram refeitas independentemente.
- [x] Resultados estão simplificados e têm unidade quando necessária.
- [x] Fórmulas seguem MathJax e todas as variáveis/condições estão definidas.
- [x] O validador local termina sem falhas.
- [x] O arquivo foi salvo na pasta oficial e esta lista foi atualizada.

## Sequência 1 — capítulos revisados

| Ordem | Ano/série | Capítulo | Aulas | Média antes da revisão | Aulas acima de 220 antes da revisão | Situação |
|---:|---|---|---:|---:|---:|---|
| 1 | 6º ano | 1 — Conceito e comparação de frações | 7 | 253,1 | 5 | [x] Concluído |
| 2 | 6º ano | 2 — Operações com frações | 5 | 246,2 | 5 | [x] Concluído |
| 3 | 7º ano | 1 — Representação e comparação de racionais | 4 | 269,5 | 3 | [x] Concluído |
| 4 | 7º ano | 2 — Operações com frações | 8 | 205,4 | 2 | [x] Concluído |
| 5 | 8º ano | 1 — Métodos de resolução de sistemas | 5 | 235,0 | 2 | [x] Concluído |
| 6 | 8º ano | 2 — Interpretação gráfica e classificação de sistemas | 3 | 280,3 | 3 | [x] Concluído |
| 7 | 8º ano | 3 — Problemas e modelagem com sistemas | 4 | 249,2 | 3 | [x] Concluído |
| 8 | 9º ano | 1 — Equações incompletas | 4 | 241,8 | 1 | [x] Concluído |
| 9 | 9º ano | 2 — Fórmula de Bhaskara e relações entre raízes | 5 | 206,0 | 2 | [x] Concluído |
| 10 | 9º ano | 3 — Fatoração algébrica | 3 | 245,7 | 2 | [x] Concluído |
| 11 | 1ª série | 1 — Elementos e gráfico da função quadrática | 6 | 212,5 | 1 | [x] Concluído |
| 12 | 1ª série | 2 — Estudo do sinal, forma canônica e gráficos | 3 | 274,3 | 2 | [x] Concluído |
| 13 | 1ª série | 3 — Otimização e modelagem | 3 | 322,0 | 3 | [x] Concluído |
| 14 | 2ª série | 1 — Conceito e classificação de sistemas lineares | 3 | 285,3 | 3 | [x] Concluído |
| 15 | 2ª série | 2 — Métodos de resolução: substituição, adição e escalonamento | 4 | 231,2 | 3 | [x] Concluído |
| 16 | 2ª série | 3 — Determinantes, Cramer e discussão de sistemas | 5 | 203,8 | 3 | [x] Concluído |
| 17 | 3ª série | 1 — Funções afim e quadrática | 4 | 232,0 | 2 | [x] Concluído |
| 18 | 3ª série | 2 — Função modular, composta e inversa | 4 | 196,2 | 1 | [x] Concluído |
| 19 | 3ª série | 3 — Funções exponencial e logarítmica | 4 | 240,8 | 3 | [x] Concluído |

## Sequência 2 — capítulos criados

| Ordem | Ano/série | Capítulo | Aulas | Situação |
|---:|---|---|---:|---|
| 20 | 6º ano | 3 — Representação e comparação de decimais | 5 | [x] Concluído |
| 21 | 6º ano | 4 — Operações com decimais | 4 | [x] Concluído |
| 22 | 6º ano | 5 — Porcentagem | 3 | [x] Concluído |
| 23 | 7º ano | 3 — Operações com decimais | 4 | [x] Concluído |
| 24 | 7º ano | 4 — Potenciação de racionais | 3 | [x] Concluído |
| 25 | 7º ano | 5 — Radiciação e números irracionais | 3 | [x] Concluído |
| 26 | 7º ano | 6 — Razão e proporção | 2 | [x] Concluído |
| 27 | 8º ano | 4 — Forma geral e equações ax² = 0 | 3 | [x] Concluído |
| 28 | 8º ano | 5 — Equações ax² + c = 0 | 3 | [x] Concluído |
| 29 | 8º ano | 6 — Equações ax² + bx = 0 | 4 | [x] Concluído |
| 30 | 8º ano | 7 — Comparação entre tipos e situações-problema | 2 | [x] Concluído |
| 31 | 9º ano | 4 — Definição e gráfico da função quadrática | 5 | [x] Concluído |
| 32 | 9º ano | 5 — Vértice e eixo de simetria | 3 | [x] Concluído |
| 33 | 9º ano | 6 — Discriminante e construção de gráficos | 4 | [x] Concluído |
| 34 | 1ª série | 4 — Inequações do 1º grau e com módulo | 4 | [x] Concluído |
| 35 | 1ª série | 5 — Inequações do 2º grau | 3 | [x] Concluído |
| 36 | 1ª série | 6 — Sistemas de inequações, produto e quociente | 3 | [x] Concluído |
| 37 | 1ª série | 7 — Modelagem com inequações | 2 | [x] Concluído |
| 38 | 2ª série | 4 — Conceitos fundamentais de polinômios | 6 | [x] Concluído |
| 39 | 2ª série | 5 — Operações com polinômios | 4 | [x] Concluído |
| 40 | 2ª série | 6 — Teoremas do resto e de D'Alembert | 2 | [x] Concluído |
| 41 | 3ª série | 4 — Matrizes, determinantes e sistemas lineares | 6 | [x] Concluído |
| 42 | 3ª série | 5 — Polinômios | 2 | [x] Concluído |
| 43 | 3ª série | 6 — Progressões aritméticas e geométricas | 4 | [x] Concluído |

## Rotina utilizada capítulo a capítulo

Para cada item da sequência, foi aplicada esta rotina:

1. ler o capítulo correspondente no blueprint e sua lista NÃO ANTECIPAR;
2. revisar o arquivo antigo ou produzir o novo conteúdo;
3. recalcular fórmulas, exemplos e respostas;
4. verificar concisão, uma operação por linha e condições de validade;
5. rodar o validador local;
6. salvar na pasta oficial somente após aprovação integral;
7. marcar o item como concluído, com data, faixa de palavras e observações.

## Registro de conclusão

| Data | Ordem | Capítulo | Validação | Destino oficial |
|---|---:|---|---|---|
| 22/07/2026 | 1, 2, 20–22 | 6º ano — 5 capítulos, 24 aulas | Aprovado | `Operações/6º Ano` |
| 22/07/2026 | 3, 4, 23–26 | 7º ano — 6 capítulos, 24 aulas | Aprovado | `Operações/7º Ano` |
| 22/07/2026 | 5–7, 27–30 | 8º ano — 7 capítulos, 24 aulas | Aprovado | `Operações/8º Ano` |
| 22/07/2026 | 8–10, 31–33 | 9º ano — 6 capítulos, 24 aulas | Aprovado | `Operações/9º Ano` |
| 22/07/2026 | 11–13, 34–37 | 1ª série — 7 capítulos, 24 aulas | Aprovado | `Operações/1ª Série` |
| 22/07/2026 | 14–16, 38–40 | 2ª série — 6 capítulos, 24 aulas | Aprovado | `Operações/2ª Série` |
| 22/07/2026 | 17–19, 41–43 | 3ª série — 6 capítulos, 24 aulas | Aprovado | `Operações/3ª Série` |
| 22/07/2026 | 1–43 | Reorganização visual global — 43 capítulos, 168 aulas | Aprovado | `Operações` |
