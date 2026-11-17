class Musicas:
    def __init__(self, nome, cantor, genero, duracao, ano):


        self._nome = self._validar_string(nome, "nome")
        self._cantor = self._validar_string(cantor, "cantor")
        self._genero = self._validar_string(genero, "genero")
        self._duracao = self._validar_int(duracao, "duracao")
        self._ano = self._validar_int(ano, "ano")
    @staticmethod
    def _validar_string(valor, nome_atributo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"O atributo {nome_atributo} deve ser um texto não vazio!")
        return valor.strip()

    @staticmethod
    def _validar_int(valor, nome_atributo):
        if type(valor) is not int or valor <= 0:
            raise ValueError(f"O atributo {nome_atributo} deve ser um número inteiro positivo!")
        return valor
   
    # Padronize os nomes das funções
    # Evite colocar o nome da função, com o mesmo nome do teclado

    def __str__(self):
        minutos = self._duracao // 60
        segundos = self._duracao % 60
        return ((f"Nome: {self._nome}\nCantor: {self._cantor}\nGênero: {self._genero}\nDuração: {minutos:02d}:{segundos:02d}"))

    # ADD PROPRIEDADES @properyty
    @property
    def nome(self):
        return self._nome
    @property
    def cantor(self):
        return self._cantor
    @property
    def genero(self):
        return self._genero

    @property
    def duracao(self):
        return self._duracao

    @property
    def ano(self):
        return self._ano

    # --------------------------------------------------------------------------------------------


    def mostrar_nome(self):
        print(f"Nome: {self._nome}")
    def mostrar_cantor(self):
        print(f"Cantor: {self._cantor}")
    def mostrar_genero(self):
        print(f"Gênero: {self._genero}")
    def mostrar_duracao(self):
        print(f"Duração: {self._duracao}")
    def mostrar_ano(self):
        print(f"Ano: {self._ano}")
    def mostrar_detahes(self):
        self.mostrar_nome()
        self.mostrar_cantor()
        self.mostrar_genero()
        self.mostrar_duracao()
        self.mostrar_ano()
        print(f"Favorito: {'Sim' if self.favorito else 'Não'}")
        print(f"Tocando: {'Sim' if self.tocando else 'Não'}")
        print(f"Reproduções: {self.reproducoes}")
# n1 = Musicas("Vida Boa", "Vitor & Leo", "Sertanejo", 120, 2010)
# n1.mostrar_nome()
# n1.mostrar_cantor()
# n1.mostrar_genero()
# n1.mostrar_duracao()
# n1.mostrar_ano()
# print("\n")
# n1.mostrar_detahes()    

# print("\n")
# n1.reproduzir()
# print(f"Reproduções: {n1.reproducoes}")
# n1.pausar()
# n1.reproduzir()
# print(f"Reproduções: {n1.reproducoes}")

    def aletear_nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O novo nome da música deve ser um texto não vazio!")
        self._nome = novo_nome
    def aletear_cantor(self, novo_cantor):
        if not isinstance(novo_cantor, str) or not novo_cantor.strip():
            raise ValueError("O novo nome do cantor deve ser um texto não vazio!")
        self._cantor = novo_cantor
    def aletear_genero(self, novo_genero):
        if not isinstance(novo_genero, str) or not novo_genero.strip():
            raise ValueError("O  genero deve ser um texto não vazio!")
        self._genero = novo_genero
    def aletear_duracao(self, nova_duracao):
        if type(nova_duracao) is not int or nova_duracao <= 0:
            raise ValueError("O novo atributo de duração deve ser um número inteiro posítivo!")
        self._duracao = nova_duracao
    def aletear_ano(self, novo_ano):
        if type(novo_ano) is not int:
            raise ValueError("O novo atributo de ano não pode ser vazio!")
        self._ano = novo_ano
    
    

