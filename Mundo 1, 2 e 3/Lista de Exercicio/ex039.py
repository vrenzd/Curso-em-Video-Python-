from datetime import date

sexo = str(input('Escolha:\n[M] - Masculino\n[F] - Feminino\n> ')).upper()
if sexo == 'F':
    print('Você não precisa se alistar, mocinha!')
else:
    nascimento = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - nascimento
    print(f'Você tem {idade} anos.')

    if idade < 18:
        passado = 18 - idade
        print(f'Ainda faltam {passado} anos, fique tranquilo!')
    elif idade == 18:
        print('Já é hora de se alistar, SOLDADO!')
    elif idade > 18:
        passado = idade - 18
        print(f'Já passou da hora de se alistar, SOLDADO!\nVocê deveria ter se alistado há {passado} anos.')
        