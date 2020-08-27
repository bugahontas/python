# Mostra a tabuada do número informado pelo usuário.

def traco(): # Traços para montar a tabela.
    print('-' * 23)

n = int(input('Tabuada do número: '))
print()

traco()
print(f'  TABUADA DE {n}')
traco()
cont = 1
while cont <= 10:
    if cont < 10: # Mantém o sinal de igual alinhado com o da última linha que está mais a frente.
        print(f'    {n} x {cont:3} = {n * cont}') 
    else:
        print(f'    {n} x {cont} = {n * cont}')
    cont = cont + 1
traco()
