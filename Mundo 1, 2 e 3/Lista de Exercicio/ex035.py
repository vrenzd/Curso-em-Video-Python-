lado_a = float(input('Comprimento do 1º lado: '))
lado_b = float(input('Comprimento do 2º lado: '))
lado_c = float(input('Comprimento do 3º lado: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
    