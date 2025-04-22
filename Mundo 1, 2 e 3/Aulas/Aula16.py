lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]} na posição {i}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print(sorted(lanche))
print('Comi muito!')

a = (5, 4, 3)
b = (1, 2, 6, 7)
c = a + b
print(c.count(5))
print(c.index(7))
