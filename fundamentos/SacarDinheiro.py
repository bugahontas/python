# Sacar dinheiro: código que realiza saques em caixas automáticos de um banco fictício com base no limite permitido, saldo do usuário e nas notas disponíveis.

from math import floor, ceil # Para evitar que arredondamentos automáticos do interpretador produzam valores indesejados.

print('*' * 20,'BANCO DA PRAÇA', '*' * 20)
print('*' * 20, 'O banco do pobre', '*' * 20)
print()
print('          ATENÇÃO: somente saques de até R$1000.00')
print('        ATENÇÃO: somente saques de até 50% do saldo')
print('          Saque em notas de R$100, R$50, R$20 e R$10')
print()

saldo = float(input('Seu saldo: R$'))
s = int(input('Valor do saque: R$ '))

porc = 50 / 100 * saldo

if s > 1000 or s > porc:
    while True:
         s = int(input('VALOR ACIMA DO PERMITIDO! Digite outro valor para saque: R$ '))
         if s <= porc:
            break

# Decompõe o valor do saque nas casas de milhar, centena, dezena e unidade.
m = floor(s  / 1000)
c = floor((s % 1000) / 100)
d = floor((s % 100) / 10)
u = floor((s % 10) / 1)

tot = 0

print()
print('=' * 5, 'A IMPRIMIR:', '=' * 5)
print()
if m == 1:
    print('10 notas de R$100.00')
    tot = 10 * 100
if c != 0:
    if c >= 6:
        qtd = c
        print(f'{qtd:.0f} nota(s) de R$100.00')
        tot = tot + qtd * 100
    else:
        qtd = (c * 100) / 50
        print(f'{qtd:.0f} nota(s) de R$50.00')
        tot = tot + qtd * 50
if d >= 2:
        qtd = ceil((d * 10) / 20)
        print(f'{qtd:.0f} nota(s) de R$20.00')
        tot = tot + qtd * 20
if u != 0:
    if d == 1: # Botei esta dezena aqui ao invés da linha 47 para evitar repetir '1 nota de 10' duas vezes caso a unidade seja diferente de 0.
        print('2 notas de R$10.00')
        tot = tot + 2 * 10
    elif tot < s: # Se o total até aqui já for maior que o valor do saque, não tem porquê acrescentar mais uma nota de R$10.
        print('1 nota de R$10.00')
        tot = tot + 10

print()
print(f'Valor final do saque = R${tot:.2f}') # O valor final calculado pode ser um pouco maior que o informado pelo usuário. Mas não tem problema, porque ainda estará dentro do saldo na conta!
