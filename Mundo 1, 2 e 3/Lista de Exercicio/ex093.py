jogador = {}

jogador['nome'] = input('Nome do jogador: ')
num_part = int(input('Números de partidas jogadas: '))
soma_gols = []

for i in range(num_part):
    gols = int(input(f'Quantos gols na partida {i+1}? '))
    soma_gols.append(gols)

# Armazena os dados no dicionário
jogador['gols'] = soma_gols
jogador['total_gols'] = sum(soma_gols)

print('Desempenho do jogador: ')
for k, v in jogador.items():
    print(f'{k}: {v}')
