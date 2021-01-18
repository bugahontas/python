# AdvinhaUmValor: jogo para dois jogadores. Cada jogador tem que advinhar um valor inteiro de 0 a 10 na sua rodada.
# O jogador que acertar o número inteiro sorteado em menos tentativas ganha!
# O enunciado é bem claro: valor INTEIRO de 0 a 10.
        # Se a criatura insistir em um valor não-inteiro ou fora do intervalo:
                # Sua tentativa não será gasta.
                # Mas o jogo não vai prosseguir até o ser iluminado querer jogar direito...

from random import randint        

def linha_topo(caractere = '*', n = 20):
    print(caractere * n)

def topo(j):
    linha_topo()
    print(f'      JOGADOR {j}')
    linha_topo()

def verifica(v):
    while True:
        if v.isdigit() and 0 <= int(v) <= 10:
            return int(v)
        else:
            v = input('CRIATURA, DIGITE UM NÚMERO ==INTEIRO ENTRE 0 e 10==: ')

def jogo(t):
    while True:
        n = input(f'Tentativa {t} - Digite um número inteiro entre 0 e 10: ')
        n = verifica(n)    
        sort = randint(0, 10)
        print(f'Número sorteado = {sort}')
        if n == sort:
            return t
        else:
            print('ERROU, TENTE NOVAMENTE!')
            print()
        t = t + 1

topo(1)
j1 = jogo(1)
print(f'--------JOGADOR 1 - ACERTOU NA {j1}a. TENTATIVA!--------')
print()

topo(2)
j2 = jogo(1)
print(f'--------JOGADOR 2 - ACERTOU NA {j2}a. TENTATIVA!--------')
print()

print(f'PLACAR - JOGADOR 1    [{j1}]    x    [{j2}]    JOGADOR 2')
print()
if j1 < j2:
    print('                      VENCEDOR = JOGADOR 1!')
elif j2 < j1:
    print('                      VENCEDOR = JOGADOR 2!')
else:
    print('                                 EMPATE!')
