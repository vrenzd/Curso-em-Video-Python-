from datetime import date

atual = date.today().year
maior = 0
menor = 0

for _ in range(7):
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'Maiores de idade: {maior}')
print(f'Menores de idade: {menor}')
        