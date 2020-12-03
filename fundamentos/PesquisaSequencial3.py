# Pesquisa Sequencial 3: pesquisa dois valores informados pelo usuário, mostra a posição deles e verifica qual foi encontrado primeiro.

lista = [22, 43, 6, 19, 0]

v1 = int(input('Busca 1 = Valor: '))
v2 = int(input('Busca 2 = Valor: '))
print()

c = 0
achou1 = False
pos1 = 0
achou2 = False
pos2 = 0
while c < len(lista):
    if lista[c] == v1:
        achou1 = True
        pos1 = c
    if lista[c] == v2:
        achou2 = True
        pos2 = c
    c = c + 1

if achou1 == True:
    print(f'Valor {v1} encontrado na posição {pos1 + 1}')
else:
    print(f'Valor {v1} não encontrado...')

print()
if achou2 == True:
    print(f'Valor {v2} encontrado na posição {pos2 + 1}')
else:
    print(f'Valor {v2} não encontrado...')

print()
if achou1 == True and achou2 == True: # Só quando os dois valores forem encontrados na lista.
    if pos1 < pos2:
        print(f'Valor {v1} encontrado primeiro!')
    else:
        print(f'Valor {v2} encontrado primeiro!')
