mais1000 = 0
total = 0
nome_barato = ''
preco_barato = float('inf')

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))
    total += preco

    if preco > 1000:
        mais1000 += 1
    if preco < preco_barato:
        preco_barato = preco
        nome_barato = nome
    
    resposta = input('Deseja continuar (S/N)? ').upper().strip()
    if resposta != 'S':
        break

print(f'Total gasto: R${total:.2f}')
print(f'Total de produtos com preço acima de R$ 1000: {mais1000}')
print(f'Nome do produto mais barato: {nome_barato}')
