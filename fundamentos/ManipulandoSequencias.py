# Manipulando Sequências: os elementos da segunda sequência são retirados da primeira, preservando os elementos repetidos da primeira.

seq1 = 'AATTGACGAC'
seq2 = 'TCT'

A = set(seq1)
B = set(seq2)

aux = A - B
C = []

for letra in aux: # Esta parte mantém os elementos repetidos da primeira sequência.
    for e in seq1:
        if e == letra:
            C.append(e)

print(f'Sequência final = [{" ".join(sorted(C))}]')
