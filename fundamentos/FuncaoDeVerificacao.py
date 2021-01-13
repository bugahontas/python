# Funcao de Verificacao: verifica se um valor está no intervalo de 0 a 10.

def verif(m, M):
    while True:
        v = int(input('Digite um número de 0 a 10: '))
        print()
        if v >= m and v <= M:
            return v
        else:
            print('ERRO!')
            print()

print(f'Você digitou o número {verif(0, 10)}!')
