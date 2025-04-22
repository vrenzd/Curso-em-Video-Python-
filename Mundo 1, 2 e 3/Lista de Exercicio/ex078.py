valores = []

# Lê 5 valores númericos 
for i in range(5):
    valores.append(int(input('Digite um valor: ')))

# Encontra o maior e o menor valor na lista
maior = max(valores)
menor = min(valores)

# Encontra as posições do maior e menor valor
pos_maior = [i+1 for i, v in enumerate(valores) if v == maior]
pos_menor = [i+1 for i, v in enumerate(valores) if v == menor]

# Exibe os resultados
print(f'O maior valor é {maior} e sua posição é: {pos_maior}')
print(f'O maior valor é {menor} e sua posição é: {pos_menor}')
