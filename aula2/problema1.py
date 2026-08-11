faturamento = [18500, 21300, 17800, 24600, 27400]

qtd_dias = len(faturamento)
faturamento_total = sum(faturamento)
medio_diario = (faturamento_total / qtd_dias)
maior = max(faturamento)
menor = min(faturamento)

print(f'Quantidade de dias analisados: {qtd_dias}')
print(f'Faturamento total: {faturamento_total}')
print(f'Faturamento médio diário: {medio_diario}')
print(f'Maior faturamento registrado: {maior}')
print(f'Menor faturamento registrado: {menor}')

if medio_diario >= 22000:
    print('Bom desempenho')
elif medio_diario >= 19000 and medio_diario < 22000:
    print('Desempenho regular')
else:
    print('Desempenho crítico')
