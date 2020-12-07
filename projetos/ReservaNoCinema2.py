# Reserva No Cinema 2: versão alternativa do código "ReservaNoCinema" também disponível neste repositório.

# Se você viu outros códigos deste repositório, já percebeu que gosto de pular linhas ao longo do código.
# Pra mim códigos muito "colados" não são visualmente agradáveis, sendo difícil saber onde começa e termina cada bloco de ações.
# ... E também porque sou muito espaçosa! XD

cine = []

c = 0
while c < 5: # Cadastro de salas e lugares disponíveis.
    sala = int(input('Sala número: '))
    disp = int(input('Total de lugares disponíveis: '))
    cine.append([sala, disp])
    c = c + 1
    print()

def fun(): # Função que mostra cada sala com seus lugares disponíveis.
    print('=' * 20)
    for e in cine:
        if e[1] != 0: # Mostra a sala apenas se tiver 1 ou mais lugares disponíveis.
            print(f'Sala {e[0]} - {e[1]} lugares disponíveis')
    print('=' * 20)

aux2 = True 
while aux2:

    fun()

    aux = True # 'aux' e 'aux2' são variáveis de controle dos loops while. Achei melhor fazer isso porque assim fica mais fácil de saber qual loop está sendo desativado.
    while aux: # Referente à escolha da sala.
        busca = int(input('Escolher sala: '))
        print()

        for e in cine:
            if e[0] == busca:
                aux = False # Sai deste laço de repetição e pula pro próximo while.
                break
        else:
            print('_' * 9, f'ERRO - Sala {busca} não encontrada!', '_' * 9)

    c = 0
    aux = True
    while aux: # Referente à reserva de lugares.
        res = int(input(f'Sala {e[0]} = {e[1]} lugares. Reservar quantos lugares? '))
        if res <= e[1]:
            e[1] = e[1] - res
            print()
            print(f'Reserva feita com sucesso!')
            aux = False # Sai deste laço de repetição e volta para o while de "aux2" (lá em cima).
        else:
            print('_' * 9, f'ERRO - Quantidade indisponível!', '_' * 9)
            print()

    print()
    print('=' * 20)
    op = input('Fazer outra reserva? [S/N] ')
    op = op.upper()
    if op == 'N':
        aux2 = False
    print()

print('Saindo...')
