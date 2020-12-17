# Caixa Registradora

estoque = {'CARNE': [20.89, 1000],
                     'BANANA': [1.99, 1000],
                     'LEITE': [4.10, 1000],
                     'OVO': [10.18, 1000]}

comp = {}

tot = 0
while True:
    aux = True
    while aux:
        prod = input('Nome do produto: ')
        prod = prod.upper()
        if prod in estoque:
            aux = False
        else:
            print('ERRO! Produto inválido.')
            print()
    aux = True
    while aux:
        qtd = int(input('Quantidade: '))
        if qtd <= estoque[prod][1]:
            aux = False
        else:
            print('ERRO! Estoque insuficiente.')
            print()      
    if prod in comp:
        comp[prod] = comp[prod] + estoque[prod][0] * qtd
    else:
        comp[prod] = estoque[prod][0] * qtd
    print()
    tot = tot + estoque[prod][0] * qtd
    resp = input('Continuar? [S/n] ')
    resp = resp.lower()
    if resp == 'n':
        break
    print()

print()
print('-' * 20, 'COMPRAS', '-' * 20)
for prod, valor in comp.items():
    unid = int(valor / estoque[prod][0])
    print(f'[{prod}] --> R${estoque[prod][0]:.2f} x {unid} un. = R${valor:5.2f}')
print('-' * 54)

print()
print(f'------Valor total da compra = R${tot:.2f}------')
