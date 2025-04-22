dia = int(input('Informe os dias alugados: '))
km = float(input('Quantos km rodados? '))
pagar = (dia * 60) + (km + 0.15)
print(f'O total a pagar é de R${pagar:.2f}')
