# Exibe o resultado da soma de valores diferentes de 0.
# Mostra estrutura de repetição while combinada com a constante 'True' e comando 'break'.

soma = 0
while True:
    v = int(input('Digite 0 pra sair ou outro valor pra somar: '))
    if v == 0:
        break
    soma = soma + v

print(f'Resultado da soma = {soma}')
