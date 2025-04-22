p_termo = int(input('1º termo da PA: '))
razao = int(input('Razão da PA: '))

termo = p_termo
contador = 1

while contador <= 10:
    print(f'Termo {contador}º: {termo}')
    termo += razao
    contador += 1
    