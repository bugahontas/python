from random import randint

todas_palavras = {1: 'bola', 2: 'dado', 3: 'casa', 4: 'parede', 5: 'assado',
                  6: 'amigo', 7: 'teclado', 8: 'divertido', 9: 'emocionante',
                  10: 'programar', 11: 'correr', 12: 'python', 13: 'cursor',
                  14: 'lista', 15: 'reclamar', 16: 'cheiroso', 17: 'bela',
                  18: 'carta', 19: 'sapato', 20: 'professor'}

def sorteia_palavra():
    chave = randint(1, 20)
    return todas_palavras[chave]

def cria_lacunas(sorteada):
    lacunas = []
    for letra in sorteada:
        lacunas.append('--')
    return lacunas
                   
def main():
    Sorteada = sorteia_palavra()
    cria_lacunas(Sorteada)
    

if __name__ == '__main__':
    main()
