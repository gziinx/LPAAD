class Musica:
    pass #PERMITE MANTER O BLOCO VAZIO VALIDO (FUNCIONANDO)
# Obs.: o pass não executa nenhuma ação

# Criando objetos
m1 = Musica()
m2 = Musica()

# Verificando o tipo do objeto
# Usando type()

print(type(m1))

# Verificar se um objeto pertence a uma classe
# Usando isintance()

print(isinstance(m1,Musica))

# Comparar dois obejtos usando is

print(m1 is m2)

m3 = m1
print(m3 is m1)

m1.nome = "Hino Corinthians"

print(m1.nome)

# Cadastro de atributos manualmente

m3 = Musica

m3.cantor = "Vitor & Leo"
m3.nome = "Vida Boa"
m3.estilo = "Sertanejo"
m3.duracao = 120

print(m3.nome)
print(m3.cantor)
print(m3.estilo)
print(m3.duracao)