# Elementos Não Compartilhados: exibe apenas os elementos exclusivos de A e exclusivos de B.

seq1 = 'AATCVERY'
seq2 = 'YAWSSQVCYT'

A = set(seq1)
B = set(seq2)
inter = A.intersection(B)
res = (A - inter) | (B - inter)

print(f'Elementos não-compartilhados = {", ".join(sorted(res))}')
