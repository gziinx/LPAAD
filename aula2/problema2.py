velocidade = int(input('DIgite a velocidade em km/h: '))

if velocidade > 70:
    km =  velocidade - 70

    multa = km * 9

    print(f'Multa de {multa} Reais')
    excesso = (velocidade - 70) / 70 * 100
    print(f"Excesso percentual: {excesso}")
else:
    print('esta dentro do limite')

