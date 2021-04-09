from random import sample, choice

def posicoes_no_tabuleiro():
    return [p for p in range(1, 65)]


def mostra_tabuleiro(posicoes, horizontal = 60, vertical = 7, caracter_linha = '-', coluna = '|'):
    linha = caracter_linha * horizontal
    inicio = 1
    fim = 9

    print()
    while fim <= 65:
        for p in range(inicio, fim):
            if p == fim - 1:
                print(f'{posicoes[p - 1]:^5}')
            else:
                print(f'{posicoes[p - 1]:^5} {coluna} ', end = '')
        if fim < 64:  
            print(linha)
        inicio = fim
        fim += 8
    print()

    return posicoes
        

def mensagem_erro1():
    return '***** ERRO - POSIÇÃO INEXISTENTE OU JÁ ESCOLHIDA!'


def mensagem_erro2():
    return '***** ERRO - VALOR INVÁLIDO!'
    
    
def jogador_posiciona(posicoes):
    ja_escolhidas = []

    for navio in range(1, 21):
        while True:
            try:
                posicao = int(input(f'=> Navio {navio} na posição: '))
                if posicao not in posicoes or posicao in ja_escolhidas:
                    print(mensagem_erro1())
                    continue
            except Exception:
                print(mensagem_erro2())
                continue
            else:
                ja_escolhidas.append(posicao)
                break

    return ja_escolhidas


def pc_posiciona(posicoes, ja_escolhidas):
    posicoes = set(posicoes)
    ja_escolhidas = set(ja_escolhidas)

    disponiveis = list(posicoes - ja_escolhidas)

    return sample(disponiveis, 20)


def jogador_ataca(posicoes):
    while True:
        try:
            posicao = int(input('Mirar na posição: '))
            if posicao not in posicoes:
                print(mensagem_erro1())
                continue
        except Exception:
                print(mensagem_erro2())
                continue
        else:
            break

    return posicao
    

def pc_ataca(posicoes, frota):
    '''posicoes_restantes = []
    #print(f'POSICOES ANTES: {posicoes}')
    for p in posicoes:
        if isinstance(p, int):
            posicoes_restantes.append(p)
    #print(f'POSICOES DEPOIS: {posicoes2}')'''

    posicoes_restantes = set(posicoes_restantes)
    frota = set(frota)

    disponiveis = list(posicoes_restantes - frota)
    #print(disponiveis)

    #escolhida = choice(disponiveis)

    return choice(disponiveis)
   

def mensagem_ataque(vez, escolhida, posicao):
    print()
    if vez % 2 != 0:
        if posicao == '*':
            return '         VOCÊ mirou na posição ' + str(escolhida) + ' e ACERTOU um navio do computador!'
        else:
            return '         VOCÊ mirou na posição ' + str(escolhida) + ' e ERROU!'
    else:
        if posicao == '*':
            return '         COMPUTADOR mirou na posição ' + str(escolhida) + ' e ACERTOU um navio seu!'
        else:
            return '         COMPUTADOR mirou na posição ' + str(escolhida) + ' e ERROU!'
        
            

def main():
    Posicoes = posicoes_no_tabuleiro()
    mostra_tabuleiro(Posicoes)

    Frota_jogador = jogador_posiciona(Posicoes)
    print(Frota_jogador)
    Frota_pc = pc_posiciona(Posicoes, Frota_jogador)
    print(Frota_pc)
    
    for n in Frota_jogador:
        Posicoes[n - 1] = 'J'

    mostra_tabuleiro(Posicoes)

    Vez = 1

    while True:
        if Vez % 2 != 0:
            Escolhida = jogador_ataca(Posicoes)

            if Escolhida in Frota_pc:
                Posicoes[Escolhida - 1] = '*'
            else:
                Posicoes[Escolhida - 1] = 'X'
        else:
            Escolhida = pc_ataca(Posicoes, Frota_pc)

            if Escolhida in Frota_jogador:
                Posicoes[Escolhida - 1] = '*'
            else:
                Posicoes[Escolhida - 1] = 'X'

        print(mensagem_ataque(Vez, Escolhida, Posicoes[Escolhida - 1]))

        mostra_tabuleiro(Posicoes)

        Vez += 1
        

if __name__ == '__main__':
    main()
