# Números e posições: cria uma lista com 5 números e exibe números e posições solicitados pelo usuário.

# Demonstra o acesso a um número e sua respectiva posição em uma lista.

# Verifica se o número e a posição existem na lista.

n = [0, 0, 0, 0, 0]

c = 0 # Cria a lista. Listas sempre começam com a posição 0.
while c <= 4:
    n[c] = int(input(f'Digite o {c + 1}o. número: ')) # Mas a posição para o usuário aqui começa a partir do 1 por fins didáticos.
    c = c + 1

print()
print('=' * 13)
print('FAZER BUSCA POR:')
print('Posição = Tecle [p]')
print('Número = Tecle [n]')
print('=' * 13)
print()
op = input('Tecla: ')

if op == 'p' or op == 'P':
    print()
    p_esc = int(input('Escolha uma posição (de 1 a 5): '))
    print()

    if p_esc < 1 or p_esc > 5: # Caso o usuário informe uma posição que não exista na lista criada.
        while True: 
            p_esc = int(input('POSIÇÃO INVÁLIDA! Digite outra posição: '))
            print()
            if p_esc >= 1 and p_esc <= 5:
                break
    
    c = 0
    while c <= 4: # Esta linha também pode ser 'while True'. Mas prefiro deixar assim para a condição ser mais explícita.
        if c == p_esc:
            print(f'Resultado -> Número na posição {p_esc} = {n[c - 1]}.') # Se eu deixar apenas 'c', o programa irá retornar o número da posição seguinte, e não da escolhida pelo usuário. Isso porquê a posição 'c' do usuário tem o valor que está na posição 'c - 1' da lista.
            break
        c = c + 1

if op == 'n' or op == 'N':
    print()
    n_esc = int(input('Escolha um número: '))
    print()

    c = 0
    sinal = 'x' # Esta variável ajudará a indicar se o número procurado pelo usuário está ou não na lista.
    while c <= 4:
        if n[c] == n_esc:
            print(f'Resultado -> Número {n_esc} na posição {c + 1}.')
            sinal = 'v' # Caso o número procurado esteja na lista.
            break
        else:
            c = c + 1

        if c > 4 and sinal == 'x': # Caso o usuário informe um número que não exista na lista criada.
            c = 0
            print('NÚMERO NÃO ENCONTRADO!')
            print()
            n_esc = int(input('Escolha um número na lista: '))
            print()
