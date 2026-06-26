# Mission Control AI - Sistema Inteligente de Monitorização de Missão Espacial

## 1. Contexto do Projeto
[cite_start]Este projeto foi desenvolvido como parte da **Global Solution (SUB GS2026.1)** para a unidade curricular de **Pensamento Computacional e Automação com Python**[cite: 308]. 

[cite_start]O **Mission Control AI** é um sistema computacional baseado em Python que simula a monitorização inteligente de uma missão espacial experimental[cite: 314]. [cite_start]O principal objetivo é acompanhar continuamente o funcionamento de sistemas críticos de um módulo espacial ao longo de vários ciclos de telemetria, identificando riscos, emitindo alertas automáticos e sugerindo ações recomendadas para apoiar a tomada de decisões da equipa em terra[cite: 312, 313].

## 2. Objetivos Principais
* [cite_start]Armazenar os dados de telemetria numa estrutura de matriz principal (`dados_missao`)[cite: 320, 353].
* [cite_start]Analisar múltiplos ciclos operacionais de forma automatizada[cite: 321].
* [cite_start]Gerar alertas com base em limites lógicos estabelecidos[cite: 321].
* [cite_start]Calcular a pontuação acumulada de risco por ciclo e por componente[cite: 322].
* [cite_start]Determinar a tendência evolutiva da missão (melhoria, piora ou estabilidade)[cite: 323, 467].
* [cite_start]Identificar a área operacional mais afetada por anomalias[cite: 324].
* [cite_start]Exibir um relatório analítico final formatado diretamente no terminal[cite: 325].

## 3. Estrutura de Dados Operacionais

### 3.1. Matriz `dados_missao`
[cite_start]Os dados de telemetria estão estruturados numa lista de listas (matriz), onde cada linha representa um **Ciclo de Monitorização** autónomo e cada coluna mapeia uma métrica específica na seguinte ordem estrita[cite: 356, 357, 366]:

[cite_start]`[temperatura, comunicacao, bateria, oxigenio, estabilidade]` [cite: 367]

* [cite_start]**Posição 0 - Temperatura:** Temperatura interna do módulo, expressa em °C[cite: 368].
* [cite_start]**Posição 1 - Comunicação:** Qualidade do sinal de comunicação com a base terrestre, expressa em %[cite: 368].
* [cite_start]**Posição 2 - Bateria:** Nível de energia disponível no sistema de baterias, expresso em %[cite: 368].
* [cite_start]**Posição 3 - Oxigénio:** Nível de oxigénio disponível nos sistemas de suporte à vida, expresso em %[cite: 368].
* [cite_start]**Posição 4 - Estabilidade:** Nível de estabilidade geral de hardware e software, expresso em %[cite: 368].

### 3.2. Áreas Monitorizadas
[cite_start]O sistema correlaciona os índices da matriz com uma lista de áreas monitoradas para facilitar a identificação visual nos relatórios[cite: 418, 426]:
* [cite_start]Índice 0: "Temperatura interna" [cite: 420]
* [cite_start]Índice 1: "Comunicação com a base" [cite: 421]
* [cite_start]Índice 2: "Sistema de energia" [cite: 422]
* [cite_start]Índice 3: "Suporte de oxigênio" [cite: 423]
* [cite_start]Índice 4: "Estabilidade operacional" [cite: 424]

---

## 4. Regras Lógicas de Alerta e Risco

[cite_start]Cada um dos cinco parâmetros é avaliado individualmente por funções analíticas dedicadas, sendo-lhe atribuída uma classificação e um peso numérico de risco[cite: 436, 453, 595]:
* [cite_start]**NORMAL** = 0 pontos [cite: 454]
* [cite_start]**ATENÇÃO** = 1 ponto [cite: 455]
* [cite_start]**CRÍTICO** = 2 pontos [cite: 456]

### 4.1. Limites de Classificação por Parâmetro

#### [cite_start]Temperatura Interna [cite: 441]
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 18°C | ATENÇÃO | 1 ponto |
| De 18°C até 30°C | NORMAL | 0 pontos |
| Maior que 30°C até 35°C | ATENÇÃO | 1 ponto |
| Maior que 35°C | CRÍTICO | 2 pontos |

#### [cite_start]Comunicação com a Base [cite: 443]
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 30% | CRÍTICO | 2 pontos |
| De 30% até 59% | ATENÇÃO | 1 ponto |
| 60% ou mais | NORMAL | 0 pontos |

#### [cite_start]Sistema de Energia (Bateria) [cite: 445]
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 20% | CRÍTICO | 2 pontos |
| De 20% até 49% | ATENÇÃO | 1 ponto |
| 50% ou mais | NORMAL | 0 pontos |

#### [cite_start]Suporte de Oxigénio [cite: 448]
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 80% | CRÍTICO | 2 pontos |
| De 80% até 89% | ATENÇÃO | 1 ponto |
| 90% ou mais | NORMAL | 0 pontos |

#### [cite_start]Estabilidade Operacional [cite: 450]
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 40% | CRÍTICO | 2 pontos |
| De 40% até 69% | ATENÇÃO | 1 ponto |
| 70% ou mais | NORMAL | 0 pontos |

---

## 5. Avaliação de Estado e Tendência

### 5.1. Classificação do Ciclo
[cite_start]A soma das pontuações individuais das 5 áreas resulta no risco total do ciclo (máximo de 10 pontos) [cite: 457][cite_start], que categoriza o estado da missão naquele instante[cite: 463]:
* [cite_start]**0 a 2 pontos:** MISSÃO ESTÁVEL [cite: 464]
* [cite_start]**3 a 5 pontos:** MISSÃO EM ATENÇÃO [cite: 464]
* [cite_start]**6 a 10 pontos:** MISSÃO CRÍTICA [cite: 464]

### 5.2. Análise de Tendência
[cite_start]A evolução temporal é obtida comparando o risco calculado no primeiro ciclo com o risco verificado no último ciclo de monitorização[cite: 466]:
* [cite_start]**Último ciclo > Primeiro ciclo:** Tendência de piora[cite: 472].
* [cite_start]**Último ciclo < Primeiro ciclo:** Tendência de melhora[cite: 473].
* [cite_start]**Último ciclo == Primeiro ciclo:** Permaneceu estável em relação ao início[cite: 474].

### 5.3. Área Mais Afetada
[cite_start]O programa mantém um contador cumulativo de pontos por área ao longo de toda a execução[cite: 477]. [cite_start]A área que somar o maior número de pontos de penalização de risco é identificada e destacada no relatório final como a mais prejudicada durante a operação[cite: 477, 483].

---

## 6. Estrutura do Repositório
[cite_start]O projeto está organizado conforme os requisitos exigidos para a entrega:
```text
mission-control-ai/
│
├── README.md               # Este ficheiro com a documentação do sistema
└── mission_control.py      # Código-fonte principal em Python
