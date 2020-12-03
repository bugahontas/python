# Pesquisa Sequencial 1: pesquisa o valor procurado pelo usuário com variável do tipo lógico.

lista = [11, 2, 70, 56, 59] # Exemplo de lista.

busca = int(input('Procurar qual valor? '))
print()

c = 0
achou = False
pos = 0
while c < len(lista):
    if lista[c] == busca:
        achou = True
        pos = c
        break
    c = c + 1

if achou == True:
    print(f'Valor {busca} encontrado na posição {pos + 1}!') # Posição a partir do 1 é mais amigável para o usuário.
else:
    print(f'Valor {busca} não encontrado.')
