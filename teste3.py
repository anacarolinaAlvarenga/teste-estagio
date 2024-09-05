print('Resposta da questão 3.')

import json

# Supondo que temos o seguinte JSON de faturamento diário
faturamento_diario = [
    1000, 2300, 3000, 0, 4500, 2000, 0, 1200, 0, 5000, 200, 6000, 4000, 0, 3000, 0, 7000
]

# Removendo dias sem faturamento
faturamento_diario = [f for f in faturamento_diario if f > 0]

# Calculando menor, maior e média
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_faturamento = sum(faturamento_diario) / len(faturamento_diario)

# Contando dias acima da média
dias_acima_da_media = len([f for f in faturamento_diario if f > media_faturamento])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
