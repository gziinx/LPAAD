class Filme:
    pass

f1 = Filme()
f2 = Filme()

f1.titulo = "Toy Story"
f1.genero = "Animação"
f1.duracao = 150

f1.titulo = "Velozes e Furiosos 2"
f1.genero = "Ação"
f1.duracao = 163


class Musica:
    def __init__(self, nome, cantores):
        self.nome = nome
        self.cantores = cantores
    def exibir_musica(self):
        print(f"Nome: {self.nome}\nCantor: {self.cantores}")
n1 = Musica("Justino", "Vida Drama")
n1.exibir_musica()

class Musicas:
    def __init__(self, nome, cantor, genero, duracao, ano):
        self.nome = nome
        self.cantor = cantor
        self.genero = genero
        self.duracao = duracao
        self.ano = ano

    # Atributos de controle
        self.reproducoes = 0
        self.tocando = False

    def reproduzir(self):
        if self.tocando == False:
            self.tocando = True
            self.reproducoes += 1
            print(f"A música {self.nome} está sendo reproduzida")
        else:
            print(f"A música {self.nome} já está sendo reproduzida")

    def pausar(self):
        if self.tocando == True:
            self.tocando = False
            print(f"A música {self.nome} foi pausada")
        else:
            print(f"A música {self.nome} não está sendo reproduzida")

    # Padronize os nomes das funções
    # Evite colocar o nome da função, com o mesmo nome do teclado
    def mostrar_nome(self):
        print(f"Nome: {self.nome}")
    def mostrar_cantor(self):
        print(f"Cantor: {self.cantor}")
    def mostrar_genero(self):
        print(f"Gênero: {self.genero}")
    def mostrar_duracao(self):
        print(f"Duração: {self.duracao}")
    def mostrar_ano(self):
        print(f"Ano: {self.ano}")
    def mostrar_detahes(self):
        self.mostrar_nome()
        self.mostrar_cantor()
        self.mostrar_genero()
        self.mostrar_duracao()
        self.mostrar_ano()
n1 = Musicas("Vida Boa", "Vitor & Leo", "Sertanejo", 120, 2010)
n1.mostrar_nome()
n1.mostrar_cantor()
n1.mostrar_genero()
n1.mostrar_duracao()
n1.mostrar_ano()
print("\n")
n1.mostrar_detahes()    

print("\n")
n1.reproduzir()
print(f"Reproduções: {n1.reproducoes}")
n1.pausar()
n1.reproduzir()
print(f"Reproduções: {n1.reproducoes}")