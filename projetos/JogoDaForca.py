# Jogo Da Forca: defina a palavra a ser advinhada na variável 'plv' e brinque com seus amigos!

plv = 'bola' # Defina a palavra aqui. Use apenas letras minúsculas e evite acentos.
letras = list(plv)

exib = list(range(len(letras))) # Gera um painel para mostrar letras e lacunas ao longo do jogo.
i = 0
while i < len(exib):
    exib[i] = '---' # A letra fica escondida por esse tracejado até a pessoa dizê-la. 
    i = i + 1

def fun_exib():
    print('        ', exib)    

tent = int(input('Jogar com quantas tentativas? ')) # Seja razoável e leve em consideração o tamanho da palavra...
print()

t = 1 # Contador de tentativas.
i = 0
sinal = '' # Verifica se tem a letra na palavra.
certas = [] # Referência para ver se a palavra foi completada ou não.
erradas = [] # Letras ditas que não constam na palavra.
while t <= tent:
    fun_exib()
    while True:
        l = input(f'{t}a. Tentativa - Digite uma letra: ')
        if l not in certas and l not in erradas:
            break
        else:
            print(f'Letra {l} já foi dita!') # Mecanismo de verificação para os desatentos que não prestarem atenção nas letras já ditas, evitando a perda de tentativas!
            print()
    print()
    for e in letras:
        if e == l:
            sinal = 'tem' # Letra dita consta na palavra.
            exib[i] = l # O tracejado revela a letra.
            certas.append(l)
        i = i + 1
    if sinal == '': # Letra dita não consta na palavra.
        erradas.append(l)
    i = 0 # Reinicia índice para a letra seguinte.
    sinal = '' # Reinicia sinal para a letra seguinte.
    if len(certas) == len(letras): # Indica que a palavra foi completada antes do máximo de tentativas.
        fun_exib()
        print('#' * 15, 'PARABÉNS! Você se livrou da forca :D', '#' * 15)
        break # Termina o laço de repetição e mostra a palavra completa.
    print(f'        Letras erradas = {erradas}')
    t = t + 1

if len(certas) != len(letras): # As tentativas acabaram e a pessoa não conseguiu advinhar todas as letras.
    fun_exib()
    print('#' * 15, 'FORCA! Você perdeu :´(', '#' * 15)

print()
print(f'        Palavra correta: {plv}')
