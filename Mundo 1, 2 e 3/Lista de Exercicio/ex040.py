def calcular_media(media):
    if media < 5.0:
        return 'REPROVADO!'
    elif 5.0 <= media < 6.9:
        return 'RECUPERAÇÃO!'
    else:
        return 'APROVADO!'
    
n1 = float(input('1ª nota: ')) 
n2 = float(input('2ª nota: '))   
media = (n1 + n2) / 2
resultado = calcular_media(media)
print(resultado)
