# Comparando listas: verifica as semelhanças e diferenças entre listas de compras.

lista1 = ['Banana', 'Maçã', 'Melão', 'Melancia', 'Uva', 'Manjericão', 'Agrião', 'Biscoito', 'Ovo'] # Lista antiga
lista2 = ['Pera', 'Maçã', 'Biscoito', 'Gelatina', 'Açúcar', 'Carne', 'Agrião'] # Lista nova

A = set(lista1) # Conversão das listas em conjuntos para efetuar operações embaixo.
B = set(lista2) # Ao invés de listas, eu poderia ter criado direto como conjuntos. Mas quis demonstrar a possibilidade de converter o tipo 'list' pra 'set'.

print(f'Itens mantidos = {sorted(A.intersection(B))}')
print()
print(f'Novos itens = {sorted(B - A)}')
print()
print(f'Itens removidos = {sorted(A - B)}')
