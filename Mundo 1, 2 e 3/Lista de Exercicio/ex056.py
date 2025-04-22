soma = 0
homem_mais_velho = 0
idade_homem_velho = 0
mulher_menor20 = 0

for i in range(1,5):
    print(f'--- {i}ª Pessoa ---')
    nome = input('Nome: ')
    idade= int(input('Idade: '))
    sexo = int(input('[1] - Masculino\n[2] - Feminino\n> '))
    soma += idade

    if sexo == 1 and idade > idade_homem_velho:
        homem_mais_velho = nome
        idade_homem_velho = idade

    if sexo == 2 and idade < 20:
        mulher_menor20 += 1

media = soma / 4
print(f'Média do grupo: {media} anos')
print(f'Homem mais velho: {homem_mais_velho}')
print(F'Mulheres com menos de 20 anos: {mulher_menor20}')
