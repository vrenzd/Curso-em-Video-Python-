def saudacao():
    print("Olá, seja bem-vindo!")
    
saudacao()

#---------------------------------

print(len("Python"))  

# Exemplo de função personalizada
def quadrado(n):
    return n * n

print(quadrado(4))  

#---------------------------------

def linha():
    print('-' * 30)

linha()

#---------------------------------

def mensagem(texto):
    print(f'--- {texto} ---')

mensagem("Início do Programa")

#---------------------------------

def contador(*num):
    for valor in num:
        print(valor, end=' ')
    print()

contador(3, 5, 1)
#---------------------------------

def dobra(lista):
    for i in range(len(lista)):
        lista[i] *= 2

valores = [2, 4, 6]
dobra(valores)
print(valores) 
