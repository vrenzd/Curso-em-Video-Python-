from random import choice

alunos = ['Victor', 'João', 'Laura', 'Pedro']
for i in range(4):
    escolhido = choice(alunos)
print(f'O aluno escolhido para apagar o quadro é {escolhido}')   
