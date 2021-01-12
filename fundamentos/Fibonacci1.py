# Fibonacci1

tot = int(input('Total de números na sequência: '))
print()

ant = 0
print(ant, end = '   ')
atu = 1
print(atu, end = '   ')

c = 3 # Porque a sequência já tem dois números, 0 e 1.
while c <= tot:
    pro = ant + atu
    print(pro, end = '   ')
    ant = atu
    atu = pro
    c = c + 1
