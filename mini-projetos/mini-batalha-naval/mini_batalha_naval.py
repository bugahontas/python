from random import sample

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

    for navio in range(1, 11):
        while True:
            try:
                posicao = int(input(f'=> Navio {navio} na posição: '))
                if posicao not in posicoes or posicao in ja_escolhidas:
                    print(mensagem_erro1())
                    continue
            except Exception:
                print(mensagem_erro2())
            else:
                ja_escolhidas.append(posicao)
                break

    return ja_escolhidas


def pc_posiciona(posicoes, ja_escolhidas):
    posicoes = set(posicoes)
    ja_escolhidas = set(ja_escolhidas)

    disponiveis = list(posicoes - ja_escolhidas)

    pc_escolhe = sample(disponiveis, 10)

    return pc_escolhe


'''def jogador_ataca():
    ja_escolhidas = []

    while True:
        try:
            posicao = int(input('Mirar na posição: '))
            if posicao not in posicoes:
                print(mensagem_erro1())
                continue
        except Exception:
                print(mensagem_erro2())
        else:
            ja_escolhidas.append(posicao)
            break'''
    
    

def main():
    Posicoes = posicoes_no_tabuleiro()
    mostra_tabuleiro(Posicoes)

    Esquadra_jogador = jogador_posiciona(Posicoes)
    Esquadra_pc = pc_posiciona(Posicoes, Esquadra_jogador)
    
    for n in Esquadra_jogador:
        Posicoes[n - 1] = 'J'

    mostra_tabuleiro(Posicoes)

    '''Vez = 1

    while True:
        if Vez % 2 != 0:
            jogador_ataca()'''
        

if __name__ == '__main__':
    main()
