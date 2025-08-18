import moeda

def main():
    preco = float(input('Digite o preço: R$ '))
    taxa = float(input('Digite a taxa (%): '))

    print(f'Aumentando {taxa}%: {moeda.aumentar(preco, taxa, True)}')
    print(f'Diminuindo {taxa}%: {moeda.diminuir(preco, taxa, True)}')
    print(f'Dobro: {moeda.dobro(preco, True)}')
    print(f'Metade: {moeda.metade(preco, True)}')

main()