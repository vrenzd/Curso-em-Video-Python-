from random import choice
from time import sleep

def jokenpo():
    opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
    usuario = int(input('Escollha:\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n> '))
    computador = choice(opcoes)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!')
    print(f'Computador: {computador}')

    if (usuario == 1 and computador == 'PEDRA') or \
       (usuario == 2 and computador == 'PAPEL') or \
       (usuario == 3 and computador == 'TESOURA'):
        return 'EMPATE!'
    elif (usuario == 1 and computador == 'TESOURA') or \
         (usuario == 2 and computador == 'PEDRA') or \
         (usuario == 3 and computador == 'PAPEL'):
        return 'VOCÊ GANHOU!'
    else:
        return 'COMPUTADOR GANHOU!'
print(jokenpo())
