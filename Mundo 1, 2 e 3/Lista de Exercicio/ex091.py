from random import randint
from time import sleep

jogadores = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}

ordem = dict(sorted(jogadores.items(), key=lambda x: x[1], reverse=True))

print('Resultado dos Jogadores')
print('-=-' * 8)
for jogador, resultado in enumerate(jogadores.items(), 1):
    print(f'{jogador}: {resultado}')
    sleep(1)
