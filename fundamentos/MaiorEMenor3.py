# Exibe o maior e o menor valor em uma lista sem as funções max e min.

lista = []

qtd = int(input('Quantidade de valores na lista: '))
print()

c = 0
while c < qtd:
    n = int(input(f'{c + 1}o. Valor = '))
    lista.append(n)
    c = c + 1

print()
print(f'Lista criada: {lista}')

maior = 0
menor = lista[0]
for e in lista:
    if e > lista[0]:
        maior = e
    elif e < lista[0]:
        menor = e

print()
print(f'Maior valor da lista = {maior}')
print(f'Menor valor da lista = {menor}')
