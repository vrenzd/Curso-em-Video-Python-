valores = (
    int(input('1º valor: ')),
    int(input('2º valor: ')),
    int(input('3º valor: ')),
    int(input('4º valor: '))
)

if 3 or 9 in valores:
    quantidade9 = valores.count(9) # A) Quantas vezes apareceu o valor 9
    posicao3 = valores.index(3) +1 # B) Em que posição foi digitado o primeiro valor 3
    print(f'O valor 9 apareceu {quantidade9} vezes.')
    print(f'O primeiro valor 3 foi digitado na {posicao3}ª posição.')
else:
    print('O valor 3 não foi digitado.')
    print('O valor 9 não foi digitado.')

# Quais foram os números pares
pares = tuple(valor for valor in valores if valor % 2 == 0)
print(f'Números pares digitados: {pares}')
