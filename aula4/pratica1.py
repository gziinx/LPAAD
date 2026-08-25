lista = [{
    "Produto": "Notebook",
    "Valor": 4200,
    "Estoque": 8
},{
   "Produto": "Mouse",
    "Valor": 120,
    "Estoque": 25
},{
   "Produto": "Monitor",
    "Valor": 1350,
    "Estoque": 4
},{
   "Produto": "Teclado",
    "Valor": 280,
    "Estoque": 15
},{
   "Produto": "Headset",
    "Valor": 450,
    "Estoque": 3 
}]
for produtos in lista:
    print(f'Produtos: {produtos['Produto']}')

print(' ')
contadoer = 0
for produtos in lista:
    if produtos['Estoque'] < 10:
        print(f'Produto com o preço inferior a 10 unidades: {produtos['Produto']} Quantidade: {produtos["Estoque"]}')
        contadoer +=1
print(' ')
for produtos in lista:
    print(f'{produtos["Produto"]} - Estoque: {produtos["Estoque"]}')

print(' ')
print(f"{contadoer} Produtos precisam de reposição")
