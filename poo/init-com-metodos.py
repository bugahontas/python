'''Mostra que é possível definir atributos dentro de métodos chamados pelo __init__'''
'''Logo, atributos podem ser criados dentro do __init__ **OU** dentro de métodos invocados pelo __init__'''
'''O que importa é que estejam dentro do __init__ para serem ativados assim que o objeto for criado'''

class Pessoa():
    def __init__(self):
        self.criaNome() #Cria o atributo self.nome
        self.criaIdade() #Cria o atributo self.idade
    def criaNome(self):
        self.nome = input('Informe o nome: ')
    def criaIdade(self):
        self.idade = int(input('Informe a idade: '))
        print()
    def __str__(self): #Mostra atributos do objeto. 
        return self.nome + ' tem ' + str(self.idade) + ' anos.' #Aqui self.idade vira string pra concatenar com as outras palavras (strings). Poderia ser print com f-string também...
    def maioridade(self):
        if self.idade >= 18:
            print('Logo, é MAIOR de idade!')
        else:
            print('Logo, é MENOR de idade!')

def separador(caractere = '-', qtd = 30): #Só para separar os dados de um objeto do outro durante a execução.
    print(caractere * qtd)

def main(): #Função principal: os comandos serão executados a partir daqui.
    separador()
    p0 = Pessoa() #Não passar parâmetro, pois nome e idade serão criados nos métodos.
    print(p0) #Chama o método especial __str__
    p0.maioridade()
    separador()
    p1 = Pessoa()
    print(p1)
    p1.maioridade()
    separador()

if __name__ == '__main__': #O módulo atual (init-com-metodos.py) tem a variável __name__ com o valor '__main__'
    main() #Logo, a função principal será chamada para que o código seja executado.
