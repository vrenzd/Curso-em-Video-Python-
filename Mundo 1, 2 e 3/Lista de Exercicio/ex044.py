def calcular_valor(p_normal, f_pagamento, parcelas=1):
    if f_pagamento == 1 or f_pagamento == 2:
        desconto = 0.10
    elif f_pagamento == 3:
        desconto = 0.05
    else:
        desconto = 0

    if parcelas >= 3:
        juros = 0.20
    else:
        juros = 0
    resultado = p_normal * (1 - desconto + juros)
    return resultado

p_normal = float(input('Preço normal do Produto: R$'))
f_pagamento = int(input('[1] - Dinheiro\n[2] - Cheque\n[3] - Cartão\n> '))
parcelas = int(input('Nº de parcelas: '))
resultado = calcular_valor(p_normal, f_pagamento, parcelas)
print(f'O valor será de R$ {resultado:.2f}.')    
