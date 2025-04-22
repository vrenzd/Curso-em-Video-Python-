nome = str(input('Informe um nome: '))
salário = float(input('Informe o salário: R$'))
aumento = salário * 0.15
novo_salário = salário + aumento
print(f'O salário de {nome} com 15% de aumento é {novo_salário:.2f}')
