# Cronômetro simples: conta de 0 até 1 hora em contagem progressiva.
# Altere a linha 'if h == 1:' do código e insira outro valor da sua preferência.

from time import sleep

s = 0
m = 0
h = 0
aux = 0
while s < 60:
    sleep(0.01)
    print('%02d' % h, ':', '%02d' % m, ':', '%02d' % s)
    if h == 1:
        break
    s = s + 1
    if s == 60:
        m = m + 1
        s = 0
    if m  == 60:
        h = h + 1
        m = 0
