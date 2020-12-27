# Notacao Posicional: o usuário informa um número inteiro e o programa exibe o valor de cada algarismo na base 10.

n = int(input('Digite um número inteiro qualquer: '))
print()

aux = str(n)
tam = len(aux)

e = tam - 1
cd = []

alg = int(n / 10 ** e)
cd.append(alg)
res = n % 10 ** e

while e > 0:
    e = e - 1
    alg = int(res / 10 ** e)
    cd.append(alg)
    res = res % 10 ** e

print(f'Algarismos do número {n} = ', end = '')
print(cd)
print()
print('Da esquerda para a direita:')

e = tam - 1
for casa in cd:
    print(f'{casa} x 10 elevado a {e} = {casa * (10 ** e)}')
    e = e - 1
