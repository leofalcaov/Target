# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

# IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
#    Estes dias devem ser ignorados no cálculo da média;

import json

# Exemplo de dados de faturamento
dados_faturamento = '''
{
    "faturamento": [1000, 2000, 0, 3000, 0, 1500, 2500, 0, 1800, 2000, 0, 2400, 0, 3000]
}
'''

# Carregar os dados do faturamento
dados = json.loads(dados_faturamento)
faturamento_diario = dados['faturamento']

# Filtrar os dias com faturamento
faturamento_diario = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_faturamento = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_faturamento)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")