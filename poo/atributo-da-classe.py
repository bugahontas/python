'''Mostra que classes também podem ter atributos'''

class Pessoa():
    total_instancia = 0 #Este é um atributo da classe, não do objeto
    def __init__(self, nome, idade):
        Pessoa.total_instancia += 1 #Incremento da quantidade total de instâncias toda vez que um objeto é criado
        self.nome = nome
        self.idade = idade
    def __str__(self):  
        return self.nome + ' tem ' + str(self.idade) + ' anos.' #Aqui self.idade vira string pra concatenar com as outras palavras (strings). Poderia ser print com f-string também...
    def maioridade(self):
        if self.idade >= 18:
            print('Logo, é MAIOR de idade!')
        else:
            print('Logo, é MENOR de idade!')

def separador(caractere = '=', qtd = 30): #Separa os dados de um objeto do outro
    print(caractere * qtd)

def main(): 
    separador()
    p0 = Pessoa('Carlos', 42) 
    print(p0) 
    p0.maioridade()
    separador()
    p1 = Pessoa('Daniela', 16)
    print(p1)
    p1.maioridade()
    separador()
    print(f'Total de objetos criados = {Pessoa.total_instancia}')

if __name__ == '__main__': #O módulo atual (atributo-da-classe.py) tem a variável __name__ com o valor '__main__'
    main() #Logo, a função principal será chamada para que o código seja executado.
