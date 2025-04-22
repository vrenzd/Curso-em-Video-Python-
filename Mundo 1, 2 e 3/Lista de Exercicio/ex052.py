def primo(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
n = int(input('Informe um número maior que 1: '))

if primo(n):
    print(f'{n} é primo.')
else:
    print(f'{n} não é primo.')
    