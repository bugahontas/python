'''Cria dois objetos da classe Pessoa e verifica se é maior ou menor de idade'''

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self): #Mostra atributos do objeto. 
        return self.nome + ' tem ' + str(self.idade) + ' anos.' #Aqui self.idade vira string pra concatenar com as outras palavras (strings). Poderia ser print com f-string também...
    def maioridade(self):
        if self.idade >= 18:
            print('Logo, é MAIOR de idade!')
        else:
            print('Logo, é MENOR de idade!')
        print()

p0 = Pessoa('Carlos', 42) #Instanciação: chama o método especial __init__
p1 = Pessoa('Daniela', 16)
print(p0) #Chama o método especial __str__
p0.maioridade()
print(p1)
p1.maioridade()
