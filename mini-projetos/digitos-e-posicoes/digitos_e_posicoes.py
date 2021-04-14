'''Autora: Helena Maruf'''
'''Data: 14/04/2021'''
'''Nome do arquivo: digitos_e_posicoes.py'''
'''Descrição: advinhe o dígito de cada posição seguindo pistas para descobrir o número secreto!'''
'''Funcionamento:
    --> Este é um jogo entre jogador (usuário) e computador.
    --> O computador irá sortear um número de 100 a 999 que não será revelado.
    --> O jogador irá informar um número de 100 a 999.
        --> Se o jogador informar uma letra ou qualquer número fora desse intervalo, o código entrará em loop até o usuário digitar os dados corretos.
    --> As pistas são dadas por dígito do número do jogador, lido da esquerda para a direita.
        --> Pista "errado": dígito não consta em nenhuma posição do número sorteado pelo computador.
        --> Pista "certo na posição errada": dígito consta no número sorteado, mas em uma posição diferente da digitada.
        --> Pista "certo na posição certa": dígito consta e está na mesma posição que no número sorteado.
    --> O jogador tem até 7 tentativas para advinhar o número sorteado a partir das pistas.
    --> Se o usuário acertar todas as posições em até 7 tentativas, vence. Se não, perde.
    --> Exemplo de rodada:
            1. Computador sorteia número "376".
            2. Jogador informa número "365".
            3. Pistas: 3 = certo na posição certa; 6 = certo na posição errada; 5 = errado.
            4. A partir das pistas, jogador informa outro número: "346".
            5. Pistas: 3 = certo na posição certa; 4 = errado; 6 = certo na posição certa.
            6. Jogador mantém os dígitos certos nas posições certas e descarta os errados.
            7. Jogador forma o número "376" na tentativa 7. Logo, vence!
    --> ATENÇÃO: ESTE JOGO TEM PEGADINHAS!! Fique esperto(a) e use sua lógica!'''
    

from random import randint


def gera_numero():
    return str(randint(100, 999))


def usuario_escolhe():
    while True:
        numero = input(f'Número (de 100 a 999): ')

        if numero.isdigit() and int(numero) >= 100 and int(numero) <= 999:
            return numero
        else:
            print('***** ERRO - Digite um número de 100 a 999!')
            print()
            

def verifica_digitos(sorteado, chute):
    total_certos = 0

    print()
    for index in range(3):
        print(f'{chute[index]} = ', end = '')

        if chute[index] in sorteado:
            print('certo ', end = '')        

            if chute[index] == sorteado[index]:
                print('na posição certa')
                total_certos += 1
            else:
                print('na posição errada')

        else:
            print('errado')
    print()

    return total_certos


def mensagem(sorteado, acertos, tentativa):
    if acertos == 3 and tentativa <= 7:
        return '--> PARABÉNS! Você acertou o número ' + sorteado + ' em ' + str(tentativa) + ' tentativa(s)!'
    else:
        return '--> QUE PENA! Você não conseguiu advinhar o número ' + sorteado + ' a tempo...'


def main():
    Sorteado = gera_numero()

    Acertos = 0
    Tentativa = 0

    while Acertos != 3 and Tentativa < 7:
        Tentativa += 1
        Chute = usuario_escolhe()
        Acertos = verifica_digitos(Sorteado, Chute)

    print(mensagem(Sorteado, Acertos, Tentativa))
            

if __name__ == '__main__':
    main()
