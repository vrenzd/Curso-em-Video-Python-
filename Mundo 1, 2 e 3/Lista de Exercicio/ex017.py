from math import hypot

co = float(input('Comprimento cateto oposto: '))
ca = float(input('Cateto adjacente de um triângulo retângulo: '))
print(f'O comprimento da hipotenusa é {hypot(co, ca):.3f}')
