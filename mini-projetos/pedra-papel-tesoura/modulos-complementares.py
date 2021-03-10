'''Autora: Helena Maruf'''
'''Data: 10/03/2021'''
'''Nome do arquivo: modulos-complementares.py'''
'''Módulos complementares que verificam as escolhas do usuário e do computador feitas no arquivo "pedra-papel-tesoura.py"'''
'''Salve este arquivo no mesmo diretório do arquivo pedra-papel-tesoura.py'''

#Verifica se o valor digitado pelo usuário é um número de 0 a 2.
def valida_valor(usuario, caractere = '!', qtd = 42): 
    print()
    while True:
        if usuario.isdigit() and usuario == '0' or usuario == '1' or usuario == '2':
            break
        else:
            print(caractere * qtd)
            usuario = input('----ERRO---- Digite um número de 0 a 2: ')
            print(caractere * qtd)
    return int(usuario)
            
#Funções a seguir comparam escolha do usuário com a escolha do pc.

#Função chamada se o usuário escolher 'PEDRA'.
def pedra(pc):
    if pc == 1: #Se pc escolher 'PAPEL'.
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

#Função chamada se o usuário escolher 'PAPEL'.
def papel(pc):
    if pc == 2: #Se pc escolher 'TESOURA'.
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

#Função chamada se o usuário escolher 'TESOURA'.
def tesoura(pc):
    if pc == 0: #Se pc escolher 'PEDRA'.
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

#Quando usuário e pc escolhem a mesma opção.
def empate():
    return 'EMPATE!'
