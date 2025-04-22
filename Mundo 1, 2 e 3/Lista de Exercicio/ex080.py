valores = []

while len(valores) < 5:
    num = int(input('Digite um número: '))

    if len(valores) == 0 or num > valores[-1]:
        valores.append(num)
    else:
        for i in range(len(valores)):
            if num <= valores[i]:
                valores.insert(i, num)
                break

print(f'Lista ordenada: {valores}')
