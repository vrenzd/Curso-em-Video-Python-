from lib.interface import menu, cabecalho

def listar():
    cabecalho('LISTAGEM')
    return '-> Aqui vai a lógica de listagem...'

def cadastrar():
    cabecalho('CADASTRO')
    nome = input('Nome: ').strip()
    return f'-> Cadastrado: {nome}'

def sobre():
    cabecalho('SOBRE')
    return 'Sistema de exemplo com menu modular.'


ACTIONS = {
    1: listar,
    2: cadastrar,
    3: sobre,
}

def main():
    opcoes = ['Listar itens', 'Cadastrar item', 'Sobre']
    while True:
        escolha = menu(opcoes)
        if escolha == 0:
            cabecalho('Saindo... Até logo!')
            break
        action = ACTIONS.get(escolha)
        if action:
            action()
        else:
            print('\033[31mAção não disponível.\033[m')


main()