'''Autora: Helena Maruf'''
'''Data: 12/03/2021'''
'''Nome do arquivo: advinhe_o_numero.py'''
'''Descrição: este código é uma implementação em modo texto de um jogo muito usado para exercitar lógica de programação.'''
'''Funcionamento:
    --> O código automaticamente sorteia um número de 0 a 9, que não é revelado.
    --> O usuário (você) tenta advinhar o número sorteado digitando um número de 0 a 9.
    --> O código só para de lhe pedir um número quando você acertar o número sorteado.
        --> Cada número digitado (certo ou errado) conta como uma tentativa.
        --> Se você digitar qualquer número fora do intervalo de 0 a 9 e/ou letras, o código dará erro e entrará em loop até você digitar um valor de 0 a 9.
    --> Ao acertar o número sorteado, a vez passa para o computador, que também irá escolher um número de 0 a 9 até acertar o número sorteado, quantas tentativas forem necessárias.
    --> Ganha o jogador que acertar o número sorteado com a MENOR quantidade de tentativas.
        --> Se usuário e computador acertarem na mesma quantidade de tentativas, o resultado será EMPATE.
    --> Exemplo de rodada:
        1. Código sorteia número 9.
        2. Vez do Usuário - Usuário digita 1 (tentativa 1)...
        3. Usuário digita 3 (tentativa 2)...
        4. Usuário digita 9 (tentativa 3). Logo, usuário acertou com 3 tentativas.
        5. Vez do Computador - Total de tentativas: 1 (acertou de primeira).
        6. Vencedor - Computador!'''
    
from random import randint

def numero_sorteado():
    return randint(0, 9)

#Exibe um cabeçalho com o jogador da vez: usuário ou computador.
def jogador_da_vez(jogador, caractere = '*', qtd = 50):
    print(caractere * qtd)
    print(f'               JOGADOR - {jogador}')
    print(caractere * qtd)
    print()

#Verifica se o valor digitado pelo usuário é um número no intervalo de 0 a 9.
def usuario_escolhe(tentativa, caractere = 'X', qtd = 36):
    usuario = input(f'Tentativa {tentativa} - Advinhe um número de 0 a 9: ')
    while True:
        if usuario.isdigit() and int(usuario) >= 0 and int(usuario) < 10:
            break
        else:
            print(caractere * qtd)
            usuario = input('ERRO - Digite um número de 0 a 9: ')
            print(caractere * qtd)
    return int(usuario)

#Cada tentativa do pc não aparece na tela como acontece no usuário.
#Mas se você achar que o pc está roubando, adicione a linha print(lista) para ver os valores gerados pelo pc.
def pc_escolhe(lista):
    while True:
        pc = randint(0, 9) #É assim que o pc gera valores aleatórios até acertar o sorteado.
        if pc not in lista: #A lista contém os valores que já foram gerados pelo pc. Isso evita do pc gerar valores repetidos e tentativas desnecessárias, deixando o jogo mais acirrado.
            lista.append(pc)
            break
    return pc

#Exibe total de tentativas de cada jogador após acertar o número sorteado.
def mensagem(jogador, sorteado, tentativa):
    print(f'--> {jogador} acertou o número {sorteado} na tentativa {tentativa}')
        
def placar(tent_usu, tent_pc, caractere = '-', qtd = 35):
    print()
    print()
    print(caractere * qtd)
    print('              PLACAR')
    print(caractere * qtd)
    print(f'USUÁRIO   {tent_usu}    X    {tent_pc}   COMPUTADOR')
    print(caractere * qtd)

def resultado(tent_usu, tent_pc):
    print()
    print()
    if tent_usu == tent_pc:
        print('        Resultado = EMPATE!')
    else:
        print('        VENCEDOR = ', end = '')
        if tent_usu < tent_pc:
            print('USUÁRIO!')
        else:
            print('COMPUTADOR!')    
        
def main():
    Sorteado = numero_sorteado()

    jogador_da_vez('USUÁRIO')
    Tentativa_usuario = 1
    while True:
        Usuario = usuario_escolhe(Tentativa_usuario)
        if Usuario == Sorteado:
            print()
            mensagem('USUÁRIO', Sorteado, Tentativa_usuario)
            break
        else:
            Tentativa_usuario += 1
    print()

    jogador_da_vez('COMPUTADOR')
    Tentativa_pc = 1
    Ja_escolhidos_pc = []
    while True:
        Pc = pc_escolhe(Ja_escolhidos_pc)
        if Pc == Sorteado:
            mensagem('COMPUTADOR', Sorteado, Tentativa_pc)
            break
        else:
            Tentativa_pc += 1

    placar(Tentativa_usuario, Tentativa_pc)
    resultado(Tentativa_usuario, Tentativa_pc)
    
if __name__ == '__main__':
    main()
