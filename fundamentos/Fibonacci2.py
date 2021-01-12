# Fibonacci2: mostra o valor da posição informada pelo usuário.

# Com função recursiva.

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

pos = int(input('Informe uma posição: '))
print()

print(f'Valor na posição {pos} = {fibo(pos - 1)}')
