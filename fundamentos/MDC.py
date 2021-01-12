# M.D.C: cálculo com base em divisões sucessivas. 

def mdc(D, d):
    while True:
        r = int(D % d)
        if r == 0:
            return d
            break # Laço se repete até a divisão ser exata.
        D = d # O divisor anterior vira o próximo dividendo.
        d = r # O resto anterior vira o próximo divisor. 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print()

print(f'M.D.C ({n1}, {n2})= {mdc(n1, n2)}')
