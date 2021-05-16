'''Autor: Helena Maruf'''
'''Data: 03/05/2021'''
'''Nome do arquivo: metro_quadrado_e_multiplos.py'''
'''Descrição: converte um valor para múltiplos e submúltiplos do metro quadrado.'''


def cria_unidades():
    unidades = {'Metro quadrado': 'm2',
                'Decâmetro quadrado': 'dam2',
                'Hectomêtro quadrado': 'hm2',
                'Quilômetro quadrado': 'km2',
                'Decímetro quadrado': 'dm2',
                'Centímetro quadrado': 'cm2',
                'Milímetro quadrado': 'mm2'}

    siglas = ['mm2', 'cm2', 'dm2', 'm2', 'dam2', 'hm2', 'km2']

    todos_expoentes = {'mm2': -6,
                       'cm2': -4,
                       'dm2': -2,
                       'm2': 0,
                       'dam2': 2,
                       'hm2': 4,
                       'km2': 6}

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
