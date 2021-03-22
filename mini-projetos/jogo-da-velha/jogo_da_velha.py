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
        
def verifica_resultado(posicoes):
    X_total = 0
    O_total = 0

    inicio = 0
    fim = 3
    while fim <= 10:
        for p in range(inicio, fim):
            if posicoes[p] == 'X':
                X_total += 1
            if posicoes[p] == 'O':
                O_total += 1
            if X_total == 3:
                sinal = 'para'
                X_venceu = True
                return sinal, X_venceu
            if O_total == 3:
                sinal = 'para'
                O_venceu = True
                return sinal, O_venceu
            
            
        inicio = fim
        fim += 3 
            
        
    
            
def main():
    Posicoes = posicoes_no_tabuleiro()

    mostra_tabuleiro(Posicoes)

    Vez = 1
    Ja_escolhidas = []
    Sinal = ''
    X_Venceu = False
    O_Venceu = False

    while Sinal == '':

        if Vez % 2 != 0:
            Escolha = escolhe_posicao('JOGADOR 1', Ja_escolhidas)
            Posicoes[Escolha - 1] = 'X'
            Sinal = verifica_resultado(mostra_tabuleiro(Posicoes))
        else:
            Escolha = escolhe_posicao('JOGADOR 2', Ja_escolhidas)
            Posicoes[Escolha - 1] = 'O'
            Sinal = verifica_resultado(mostra_tabuleiro(Posicoes))

        Vez += 1

        



if __name__ == '__main__':
    main()

