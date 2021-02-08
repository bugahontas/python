'''Algoritmo de posição na lista com funções'''
# Cria uma lista,
# Procura o valor informado pelo usuário e
# Se o valor for encontrado, informa sua posição na lista.
# Modularização do código em funções: cada função executa uma tarefa de:
                #Criar lista;
                #Pedir que o usuário digite o valor;
                #Procurar o valor na lista;
                #Se encontrado, verificar a sua posição;
                #Mostrar mensagem final ao usuário.
                #Função main: Chamar todas as outras funções do código.
# Escrever assim é mais trabalhoso, mas isso facilita a leitura, organização e manutenção do código.

def main():
    Lista = cria_lista()
    Busca = informa_numero()
    Resultado = busca_numero(Busca, Lista)
    Posicao = None
    if Resultado != None:
        Posicao = informa_posicao(Resultado, Lista)
        mensagem(Resultado, Busca, Posicao)
    else:
        mensagem(Resultado, Busca)

def cria_lista():
    lista = []
    for n in range(5, 16): #Você pode mudar o começo e o fim do range.
        lista.append(n)
    return lista

def informa_numero():
    busca = int(input('Procurar qual valor? '))
    return busca

def busca_numero(busca, lista):
    for numero in lista:
        if numero == busca:
            return numero
    else:
        return None

def informa_posicao(resultado, lista):
    posicao = 0
    while posicao < len(lista): #Botei bloco while aqui só pra não usar bloco for o tempo todo...
        if lista[posicao] == resultado:
            return posicao + 1
        posicao = posicao + 1

def mensagem(resultado, busca, posicao = -1):
    print()
    if resultado == None:
        print(f'Número {busca} não encontrado...')
    else:
        print(f'Número {busca} encontrado na posição {posicao}!')

main()
