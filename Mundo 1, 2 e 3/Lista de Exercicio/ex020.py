from random import shuffle

nome1 = input('1º nome: ')
nome2 = input('2º nome: ')
nome3 = input('3º nome: ')
nome4 = input('4º nome: ')

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print(f'Ordem de apresentação: {lista}')
