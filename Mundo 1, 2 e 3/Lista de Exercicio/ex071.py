valor = int(input('Qual valor você deseja sacar? R$'))
  
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1 = 0
  
while valor > 0:
    if valor >= 50:
        cedula50 += 1
        valor -= 50
    elif valor >= 20:
        cedula20 += 1
        valor -= 20
    elif valor >= 10:
        cedula10 += 1
        valor -= 10
    else:
        cedula1 += 1
        valor -= 1
 
print(f'Cédulas de R$50: {cedula50}')
print(f'Cédulas de R$20: {cedula20}')
print(f'Cédulas de R$10: {cedula10}')
print(f'Cédulas de R$1: {cedula1}')