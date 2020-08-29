# Caixa registradora: calcula o valor total da compra com base no código do produto e na quantidade.
# Este código combina estruturas condicionais e de repetição.

tot = 0

while True:
    cod = int(input('Código do produto: '))
    if cod != 1 and cod != 2 and cod != 3 and cod != 5 and cod != 9: # Validação do código digitado
        while True: # Repete a frase abaixo até que o usuário digite um código de produto previamente cadastrado
            cod = int(input('CÓDIGO INVÁLIDO! Digite novamente: '))
            if cod == 1 or cod == 2 or cod == 3 or cod == 5 or cod == 9: #Códigos previamente cadastrados
                break 

    qtd = int(input('Quantidade: '))   
    if cod == 1:
        prod = qtd * 0.5
    if cod == 2:
        prod = qtd * 1
    if cod == 3:
        prod = qtd * 4
    if cod == 5:
        prod = qtd * 7
    if cod == 9:
        prod = qtd * 8
    tot = tot + prod

    resp = input('Continuar? [S/N] ') # Tecle 'S' ou 's' para continuar comprando.
    if resp == 'N' or resp == 'n': # Para de perguntar ao usuário e mostra o valor total da compra.
        break

print()
print(f'Valor total da compra = R${tot:.2f}')
