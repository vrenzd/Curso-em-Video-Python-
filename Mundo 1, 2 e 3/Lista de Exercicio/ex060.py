n = int(input('Digite um número: '))

fatorial = 1
contador = 1

while contador <= n:
    fatorial *= contador
    contador += 1
print(f'O fatorial de {n} é {fatorial}')
