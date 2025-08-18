from modulo_moeda import aumentar, diminuir, dobro, metade

def main() -> None:
    preco = float(input('Digite o preço: R$ '))
    taxa = float(input('Digite a taxa (%): '))
    
    print(f"Aumentando {taxa:.2f}%: R$ {aumentar(preco, taxa):.2f}")
    print(f"Diminuindo {taxa:.2f}%: R$ {diminuir(preco, taxa):.2f}")
    print(f"Dobro: R$ {dobro(preco):.2f}")
    print(f"Metade: R$ {metade(preco):.2f}")

main()