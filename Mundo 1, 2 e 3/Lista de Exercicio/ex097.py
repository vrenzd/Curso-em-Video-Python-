def escreva(txt):
    print('=' * (len(txt) + 3))
    print(f'  {txt}  ')
    print('=' * (len(txt) + 3))


texto = input('Digite um texto: ').strip()
escreva(texto)
