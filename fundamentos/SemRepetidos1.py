# Sem Repetidos 1: verifica e retira elementos repetidos dentro de uma lista.

lista = ['a', 'b', 'a'] # Você pode mudar esta lista adicionando e substituindo os valores que você quiser!
print(f'Antes = {lista}')

a = 0 # Contador do laço 1
b = 1 # Contador do laço 2

while a < (len(lista) - 1): # Laços while aninhados para comparar um elemento com os seguintes. 
    while b < len(lista):
        if lista[a] == lista[b]:
            lista[b] = 'X' # Escolhi 'X' como um marcador de elementos replicados, a serem excluídos da nova lista.
        b = b + 1
    a = a + 1
    b = a + 1

nova = []
a = 0 # Usei 'a' aqui também só pra não ter que criar um terceiro contador...
while a < len(lista):
    if lista[a] != 'X':
        nova.append(lista[a]) # Inclusão do elemento e exclusão das suas réplicas agora representadas por 'X'.
    a = a + 1

print(f'Depois = {nova}')
