from random import randint

numeros = []

def sorteia():
    print('Sorteando 5 números: ', end='')
    
    for _ in range(5):
        n = randint(1,10)
        numeros.append(n)
        print(f'{n} ', end='')
    print()
    
def somaPar():
    soma = sum(n for n in numeros if n % 2 == 0)
    print(f'A soma dos valores pares de {numeros} é {soma}')
    
sorteia()
somaPar()