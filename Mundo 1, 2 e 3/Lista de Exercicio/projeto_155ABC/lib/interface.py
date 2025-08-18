from typing import List

def linha(tam: int = 42) -> str:
    return "-" * tam

def cabecalho(txt: str) -> None:
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg: str) -> int:
    while True:
        try:
            entrada = input(msg).strip()
            valor = int(entrada)
            return valor
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada interrompida pelo usuário.\033[m')
            return 0

def menu(opcoes: List[str], titulo: str = 'MENU PRINCIPAL') -> int:
    while True:
        cabecalho(titulo)
        for i, item in enumerate(opcoes, start=1):
            print(f'{i} - {item}')
        print('0 - Sair')
        print(linha())
        opc = leiaInt('Sua opção: ')
        if 0 <= opc <= len(opcoes):
            return opc
        print('\033[31mOpção inválida. Tente novamente.\033[m')