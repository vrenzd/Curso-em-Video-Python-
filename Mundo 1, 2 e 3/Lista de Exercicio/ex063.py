n = int(input('Quantos termos você quer mostrar? '))

a, b = 0, 1
contador = 0 

while contador < n:
    print(a, end=' -> ')
    a, b = b, a + b
    contador += 1