# Caixa Registradora Básica: calcula o total da compra com base no código e quantidade do produto.

tot = 0

while True:
    cod = int(input('Código do produto = ')) # Cada produto é identificado por um código.
    print()

    if cod != 1 and cod != 2 and cod != 3 and cod != 5 and cod != 9: # Trecho de validação. O programa só continua se o usuário digitar um destes códigos.
        while True:
            cod = int(input('CÓDIGO INVÁLIDO! Insira outro código: '))
            if cod == 1 or cod == 2 or cod == 3 or cod == 5 or cod == 9:
                break

    print()
    qtd = int(input('Quantidade = '))
    print()

    if cod == 1: # O código informa o preço do produto. Nesta parte p é "preço" e recebe o valor do produto vezes a sua quantidade.
        p = 0.5 * qtd
    elif cod == 2:
        p = 1 * qtd
    elif cod == 3:
        p = 4 * qtd
    elif cod == 5:
        p = 7 * qtd
    elif cod == 9:
        p = 8 * qtd
    
    tot = tot + p 
    
    resp = input('Continuar? [S/N] ') # Outro trecho de validação. Permite inserir novos produtos.
    print()
    resp = resp.upper()
    if resp == 'N': # caso todos os produtos já tenham sido registrados.
        break

print(f'Valor total da compra = R${tot:.2f}')
