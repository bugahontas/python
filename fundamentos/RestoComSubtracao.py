# Resto com subtração: calcula o resto de uma divisão a partir de subtrações sucessivas entre dividendo e divisor.

n1 = int(input('Dividendo: '))
n2 = int(input('Divisor: '))
print()

res = n1 - n2
while True:
    res = res - n2
    if res < n2:
        break

print(f'{n1} dividido por {n2} dá resto {res}')
