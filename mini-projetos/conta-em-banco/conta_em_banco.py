from random import randint, uniform

class Conta():

    def __init__(self):
        self.criaAgencia()
        self.criaConta()
        self.criaSaldo()
        
    def criaAgencia(self):
        self.agencia = (f'{randint(1, 5000)}-{randint(0, 9)}')
        return self.agencia

    def criaConta(self):
        self.conta = (f'{randint(1, 500000)}-{randint(0, 9)}')
        return self.conta

    def criaSaldo(self):
        self.saldo = (f'{uniform(1, 1000000000):.2f}')
        return self.saldo
        

def main():
    Usuario = Conta()
    print(Usuario.criaSaldo())

if __name__ == '__main__':
    main()
