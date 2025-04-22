from datetime import date

dados = {}
dados['nome'] = input('Nome: ')

nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc

dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))

    contrib = date.today().year - dados['contrato']
    aposentar = 35 - contrib
    dados['aposentadoria'] = date.today().year + aposentar

    if aposentar <= 0:
        dados['aposentadoria'] = date.today().year

print('\nDados do trabalhador:')
print()
for chave, valor in dados.items():
    print(f'{chave}: {valor}')
