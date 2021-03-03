'''Calcula a quantidade de azulejos para revestir o piso de um cômodo'''

from math import ceil

class Quadrado():
    def __init__(self, lado):
        self.lado = lado
    def calculaArea(self):
        return pow(self.lado, 2)
        
class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calculaArea(self):
        return self.base * self.altura

def topo(elemento = '', caractere = '*', qtd = 10):
    if elemento != '':
        print(caractere * qtd, elemento, caractere * qtd)
    else:
        print(caractere * qtd)
    print()

def criaMedidas(c):
    if c == 1: #Medidas do cômodo
        lado1 = float(input('Lado 1 (m) = '))
        lado2 = float(input('Lado 2 (m) = '))
    else: #Medidas de cada azulejo
        lado1 = float(input('Lado 1 (cm) = '))
        lado2 = float(input('Lado 2 (cm) = '))
        lado1 /= 100 #Converte para metro
        lado2 /= 100
    print()
    return lado1, lado2
    
def criaObjeto(lado1, lado2):
    if lado1 == lado2:
        obj = Quadrado(lado1) #Azulejo sempre será quadrado
    else:
        obj = Retangulo(lado1, lado2) #Cômodo pode ser quadrado ou retângulo
    return obj
    
def mostraDados(lado1, lado2, obj):
    print(f'--> Dimensões = {lado1}m x {lado2}m')
    print(f'--> Área total = {obj.calculaArea():.2f}m2')
    print()

def totalAzulejo(lista): #Calcula quantidade de azulejos para revestir o piso do cômodo
    print(f'Serão necessários {ceil(lista[0] / lista[1])} azulejos.') #O primeiro valor da lista é a área do cômodo e o segundo é a área de cada azulejo
    
def main():
    ListaAreas = []
    for contador in range(1, 3): #Repete duas vezes, uma para o cômodo e outra para o azulejo
        if contador == 1: #Vez do cômodo
            topo('CÔMODO')
        else: #Vez do azulejo
            topo('AZULEJO')
        Lado1, Lado2 = criaMedidas(contador)
        objeto = criaObjeto(Lado1, Lado2) #Cria objeto do tipo quadrado ou retângulo
        mostraDados(Lado1, Lado2, objeto)
        ListaAreas.append(objeto.calculaArea()) #Acumula áreas dos dois objetos criados em cada repetição; necessário para calcular o total de azulejos
    topo(qtd = 35)
    totalAzulejo(ListaAreas)

if __name__ == '__main__':
    main()
