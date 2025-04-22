numeros = []

while True:
    try:
        valor = int(input('Digite um número (ou "s" para sair): '))
        if valor not in numeros:
            numeros.append(valor)
            print(f'Número {valor} adicionado.')
        else:
            print(f'Número {valor} duplicado. Ignorado.')
    except ValueError:
        print('Finalizando a entrada de valores.')
        break

numeros.sort()
print(f'Valores únicos digitados em ordem crescente:')
for numero in numeros:
    print(numero, end=', ')
    