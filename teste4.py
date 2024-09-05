print('Resposta da questão 4.')
def calcular_percentuais(faturamento_por_estado):
    """Calcula o percentual de representação de cada estado no faturamento total.

    Args:
        faturamento_por_estado: Um dicionário onde as chaves são os estados e os valores são os faturamentos.

    Returns:
        Um dicionário onde as chaves são os estados e os valores são os percentuais de representação.
    """

    faturamento_total = sum(faturamento_por_estado.values())
    percentuais = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / faturamento_total) * 100
        percentuais[estado] = percentual
    return percentuais

# Dados de faturamento por estado (substitua pelos seus dados)
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula os percentuais
percentuais = calcular_percentuais(faturamento_por_estado)

# Imprime os resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")