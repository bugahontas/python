# Pesquisa Sequencial 4: com loop --for--.

lista = [18, 297, 55, 3, 40]

busca = int(input('Procurar qual valor? '))
print()

pos = 0
for v in lista:
    if v == busca:
        print(f'Valor {busca} encontrado na posição {pos + 1}!')
        break
    pos = pos + 1
else:
    print(f'Valor {busca} não encontrado...')
