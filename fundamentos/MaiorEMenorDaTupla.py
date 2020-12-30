# MaiorEMenorDaTupla: mostra como gerar 10 elementos (valores inteiros) em uma tupla.

from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
               randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Tupla gerada = {tupla}')
print()
print(f'Maior valor = {max(tupla)}')
print(f'Menor valor = {min(tupla)}')
