expressao = input('Digite uma expressão: ')
pilha = []
correto = True

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) == 0 or pilha.pop() != ')':
            correto = False
            break

if len(pilha) and correto:
    print('Expressão está válida.')
else:
    print('Expressão está inválida.')
    
