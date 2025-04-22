lista = []

while True:
    num = input('Digite um número (ou "S" para sair): ').upper().strip()
    if num == 'S':
        break
    lista.append(int((num)))

print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista de forma decrescente: {lista}')

if 5 in lista:
    print('O valor 5 foi encontrado e digitado na lista.')
else:
    print('O valor 5 não foi encontrado e digitado na lista.')
