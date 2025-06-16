def titulo(mensagem, cor=0):
    cores = [
        '\033[m',        # 0 - sem cor
        '\033[0;30;41m', # 1 - vermelho
        '\033[0;30;42m', # 2 - verde
        '\033[0;30;43m', # 3 - amarelo
        '\033[0;30;44m', # 4 - azul
        '\033[0;30;45m', # 5 - roxo
    ]
    tam = len(mensagem) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {mensagem}')
    print('~' * tam)
    print('\033[m', end='')

def ajuda(comando):
    titulo(f"Acessando o manual do comando '{comando}'", 4)
    print('\033[7m', end='')  # fundo branco, texto preto
    help(comando)
    print('\033[m', end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca > ').strip()
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)