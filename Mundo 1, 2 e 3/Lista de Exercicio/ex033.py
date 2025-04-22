n1 = float(input('1º número: '))
n2 = float(input('2º número: '))
n3 = float(input('3º número: '))

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

print(f'O maior número é {maior}') 
print(f'O menor número é {menor}') 
      