# Parâmetro end: faz a função print exibir valores lado a lado, sem pular linha.

lista = []

c = 0
for n in range (0, 12, 2): # O intervalo começa no 0 e é aberto em 12, com valores pulando de 2 em 2.
    lista.append(n)
    c = c + 1
    if c == 6:
        print(n, end = '')
    else:
        print(n, end = '-') # Imprime traço apenas entre os valores.

print()
print(f'Lista criada = {lista}')
