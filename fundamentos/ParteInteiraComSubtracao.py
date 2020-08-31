# Parte inteira com subtração: calcula a parte inteira do quociente de uma divisão a partir de subtrações sucessivas entre dividendo e divisor.

# Também mostra o resto.

n1 = int(input('Dividendo: '))
n2 = int(input('Divisor: '))
print()

if n1 % n2 == 0:
    aux = n1 - n2
    q = 1
    while aux != 0:
        aux = aux - n2
        q = q + 1 # 'q' aqui é uma espécie de contador que conta quantas vezes 'n2' cabe em 'n1'
else:
    novo_n1 = n1 - (n1 % n2) # Desconsidera o resto para se obter apenas a parte inteira do quociente.
    aux = novo_n1 - n2
    q = 1
    while aux != 0:
        aux = aux - n2
        q = q + 1

print(f'{n1} / {n2} = {q}') 
print(f'Resto = {n1 % n2}')
