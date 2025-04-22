while True:
    sexo = str(input('[M] - Masculino\n[F] - Feminino\n> ')).upper().strip()
    if sexo in ['M', 'F']:
        break
    else:
        print('Valor inválido. Digite Novamente (M/F).')
       
print(f'Sexo registrado: {sexo}')
    