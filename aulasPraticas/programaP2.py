# hip = diametro
from math import*
a = float(input('Valor do primeiro cateto: '))
b = float(input('Valor do segundo cateto: '))
h = sqrt((a ** 2) + (b ** 2))
r = h / 2
area = pi * (r ** 2)
print('O valor do raio é de %.2f' %r)
print('O valor da área é de %.2f' %area)