# ==============================================================================
# MISSION CONTROL AI - SISTEMA INTELIGENTE DE MONITORAMENTO DE MISSÃO ESPACIAL
# Global Solution 2026.1 - Pensamento Computacional e Automação com Python
# ==============================================================================


NOME_MISSAO = "Orion Test Alpha"
NOME_EQUIPE = "Equipe Apollo"


areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [24, 92, 88, 96, 90],  # Ciclo 1
    [27, 80, 72, 94, 85],  # Ciclo 2
    [31, 65, 58, 91, 70],  # Ciclo 3
    [36, 42, 38, 87, 55],  # Ciclo 4
    [39, 28, 19, 78, 35],  # Ciclo 5
    [34, 55, 32, 82, 50]   # Ciclo 6
]




def analisar_temperatura(temp):
    """Classifica a temperatura e retorna (Classificação, Pontos, Mensagem)"""
    if temp < 18:
        return "ATENÇÃO", 1, "Temperatura baixa"
    elif 18 <= temp <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif 30 < temp <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(com):
    """Classifica a comunicação e retorna (Classificação, Pontos, Mensagem)"""
    if com < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif 30 <= com <= 59:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(bat):
    """Classifica a bateria e retorna (Classificação, Pontos, Mensagem)"""
    if bat < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif 20 <= bat <= 49:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(ox):
    """Classifica o oxigênio e retorna (Classificação, Pontos, Mensagem)"""
    if ox < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif 80 <= ox <= 89:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(est):
    """Classifica a estabilidade e retorna (Classificação, Pontos, Mensagem)"""
    if est < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif 40 <= est <= 69:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontos):
    """Retorna a classificação do ciclo baseada na pontuação total (Requisito 10)"""
    if 0 <= pontos <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontos <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def analisar_tendencia(primeiro_risco, ultimo_risco):
    """Compara o risco do primeiro e do último ciclo (Requisito 11)"""
    if ultimo_risco > primeiro_risco:
        return "A missão apresentou tendência de piora."
    elif ultimo_risco < primeiro_risco:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def gerar_recomendacao(classificacao, t_status, c_status, b_status, o_status, e_status):
    """Gera recomendações automáticas com base nos dados analisados (Seção 11)"""
    if classificacao == "MISSÃO ESTÁVEL" and t_status == "NORMAL":
        return "Manter operação normal e continuar monitoramento."
    elif t_status == "ATENÇÃO" and classificacao == "MISSÃO ESTÁVEL":
        return "Verificar controle térmico da missão."
    elif t_status == "CRÍTICO" and c_status == "ATENÇÃO":
        return "Verificar controle térmico da missão."
    elif classificacao == "MISSÃO CRÍTICA" and t_status == "CRÍTICO" and c_status == "CRÍTICO":
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    else:
        return "Monitorar sistemas em atenção e preparar plano de contingência."


# ==============================================================================
# PROCESSAMENTO DOS CICLOS 
# ==============================================================================

print("====")
print("=============")
print("MISSION CONTROL AI")
print("=============")
print(f"Missão: {NOME_MISSAO}")
print(f"Equipe: {NOME_EQUIPE}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=====\n========================")


soma_temp = soma_com = soma_bat = soma_ox = soma_est = 0
pontos_acumulados_area = [0, 0, 0, 0, 0]  # Ordem: Temp, Com, Bat, Ox, Est
historico_riscos = []
qtd_ciclos_criticos = 0


