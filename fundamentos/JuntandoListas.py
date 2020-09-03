# Juntando listas: cria e junta duas listas em uma terceira.

l1 = []
l2 = []
l3 = []

print('Lista 1:')
print()
c = 0
while c <= 2:
    n1 = int(input(f'{c + 1}o. Elemento: '))
    l1.append(n1)
    l3.append(n1)
    c = c + 1

print()
print('Lista 2:')
print()
c = 0
while c <= 2:
    n2 = int(input(f'{c + 1}o. Elemento: '))
    l2.append(n2)
    l3.append(n2)
    c = c + 1

print()
print(f'Lista 1 = {l1}')
print(f'Lista 2 = {l2}')
print(f'Lista 3 = {l3}')
