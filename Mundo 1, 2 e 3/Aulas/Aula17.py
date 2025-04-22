num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(2)

if 4 in num:
    num.remove(2)
else:
    print('Não achei o número 5')

print(num)
print(f'Essa lista tem {len(num)} elementos.')



valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for i, v in enumerate(valores):
    print(f'Na posição {i} encontrei o valor {v}!')
print('Cheguei ao final da lista.')




a = [2, 5, 9, 1]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
