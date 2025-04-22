distancia = float(input('Distância percorrida: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'O custo da viagem será de R${preço:.2f}')    
