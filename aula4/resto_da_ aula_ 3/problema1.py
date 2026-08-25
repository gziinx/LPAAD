estoque = [18, 5, 0, 32, 4, 7, 0, 14, 3]
esgotados = 0
critico = 0
for i in estoque:
    if i == 0:
        esgotados += 1
    elif i >= 1 and i <= 5:
        critico += 1

total = esgotados + critico
dsp =  len(estoque) - total 
percentual = (total/len(estoque)) * 100
print(f'Produtos disponiveis: {dsp}')
print(f'Produtos esgotados: {esgotados}')
print(f'Produtos criticos: {critico}')
print(f'Percentual que precisa de reposição: {percentual:.1f}%')