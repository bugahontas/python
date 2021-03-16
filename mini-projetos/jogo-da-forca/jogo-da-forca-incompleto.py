from random import randint

todas_palavras = {1: 'bola', 2: 'dado', 3: 'casa', 4: 'parede', 5: 'assado',
                  6: 'amigo', 7: 'teclado', 8: 'divertido', 9: 'tatu',
                  10: 'programar', 11: 'correr', 12: 'python', 13: 'cursor',
                  14: 'lista', 15: 'reclamar', 16: 'cheiroso', 17: 'bela',
                  18: 'usado', 19: 'sapato', 20: 'professor', 21: 'roupa',
                  22: 'jogo', 23: 'animal', 24: 'boneca', 25: 'ganhar',
                  26: 'ditado', 27: 'popular', 28: 'escrever', 29: 'falar',
                  30: 'querida'}

def sorteia_palavra():
    chave = randint(1, 20)
    return todas_palavras[chave]

def total_tentativas(sorteada):
    return len(sorteada) * 3

def cria_lacunas(sorteada):
    lacunas = []
    for letra in sorteada:
        lacunas.append('--')
    return lacunas

def usuario_escolhe():
    while True:
        escolha = input('Escolha uma letra: ')
        if escolha.isalpha() and len(escolha) == 1:
            return escolha.lower()
        else:
            print('ERRO!')
            print()

def acertou_ou_errou(escolha, sorteada, lacunas, erradas):
    i = 0
    if escolha in sorteada:
        for letra in sorteada:
            if letra == escolha:
                lacunas[i] = letra
            i += 1
    else:
        erradas.append(escolha)

    return lacunas, erradas

def mostra_chutes(lacunas, erradas):
    print()
    print(f'         Palavra da vez: {lacunas}')
    print()
    print(f'Chutes errados: {erradas}')
    print()
        
        
                   
def main():
    Sorteada = sorteia_palavra()
    Limite = total_tentativas(Sorteada)
    Lacunas = cria_lacunas(Sorteada)
    Erradas = []
    Tentativa = 1
    Index = 0
    print(Sorteada)
    while Tentativa <= Limite:
        Escolha = usuario_escolhe()
        Lacunas, Erradas = acertou_ou_errou(Escolha, Sorteada, Lacunas, Erradas)
        mostra_chutes(Lacunas, Erradas)

if __name__ == '__main__':
    main()
