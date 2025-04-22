while True:
    a = int(input('1º número: '))
    b = int(input('2º número: '))
    
    print('''Escolha uma opção:
    [1] - Soma
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair do Programa''')

    opcao = int(input('> '))
    
    if opcao == 1:
        soma = a + b
        print(f'A soma entre {a} e {b} é: {soma}')
    elif opcao == 2:
        multiplicar = a * b
        print(f'A multiplicação de {a} x {b} = {multiplicar}')
    elif  opcao == 3:
        maior = max(a, b)
        print(f'O maior número entre {a} e {b} é: {maior}')
    elif opcao == 4:
        continue
    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('Opçãao inválida. Tente novamente.')
