lista = [1,1,2,2,3,3,3,3,4,4,4,5,5,5,5,5]

def moda (listinha):
    # for i in range(len(listinha)):
    #     ord = sorted[listinha]
    #     cont = 0

    #     if ord[i] == ord[i+1]:
    #         cont +=1
    #         if cont > cont:
    #             cont
    modas = {}
    opa = []
    for i in listinha:
        
        cont = listinha.count(i)
        if max.cont 
        modas[f"{i}"]  = cont
    for i,j in modas.values():
        maior = max(j)
        cont = 0
        if j == maior:
            cont += 1
            opa.append(i)
        else:
            return f"Unimodal {maior}"
    for i in opa:
        if len(opa) == 2:
            return f"Bimodal: {opa}"
        if len(opa) > 2:
            return f"MultiModal: {opa}"

print(moda(lista))