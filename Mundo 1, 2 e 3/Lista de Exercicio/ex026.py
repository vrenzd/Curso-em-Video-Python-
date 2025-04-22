frase = str(input('Informe uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A primeira letra A apareceu na {frase.find('A')+1}ª posição')
print(f'A última letra A apareceu na {frase.rfind('A')+1}ª posição')
