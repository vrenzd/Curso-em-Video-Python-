from time import sleep

def analisar_triangulo(a,b,c):
    if a == b == c:
        return 'Equilátero'
    elif a == b or a == c or b == c:
        return 'Isósceles'
    else:
        return 'Escaleno'
    
a = float(input('1º lado: '))
b = float(input('2º lado: '))
c = float(input('3º lado: '))

print('-=-' * 10)
print('Analisando o triângulo')
print('-=-' * 10)
sleep(1.5)

resultado = analisar_triangulo(a, b, c)
print(f'O triangulo é {resultado}.')
