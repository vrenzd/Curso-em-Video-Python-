def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

def status_imc(imc):
    if imc < 18.5:
        return 'Abaixo do Peso'
    elif 18.5 <= imc < 25:
        return 'Peso ideal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 40:
        return 'Obesidade'
    else:
        return 'Obesidade Mórbida'
    
peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = calcular_imc(peso, altura)
resultado = status_imc(imc)
print(f'Seu IMC: {imc:.2f}.\nStatus: {resultado}.')
