# É ou não é primo: verifica se o número digitado pelo usuário é ou não é primo. 

n = int(input('Digite um número: '))
print()

cont = 1
div = 0
while cont <= n:
    if n % cont == 0:
        div = div + 1
    cont = cont + 1

if div == 2:
    print(f'{n} É um número primo!')
else:
    print(f'{n} NÃO É um número primo!')
