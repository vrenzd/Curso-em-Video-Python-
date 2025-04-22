from time import sleep

def contador(*num):
    for i in range(1, 11, 1):
        print(i, end=' ', flush=True)
        sleep(0.5)

    print('FIM!')
    print('-=' * 15)
    print()

    for i in range(10, -1, -2):
        print(i, end=' ', flush=True)
        sleep(0.5)

    print('FIM!')
    print('-=' * 15)
    print()

    print('=' * 23)
    print('CONTAGEM PERSONALIZADA')
    print('=' * 23)

    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        passo = 1
    elif inicio > fim:
        passo *= -1
        fim -= 1

    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)

    print('FIM!')

contador()
