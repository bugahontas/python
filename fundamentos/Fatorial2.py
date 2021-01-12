# Fatorial2

def fatorial(n):
    c = 1
    fat = 1
    while c <= n:
        fat = fat * c
        c = c + 1
    return fat

n = int(input('Fatorial do número: '))
print()
print(f'{n}! = {fatorial(n)}')
