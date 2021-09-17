from math import*
print('Calculadora da hipotenusa, perimetro e area de um triangulo retangulo')
c1 = float(input('Valor do primeiro cateto: '))
c2 = float(input('Valor do segundo cateto: '))
hip = sqrt((c1 ** 2) + (c2 ** 2))
a = (c1 * c2) / 2
p = c1 + c2 + hip
print('O triangulo tem', hip , 'de hipotenusa,', p , 'de perimetro e', a , 'de area' )