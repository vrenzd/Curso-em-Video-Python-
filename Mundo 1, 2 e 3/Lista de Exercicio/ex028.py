from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um número de 0 a 5. Adivinhe!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print('PARABÉNS! Você venceu!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')
    