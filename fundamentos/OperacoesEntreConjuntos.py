# Operações Entre Conjuntos: determina a união, intersecção e diferença entre dois conjuntos A e B.

A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {55, 3, 19, 0, 7, 12}

print(f'Todos os valores = {A | B}')
print()
print(f'Valores comuns entre os conjuntos A e B = {A.intersection(B)}')
print()
print(f'Valores exclusivos do conjunto A = {A - B}')
print()
print(f'Valores exclusivos do conjunto B = {B - A}')

