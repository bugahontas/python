# Produto Cartesiano: informa os pares ordenados do conjunto AxB.

A = [1, 2, 3, 4, 5]
B = [6, 1, 3]

print('Produto cartesiano AxB = {', end = '')
a = 0
b = 0
while a < len(A):
    while b < len(B):
        if a == (len(A) - 1) and b == (len(B) - 1):
            print(f'({A[a]}, {B[b]})', end = '') # Imprime o último par ordenado sem vírgula após parêntese.
        else:
            print(f'({A[a]}, {B[b]}), ', end = '') # Imprime os pares ordenados separados entre si por vírgula.
        b = b + 1
    a = a + 1
    b = 0
print('}')
