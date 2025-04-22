teste = list()
teste.append('Victor')
teste.append(26)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)

print()
galera = [['João', 11], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for i in galera:
    #print(galera[2][1])
    print(i)
print()

galera = list()
dado = list()
tmaior = 0
tmenor = 0
for i in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade.')
        tmaior += 1
    else:
        print(f'{i[0]} é menor de idade.')
        tmenor += 1

print(f'Temos {tmaior} maiores e {tmenor} menores de idade.')
