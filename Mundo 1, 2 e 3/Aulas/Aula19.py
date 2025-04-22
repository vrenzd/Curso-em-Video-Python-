meu_dicionario = {'nome': 'João', 'idade': 25, 'cidade':'Rio Claro'}
print(meu_dicionario['cidade'])

meu_dicionario['profissão'] = 'Engenheiro'
meu_dicionario['cidade'] = 26

del meu_dicionario['cidade']
idade = meu_dicionario.pop('idade')

chaves = meu_dicionario.keys() # Retorna todas as chaves do dicionário
valores = meu_dicionario.values() # Retorna todos os valores do dicionário
itens = meu_dicionario.items()  # Retorna uma lista de tuplas com pares chave-valor

print(meu_dicionario)

for chave in meu_dicionario:
    print(chave, meu_dicionario[chave])
