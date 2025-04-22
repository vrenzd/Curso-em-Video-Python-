p_termo = float(input('1º termo da PA: '))
razao = float(input('Razão da PA: '))

termo = p_termo
contador = 1
mais_termos = 10

while mais_termos != 0:
    total = contador + mais_termos
    while contador < total:
        print(f'Termo {contador}º: {termo}')
        termo += razao
        contador += 1
    mais_termos = int(input('Quer mostar mais quantos termos? [0] - encerrar\n> '))
    
print('Programa encerrado!')



