def maior(*numeros):
    if not numeros:
        print('Nenhum número foi informado.')
        return
    
    maior_num = max(numeros)
    print(f'Os números informados foram: {numeros}')
    print(f'O maior valor é {maior_num}')
    
maior(18, 2, 4, 20, 11)