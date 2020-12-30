# Palavras E Vogais: mostra as vogais de cada palavra da tupla.

tupla = ('oi', 'Helena', 'Mercado', 'Python', 'calculadora', 'tupla', 'APRENDER')

print('Palavras e suas vogais:')
print()
for palavra in tupla:
    palavra = palavra.lower()
    print(palavra, ':', end = '  ')
    for letra in palavra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            print(letra, end = '   ')
    print()
