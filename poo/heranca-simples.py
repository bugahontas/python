'''Herança simples onde a classe Pedido() herda da classe Cliente()'''

from random import randint

class Cliente(object): #Dados do cliente
    def __init__(self):
        self.criaCliente()
        self.criaEndereco()
        self.criaContatos()
    def criaCliente(self):
        self.cliente = input('Nome completo do cliente: ')
    def criaEndereco(self):
        self.endereco = input('Endereço de entrega: ')
    def criaContatos(self):
        self.fone = input('Telefone para contato: ')
        self.mail = input('E-mail: ')

class Pedido(Cliente): #Dados do pedido, incluindo (herdando) os dados do cliente
    def __init__(self):
        super().__init__()
        self.criaProduto()
        self.criaValor()
    def criaProduto(self):
        self.produto = input('Nome do produto: ')
    def criaValor(self):
        self.valor = float(input('Valor total = R$'))

def separador(caractere = '*', qtd = 25):
    print(caractere * qtd)

def cabecalho():
    numero = randint(1, 100000) #Número gerado será a chave do dicionário, que é a forma de identificar cada pedido
    print(f'    PEDIDO no. {numero}')
    return numero

def quantosPedidos():
    return int(input('Registrar quantos pedidos? '))
    
def main():
    todos_pedidos = {} #Dicionário que armazena todos os pedidos
    for contador in range(1, quantosPedidos() + 1): 
        separador()
        Numero = cabecalho()
        separador()
        ped = Pedido() #Instanciação de cada pedido
        todos_pedidos[Numero] = [ped.cliente, ped.endereco, ped.fone, ped.mail, ped.produto, ped.valor]
        print()
    separador()
    print('         RESUMO')
    separador()
    for chave, valor in todos_pedidos.items(): #Método items() de dicionários lista cada chave e seus valores 
        print(f'PEDIDO No.{chave} CLIENTE {valor[0]} ENTREGAR EM {valor[1]} TELEFONE {valor[2]} E-MAIL {valor[3]} PRODUTO {valor[4]} TOTAL R${valor[5]:.2f}')
        print()

if __name__ == '__main__':
    main()
