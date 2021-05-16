'''Autor: Helena Maruf'''
'''Data: 17/03/2021'''
'''Nome do arquivo: jogo_da_forca.py'''
'''Descrição: este código é uma implementação em modo texto do clássico jogo da Forca.'''
'''Funcionamento:
    --> O código conta com uma coleção de 30 palavras e sorteia uma delas.
    --> A palavra sorteada permanece escondida na forma de lacunas vazias.
    --> O usuário deve digitar uma letra em cada tentativa.
        --> Neste código, o número total de tentativas é igual ao tamanho da palavra sorteada vezes 2.
        --> Se a letra digitada constar na palavra, a lacuna é preenchida com essa letra.
        --> Se a letra digitada não constar na palavra, a tentativa é gasta e não haverá nenhuma substituição de lacuna por letra.
        --> Se o usuário digitar um número, mais de uma letra na mesma tentativa ou uma letra que já foi dita, o código dará erro e entrará em loop até o usuário digitar uma letra nova e válida.
    --> A palavra será revelada aos poucos conforme o usuário for digitando letras certas.
    --> Se o usuário completar a palavra dentro do limite máximo de tentativas, ele ganha.
    --> Se o limite máximo de tentativas estourar e ainda houver lacunas vazias, será FORCA e o usuário perde.
    --> Exemplo de rodada:
        1. Palavra sorteada: "jogo" (Escondida em 4 lacunas: --,--,--,--). Então, o máximo de tentativas será: 4 letras x 2 = 8
        2. Tentativa 1: usuário digita letra errada "a", que não consta em "jogo".
        3. Tentativa 2: usuário digita letra certa "o". Assim, as lacunas ficam: --, o, --, o.
        4. As tentativas seguintes serão no mesmo esquema das tentativas 1 e 2.
        5. Se o usuário completar a palavra "jogo" em até 8 tentativas, vence.
        6. Passadas as 8 tentativas, se ainda houver lacuna vazia, o resultado será FORCA e o usuário perde.'''
             
from random import randint

# Dicionário que contém todas as palavras possíveis de serem sorteadas pelo código.
todas_palavras = {1: 'bola', 2: 'dado', 3: 'casa', 4: 'parede', 5: 'assado',
                  6: 'amigo', 7: 'teclado', 8: 'divertido', 9: 'tatu',
                  10: 'programar', 11: 'correr', 12: 'python', 13: 'cursor',
                  14: 'lista', 15: 'reclamar', 16: 'cheiroso', 17: 'bela',
                  18: 'usado', 19: 'sapato', 20: 'professor', 21: 'roupa',
                  22: 'jogo', 23: 'animal', 24: 'boneca', 25: 'ganhar',
                  26: 'ditado', 27: 'popular', 28: 'escrever', 29: 'falar',
                  30: 'querida'}

# Sorteia um número inteiro de 1 a 30 que corresponde à chave de cada palavra do dicionário.
def sorteia_palavra():
    chave = randint(1, 30)
    return todas_palavras[chave]

def total_tentativas(sorteada):
    return len(sorteada) * 2

def cria_lacunas(sorteada):
    lacunas = []
    for letra in sorteada:
        lacunas.append('--')
    return lacunas

# Separa uma tentativa da outra, organizando mais o visual do jogo.
def separador(caractere = '-', qtd = 70):
    print(caractere * qtd)

# Valida input do usuário.
def usuario_escolhe(tentativa, escolhidas):
    while True:
        escolha = input(f'Tentativa {tentativa} - Escolha uma nova letra: ')
        if escolha.isalpha() and len(escolha) == 1: # '== 1' para caso o usuário digite duas letras em uma mesma tentativa.
            if escolha not in escolhidas:
                escolhidas.append(escolha) # Lista que contém letras já digitadas pelo usuário.
                break
            else:
                print(f'ERRO - Letra {escolha} já foi escolhida!') #O código também não admite que o usuário digite qualquer letra certa ou errada mais de uma vez.
                print()
        else:
            print('ERRO - Você não digitou uma letra!')
            print()
    return escolha.lower()

# Se a letra digitada for certa, a letra substitui a lacuna da mesma posição que ocupa na palavra.
def acertou_ou_errou(escolha, sorteada, lacunas, erradas):
    i = 0 # Posição
    if escolha in sorteada:
        for letra in sorteada:
            if letra == escolha:
                lacunas[i] = letra
            i += 1
    else:
        erradas.append(escolha)

    return lacunas, erradas

# Mostra lacunas e letras erradas a cada tentativa.
def mostra_chutes(lacunas, erradas):
    print()
    print(f'         Palavra da vez: {lacunas}')
    print()
    print(f'Chutes errados: {erradas}')
    print()
        
def resultado(tentativa, limite, sorteada):
    print()
    if tentativa > limite:
        print('                          FORCA!')
        print()
        print(f'            A palavra correta era:    {sorteada}')
    else:
        print('               PARABÉNS! Você acertou a palavra!')
                      
def main():
    Sorteada = sorteia_palavra()
    Limite = total_tentativas(Sorteada)
    Lacunas = cria_lacunas(Sorteada)

    Escolhidas = []
    Erradas = []
    Tentativa = 1
    Index = 0

    while Tentativa <= Limite:
        separador()
        Escolha = usuario_escolhe(Tentativa, Escolhidas)
        Lacunas, Erradas = acertou_ou_errou(Escolha, Sorteada, Lacunas, Erradas)
        mostra_chutes(Lacunas, Erradas)
        if '--' not in Lacunas: # Indica que todas as lacunas já foram substituídas por letras certas.
            break
        else:
            Tentativa += 1

    resultado(Tentativa, Limite, Sorteada)

if __name__ == '__main__':
    main()
