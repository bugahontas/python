'''Autor: Helena Maruf'''
'''Data: 30/04/2021'''
'''Nome do arquivo: metro_e_multiplos.py'''
'''Descrição: este código converte um valor em uma unidade para múltiplos e submúltiplos do metro.'''
'''Funcionamento:
    --> Informe um valor.
    --> Informe a unidade de medida desse valor.
    --> Informe a unidade de medida para a qual deseja converter o valor.
    --> O resultado irá conter o valor com a unidade convertidos em potência de 10.
    --> Exemplo de uso:
        1. Você deseja converter 1 metro para centímetros.
        2. Você informa o valor 1.
        3. Em seguida, você informa a unidade atual que é metro.
        4. Você também informa a unidade para a qual deseja converter (no caso, centímetro).
        5. O código retorna como resultado "1m = 1 x 10^2cm" (lê-se "1 metro vale 1 vezes 10 elevado a 2 centímetros").'''


# Para criar conversores com outras unidades, basta alterar unidades, siglas e expoentes
    # apenas nesta função! 
# Facilita a reutilização deste código.
def cria_unidades():
    unidades = {'Metro': 'm',
                'Decâmetro': 'dam',
                'Hectomêtro': 'hm',
                'Quilômetro': 'km',
                'Decímetro': 'dm',
                'Centímetro': 'cm',
                'Milímetro': 'mm',
                'Micrômetro': 'mic',
                'Nanômetro': 'nm',
                'Picômetro': 'pm'}

    siglas = ['pm', 'nm', 'mic', 'mm', 'cm', 'dm', 'm', 'dam', 'hm', 'km']

    todos_expoentes = {'pm': -12,
                       'nm': -9,
                       'mic': -6,
                       'mm': -3,
                       'cm': -2,
                       'dm': -1,
                       'm': 0,
                       'dam': 1,
                       'hm': 2,
                       'km': 3}

    return unidades, siglas, todos_expoentes


def menu(unidades, caractere = '=', total = 27):
    linha = caractere * total
    print(linha)
    print('          OPÇÕES:')
    print(linha)
    for chave, valor in unidades.items():
        print(f'{chave:^13} = Tecle [{valor}]')
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
