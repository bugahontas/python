# Ordem Invertida: inverte a posição dos elementos de trás pra frente em uma lista.

lista = [10, 20, 30, 40, 50] # Exemplo de lista

c = -1 # Contagem da direita para a esquerda
while c >= -len(lista): 
    print(lista[c])
    c = c - 1
