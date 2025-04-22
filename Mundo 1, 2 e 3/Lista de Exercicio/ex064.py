soma = 0
quantidade = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    quantidade += 1

print(f'Quantidade de número digitados: {quantidade}')
print(f'Soma dos números digitados: {soma}')
