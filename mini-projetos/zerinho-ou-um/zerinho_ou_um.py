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
        print(f'{chave} = {valor}')
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
