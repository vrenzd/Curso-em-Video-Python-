def aprovar_emprestimo(casa, salario, anos):
    mensal = casa / (anos * 12)
    limite = salario * 0.3
    if mensal <= limite:
        return f'Empréstimo APROVADO! Prestação mensal: R${mensal:.2f}'
    else:
        return f'Empréstimo NEGADO! Excedeu o limite de 30% do salário'

casa = float(input('Valor da Casa: R$'))
salario = float(input('Salário: R$'))   
anos = int(input('Financiado em '))
resultado = aprovar_emprestimo(casa, salario, anos)
print(resultado)
