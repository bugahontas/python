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

def unidadeMedida():
    print('Tecle [m] para METRO')
    print('Tecle [cm] para CENTÍMETRO')
    return input('Informe a unidade de medida: ')
    
def criaMedidas(c):
    if c == 1:
        lado1 = float(input('Lado 1 (m) = '))
        lado2 = float(input('Lado 2 (m) = '))
    else:
        lado1 = float(input('Lado 1 (cm) = '))
        lado2 = float(input('Lado 2 (cm) = '))
        lado1 /= 100
        lado2 /= 100
    print()
    return lado1, lado2
    
def criaObjeto(lado1, lado2):
    if lado1 == lado2:
        obj = Quadrado(lado1)
    else:
        obj = Retangulo(lado1, lado2)
    return obj
    
def mostraDados(lado1, lado2, obj):
    print(f'--> Dimensões = {lado1}m x {lado2}m')
    print(f'--> Área total = {obj.calculaArea():.2f}m2')
    print()

def totalAzulejo(lista):
    print(f'Serão necessários {ceil(lista[0] / lista[1])} azulejos.') 
    
def main():
    ListaAreas = []
    for contador in range(1, 3):
        if contador == 1:
            topo('CÔMODO')
        else:
            topo('AZULEJO')
        Lado1, Lado2 = criaMedidas(contador)
        objeto = criaObjeto(Lado1, Lado2)
        mostraDados(Lado1, Lado2, objeto)
        ListaAreas.append(objeto.calculaArea())
    topo(qtd = 30)
    totalAzulejo(ListaAreas)

if __name__ == '__main__':
    main()
