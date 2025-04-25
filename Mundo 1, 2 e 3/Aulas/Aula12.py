from time import sleep

nome = str(input('Informe seu nome: '))
print('-=-' * 10)
print('Analisando seu nome...')
print('-=-' * 10)
sleep(1.3)

if nome == 'Victor':
    print('Você é o rei do oeste!')
elif nome in ['Maria', 'Ana', 'Julia']:
    print('Vocês são incríveis!')
elif nome == 'Eduardo':
    print('Você tem um nome forte e marcante!')
else:
    print(f'{nome}, você é único e especial!')
