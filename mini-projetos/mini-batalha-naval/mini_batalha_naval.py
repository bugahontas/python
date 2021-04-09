'''Autora: Helena Maruf'''
'''Data: 09/04/2021'''
'''Nome do arquivo: mini_batalha_naval.py'''
'''Descrição: este código é uma implementação mais simples do jogo clássico "Batalha naval", pois aqui cada navio mede apenas uma célula.'''
'''Funcionamento:
    --> Este é um jogo entre jogador (usuário) e computador.
    --> Jogador e computador tem 10 navios cada para posicionarem em um tabuleiro com posições numeradas de 1 a 40.
        --> Cada um escolhe suas posições separadamente e um não sabe das posições do outro. 
    --> Jogador advinha uma posição em que um navio do computador possa estar.
    --> Em seguida, Computador advinha uma posição em que um navio do Jogador possa estar.
    --> Jogador e Computador se alternam ao longo da partida.
        --> Se Jogador/Computador acertar uma posição, esta é marcada com um "*", o navio é atacado e a frota do adversário é reduzida em um navio. 
        --> Se Jogador/Computador errar a posição, esta é marcada com um "X" e nenhuma das frotas é alterada.
        --> Se Jogador digitar uma posição inválida ou já escolhida por alguém, o código entrará em loop até o Jogador digitar uma posição válida e disponível para ataque.
    --> Vence quem atacar primeiro todos os navios da frota inimiga (isto é, reduzi-la a 0).
    --> Exemplo de rodada:
            1. Jogador escolhe posições [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] do tabuleiro.
            2. Computador escolhe posições [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] do tabuleiro.
            3. Jogador mira na posição [40] e erra. Então posição [40] recebe um "X".
            4. Computador mira na posição [5] e acerta um navio adversário. Então posição [5] recebe um "*".
            5. O jogo continua e Computador acerta todas as posições do Jogador enquanto Jogador acertou apenas 3 posições do Computador.
            6. Navios restantes: Jogador   0 X 7  Computador. Logo, Computador vence!'''



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
            if p == fim - 1: # Para posições da ponta direita (8, 16, 24, 32, 40) que não têm coluna à direita.
                print(f'{posicoes[p - 1]:^5}')
            else:
                print(f'{posicoes[p - 1]:^5} {coluna} ', end = '')
        if fim < 40:  
            print(linha) # Exclui posições da última linha (33 a 40) que não têm linha abaixo.
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

    return sorted(frota) # Ordem crescente para organizar a apresentação das posições escolhidas.


def mensagem_frota_jogador(frota):
    print(f'==> Sua frota nas posições: {frota} <==') # Sempre exibida para Jogador não se perder e não mirar na própria frota.
    print()


def pc_posiciona(posicoes, frota):
    posicoes = set(posicoes)
    frota = set(frota)

    disponiveis = list(posicoes - frota) # Aqui também um "for" com "not in", mas preferi abordar com conjuntos se não o código fica com muito "for".

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
        if isinstance(p, int): # Testa se a posição é um número inteiro (ou seja, ainda disponível) ou se é um caractere ('*' ou 'X') e, portanto, já usada.
            posicoes_restantes.append(p)

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
    print()
    print('                   VENCEDOR = ', end = '')
    if restantes_jog == 0:
        print('COMPUTADOR!')
    else:
        print('JOGADOR!')


def main():
    Posicoes = posicoes_no_tabuleiro()
    mostra_tabuleiro(Posicoes)

    Frota_jogador = jogador_posiciona(Posicoes)
    Frota_pc = pc_posiciona(Posicoes, Frota_jogador)

    mostra_tabuleiro(Posicoes)

    Navios_jogador = len(Frota_jogador)
    Navios_pc = len(Frota_pc)

    Vez = 1

    while Navios_jogador != 0 and Navios_pc != 0: # Repete até que a frota de um ou outro seja igual a 0.
        if Vez % 2 != 0:
            mensagem_frota_jogador(Frota_jogador)

            Escolhida = jogador_ataca(Posicoes, Frota_jogador)

            if Escolhida in Frota_pc: # Indica que Jogador acertou uma posição do Computador.
                Posicoes[Escolhida - 1] = '*'
                Navios_pc -= 1 
            else:
                Posicoes[Escolhida - 1] = 'X'

            mensagem_ataque('VOCÊ', Escolhida, Posicoes[Escolhida - 1])

        else:
            Escolhida = pc_ataca(Posicoes, Frota_pc)

            if Escolhida in Frota_jogador: # Indica que Computador acertou uma posição do Jogador.
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
