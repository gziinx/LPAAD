conjuntoA = [23,14,31,17,20]
conjuntoB = [75,1,4,3,19,50,64,31]

def calcular_medaiana(listinha):
    ord = sorted(listinha)
    print(ord)
    if len(ord) % 2 == 0:
        for i in range(len(ord)):
            if i == len(ord) / 2:
                mediana = (ord[i] + ord[i - 1]) / 2
                return mediana
    for i in range(len(ord)):
        if i == len(ord) // 2:
            return ord[i]

print(calcular_medaiana(conjuntoA))
print(calcular_medaiana(conjuntoB))