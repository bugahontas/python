def valida_valor(usuario, caractere = '!', qtd = 42):
    print()
    while True:
        if usuario >= 0 and usuario <= 2:
            break
        else:
            print(caractere * qtd)
            usuario = int(input('----ERRO---- Digite um número de 0 a 2: '))
            print(caractere * qtd)
    return usuario
            
def pedra(pc): 
    if pc == 1:
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

def papel(pc):
    if pc == 2:
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

def tesoura(pc):
    if pc == 0:
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

def empate():
    return 'EMPATE!'
