matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]'))

print('\nMatriz:')
for linha in matriz:
    for elemento in linha:
        print(f'{elemento:^5}', end=' ')
    print()

#A) A soma de todos os valores pares digitados.
par = 0
for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            par += elemento

#B) A soma dos valores da terceira coluna.
terceira_coluna = 0
for i in range(3):
    terceira_coluna += matriz[i][2]

#C) O maior valor da segunda linha.
maior_valor_segunda_linha = max(matriz[1])

#Imprimindo os resultados.
print(f'\nA soma dos valores pares da matriz é: {par}')
print(f'A soma dos valores da 3ª coluna é: {terceira_coluna}')
print(f'O maior valor da 2ª linha é: {maior_valor_segunda_linha}')
