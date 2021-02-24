'''Mostra que é possível criar métodos orientados à classe'''

class Pessoa():
    total_instancia = 0 #Este é um atributo da classe, não do objeto
    @classmethod #Decorador que habilita o método contaInstancia a funcionar com o parâmetro da classe ao invés do objeto (self)
    def contaInstancia(classe): #Aqui "Pessoa" é passado para o parâmetro "classe"
        classe.total_instancia += 1 #Modifica o atributo da classe toda vez que um objeto é criado
    def __init__(self):
        Pessoa.contaInstancia() #Chama o método orientado à classe a cada instanciação
        self.criaNome()
        self.criaIdade()
    def criaNome(self):
        self.nome = input('Digite o nome: ')
    def criaIdade(self):
        self.idade = int(input('Digite a idade: '))
        print()
    def __str__(self):  
        return self.nome + ' tem ' + str(self.idade) + ' anos.'
    def maioridade(self):
        if self.idade >= 18:
            print('Logo, é MAIOR de idade!')
        else:
            print('Logo, é MENOR de idade!')

def separador(caractere = '=', qtd = 30):
    print(caractere * qtd)

def main(): 
    separador()
    p0 = Pessoa() 
    print(p0) 
    p0.maioridade()
    separador()
    p1 = Pessoa()
    print(p1)
    p1.maioridade()
    separador()
    p2 = Pessoa()
    print(p2)
    p2.maioridade()
    separador()
    print(f'Total de objetos criados = {Pessoa.total_instancia}')

if __name__ == '__main__': #O módulo atual (atributo-da-classe.py) tem a variável __name__ com o valor '__main__'
    main() #Logo, a função principal será chamada para que o código seja executado.
