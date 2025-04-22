pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F] ').strip().upper()
    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar != 'S':
        break

# A) Número de pessoas cadastradas
tot_pessoas = len(pessoas)

# B) Média de idade
soma_idade = sum(pessoa['idade'] for pessoa in pessoas)
media_idade = soma_idade / tot_pessoas

# C) Quantidade de mulheres
mulheres = [pessoa for pessoa in pessoas if pessoa['sexo'] == 'F']

# D) Lista com todas as pessoas com idade acima da média
acima_media = [pessoa for pessoa in pessoas if pessoa['idade'] > media_idade]

# Exibe os resultados
print(f'\nTotal de pessoas cadastradas: {tot_pessoas}')
print(f'Média de idade: {media_idade:.2f} anos')

print('Lista de todas as mulheres:')
for mulher in mulheres:
    print(f'{mulher['nome']}, {mulher['idade']} anos')

print('Pessoas com idade acima da média:')
for pessoa in acima_media:
    print(f'{pessoa['nome']}, {pessoa['idade']} anos')
