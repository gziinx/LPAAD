unidades = [[120,135,128,141],
            [98,105,110,103],
            [150,145,160,155],
            [116,161,108,121]]
maior = 0
abaixos = 0

for i in range(len(unidades)):
    maior_sem = 0
    total = sum(unidades[i])
    print(f'Unidade: {i+1} total de atendimentos: {total} ')
    
    if total > maior:
        maior = total
    for j in range(len(unidades)):
        if unidades[i][j] < 110:
            abaixos += 1
        if unidades [j][i] > maior_sem:
            maior_sem = unidades[j][i]
    print(f'Maior quntidade de atendimentos da semana {i+1}: {maior_sem}')    
print(f'Unidade que mais realizou atendimento: {maior}')
print(f'Quantidade de registros que ficou abaixo de 110 atendimentos: {abaixos}')