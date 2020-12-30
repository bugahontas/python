# Pesquisando Em String: verifica se o trecho procurado pelo usuário existe em uma dada string.

seq = 'AATTCGGACTTTTAACGGC'

busca = input('Buscar trecho = ')
busca = busca.upper()
print()

p = 0
enc = ''
lista = []
while p != -1:
    p = seq.find(busca, p)
    if p != -1:
        enc = 'sim'
        lista.append(p)
        p = p + 1

if enc == 'sim':
    print(f'Trecho {busca} encontrado em {len(lista)} ponto(s): | ', end = '')
    for e in lista:
        print(e, end = ' | ')    
else:
    print(f'Trecho {busca} não encontrado...')
