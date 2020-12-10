# Dicionario Em Lista: junta chaves e valores em uma lista.

# Esse código não costuma ser necessário, mas achei legal fazê-lo como um desafio! ;)

dic = {'Ana': 7.5,
            'Carlos': 4.8,
            'Bia': 9.1,
            'João': 10}

lista1 = list(dic.keys()) # Transformei chaves em uma lista e valores em outra para juntá-las em uma lista final.
lista2 = list(dic.values())
lista3 = []

c = 0
while c < len(lista1):
    lista3.append([lista1[c], lista2[c]]) # Organiza cada chave com seu valor em uma lista.
    c = c + 1

for c, e in enumerate(lista3, 1):
    print(f'[{c}] {e[0]} - {e[1]}') # Mostra lista com cada chave e seu valor lado a lado.
