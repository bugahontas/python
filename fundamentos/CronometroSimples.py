# Cronômetro simples: conta de 0 até 20 minutos em contagem progressiva.
# Altere a linha 'if m == 20:' do código e insira outro valor da sua preferência.
# Este código aceita valores de 1 a 59 minutos.

from time import sleep

s = 0
m = 0
aux = 0
while s < 60:
    sleep(1)
    print('%02d' % m, ':', '%02d' % s)
    if m == 20:
        break
    s = s + 1
    if s % 60 == 0:
        m = m + 1
        s = 0
