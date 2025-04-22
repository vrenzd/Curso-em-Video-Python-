frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
    