def leiaInt(mensagem):
    '''
    Lê um número inteiro do usuário com validação.
    
    Parâmetros:
    mensagem (str): A mensagem a ser exibida no input.
    
    Retorna:
    int: O número inteiro digitado pelo usuário.
    '''
    while True:
        valor = input(mensagem)
        
        if valor.strip().lstrip('-').isdigit():
            return int(valor)
        else:
            return '\033[31mERRO!\033[m Digite um número inteiro válido.'
        
n = leiaInt('Digite um número inteiro: ') 
print(f'Você acabou de digitar o número {n}.')       