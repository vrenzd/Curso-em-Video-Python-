from utilidadesCeV import moeda, dado

def main():
    preco = dado.leiaDinheiro("Digite o preço: R$ ")
    aumento = dado.leiaInt("Taxa de aumento (%): ")
    reducao = dado.leiaInt("Taxa de redução (%): ")

    # Relatório completo
    moeda.resumo(preco, aumento, reducao)

    print()
    print('Exemplos isolados:')
    print('==================')
    print(f'Aumentando {aumento}%: {moeda.aumentar(preco, aumento, True)}')
    print(f'Diminuindo {reducao}%: {moeda.diminuir(preco, reducao, True)}')
    print(f'Dobro (numérico): {moeda.dobro(preco)}')
    print(f'Metade (formatado): {moeda.metade(preco, True)}')

main()