def notas(*n, sit=False):
    """
    -> Função para analisar notas e situaçẽs de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informaçoes sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['stuação'] = 'Boa'
        elif r['média'] >= 5:
            r['stuação'] = 'Rasoavel'
        else:
            r['stuação'] = 'Ruim'
    return r


# Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
