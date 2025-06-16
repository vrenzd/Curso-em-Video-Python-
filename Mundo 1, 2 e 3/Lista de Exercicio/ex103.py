def ficha(jogador='<desconhecido>', gols=0):
    '''
    Exibe a ficha de um jogador com o nome e número de gols.
    
    Parâmetros:
    jogador (str): Nome do jogador. Padrão '<desconhecido>'
    gols (int): Número de gols. Padrão: 0
    
    Retorna:
    str: Texto formatado com os dados do jogador.
    '''
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato'

# Coletando dados com tratamento    
nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ').strip()

# Convertendo 'gols' para inteiro, se possível
gols = int(gols) if gols.isnumeric() else 0

# Chamando a função com base nas entradas
if nome == '':
    print(ficha(gols=gols))
else:
    print(ficha(nome, gols))
    