# Busca sem repetidos: dada uma lista, mostra a posição dos valores da lista e qual deles foi encontrado primeiro.

# Você pode mudar os números e a quantidade deles na lista, mas evite números repetidos. Para ver código de busca com elementos repetidos, consulte 'BuscaComRepetidos' 

lista = [1, 2, 3, 4, 5]

busca1 = int(input('Procurar um número: '))
busca2 = int(input('Procurar outro número: '))
print()

print('-' * 11,'RESULTADO DA BUSCA', '-' * 11)

c = 0
tot1 = 0
tot2 = 0
while c < len(lista):
    if lista[c] == busca1:
        print(f' => Número {busca1} encontrado na posição {c}!')
        break
    c = c + 1
tot1 = c

c = 0
while c < len(lista):
    if lista[c] == busca2:
        print(f' => Número {busca2} encontrado na posição {c}!')
        break
    c = c + 1
tot2 = c

if tot1 < len(lista) and tot2 < len(lista): # Os dois valores foram encontrados, então dá pra ver qual foi encontrado antes!
    if tot2 > tot1:
        print(f' => Número {busca1} encontrado primeiro!')
    elif tot1 > tot2:
        print(f' => Número {busca2} encontrado primeiro!')

if tot1 == len(lista): # O limite máximo da lista indica que todas as posições já foram esgotadas e o número procurado não foi encontrado.
    print(f'ERRO! Número {busca1} não encontrado!')
if tot2 == len(lista):
    print(f'ERRO! Número {busca2} não encontrado!')
print('-' * 52)
