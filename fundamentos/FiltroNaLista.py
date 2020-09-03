# Filtro na lista: define uma lista de números e verifica quais deles são pares e quais são ímpares.

# Útil para filtrar e extrair dados específicos de listas muito grandes. Coloque na lista os valores que você quiser e manipule blocos condicionais e de repetição a seu favor!

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l_par = []
l_impar = []

print(f'Lista de números = {l}')
print()

c = 0
while c <= 9:
    if l[c] % 2 == 0:
        l_par.append(l[c])
    else:
        l_impar.append(l[c])
    c = c + 1

print(f'Valores pares da lista = {l_par}')
print()
print(f'Valores ímpares da lista = {l_impar}')
