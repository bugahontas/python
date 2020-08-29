# Mostra o valor do milhar, centena, dezena e unidade de um número digitado.

from math import floor # Esta função arredonda os valores pra baixo. Sem ela, o interpertador arredonda o valor da casa pra cima automaticamente, mostrando valores errados.

def traco():
    print('=' * 16)

n = int(input('Digite um número: '))
print()

m = floor(n  / 1000)
c = floor((n % 1000) / 100)
d = floor((n % 100) / 10)
u = floor((n % 10) / 1)

traco()
print(f'Partes do número {n}:')
traco()
print()
print(f'Milhar = {m:.0f}')
print(f'Centena = {c:.0f}')
print(f'Dezena = {d:.0f}')
print(f'Unidade = {u:.0f}')
