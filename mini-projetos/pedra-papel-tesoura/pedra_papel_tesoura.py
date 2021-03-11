'''Autora: Helena Maruf'''
'''Data: 10/03/2021'''
'''Nome do arquivo: pedra-papel-tesoura.py'''
'''Descrição: este código é uma implementação em texto do jogo clássico "Pedra, Papel, Tesoura."'''
'''Funcionamento:
    --> O usuário escolhe uma opção teclando 0 para "PEDRA," 1 para "PAPEL" ou 2 para "TESOURA".
    --> Depois, é a vez do computador escolher gerando aleatoriamente um desses valores.
    --> Se o número escolhido pelo usuário for válido, ele é comparado com o número escolhido pelo computador.
        OBS.: se o usuário digitar letras e/ou números fora do intervalo de 0 a 2, o código dará erro e entrará em loop até o usuário digitar 0, 1 ou 2.
    --> Lembrando que PEDRA vence TESOURA, TESOURA vence PAPEL, PAPEL vence PEDRA.
        -- Se usuário e computador escolherem a mesma opção (PEDRA-PEDRA, PAPEL-PAPEL ou TESOURA-TESOURA), haverá empate!
    --> Para sair do jogo, tecle 9. Para continuar jogando, aperte qualquer tecla sem ser o 9.
    --> Exemplo de rodada:
            1. Usuário tecla 0 (referente a PEDRA)
            2. Computador gera aleatoriamente o número 1 (referente a PAPEL)
            3. Então, o placar será mostrado como PEDRA X PAPEL
            4. PAPEL vence PEDRA. Logo, computador vence!'''

from random import randint

opcoes = {0: 'PEDRA',
          1: 'PAPEL',
          2: 'TESOURA'}

def menu(caractere = '=', qtd = 29):
    print(caractere * qtd)
    print('   PEDRA----------Tecle [0]   ')
    print('   PAPEL----------Tecle [1]   ')
    print('  TESOURA---------Tecle [2]   ')
    print(caractere * qtd)

def usuario_escolhe(): 
    return input('Qual você escolhe? ')

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

def pc_escolhe():
    pc = randint(0, 2) #Aqui o pc escolhe (gera) um número aleatório de 0 a 2.
    return pc

def placar(usuario, pc, caractere = '-', qtd = 25):
    print()
    print(caractere * qtd)
    print('         PLACAR        ')
    print(caractere * qtd)
    print(f'   {opcoes[usuario]}  X  {opcoes[pc]}')
    print(caractere * qtd)

#Funções pedra(), papel(), tesoura() e empate() comparam a escolha do usuário com a escolha do pc.

#Esta função será chamada se a escolha do usuário for PEDRA.
def pedra(pc): 
    if opcoes[pc] == 'PAPEL':
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

#Esta função será chamada se a escolha do usuário for PAPEL.
def papel(pc):
    if opcoes[pc] == 'TESOURA':
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

#Esta função será chamada se a escolha do usuário for TESOURA.
def tesoura(pc):
    if opcoes[pc] == 'PEDRA':
        return 'COMPUTADOR!'
    else:
        return 'VOCÊ!'

#Esta função será chamada se usuário e pc fizerem a mesma escolha.
def empate():
    return 'EMPATE!'

#Mostra quem venceu ou se houve empate.
def mensagem_final(usuario, pc):
    print()
    if opcoes[usuario] == opcoes[pc]:
        print(f'  RESULTADO = {empate()}')
    else:
        print('   VENCEDOR = ', end = '')
        if opcoes[usuario] == 'PEDRA':
            print(pedra(pc))
        elif opcoes[usuario] == 'PAPEL':
            print(papel(pc))
        else:
            print(tesoura(pc))
    print()

def para_ou_repete():
    return input('Jogar de novo? [Tecle 9 para sair] ')

def main():
    while True:
        menu()
        Usuario = valida_valor(usuario_escolhe())
        Pc = pc_escolhe()
        placar(Usuario, Pc)
        mensagem_final(Usuario, Pc)
        Loop = para_ou_repete() 
        if Loop == '9':
            break
        print()
    
if __name__ == '__main__':
    main()
