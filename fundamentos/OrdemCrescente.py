# Ordem Crescente: organiza os elementos de uma lista do menor para o maior de forma manual.

# Eficiente para listas pequenas.

lista = []

qtd = int(input('Criar lista com quantos números? '))
print()

c1 = 0
while c1 < qtd:
    n = float(input(f'Digite o {c1 + 1}o. número: '))
    lista.append(n)
    c1 = c1 + 1

print()
print(f'Lista criada = {lista}')

c1 = 0
c2 = 1
aux = 0
while c1 <= qtd - 2:
    while c2 <= qtd - 1:
        if lista[c1] > lista[c2]:
            aux = lista[c1]
            lista[c1] = lista[c2]
            lista[c2] = aux
        c2 = c2 + 1
    c1 = c1 + 1
    c2 = c1 + 1

print()
print(f'Nova lista em ordem crescente = {lista}')
