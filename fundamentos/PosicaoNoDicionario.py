# Posição No Dicionário: revela a posição de uma chave no dicionário.

# O loop for não é necessário para se saber o valor de uma chave. Só botei ele pra informar a posição da chave no dicionário.

# A função enumerate também informa a posição, só que de todas as chaves. Nesse caso quero apenas a posição da chave digitada pelo usuário.

dic = {'alface': 0.45,         # Dicionário com produto (chave) e preço (valor).
            'batata': 1.20,
            'tomate': 2.30,
            'biscoito': 1.50,
            'manga': 5.00}

chave = input('Digite um produto: ')
chave = chave.lower() 
print()

c = 0 # Aqui escolhi começar do zero. 
if chave in dic:
    for e in dic: # Achei legal botar o loop for para informar a posição no dicionário da chave informada pelo usuário.
        if e == chave:
            print(f'Produto [{chave}] na posição {c} - Preço = R${tabela[chave]:.2f}')   
        c = c + 1
else:
    print('ERRO - Produto não encontrado!')
