alunos = []

# Loop infinito para entrada de dados dos alunos
while True:
    nome = input('Nome do aluno: ')
    if not nome:  # Interrompe se o nome for vazio
        break
    
    notas = []
    for i in range(2):
        while True:
            try:
                notas.append(float(input(f'Nota {i+1}: ')))
                break
            except ValueError:
                print('Digite um número válido.')
    
    media = sum(notas) / len(notas)
    alunos.append([nome, notas, media])

# Mostra o boletim com as médias dos alunos
print('\nBoletim:')
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, aluno in enumerate(alunos):
    print(f'{i+1:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

# Permite que o usuário veja as notas de cada aluno individualmente
while True:
    opcao = input('\nMostrar notas de qual aluno? (999 para sair): ')
    if opcao.isdigit():
        opcao = int(opcao) 
        if opcao == 999:
            print('Finalizando...')
            break
        elif 0 <= opcao < len(alunos):
            print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
        else:
            print('Opção inválida. Tente novamente.')
    else:
        print('Digite um número válido.')
