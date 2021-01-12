# Fatorial3: com função recursiva.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input('Fatorial do número: '))
print()
print(f'{n}! = {fatorial(n)}')
