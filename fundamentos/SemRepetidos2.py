# Sem Repetidos 2: junta duas listas em uma só e aplica o código 'Sem Repetidos 1' para retirar elementos repetidos.

lista1 = [1, 2, 2, 3, 4, 5, 3, 1] # Você pode mudar as listas 1 e 2 adicionando e substituindo os valores que você quiser!
lista2 = [10, 2, 4, 0, 10]

aux = []
aux.extend(lista1) # Junção das listas 1 e 2 na lista auxiliar para criar uma lista só.
aux.extend(lista2)

a = 0 # Contador do laço 1
b = 1 # Contador do laço 2

while a < (len(aux) - 1): # Laços while aninhados para comparar um elemento com os seguintes. 
    while b < len(aux):
        if aux[a] == aux[b]:
            aux[b] = 'X' # Escolhi 'X' como um marcador de elementos replicados, a serem excluídos da nova lista.
        b = b + 1
    a = a + 1
    b = a + 1

lista3 = []
a = 0 # Usei 'a' aqui também só pra não ter que criar um terceiro contador...
while a < len(aux):
    if aux[a] != 'X': # Conversão da lista auxiliar na lista 3 que é a que queremos.
        lista3.append(aux[a]) # Inclusão do elemento e exclusão das suas réplicas agora representadas por 'X'.
    a = a + 1

print(f'Lista 1 = {lista1}')
print(f'Lista 2 = {lista2}')
print(f'Lista final = {lista3}')
