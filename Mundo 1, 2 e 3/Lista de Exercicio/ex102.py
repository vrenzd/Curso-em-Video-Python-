def fatorial(n, show=False):
    '''
    Calcula o fatorial de um número.
    
    Parâmetros:
    n (int): O número a ser calculado.
    show (bool): Mostra ou não o processo da conta. (Padrão é False)
    
    Retorna:
    int: O resultado do fatorial de n.
    '''
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
    return f

print(fatorial(5, show=True)) # Mostra o cálculo 