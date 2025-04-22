lista = []
par = []
impar = []

while True:
    num = input('Digite um número (ou "S" para sair): ').strip().upper()
    if num == 'S':
        break

    try:
        num = int(num)
        lista.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    except ValueError:
        print('Valor inválido. Digite um número inteiro.')

print(f'Números da lista: {lista}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
