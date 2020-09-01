# Média do aluno: calcula a média ponderada das 3 notas de um aluno com seus respectivos pesos.

# Uso de listas junto com estrutura de repetição.

nome = input('Nome: ')
print()

nota = [0, 0, 0]
peso = [0, 0, 0]

c = 0
soma_n = 0
soma_p = 0
while c <= 2:
    nota[c] = float(input(f'{c + 1}a. Nota = '))
    peso[c] = int(input(f'Peso da {c + 1}a. Nota = '))
    print()
    np = nota[c] * peso[c]
    soma_n = soma_n + np
    soma_p = soma_p + peso[c]
    c = c + 1

c = 0
print()
while c <= 2:
    print(f'Nota {c + 1} = {nota[c]} x peso {peso[c]}')
    c = c + 1

med = soma_n / soma_p

print()
print(f'Média final de {nome}= {med:.2f}')
