def mostrar_vogais(palavras):

    vogais = 'aeiouAEIOU'

    for palavra in palavras:
        resultado = [letra for letra in palavra if letra in vogais]
        print(f'{palavra} - Vogais: {', '.join(resultado)}')

mostrar_vogais(palavras=(
    'banana',
    'maca',
    'pera',
    'uva',
    'laranja',
    'abacaxi',
    'morango',
    'kiwi',
    'melancia',
    'cereja'))
