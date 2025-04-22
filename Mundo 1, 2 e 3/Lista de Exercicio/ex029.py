velocidade = float(input('Velocidade: '))
limite = 80
if velocidade > limite:
    km_acima = velocidade - limite
    multa = km_acima * 7.0
    print('Você foi multado!')
    print(f'Multa a pagar R${multa:.2f}')
else:
    print('Velcidade dentro do limite. Dirija com segurança!')
    