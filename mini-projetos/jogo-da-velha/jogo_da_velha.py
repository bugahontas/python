def posicoes_no_tabuleiro():
    return [p for p in range(1, 10)]

def mostra_tabuleiro(posicoes, horizontal = 21, vertical = 2, caracter_linha = '-', coluna = '|', espaco = '      '):
    linha = caracter_linha * horizontal
    inicio = 1
    fim = 4
    while fim <= 10:
        for p in range(inicio, fim):
            if p == fim - 1:
                print(f'{posicoes[p - 1]:^5}')
            else:
                print(f'{posicoes[p - 1]:^5} {coluna} ', end = '')
        if fim < 10:          
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
            return 'JOGADOR 1 VENCE!'
        elif O_total == 3:
            return 'JOGADOR 2 VENCE!'

        inicio = fim
        fim += 3 
        X_total = 0
        O_total = 0

    if fim > 9:
        return ''

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
    
    

def main():
    Posicoes = posicoes_no_tabuleiro()

    mostra_tabuleiro(Posicoes)

    Vez = 1
    Ja_escolhidas = []
    Resultado = ''
    
    while Resultado == '':

        if Vez % 2 != 0:
            Escolha = escolhe_posicao('JOGADOR 1', Ja_escolhidas)
            Posicoes[Escolha - 1] = 'X'
            Resultado = analisa_horizontais(Posicoes)
            Resultado = analisa_verticais(Posicoes)
        else:
            Escolha = escolhe_posicao('JOGADOR 2', Ja_escolhidas)
            Posicoes[Escolha - 1] = 'O'
            Resultado = analisa_horizontais(Posicoes)
            Resultado = analisa_verticais(Posicoes)

        mostra_tabuleiro(Posicoes)

        Vez += 1

    print()
    print()
    print(Resultado)

if __name__ == '__main__':
    main()

