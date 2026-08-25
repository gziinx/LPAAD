estoque = {
    "Produto": "Notebook",
    "Valor": 4200,
    "Estoque": 8
}
for i in estoque.keys():
    print(f'Chaves: {i}')

print(' ')
for i in estoque.values():
    print(f'Valor: {i}')
   
print(' ')
for i,j in estoque.items():
    print(f'{i}: {j}')