# Parênteses na expressão: verifica se há fechamento de parênteses em uma expressão matemática.

exp = input('Digite a expressão: ')

if exp[0] == ')':
    while True:
        print()
        print('--> ERRO! A expressão deve começar com "(".')
        exp = input('Digite novamente a expressão: ')
        if exp[0] == '(':
            break

print()
exp = ''.join(exp) # Para eliminar possíveis espaços vazios deixados pelo usuário.
tam = len(exp) - 1

tot = 0
c = 0
while c <= tam:
    if exp[c] == '(':
        tot = tot + 1
    elif exp[c] == ')':
        tot = tot - 1
    c = c + 1

print('=' * 10,'RESULTADO', '=' * 10)
if tot == 0: # Para cada abre-parênteses (+1) tem que ter um fecha-parênteses (-1), sempre resultando em 0.
    print('                     Expressão correta!')
else: # Se o tot final for diferente de 0, é porque algum parêntese não foi fechado.
    print('Expressão errada! Parênteses não fecham.')
