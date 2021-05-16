'''Autor: Helena Maruf'''
'''Data: 24/03/2021'''
'''Nome do arquivo: jogo_da_velha.py'''
'''Descrição: este código é uma implementação em modo texto do clássico jogo da Velha.'''
'''Funcionamento:
    --> Este jogo foi feito para duas pessoas jogarem.
    --> O jogador 1 escolhe uma posição do tabuleiro (de 1 a 9) para marcar um 'X'.
    --> Em seguida, o jogador 2 escolhe outra posição do tabuleiro para marcar um 'O'.
        --> Se o jogador escolher uma posição inválida ou já escolhida, o código dará erro e entrará em loop até o jogador digitar uma posição válida ou que ainda não tenha sido escolhida.
    --> O jogo segue alternando entre jogador 1 e jogador 2.
    --> O jogo só termina se um dos jogadores completar uma linha na vertical OU uma linha na horizontal OU uma das diagonais OU dar empate.
    --> O jogo empata se nenhum jogador conseguir fechar uma linha ou diagonal em até 9 jogadas.
    --> Exemplo de rodada:
        1. Jogador 1 bota 'X' na posição 1.
        2. Jogador 2 bota 'O' na posição 5.
        3. Jogador 1 bota 'X' na posição 4.
        4. Jogador 2 bota 'O' na posição 7.
        3. Jogador 1 bota 'X' na posição 8.
        4. Jogador 2 bota 'O' na posição 3 e fecha a diagonal 3-5-7.
        5. Resultado: Jogador 2 vence!'''


def posicoes_no_tabuleiro():
    return [p for p in range(1, 10)]


def mostra_tabuleiro(posicoes, horizontal = 21, vertical = 2, caracter_linha = '-', coluna = '|', espaco = '      '):
    linha = caracter_linha * horizontal
    inicio = 1
    fim = 4

    print()
    while fim <= 10:
        for p in range(inicio, fim):
            if p == fim - 1: # Para posições da ponta direita (3, 6 e 9) que não têm coluna à direita.
                print(f'{posicoes[p - 1]:^5}')
            else:
                print(f'{posicoes[p - 1]:^5} {coluna} ', end = '')
        if fim < 10: # Exclui posições da última linha (7, 8 e 9) que não têm linha abaixo.         
            print(linha)
        inicio = fim
        fim += 3

    return posicoes
            

def escolhe_posicao(jogador, ja_escolhidas):
    print()

    if jogador == 'JOGADOR 1':
        escolha = input(f'{jogador} - Botar "X" na posição: ')    
    else:
        escolha = input(f'{jogador} - Botar "O" na posição: ')
    print()

    while True:
        if escolha.isdigit() and 1 <= int(escolha) <= 9 and escolha not in ja_escolhidas:
            ja_escolhidas.append(escolha)
            escolha = int(escolha)
            return escolha
        else:
            print('ERRO - POSIÇÃO INVÁLIDA OU JÁ ESCOLHIDA!')
            escolha = input('Escolha outra posição: ')
            print()
            

# Detecta as marcações feitas em todas as linhas horizontais do tabuleiro.
def analisa_horizontais(posicoes):
    inicio = 0
    fim = 3
    X_total = 0
    O_total = 0

    while fim <= 9:
        for p in range(inicio, fim):
            if posicoes[p] == 'X':
                X_total += 1
            elif posicoes[p] == 'O':
                O_total += 1
        if X_total == 3:
            return 'JOGADOR 1 VENCE!' # Será armazenado na variável Resultado lá em main().
        elif O_total == 3:
            return 'JOGADOR 2 VENCE!' # Será armazenado na variável Resultado lá em main().
        inicio = fim
        fim += 3 
        X_total = 0
        O_total = 0

    if fim > 9:
        return ''


# Detecta as marcações feitas em todas as linhas verticais do tabuleiro.
def analisa_verticais(posicoes):
    inicio = 0
    fim = 6
    X_total = 0
    O_total = 0

    while fim <= 8:
        for p in range(inicio, fim + 1, 3):
            if posicoes[p] == 'X':
                X_total += 1
            elif posicoes[p] == 'O':
                O_total += 1
        if X_total == 3:
            return 'JOGADOR 1 VENCE!'
        elif O_total == 3:
            return 'JOGADOR 2 VENCE!'
        inicio += 1 
        fim += 1 
        X_total = 0
        O_total = 0

    if fim > 8:
        return ''


# Detecta as marcações feitas em ambas as diagonais do tabuleiro.
def analisa_diagonal(posicoes):
    X_total = 0
    O_total = 0
    inicio = 0
    fim = 8
    passo = 4

    while fim != 4:
        for p in range(inicio, fim + 1, passo):
            if posicoes[p] == 'X':
                X_total += 1
            elif posicoes[p] == 'O':
                O_total += 1
            if X_total == 3:
                return 'JOGADOR 1 VENCE!'
            elif O_total == 3:
                return 'JOGADOR 2 VENCE!'
        inicio += 2
        fim -= 2
        passo = 2
        X_total = 0
        O_total = 0
    
    if fim == 4:
        return ''


def mensagem_final(resultado, caractere = '=', qtd = 20):
    print()
    print()
    print(f'{caractere * qtd} RESULTADO = ', end = '')
    if resultado == '':
        print(f'EMPATE! {caractere * qtd}')
    else:    
        print(f'{resultado} {caractere * qtd}')
    

def main():
    Posicoes = posicoes_no_tabuleiro()

    mostra_tabuleiro(Posicoes)

    Vez = 1
    Ja_escolhidas = [] # Lista com posições já escolhidas durante a rodada.
    Resultado = ''
    
    while Resultado == '' and Vez < 10:
        if Vez % 2 != 0:
            Escolha = escolhe_posicao('JOGADOR 1', Ja_escolhidas)
            Posicoes[Escolha - 1] = 'X'
            Resultado = analisa_horizontais(Posicoes)
            if Resultado == '':
                Resultado = analisa_verticais(Posicoes) # Chamada somente se o Resultado anterior for vazio.
                if Resultado == '':
                    Resultado = analisa_diagonal(Posicoes) # Chamada somente se o Resultado anterior for vazio.
        else:
            Escolha = escolhe_posicao('JOGADOR 2', Ja_escolhidas)
            Posicoes[Escolha - 1] = 'O'
            Resultado = analisa_horizontais(Posicoes)
            if Resultado == '':
                Resultado = analisa_verticais(Posicoes)
                if Resultado == '':
                    Resultado = analisa_diagonal(Posicoes)

        mostra_tabuleiro(Posicoes)

        Vez += 1

    mensagem_final(Resultado)


if __name__ == '__main__':
    main()
