help(print)
print(print.__doc__)

#---------------------------------

def saudacao(nome):
    """Exibe uma saudação personalizada.
    
    Parâmetro:
    nome -- nome da pessoa a ser saudada
    """
    print(f"Olá, {nome}!")

# Depois
help(saudacao) # vai exibir a explicação contida na docstring

#---------------------------------

def soma(a=0, b=0, c=0):
    return a + b + c

print(soma(3, 4))       # Saída: 7
print(soma())           # Saída: 0
print(soma(1, c=5))     # Saída: 6

x = 5  # escopo global

#---------------------------------

def exemplo():
    x = 10  # escopo local
    print(f"Dentro da função, x = {x}")

exemplo()
print(f"Fora da função, x = {x}")

#---------------------------------

# Com global
def modifica():
    global x
    x = 20

modifica()
print(f"x agora vale {x}")  # Agora x será 20

#---------------------------------

# Em vez de imprimir dentro da função, retorna o valor
def multiplica(a, b):
    return a * b

resultado = multiplica(3, 5)
print(f"O resultado da multiplicação é {resultado}")

#---------------------------------

# Também pode retornar valores lógicos, strings, listas, dicionários...
def par_ou_impar(n):
    return "Par" if n % 2 == 0 else "Ímpar"


