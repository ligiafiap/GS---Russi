# Mission Control AI - Sistema Inteligente de Monitorização de Missão Espacial

## 1. Contexto do Projeto
Este projeto foi desenvolvido como parte da **Global Solution** para a unidade curricular de **Pensamento Computacional e Automação com Python**. 

O **Mission Control AI** é um sistema computacional baseado em Python que simula a monitorização inteligente de uma missão espacial experimental. O principal objetivo é acompanhar continuamente o funcionamento de sistemas críticos de um módulo espacial ao longo de vários ciclos de telemetria, identificando riscos, emitindo alertas automáticos e sugerindo ações recomendadas para apoiar a tomada de decisões da equipa em terra.

## 2. Objetivos Principais
* Armazenar os dados de telemetria numa estrutura de matriz principal (`dados_missao`).
* Analisar múltiplos ciclos operacionais de forma automatizada.
* Gerar alertas com base em limites lógicos estabelecidos.
* Calcular a pontuação acumulada de risco por ciclo e por componente.
* Determinar a tendência evolutiva da missão (melhoria, piora ou estabilidade).
* Identificar a área operacional mais afetada por anomalias.
* Exibir um relatório analítico final formatado diretamente no terminal.

## 3. Estrutura de Dados Operacionais

### 3.1. Matriz `dados_missao`
Os dados de telemetria estão estruturados numa lista de listas (matriz), onde cada linha representa um **Ciclo de Monitorização** autónomo e cada coluna mapeia uma métrica específica na seguinte ordem estrita:

`[temperatura, comunicacao, bateria, oxigenio, estabilidade]` 

* **Posição 0 - Temperatura:** Temperatura interna do módulo, expressa em °C].
* **Posição 1 - Comunicação:** Qualidade do sinal de comunicação com a base terrestre, expressa em %.
* ]**Posição 2 - Bateria:** Nível de energia disponível no sistema de baterias, expresso em %.
* **Posição 3 - Oxigénio:** Nível de oxigénio disponível nos sistemas de suporte à vida, expresso em %].
* **Posição 4 - Estabilidade:** Nível de estabilidade geral de hardware e software, expresso em %].

### 3.2. Áreas Monitorizadas
O sistema correlaciona os índices da matriz com uma lista de áreas monitoradas para facilitar a identificação visual nos relatórios:
* Índice 0: "Temperatura interna" 
* Índice 1: "Comunicação com a base" 
* Índice 2: "Sistema de energia" 
* Índice 3: "Suporte de oxigênio" 
* Índice 4: "Estabilidade operacional" 

---

## 4. Regras Lógicas de Alerta e Risco

Cada um dos cinco parâmetros é avaliado individualmente por funções analíticas dedicadas, sendo-lhe atribuída uma classificação e um peso numérico de risco:
* **NORMAL** = 0 pontos 
* **ATENÇÃO** = 1 ponto 
* **CRÍTICO** = 2 pontos 

### 4.1. Limites de Classificação por Parâmetro

#### Temperatura Interna 
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

#### Sistema de Energia (Bateria) 
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 20% | CRÍTICO | 2 pontos |
| De 20% até 49% | ATENÇÃO | 1 ponto |
| 50% ou mais | NORMAL | 0 pontos |

#### Suporte de Oxigénio
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 80% | CRÍTICO | 2 pontos |
| De 80% até 89% | ATENÇÃO | 1 ponto |
| 90% ou mais | NORMAL | 0 pontos |

#### Estabilidade Operacional 
| Condição | Classificação | Pontos |
| :--- | :--- | :--- |
| Menor que 40% | CRÍTICO | 2 pontos |
| De 40% até 69% | ATENÇÃO | 1 ponto |
| 70% ou mais | NORMAL | 0 pontos |

---

## 5. Avaliação de Estado e Tendência

### 5.1. Classificação do Ciclo
A soma das pontuações individuais das 5 áreas resulta no risco total do ciclo (máximo de 10 pontos), que categoriza o estado da missão naquele instante:
* **0 a 2 pontos:** MISSÃO ESTÁVEL 
* **3 a 5 pontos:** MISSÃO EM ATENÇÃO 
* **6 a 10 pontos:** MISSÃO CRÍTICA 

### 5.2. Análise de Tendência
A evolução temporal é obtida comparando o risco calculado no primeiro ciclo com o risco verificado no último ciclo de monitorização:
* **Último ciclo > Primeiro ciclo:** Tendência de piora.
* **Último ciclo < Primeiro ciclo:** Tendência de melhora.
* **Último ciclo == Primeiro ciclo:** Permaneceu estável em relação ao início.

### 5.3. Área Mais Afetada
O programa mantém um contador cumulativo de pontos por área ao longo de toda a execução. A área que somar o maior número de pontos de penalização de risco é identificada e destacada no relatório final como a mais prejudicada durante a operação.

---

## 6. Estrutura do Repositório
O projeto está organizado conforme os requisitos exigidos para a entrega:
```text
mission-control-ai/
│
├── README.md               # Este ficheiro com a documentação do sistema
└── mission_control.py      # Código-fonte principal em Python
