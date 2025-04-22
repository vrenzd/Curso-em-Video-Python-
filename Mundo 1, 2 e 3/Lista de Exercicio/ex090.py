aluno = {}

aluno['nome'] = input('Nome do Aluno: ')
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))

situacao = 'Aprovado' if aluno['media'] >= 7 else 'Reprovado'
aluno['situacao'] = situacao

print('\nDados do Aluno:')
print()
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
    