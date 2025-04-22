soma = 0
quantidade = 0 
maior = None
menor = None

while True:
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
    
    continuar = input('Quer continuar? [S/N] -> ').upper().strip()
    if continuar != 'S':
        break

media = soma / quantidade
print(f'A média entre todos os valores: {media}')
print(f'O maior valor é {maior} e o menor é {menor}')
