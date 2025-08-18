def leiaDinheiro(msg:str) -> float:
    while True:
        entrada = input(msg).strip()
        
        limpo = (
            entrada.replace('R$', '')
            .replace('U$', '')
            .replace('€', '')
            .replace(' ', '')
            .replace(',', '.')
        )
        
        try:
            valor = float(limpo)
            return valor
        except ValueError:
            print(f"\033[31mERRO: '{entrada}' é um preço inválido.\033[m")


def leiaInt(msg: str) -> int:
    while True:
        try:
            entrada = input(msg).strip()
            valor = int(entrada)
            return valor
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0


def leiaFloat(msg: str) -> float:
    while True:
        try:
            entrada = input(msg).strip().replace(',', '.')
            valor = float(entrada)
            return valor
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0