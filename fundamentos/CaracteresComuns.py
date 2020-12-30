# Caracteres Comuns: verifica caracteres comuns às duas strings através de conjuntos e método .intersection

seq1 = 'AAACTBF'
seq2 = 'CBTAF'

conj1 = set(seq1)
conj2 = set(seq2)
res = conj1.intersection(conj2)

print(f'Caracteres comuns = [{"".join(res)}]')
