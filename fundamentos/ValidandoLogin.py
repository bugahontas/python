# Validando Login: permite ao usuário criar senha e verifica se a senha digitada durante login é igual à senha criada.

senha = input('Crie sua senha: ')
print()

login = input('Digite sua senha: ')
print()

if login != senha:
    while True:
        login = input('SENHA INCORRETA! Redigite a senha: ')
        if login == senha:
            break

print()
print('Acesso liberado!')
