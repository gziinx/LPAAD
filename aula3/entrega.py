tempos = [32,48,27,55,41,29]
max = False
total = 0
atrasados = 0
for i in range(len(tempos)):
    total += tempos[i]
    if tempos[i] > 40:
        max = True
        atrasados += 1
    else:
        max = False    
    print(f"{i}: Tempo de entrega: {tempos[i]} - {'Atrasou' if max == True else 'Não atrasou'}")
porcentagem = (atrasados / len(tempos)) * 100
media = total / len(tempos)
horas = total // 60
minutos = total % 60
print(f"tempo de entregas: {horas}:{minutos}h , tempo medio das entregas: {media:.2f}, Quantidade de entregas: {len(tempos)}, porcentagem de atrasos: {porcentagem}")