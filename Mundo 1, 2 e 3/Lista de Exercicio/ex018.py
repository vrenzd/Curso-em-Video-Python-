from math import radians, asin, acos, atan
a = float(input('Informe o ângulo: '))
ar = radians(a)
print(f'O valor de seno {asin(ar):.3f}, cosseno {acos(ar):.3f} e a tangente é {atan(ar):.3f}')
