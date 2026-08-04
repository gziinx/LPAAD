print('Bem vindo!! ao curso de LPAAD')
##------------------------------
nome = "GUSTAVO"

idade = 18

profissao = 'Atleta'
print(type(nome))
print(type(idade))
print(type(profissao))
##------------------------------


print("Ola", nome,"\n" "voce tem", idade ,"\ne é", profissao, "\n")

##------------------------------
nome = input("\nDigite seu nome que será cadastrado no sistema: ")

print("\nOla", nome, "\nCadastrado com sucesso!!")

##------------------------------
nome = "GUSTAVO"

idade = 18

altura = 1.72
print(type(nome))
print(type(idade))
print(type(altura))

##------------------------------

nome = input("\nDigite o seu nome: ")

peso = input("Digite o seu peso: ")

idade = input("Digite a soma da idade de seu pai somada com a de sua mãe: ")

print(type(nome))
print(type(idade))
print(type(peso))


salario = input("Digite o seu salario: ")

salarionovo = (float(salario) * 1.15)

print(f"Seu novo salario é: {salarionovo} com bonus de 15%")