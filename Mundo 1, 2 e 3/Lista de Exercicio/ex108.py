import moeda

def main():
    preco = float(input('Digite o preço: R$ '))
    taxa = float(input('Digite a taxa (%): '))

    print(f'Aumentando {taxa}%: {moeda.moeda(moeda.aumentar(preco, taxa))}')
    print(f'Diminuindo {taxa}%: {moeda.moeda(moeda.diminuir(preco, taxa))}')
    print(f'Dobro: {moeda.moeda(moeda.dobro(preco))}')
    print(f'Metade: {moeda.moeda(moeda.metade(preco))}')

main()