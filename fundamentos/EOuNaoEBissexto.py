# É ou Não É Bissexto: verifica se o ano digitado pelo usuário é ou não é bissexto.

ano = int(input('Digite um ano: '))
print()

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
