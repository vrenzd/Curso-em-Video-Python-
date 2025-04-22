salario = float(input('Salário: R$'))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento
print(f'Quem ganhava R${salario:.2f}, 
      passa a ganhar R${novo_salario:.2f} agora')    
