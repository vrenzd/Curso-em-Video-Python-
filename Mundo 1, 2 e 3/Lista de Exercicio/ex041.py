def determinar_categoria(idade):
    if idade <= 9:
        return 'MIRIM'
    elif idade <= 14:
        return 'INFANTIL'
    elif idade <= 19:
        return 'JUNIOR'
    elif idade <= 20:
        return 'SÊNIOR'
    else:
        return 'MASTER'
    
from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
resultado = determinar_categoria(idade)
print(f'Você tem {idade} anos e sua categoria é {resultado}.')
    