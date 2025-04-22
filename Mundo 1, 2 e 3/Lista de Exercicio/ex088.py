from random import sample

quantidade_jogos = int(input('Quantos jogos você deseja gerar? '))
 
jogos = []

# Gerando os jogos
for _ in range(quantidade_jogos):
    jogo = sorted(sample(range(1, 61), 6))
    jogos.append(jogo)
    
# Mostrando os jogos na tela
print('Os jogos da MEGA SENA são:')
for i, jogo in enumerate(jogos, 1):
    print(f'Jogo {i}: {jogo}')
