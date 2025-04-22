from random import randint

num_aleatorios = tuple(randint(1, 10) for _ in range(5))

maior = max(num_aleatorios)
menor = min(num_aleatorios)

print('GERADOR DE NÚMEROS ALEATÓRIOS')
print('-=-' * 10)

print(f'Números gerados: {num_aleatorios}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