for i, ciclo in enumerate(dados_missao):
    num_ciclo = i + 1
    temp, com, bat, ox, est = ciclo
    
   
    soma_temp += temp
    soma_com += com
    soma_bat += bat
    soma_ox += ox
    soma_est += est
    
    
    t_class, t_pts, t_msg = analisar_temperatura(temp)
    c_class, c_pts, c_msg = analisar_comunicacao(com)
    b_class, b_pts, b_msg = analisar_bateria(bat)
    o_class, o_pts, o_msg = analisar_oxigenio(ox)
    e_class, e_pts, e_msg = analisar_estabilidade(est)
    
   
    risco_ciclo = t_pts + c_pts + b_pts + o_pts + e_pts
    historico_riscos.append(risco_ciclo)
    
    
    pontos_acumulados_area[0] += t_pts
    pontos_acumulados_area[1] += c_pts
    pontos_acumulados_area[2] += b_pts
    pontos_acumulados_area[3] += o_pts
    pontos_acumulados_area[4] += e_pts
    
   
    classificacao_atual = classificar_ciclo(risco_ciclo)
    if classificacao_atual == "MISSÃO CRÍTICA":
        qtd_ciclos_criticos += 1
        
    
    rec_ciclo = gerar_recomendacao(classificacao_atual, t_class, c_class, b_class, o_class, e_class)
    
    
    print(f"\nCICLO {num_ciclo}")
    print(f"Temperatura: {temp}°C | {t_class} | {t_msg}")
    print(f"Comunicação: {com}% | {c_class} | {c_msg}")
    print(f"Bateria: {bat}% | {b_class} | {b_msg}")
    print(f"Oxigênio: {ox}% | {o_class} | {o_msg}")
    print(f"Estabilidade: {est}% | {e_class} | {e_msg}")
    print(f"Pontuação de risco do ciclo: {risco_ciclo}")
    print(f"Classificação do ciclo: {classificacao_atual}")
    print(f"Recomendação: {rec_ciclo}")

print("\n" + "="*60)
print("RELATÓRIO FINAL DA MISSÃO")
print("="*60)

# ==============================================================================
# CÁLCULOS FINAIS E GERAÇÃO DE RELATÓRIO 
# ==============================================================================
total_ciclos = len(dados_missao)

# Médias aritméticas dos parâmetros
med_temp = soma_temp / total_ciclos
med_com = soma_com / total_ciclos
med_bat = soma_bat / total_ciclos
med_ox = soma_ox / total_ciclos
med_est = soma_est / total_ciclos

# Identificação do ciclo mais crítico
maior_risco = max(historico_riscos)
# Adiciona 1 ao index para converter a posição da lista (0-indexed) no número real do ciclo
num_ciclo_mais_critico = historico_riscos.index(maior_risco) + 1 
risco_medio_missao = sum(historico_riscos) / total_ciclos

# Análise de tendência de evolução
tendencia_texto = analisar_tendencia(historico_riscos[0], historico_riscos[-1])

# Identificação da área que acumulou maior risco (Requisito 12)
maior_pontuacao_area = max(pontos_acumulados_area)
indice_area_mais_afetada = pontos_acumulados_area.index(maior_pontuacao_area)
area_mais_afetada = areas_monitoradas[indice_area_mais_afetada]

# Classificação Final da Missão Geral baseada no Risco Médio
classificacao_final = classificar_ciclo(int(risco_medio_missao))

# Saída de Dados Formatada do Relatório Final
print(f"Missão: {NOME_MISSAO}")
print(f"Equipe: {NOME_EQUIPE}")
print(f"\nQuantidade de ciclos analisados: {total_ciclos}")
print(f"\nMédia de temperatura: {med_temp:.2f} °C")
print(f"Média de comunicação: {med_com:.2f}%")
print(f"Média de bateria: {med_bat:.2f}%")
print(f"Média de oxigênio: {med_ox:.2f}%")
print(f"Média de eficiência/estabilidade: {med_est:.2f}%")

print(f"\nCiclo mais crítico: Ciclo {num_ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio_missao:.2f}")
print(f"Quantidade de ciclos críticos: {qtd_ciclos_criticos}")

print(f"\nTendência da missão:\n{tendencia_texto}")

print(f"\nPontuação acumulada por área:")
for idx, area in enumerate(areas_monitoradas):
    print(f"  {area}: {pontos_acumulados_area[idx]} pontos")

print(f"\nÁrea mais afetada:\n{area_mais_afetada}")
print(f"\nClassificação final da missão:\n{classificacao_final}")
print(f"\nConclusão:\nA missão apresentou instabilidade relevante durante a operação.")
print("Apesar da tentativa de recuperação no último ciclo, ainda existem sistemas em")
print("atenção e a equipe deve manter o plano de contingência ativo.")
print("="*60)