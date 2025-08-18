# main.py
import moeda

def main():
    preco = float(input('Digite o preço: R$ '))
    aumento = float(input('Digite a taxa de aumento (%): '))
    reducao = float(input('Digite a taxa de redução (%): '))

    moeda.resumo(preco, aumento, reducao)

main()