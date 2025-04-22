p_termo = float(input('1º termo da PA: '))
razao = float(input('Razão da PA: '))
print('Os 10 primeiros da PA são:')

for i in range(10):
    termo = p_termo + i * razao
    print(f'Termo {i+1}º: {termo}')
    