numeros = [[], []]

for i in range(7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f'Valores pares em ordem crescente: {numeros[0]}')
print(f'Valores ímpares em ordem crescente: {numeros[1]}')
