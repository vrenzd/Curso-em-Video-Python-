def aumentar(valor:float, taxa:float, formato:bool=False):
    res = valor * (1+ taxa / 100)
    return res if not formato else moeda(res)

def diminuir(valor:float, taxa:float, formato:bool=False):
    res = valor * (1 - taxa / 100)
    return res if not formato else moeda(res)

def dobro(valor:float, formato:bool=False):
    res = valor * 2
    return res if not formato else moeda(res)

def metade(valor:float, formato:bool=False):
    res = valor / 2
    return res if not formato else moeda(res)

def moeda(valor:float, simbolo:str='R$') -> str:
    return f'{simbolo} {valor:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')

def resumo(valor:float, taxa_aumento:float, taxa_reducao:float):
    print("-" * 40)
    print('RESUMO DO VALOR'.center(40))
    print("-" * 40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Aumentando {taxa_aumento}%: \t{aumentar(valor, taxa_aumento, True)}')
    print(f'Reduzindo {taxa_reducao}%: \t{diminuir(valor, taxa_reducao, True)}')
    print("-" * 40)
