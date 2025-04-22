def converter_base(numero, base):
    if base == 1:
        return bin(numero)[2:]
    elif base == 2:
        return oct(numero)[2:]
    elif base == 3:
        return hex(numero)[2:]
    else:
        return 'Base Inválida! Tente Novamente.'

numero = int(input('Informe um número: '))
base = int(input('''Escolha a base de conversão:
                 1 - Bínario
                 2 - Octal
                 3 - Hexadecimal
                 > ''')) 
resultado = converter_base(numero, base)
print(f'Resultado: {resultado}')
