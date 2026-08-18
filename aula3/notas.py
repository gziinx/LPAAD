notas = [8.5,4.0,7.5,9.0,5.0]
acima = 0
total = 0
media = 0
for i in notas:
    if i >= 6.0:
        acima += 1
        total += i
    media = total / acima
print(f'Alunos com nota igual ou maior a 6: {acima}, e a media deles: {media:.2f}')