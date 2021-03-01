'''O mesmo método __str__ retorna mensagens diferentes dependendo da classe do objeto chamado'''

class Pessoa(object):
    def __init__(self, nome): #Se os métodos criaIdade() e criaLazer() estivessem aqui, eles seriam herdados lá embaixo, mas só quero herdar mesmo o atributo nome
        self.nome = nome
    def criaIdade(self):
        return int(input('Idade: '))
    def criaLazer(self):
        return input('Atividade preferida: ')
    def __str__(self): #__str__() de qualquer objeto da classe Pessoa() irá exibir esta mensagem
        return self.nome + ' tem ' + str(self.criaIdade()) + ' anos e seu passatempo é ' + self.criaLazer()

class Funcionario(Pessoa):
    def __init__(self, nome): #Herda de Pessoa() apenas o atributo nome
        super().__init__(nome)
    def criaCargo(self):
        return input('Cargo: ')
    def criaSalario(self):
        return float(input('Salário = R$'))
    def __str__(self): #__str__() de qualquer objeto da classe Funcionário() irá exibir esta outra mensagem
        return self.nome + ' trabalha como ' + self.criaCargo() + ' e recebe um salário de R$' + str(self.criaSalario())

def criaNome():
    return input('Informe um nome: ') #Nome que será usado na instanciação de Pessoa() e Funcionario()

def separador(caractere = '-', qtd = 65):
    print(caractere * qtd)

def main():
    pessoa = Pessoa(criaNome()) 
    separador()
    print(pessoa) #Mensagem do objeto pessoa
    separador()
    funcionario = Funcionario(pessoa.nome)
    print(funcionario) #Mensagem do objeto funcionario
    separador()

if __name__ == '__main__':
    main()
