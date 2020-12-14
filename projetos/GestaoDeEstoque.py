# Gestão De Estoque: solicita ao usuário produto e quantidade a comprar, exibe o valor total da compra e o novo estoque após a transação.

estoque = {'Macarrão': [433, 5.40],          # Produtos do estoque com suas quantidades e preços unitários.
                     'Refrigerante': [1000, 2.19],
                     'Biscoito': [2470, 0.99],
                     'Sorvete': [100, 24.50]}

venda = []
while True:
    aux = True
    while aux: # Verifica se o produto informado pelo usuário existe no estoque.
        prod = input('Produto: ')
        if prod in estoque:
            aux = False
        else:
            print('ERRO - Produto inválido!')
            print()
    aux = True
    while aux: # Verifica se a quantidade informada pelo usuário está disponível em estoque.
        qtd = int(input('Quantidade: '))
        if qtd <= estoque[prod][0]:
            aux = False
        else:
            print('ERRO - Estoque insuficiente!')
            print()
    venda.append([prod, qtd]) # Lista com todos os produtos e quantidades informados pelo usuário.
    print()
    resp = input('Continuar? [S/n] ')
    resp = resp.lower()
    if resp == 'n':
        break
    print()
print()

tot = 0
for e in venda:
    prod, qtd = e
    preco = estoque[prod][1]
    custo = preco * qtd # Referente a cada produto.
    print(f'{prod} - {preco:.2f} x {qtd} = R${custo:.2f}')
    tot = tot + custo # Soma o custo de todos os produtos comprados.
    estoque[prod][0] = estoque[prod][0] - qtd

print()
print(f'Valor total da compra = R${tot:.2f}')
print()

print('Estoque atual:')
for chave, valor in estoque.items(): # Mostra produtos e novas quantidades após a compra.
    print(f'Produto: {chave}')
    print(f'Quantidade: {valor[0]}')
    print(f'Preço: R${valor[1]:.2f}')
    print()
