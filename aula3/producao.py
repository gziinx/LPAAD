producao = []
saida = -1
while saida != 0:
    n = int(input("Digite um numero entre 300 a 800(digite 0 para sair): "))
    if n >= 300 and n<=800:
        producao.append(n)
    if n == 0:
        saida = n

media_atiginda = []
total = 0
quantidade = 0
qtd_atingida = 0
for i in range(len(producao)):
    total += producao[i]
    quantidade += 1
    if producao[i] >= 500:
        print(f'Produção do turno: {producao[i]} \nMeta atingida\n')
        qtd_atingida += 1
        media_atiginda.append(producao[i])
    elif producao[i] >= 400:
        print(f'Produção do turno: {producao[i]} \nAbaixo da média\n')
    else:
        print(f'Produção do turno: {producao[i]} \nCritico\n')
media = total / len(producao)
percentual = (qtd_atingida / quantidade) * 100

print(f"Produção total: {total}\n Quantidade de turnos: {len(producao)} \n Produção média: {media} \n quantidade que atingiram a meta: {qtd_atingida} \n Percentual dos turnos atingidos: {percentual}")