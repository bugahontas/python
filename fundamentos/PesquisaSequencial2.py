# Pesquisa Sequencial 2: pesquisa o valor procurado pelo usuário sem variável do tipo lógico.

lista = [11, 2, 70, 56, 59] # Exemplo de lista.

busca = int(input('Procurar qual valor? '))
print()

c = 0
pos = 0
while c < len(lista):
    if lista[c] == busca:
        pos = c
        print(f'Valor {busca} encontrado na posição {pos + 1}!') # Posição a partir do 1 é mais amigável para o usuário.
        break
    c = c + 1

if c == len(lista): # Contador chegou ao fim sem achar o valor procurado.
    print(f'Valor {busca} não encontrado.')
