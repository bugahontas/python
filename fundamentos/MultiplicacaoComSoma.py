# Multiplicação com soma: calcula o produto a partir de somas sucessivas entre os números digitados pelo usuário.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print()

cont = 1
res = 0
while cont <= n2:
    res = res + n1
    cont = cont + 1

print(f'{n1} x {n2} = {res}')
