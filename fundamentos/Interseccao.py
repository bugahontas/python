# Intersecção: verifica quais elementos pertencem às duas listas ao mesmo tempo.

lista1 = [1, 2, 3, 4, 5, 0, 1.1]
lista2 = [0, 7, 0, 4, 1.1, 1.1, 13, 54, 2]
lista3 = [] # Conjunto intersecção das listas 1 e 2.

a = 0
b = 0
while a < len(lista1):
    while b < len(lista2):
        if lista1[a] == lista2[b]:
            if lista1[a] not in lista3: # Adiciona o elemento à lista 3 somente se esse elemento ainda não estiver na lista. Se já estiver, não adiciona de novo.
                lista3.append(lista1[a])
        b = b + 1
    a = a + 1
    b = 0

if len(lista3) == 0: # Indica que a lista 3 (que é a intersecção) é um conjunto vazio.
    print('Intersecção vazia --> Listas 1 e 2 não têm elementos em comum!')
    print('*' * 18, 'Logo, são conjuntos disjuntos!', '*' * 18)
else:
    lista3.sort()
    print(f'Intersecção lista1-lista2 = {lista3}')
