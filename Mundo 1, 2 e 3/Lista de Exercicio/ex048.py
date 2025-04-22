soma = 0
contador = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        contador += 1
print(f'A soma de todos os {contador} é {soma}') 
       