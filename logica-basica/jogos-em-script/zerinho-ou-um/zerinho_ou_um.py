'''Autora: Helena Maruf'''
'''Data: 15/03/2021'''
'''Nome do arquivo: zerinho_ou_um.py'''
'''Descrição: este código é uma implementação em modo texto do jogo clássico "Zerinho ou Um."'''
'''Funcionamento:
    --> O usuário escolhe com quantos amigos quer jogar e o nome de cada amigo.
    --> O usuário deve informar 0 ou 1.
    --> Cada amigo criado também escolherá 0 ou 1 de forma aleatória.
    --> Vence quem escolher um número diferente de todos os outros participantes.
        --> Se não houver apenas uma pessoa com 0 ou uma pessoa com 1, a rodada será repetida até que alguém vença.
    --> Exemplos de rodada:
            1. Você escolhe jogar com dois amigos: Ana e Bia.
            2. Situação 1: Você escolhe "0"; Ana escolhe "0"; Bia escolhe "1".
            3. Bia foi a única que escolheu 1. Logo, a vencedora é Bia.

            1.1 Supondo que você queira jogar de novo com Ana e Bia.
            1.2 Situação 2: Você escolhe "0"; Ana escolhe "1"; Bia escolhe "1".
            1.3 Você foi o único que escolheu 0. Logo, você vence.

            2.1 Supondo que você queira jogar de novo, mas dessa vez com Ana, Bia e Daniel.
            2.2 Situação 3: Você escolhe "0"; Ana escolhe "1"; Bia escolhe "1" e Daniel escolhe "0".
            2.3 Tanto o 0 quanto o 1 foram escolhidos por mais de uma pessoa no grupo.
            2.4 Então há uma nova rodada: Você escolhe "1"; Ana escolhe "1"; Bia escolhe "1" e Daniel escolhe "0"
            2.5 Logo, Daniel vence.'''


from random import randint


def mensagem_erro():
    print('***** ERRO - VALOR INVÁLIDO! *****')
    print()


def total_amigos():
    while True:
        try:
            total = int(input('Jogar com quantos amigos? '))
        except Exception:
            mensagem_erro()
        else:
            return total


def cria_amigos(total, padrao = -1):
    nome_e_escolha = {}
    nomes = []

    print()
    for a in range(1, total + 1):
        while True:
            nome = input(f'Amigo no. {a}: Nome = ')
            nome = nome.strip()
            if len(nome) == 0:
                mensagem_erro()
            else:
                break
        nome = nome.upper()
        nomes.append(nome)
        nome_e_escolha[nome] = padrao

    nomes.append('VOCÊ')
    nome_e_escolha['VOCÊ'] = padrao
    print()

    return nome_e_escolha, nomes


def zerinho_ou_um(total, nome_e_escolha, nomes):
    sua_escolha = int(input('Digite 0 ou 1: '))
    nome_e_escolha['VOCÊ'] = sua_escolha
    print()

    for index in range(len(nomes) - 1):
        nome_e_escolha[nomes[index]] = randint(0, 1)

    return nome_e_escolha


def mostra_escolhas(nome_e_escolha, caractere = '.'):
    linha1 = caractere * 5
    linha2 = linha1 * 4
    print(linha2)
    print(f'{linha1} ESCOLHAS {linha1}')
    print(linha2)

    for chave, valor in nome_e_escolha.items():
        print(f'{chave.center(15, " ")} = {valor}')
    print()


def verifica_resultado(nome_e_escolha, sinal, padrao = -1):
    total_0 = 0
    total_1 = 0
    buscar_valor = padrao

    for chave, valor in nome_e_escolha.items():
        if valor == 0:
            total_0 += 1
        else:
            total_1 += 1

    if total_0 == 1 or total_1 == 1:
        sinal = False

        if total_0 == 1:
            buscar_valor = 0
        else:
            buscar_valor = 1

    return sinal, buscar_valor
        

def busca_vencedor(nome_e_escolha, procurado):
    for chave, valor in nome_e_escolha.items():
        if valor == procurado:
            return chave


def mensagem_final(vencedor):
    print(f'    VENCEDOR: {vencedor}!')


def main():
    Total = total_amigos()
    Nome_e_escolha, Nomes = cria_amigos(Total)

    
    Sinal = True
    while Sinal:
        Nome_e_escolha = zerinho_ou_um(Total, Nome_e_escolha, Nomes)
        mostra_escolhas(Nome_e_escolha)
        Sinal, Buscar_valor = verifica_resultado(Nome_e_escolha, Sinal)

    Vencedor = busca_vencedor(Nome_e_escolha, Buscar_valor)

    mensagem_final(Vencedor)
    

if __name__ == '__main__':
    main()
