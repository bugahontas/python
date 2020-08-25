# Calcula o valor da conta de luz com base no kWh e no tipo de estabelecimento.
# Este código é um exemplo de uso de blocos condicionais aninhados.

def traco():
    print('-' * 40)

kwh = float(input('Consumo total (kWh): '))
print()

traco()
print('  TIPO DE ESTABELECIMENTO')
traco()
print('        Residência: Tecle [R]      ')
print('         Comércio: Tecle [C]       ')
print('         Indústria: Tecle [I]      ')
traco()
print()
tipo = input('Tecla: ')
print()

if tipo == 'R' or tipo == 'r':
    if kwh <= 500:
        pre = kwh * 0.4
    else:
        pre = kwh  * 0.65
elif tipo == 'C' or tipo == 'c':
     if kwh <= 1000:
        pre = kwh * 0.55
     else:
        pre = kwh  * 0.6
elif tipo == 'I' or tipo == 'i':
     if kwh <= 5000:
        pre = kwh * 0.55
     else:
        pre = kwh  * 0.6

print(f'Total a pagar: R${pre:.2f}')
