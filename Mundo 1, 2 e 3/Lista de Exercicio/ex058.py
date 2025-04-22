from random import randint
from time import sleep

computador = randint(0, 10)
print('-=-' * 20)
print('Estou pensando em um número de 0 a 10. Adivinhe!')
print('-=-' * 20)

acertou = False
tentativas = 0

while True:
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    tentativas += 1
    if jogador == computador:
        acertou = True
        print(f'PARABÉNS! Você venceu com {tentativas} tentativas!')
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')      
