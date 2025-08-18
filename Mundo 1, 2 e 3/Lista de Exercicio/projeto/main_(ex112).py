from utilidadesCeV import dado, moeda

def main():
    preco = dado.leiaDinheiro('Digite o preço: R$ ')
    moeda.resumo(preco, 20, 12)  

main()