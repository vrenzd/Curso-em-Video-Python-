def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    
    boletim = dict()
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = sum(n) / len(n)
    
    if sit:
        if boletim['média'] >= 7:
            boletim['situação'] = 'Boa'
        elif boletim['média'] >= 5:
            boletim['situação'] = 'Razoável'
        else:
            boletim['situação'] = 'Ruim'
    return boletim

resposta = notas(5.5, 9.5, 7, 8.5, sit=True)
print(resposta)