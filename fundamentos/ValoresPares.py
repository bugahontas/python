# Exibe todos os valores pares no intervalo informado pelo usuário.

def traco(): # Traços para montagem da tabela.
    print('=' * 17)

ini = int(input('Primeiro número: '))
fim = int(input('Último número: '))
print()

traco()
print(f'Números pares de {ini} a {fim}:')
traco()
n = ini
while n <= fim:
    if n % 2 == 0:
        print('                  ', n)
    n = n + 1
traco()
