from random import sample, choice

def posicoes_no_tabuleiro():
    return [p for p in range(1, 41)]


def mostra_tabuleiro(posicoes, horizontal = 60, vertical = 7, caracter_linha = '-', coluna = '|'):
    linha = caracter_linha * horizontal
    inicio = 1
    fim = 9

    print()
    while fim <= 41:
        for p in range(inicio, fim):
            if p == fim - 1:
                print(f'{posicoes[p - 1]:^5}')
            else:
                print(f'{posicoes[p - 1]:^5} {coluna} ', end = '')
        if fim < 40:  
            print(linha)
        inicio = fim
        fim += 8
    print()

    return posicoes
        

def mensagem_erro1():
    print('***** ERRO - POSIÇÃO INEXISTENTE OU JÁ ESCOLHIDA! *****')


def mensagem_erro2():
    print('***** ERRO - VALOR INVÁLIDO! *****')
    
    
def jogador_posiciona(posicoes):
    frota = []

    for navio in range(1, 11):
        while True:
            try:
                posicao = int(input(f'=> Navio {navio} na posição: '))
                if posicao not in posicoes or posicao in frota:
                    mensagem_erro1()
                    continue
            except Exception:
                mensagem_erro2()
                continue
            else:
                frota.append(posicao)
                break

    return frota


def mensagem_frota_jogador(frota):
    print(f'==> Sua frota nas posições: {frota} <==') 
    print()


def pc_posiciona(posicoes, frota):
    posicoes = set(posicoes)
    frota = set(frota)

    disponiveis = list(posicoes - frota)

    return sample(disponiveis, 10)


def jogador_ataca(posicoes, frota):
    while True:
        try:
            posicao = int(input('Mirar na posição: '))
            if posicao not in posicoes or posicao in frota:
                mensagem_erro1()
                continue
        except Exception:
                mensagem_erro2()
                continue
        else:
            break

    return posicao
    

def pc_ataca(posicoes, frota):
    posicoes_restantes = []
    
    for p in posicoes:
        if isinstance(p, int):
            posicoes_restantes.append(p)

    #print(posicoes_restantes)
    posicoes_restantes = set(posicoes_restantes)
    frota = set(frota)

    disponiveis = list(posicoes_restantes - frota)

    return choice(disponiveis)
   

def mensagem_ataque(quem, escolhida, posicao):
    print()
    print(f'###### {quem} ', end = '')
    if posicao == '*':
        print(f'mirou na posição {escolhida} e ACERTOU um navio inimigo!')
    else:
        print(f'mirou na posição {escolhida} e ERROU!')
        
            
def placar(restantes_jog, restantes_pc, caractere = '=', total = 36):
    linha = caractere * total

    print()
    print('           ', linha)
    print('                          PLACAR')
    print(f'                 JOGADOR  {restantes_jog} X {restantes_pc}  COMPUTADOR')
    print('           ', linha)
    

def resultado(restantes_jog, restantes_pc):
    print('VENCEDOR = ', end = '')
    if restantes_jog == 0:
        print('COMPUTADOR!')
    else:
        print('JOGADOR!')


def main():
    Posicoes = posicoes_no_tabuleiro()
    mostra_tabuleiro(Posicoes)

    Frota_jogador = jogador_posiciona(Posicoes)
    Frota_pc = pc_posiciona(Posicoes, Frota_jogador)
    #print(Frota_pc)

    mostra_tabuleiro(Posicoes)

    Navios_jogador = len(Frota_jogador)
    Navios_pc = len(Frota_pc)

    Vez = 1

    while Navios_jogador != 0 or Navios_pc != 0:
        if Vez % 2 != 0:
            mensagem_frota_jogador(Frota_jogador)

            Escolhida = jogador_ataca(Posicoes, Frota_jogador)

            if Escolhida in Frota_pc:
                Posicoes[Escolhida - 1] = '*'
                Navios_pc -= 1 
            else:
                Posicoes[Escolhida - 1] = 'X'

            mensagem_ataque('VOCÊ', Escolhida, Posicoes[Escolhida - 1])

        else:
            Escolhida = pc_ataca(Posicoes, Frota_pc)

            if Escolhida in Frota_jogador:
                Posicoes[Escolhida - 1] = '*'
                Navios_jogador -= 1
            else:
                Posicoes[Escolhida - 1] = 'X'
            
            mensagem_ataque('COMPUTADOR', Escolhida, Posicoes[Escolhida - 1])

        placar(Navios_jogador, Navios_pc)
        
        mostra_tabuleiro(Posicoes)

        Vez += 1

    resultado(Navios_jogador, Navios_pc)
        

if __name__ == '__main__':
    main()
