from time import sleep

jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome do jogador: ')
    num_part = int(input(f'Número de partidas jogadas por {jogador["nome"]}: '))

    gols_partida = []

    for i in range(num_part):
        gols = int(input(f'Quantos gols na partida {i + 1}? '))
        gols_partida.append(gols)

    jogador['gols'] = gols_partida
    jogador['tot_gols'] = sum(gols_partida)

    jogadores.append(jogador)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar != 'S':
        break

print('\n=== Desempenho dos Jogadores ===')
for jogador in jogadores:
    print(f'\nNome: {jogador['nome']}')
    sleep(1)
    print(f'Total de gols: {jogador['tot_gols']}')
    sleep(1)
    print('Gols por partida:')
    for i, gols in enumerate(jogador['gols']):
        sleep(1)
        print(f'{i + 1}ª partida: {gols} gols.')

while True:
    nome_jogador = input('\nDigite o nome do jogador para ver detalhes (ou "quit" para encerrar): ')
    if nome_jogador.lower() == 'quit':
        break

    jogador_encontrado = next((jogador for jogador in jogadores if jogador['nome'].lower() == nome_jogador.lower()), None)

    if jogador_encontrado:
        sleep(1)
        print(f'\n=== Detalhes do jogador: {jogador_encontrado['nome']} ===')
        sleep(1)
        print(f'Total de gols: {jogador_encontrado['tot_gols']}')
        sleep(1)
        print('Gols por partida:')
        for i, gols in enumerate(jogador_encontrado['gols']):
            sleep(1)
            print(f'{i + 1}ª partida: {gols} gols.')
            
    else:
        print(f'Jogador {nome_jogador} não encontrado!')

print('\nPrograma encerrado.')
