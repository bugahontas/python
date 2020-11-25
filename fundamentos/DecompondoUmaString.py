# Decompondo Uma String: dada uma string ''s'', verifica a quantidade de letras e quais letras ocupam as posições 1, última e do meio.

s = 'abcdefghijk'

print(f'Tamanho da string = {len(s)} letras')
print(f'Primeira letra = {s[0]}')
print(f'Última letra = {s[-1]}') #O sinal de menos da frente indica contagem a partir da direita.

if (len(s) - 1) % 2 == 0: # A contagem começa do 0, então o total de letras passa a ser o tamanho - 1. Só existe meio para totais (tamanho - 1) pares.
    meio = int((len(s) - 1) / 2) # Converte 4.0 (float) para 4 (interger) porque o índice deve ser um valor inteiro.
    print(f'Letra do meio = {s[meio]}')
