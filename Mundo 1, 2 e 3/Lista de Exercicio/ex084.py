pessoas = []

# Loop infinito para entrada de dados
while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    pessoas.append([nome, peso])
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

# Determinando os mais pesados e mais leves
maior_peso = pessoas[0][1]
menor_peso = pessoas[0][1]

for pessoa in pessoas:
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    if pessoa[1] < menor_peso:
        menor_peso = pessoa[1]

mais_pesados = []
mais_leves = []

for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        mais_pesados.append(pessoa)
    if pessoa[1] == menor_peso:
        mais_leves.append(pessoa)

# Saída de dados
print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')

print(f'\nPessoas mais pesadas (peso: {maior_peso} kg):')
for pessoa in mais_pesados:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]} kg')

print(f'\nPessoas mais leves (peso: {menor_peso} kg):')
for pessoa in mais_leves:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]} kg')
