# Busca com repetidos: mostra a posição dos valores procurados pelo usuário na lista criada.

# Mostra todas as posições de um número repetido procurado.

tam = int(input('Lista com quantos números? '))
print()

lista = []

c = 0
while c < tam:
    n = int(input('Digite um número: '))
    lista.append(n)
    c = c + 1

print()
print(f'Lista criada = {lista}')
print()

busca1 = int(input('Procurar um número: '))
busca2 = int(input('Procurar outro número: '))
print()

print('-' * 11,'RESULTADO DA BUSCA', '-' * 11)

c = 0
achei1 = False
achei2 = False
while c < len(lista):
    if lista[c] == busca1:
        achei1 = True
        print(f' => Número {busca1} encontrado na posição {c}!')
    c = c + 1

c = 0
while c < len(lista):
    if lista[c] == busca2:
        achei2 = True
        print(f' => Número {busca2} encontrado na posição {c}!')
    c = c + 1

if achei1 == False:
    print(f'ERRO! Número {busca1} não encontrado!')
if achei2 == False:
    print(f'ERRO! Número {busca2} não encontrado!')
print('-' * 52)
