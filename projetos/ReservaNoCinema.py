#Reserva no cinema: permite ao usuário reservar os lugares que quiser nas salas e acentos disponíveis.

sala = [10, 11, 12, 13, 14]
vago = [1, 2, 3, 4, 5]

def traco():
    print('=' * 20)

while True:
    print()
    print('         CINEMA POEIRINHA')
    traco()
    c = 0
    for e in sala:
        print(f'Sala {e} = {vago[c]} lugar(es) vago(s)')
        c = c + 1
    traco()

    print()
    busca = int(input('Digite o número da sala: '))
    print()
    if busca != 10 and busca != 11 and busca != 12 and busca != 13 and busca != 14:
        while True:
            busca = int(input('SALA INEXISTENTE! Digite outro número de sala: '))
            if busca == 10 or busca == 11 or busca == 12 or busca == 13 or busca == 14:
                break
            
    print()
    c = 0
    while True:
        if sala[c] == busca:
            print(f'Sala {sala[c]} = {vago[c]} lugar(es) vago(s)')
            break
        c = c + 1
             
    print()
    if vago[c] != 0:
        res = int(input('Reservar quantos lugares? '))
        print()
        if res > vago[c]:
            while True:
                 res = int(input('ERRO! Quantidade indisponível. Reservar quantos lugares? '))
                 if res <= vago[c]:
                     break
        print()
        print(f'Reserva feita com sucesso!')
        vago[c] = vago[c] - res
    else:
        print(f'ERRO! Todos os lugares da sala já estão ocupados.')

    print()
    op = input('Fazer outra reserva? [S/n] ')
    if op == 'N' or op == 'n':
        print()
        print('OBRIGADO E VOLTE SEMPRE!')
        break
