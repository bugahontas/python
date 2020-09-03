# Sem repetido: compara duas listas e cria uma terceira sem números repetidos.

# Atenção: para que o código funcione corretamente, cada lista deve conter 5 números diferentes entre si.

l1 = [10, 0, 54, 7.2, 9]
l2 = [0, 3, 7.2, 54, 1.1]
l3 = []

print(f'Lista 1 = {l1}')
print()

l3.extend(l1)

print(f'Lista 2 = {l2}')
print()
c2 = 0
while c2 <= 4:
    c3 = 0
    tot = 0
    while c3 <= 4:
        if l2[c2] != l3[c3]:
            tot = tot + 1
        c3 = c3 + 1
    if tot == 5:
        l3.append(l2[c2])
    c2 = c2 + 1

print(f'Lista 3 = {l3}')
