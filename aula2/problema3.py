producao  = [485,510,472,498,455,520]

turno = len(producao)
total = sum(producao)
media = total / turno
min = min(producao)
max = max(producao)

print(f'Quantidade de turnos analisados: {turno}')
print(f'Produção total: {total}')
print(f'Produção média: {media}')
print(f'Maior: {max}')
print(f'Menor: {min}')

if media >= 500:
    print('Meta atingida')
elif media >= 480 and media < 500:
    print('atenção')
else:
    print('Abaixo da meta')

if min  < 460:
    print('ALERTA OPERACIONAL !!')