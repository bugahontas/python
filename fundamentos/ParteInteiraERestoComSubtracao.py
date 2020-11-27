# Parte Inteira E Resto Com Subtração: junção de "ParteInteiraComSubtração" e "RestoComSubtração" em um código só.

# O programa aceita apenas valores inteiros.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print()

aux = n1 - n2 #Variável auxiliar.
q = 1 #O contador é o quociente.
while aux != 0:
    aux = aux - n2
    if aux >= 0:
        q = q + 1 
    else:
        break #Interrompe o laço de repetição.
r = n1 - q * n2 #Fórmula para o cálculo do resto.

print(f'Quociente = {q}')
print(f'Resto = {r}')
