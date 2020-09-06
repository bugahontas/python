# Organizando fila: mostra quantos clientes tem na fila, quais foram atendidos, quantos ainda faltam e o último da fila. Também mostra o total de clientes atendidos.

ult = int(input('Quantidade de clientes na fila: '))
print()

fila = list(range(1, ult + 1)) # O valor 1 ocupa a posição 0 e 'ult + 1' só foi colocado para que o valor 5 seja incluído na linha 7. Se terminar em 'ult', a fila só vai até o valor 4 porque a contagem começa em 0.

print(f' --> Fila atual com {len(fila)} cliente(s)')
print(f' --> Clientes não atendidos: {fila}')
print()

tot = 0
while True:
    print()
    print('=' * 12, 'MENU', '=' * 12)
    print('    Incluir cliente no fim da fila = Tecle [F]')
    print('             Atender cliente = Tecle [A]')
    print('                        Sair = Tecle [S]')
    print('=' * 29)
    print()
    op = input('TECLA: ')
    print()
    if op == 'A' or op == 'a':
        if len(fila) == 0:
            print('NENHUM CLIENTE NA FILA!')
        else:
            print('-' * 15, f'Cliente número {fila.pop(0)} atendido!', '-' * 15) # O primeiro cliente da fila sempre é o de posição 0.
            print(f' --> Clientes não atendidos: {fila}')
            print(f' --> Total na fila: {len(fila)}')
            tot = tot + 1 # Total de clientes atendidos.
    elif op == 'F' or op == 'f':
        if len(fila) == 0: # Se a fila estiver vazia.
            ult = 1  # O primeiro da fila também é o último, pois a fila começa e termina nele.
            fila.append(1) 
        else:
            ult = ult + 1 # Todo cliente que chega depois ocupa uma posição seguida do último cliente anterior.
            fila.append(ult)
        print('-' * 15, f'Adicionando cliente número {ult}', '-' * 15) # O novo cliente passa a ser o último da fila.
        print(f' --> Clientes não atendidos: {fila}')
        print(f' --> Total na fila: {len(fila)}')
    elif op == 'S' or op == 's':
        print('SAINDO DO PROGRAMA...')
        print()
        break

print(f'Foram atendidos {tot} cliente(s)!')
