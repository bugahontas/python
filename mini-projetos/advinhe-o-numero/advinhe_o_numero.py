from random import randint

def numero_sorteado():
    return randint(0, 9)

def jogador_da_vez(jogador, caractere = '*', qtd = 50):
    print(caractere * qtd)
    print(f'               JOGADOR - {jogador}')
    print(caractere * qtd)
    print()

def usuario_escolhe(tentativa, caractere = 'X', qtd = 36):
    usuario = input(f'Tentativa {tentativa} - Advinhe um número de 0 a 9: ')
    while True:
        if usuario.isdigit() and int(usuario) >= 0 and int(usuario) < 10:
            break
        else:
            print(caractere * qtd)
            usuario = input('ERRO - Digite um número de 0 a 9: ')
            print(caractere * qtd)
    return int(usuario)

def pc_escolhe(lista):
    while True:
        pc = randint(0, 9)
        if pc not in lista:
            lista.append(pc)
            break
    return pc

def mensagem(jogador, sorteado, tentativa):
    print(f'--> {jogador} acertou o número {sorteado} na tentativa {tentativa}')
        
def placar(tent_usu, tent_pc, caractere = '-', qtd = 35):
    print()
    print()
    print(caractere * qtd)
    print('              PLACAR')
    print(caractere * qtd)
    print(f'USUÁRIO   {tent_usu}    X    {tent_pc}   COMPUTADOR')
    print(caractere * qtd)

def resultado(tent_usu, tent_pc):
    print()
    print()
    if tent_usu == tent_pc:
        print('        Resultado = EMPATE!')
    else:
        print('        VENCEDOR = ', end = '')
        if tent_usu < tent_pc:
            print('USUÁRIO!')
        else:
            print('COMPUTADOR!')    
        
def main():
    Sorteado = numero_sorteado()

    jogador_da_vez('USUÁRIO')
    Tentativa_usuario = 1
    while True:
        Usuario = usuario_escolhe(Tentativa_usuario)
        if Usuario == Sorteado:
            print()
            mensagem('USUÁRIO', Sorteado, Tentativa_usuario)
            break
        else:
            Tentativa_usuario += 1
    print()

    jogador_da_vez('COMPUTADOR')
    Tentativa_pc = 1
    Ja_escolhidos_pc = []
    while True:
        Pc = pc_escolhe(Ja_escolhidos_pc)
        if Pc == Sorteado:
            mensagem('COMPUTADOR', Sorteado, Tentativa_pc)
            break
        else:
            Tentativa_pc += 1

    placar(Tentativa_usuario, Tentativa_pc)
    resultado(Tentativa_usuario, Tentativa_pc)
    
if __name__ == '__main__':
    main()
