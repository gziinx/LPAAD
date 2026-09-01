def cor_azul (texto, cor):
    if cor ==  "vermelho":
        cod = 31
    elif cor == "verde":
        cod = 32
    elif cor == "amarelo":
        cod = 33
    elif cor == "azul":
        cod = 34
    else:
        cod = 0
    return f"\033[{cod}m{texto}\033[0m"

print(cor_azul("op", "vermelho"))

