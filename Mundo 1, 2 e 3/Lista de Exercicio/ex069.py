print('-=-' * 9)
print('Análise de dados do grupo')
print('-=-' * 9)

maiores_18 = 0
homens = 0
mulheres_menor20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('[M] - Masculino\n[F] - Feminino\n> ').strip().upper()

    if idade > 18:
        maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor20 += 1

    continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar != 'S':
        break

print(f'Total de maiores de 18 anos: {maiores_18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres_menor20}')
