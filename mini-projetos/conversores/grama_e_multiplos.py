'''Autor: Helena Maruf'''
'''Data: 03/05/2021'''
'''Nome do arquivo: grama_e_multiplos.py'''
'''Descrição: converte um valor para múltiplos e submúltiplos do grama.'''


def cria_unidades():
    unidades = {'Grama': 'g',
                'Decagrama': 'dag',
                'Hectograma': 'hg',
                'Quilolgrama': 'kg',
                'Decigrama': 'dg',
                'Centigrama': 'cg',
                'Miligrama': 'mg'}

    siglas = ['g', 'dag', 'hg', 'kg', 'dg', 'cg', 'mg']

    todos_expoentes = {'mg': -3,
                       'cg': -2,
                       'dg': -1,
                       'g': 0,
                       'dag': 1,
                       'hg': 2,
                       'kg': 3}

    return unidades, siglas, todos_expoentes


def menu(unidades, caractere = '=', total = 26):
    linha = caractere * total
    print(linha)
    print('          OPÇÕES:')
    print(linha)
    for chave, valor in unidades.items():
        print(f'{chave:^12} = Tecle [{valor}]')
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
