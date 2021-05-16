'''Autor: Helena Maruf'''
'''Data: 03/05/2021'''
'''Nome do arquivo: metro_cubico_e_multiplos.py'''
'''Descrição: converte um valor para múltiplos e submúltiplos do metro cúbico.'''


def cria_unidades():
    unidades = {'Metro cúbico': 'm3',
                'Decâmetro cúbico': 'dam3',
                'Hectomêtro cúbico': 'hm3',
                'Quilômetro cúbico': 'km3',
                'Decímetro cúbico': 'dm3',
                'Centímetro cúbico': 'cm3',
                'Milímetro cúbico': 'mm3'}

    siglas = ['mm3', 'cm3', 'dm3', 'm3', 'dam3', 'hm3', 'km3']

    todos_expoentes = {'mm3': -9,
                       'cm3': -6,
                       'dm3': -3,
                       'm3': 0,
                       'dam3': 3,
                       'hm3': 6,
                       'km3': 9}

    return unidades, siglas, todos_expoentes


def menu(unidades, caractere = '=', total = 35):
    linha = caractere * total
    print(linha)
    print('              OPÇÕES:')
    print(linha)
    for chave, valor in unidades.items():
        print(f'{chave:^20} = Tecle [{valor}]')
    print(linha)
    print()
    

def mensagem_erro():
    return '****** ERRO - DADO INVÁLIDO!'


def valor_a_converter():
    while True:
        try:
            numero = float(input('Converter qual valor? '))
        except Exception:
            print(mensagem_erro())
            print()
        else:
            print()
            return numero


def unidade_original(siglas):
    while True:
        original = input('Unidade atual = ')
        original = original.lower()
    
        if original not in siglas:
            print(mensagem_erro())
            print()
        else:
            print()
            return original
            

def unidade_alvo(siglas):
    while True:
        alvo = input('Converter para = ')
        alvo = alvo.lower()
    
        if alvo not in siglas:
            print(mensagem_erro())
            print()
        else:
            print()
            return alvo


def conversao(todos_expoentes, numero, original, alvo):
    for chave, valor in todos_expoentes.items():
        if original == chave:
            expoente_1 = todos_expoentes[chave]
        if alvo == chave:
            expoente_2 = todos_expoentes[chave]

    expoente = expoente_1 - expoente_2
    
    return expoente


def mostra_resultado(numero, original, expoente, alvo):
    print(f'--> RESULTADO: {numero}{original} = {numero} x 10^{expoente}{alvo}')


def main():
    Unidades, Siglas, Todos_expoentes = cria_unidades()

    menu(Unidades)

    Valor = valor_a_converter()

    Original = unidade_original(Siglas)

    Alvo = unidade_alvo(Siglas)

    Expoente = conversao(Todos_expoentes, Valor, Original, Alvo)

    mostra_resultado(Valor, Original, Expoente, Alvo)
    

if __name__ == '__main__':
    main()
