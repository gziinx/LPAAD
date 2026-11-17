from musica import Musicas

class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None
        self.reproducoes = {}
        self.favorito = []

    def adicionar_musica(self, musica):
        if not isinstance(musica, Musicas):
            raise TypeError("É necessário fornecer um objeto do tipo Musicas.")
        self.musicas.append(musica)
        self.reproducoes[musica] = 0
        return f"Música '{musica.nome}' adicionada ao catálogo."
    
    def verificar_duplicado(self, musica):
        for m in self.musicas:
            if m.nome == musica.nome and m.cantor == musica.cantor:
                return True
        return False