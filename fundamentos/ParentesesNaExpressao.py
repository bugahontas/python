# Parênteses na expressão: verifica se há fechamento de parênteses em uma expressão.
## Ex1.: digite () e o programa irá mostrar 'Expressão correta'
## Ex2.: digite ())) e o programa irá mostrar erro - 'Parênteses não fecham'
## Ex3.: digite )() e o programa irá mostrar erro - 'Expressão deve começar com '(''.
# ATENÇÃO: digite apenas parênteses. 

exp = input('Digite os parênteses: ')

if exp[0] == ')':
    while True:
        print()
        print('--> ERRO! A expressão deve começar com "(".')
        exp = input('Digite novamente os parênteses: ')
        if exp[0] == '(':
            break

print()
tam = len(exp) - 1

tot = 0
c = 0
while c <= tam:
    if exp[c] == '(':
        tot = tot + 1
    else:
        tot = tot - 1
    c = c + 1

print('=' * 10,'RESULTADO', '=' * 10)
if tot == 0:
    print('                     Expressão correta!')
else:
    print('Expressão errada! Parênteses não fecham.')
