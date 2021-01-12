# Fibonacci3

def fibo(a, b):
    cont = 3
    seq = []
    seq.append(a)
    seq.append(b)
    while cont < 10:
        c = a + b
        seq.append(c)
        a = b
        b = c
        cont = cont + 1
    return seq

ant = 0
atu = 1
print(fibo(ant, atu))
