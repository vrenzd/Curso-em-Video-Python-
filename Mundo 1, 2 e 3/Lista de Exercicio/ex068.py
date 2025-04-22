from random import randint

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()
    computador = randint(0, 10) 
    total = jogador + computador
    par = total % 2 == 0
    impar = total % 2 != 0

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')

    if par:
        print('DEU PAR!')
    else:
        print('DEU ÍMPAR!')

    if (escolha == 'P' == par) or (escolha == 'I' == impar):
        print('Você VENCEU!')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break

print(f'GAME OVER! Você venceu {vitorias} vezes.')
