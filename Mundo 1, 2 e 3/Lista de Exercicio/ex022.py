from time import sleep

nome = str(input('Nome completo: ')).strip()
sleep(0.5)
print('Analisando seu nome...')
sleep(0.5)
print(f'Seu nome em maiúsculas é {nome.upper()}')
sleep(0.5)
print(f'Seu nome em minúsculas é {nome.lower()}')
sleep(0.5)
print(f'Seu nome tem ao todo tem {len(nome) - nome.count(' ')} letras.')
sleep(0.5)
separa = nome.split()
print(f'Seu primeiro é {separa[0]} e ele tem {len(separa[0])} letras.')
