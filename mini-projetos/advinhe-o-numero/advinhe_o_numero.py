from random import randint, sample

def gera_intervalo():
    lista_numeros = []
    for numero in range(0, 10):
        lista_numeros.append(numero)
    return lista_numeros

def numero_sorteado(lista):
    return sample(lista, 1)

def jogador_da_vez(jogador, caractere = '*', qtd = 50):
    print(caractere * qtd)
    print(f'               JOGADOR - {jogador}')
    print(caractere * qtd)
    print()

def usuario_escolhe(tentativa):
    return input(f'Tentativa {tentativa} - Advinhe um número de 0 a 9: ')

def valida_valor(usuario, caractere = 'X', qtd = 36):
    while True:
        if usuario.isdigit() and int(usuario) >= 0 and int(usuario) < 10:
            break
        else:
            print(caractere * qtd)
            usuario = input('ERRO - Digite um número de 0 a 9: ')
            print(caractere * qtd)
    return int(usuario)

def pc_escolhe():
    pc = randint(0, 9)
    return pc

def mensagem(jogador, sorteado, tentativa):
    print(f'--> {jogador} acertou o número {sorteado} na tentativa {tentativa}')
        
        
def main():
    Sorteado = numero_sorteado(gera_intervalo())

    jogador_da_vez('USUÁRIO')
    Tentativa_usuario = 1
    while True:
        Usuario = valida_valor(usuario_escolhe(Tentativa_usuario))
        if Usuario == Sorteado[0]:
            print()
            mensagem('USUÁRIO', Sorteado[0], Tentativa_usuario)
            break
        else:
            Tentativa_usuario += 1
    print()

    jogador_da_vez('COMPUTADOR')
    Tentativa_pc = 1
    while True:
        Pc = pc_escolhe()
        if Pc == Sorteado[0]:
            mensagem('COMPUTADOR', Sorteado[0], Tentativa_pc)
            break
        else:
            Tentativa_pc += 1
    

if __name__ == '__main__':
    main()
