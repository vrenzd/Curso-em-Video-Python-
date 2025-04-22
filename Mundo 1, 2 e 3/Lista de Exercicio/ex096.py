def area():
    print('Controle de Terrenos')
    print('-'*20)
    print(f'A área de um terreno {l}x{c} é de {l*c} m²')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)
