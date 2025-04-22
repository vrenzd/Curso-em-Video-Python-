from tabulate import tabulate

produtos = (('tenis', 199),
            ('computador', 4999),
            ('TV', 7999),
            ('geladeira', 5500),
            ('Fogão', 3200))

tabela = tabulate(produtos, headers=["Produto", 'Preço R$'], tablefmt="psql")
print(tabela)
