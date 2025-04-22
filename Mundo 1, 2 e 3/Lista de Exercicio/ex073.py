tabela = ('Vitória', 'Sport', 'Ceará', 'Juventude', 'Guarani', 
          'Criciúma', 'Ponte Preta', 'Londrina', 'Sampaio Corrêa', 'CRB', 
          'Avaí', 'Novorizontino', 'Tombense', 'Chapecoense', 'Botafogo-SP', 
          'Vila Nova', 'CSA', 'Operário-PR', 'Confiança', 'ABC') 

print('=-=' * 6)
print('BRASILEIRÃO SÉRIE B')
print('=-=' * 6)

os5_primeiros = tabela[:5]
os4_ultimos = tabela[-4:]
alfabetica = sorted(tabela)
posicao = tabela.index('Chapecoense') + 1

print(f'Os 5 primeiros: {os5_primeiros}')    
print(f'Os 4 últimos: {os4_ultimos}')
print(f'A tabela em ordem alfabética: {alfabetica}')
print(f'A Chapecoense está na {posicao}ª posição')
