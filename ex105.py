def notas(*nota, sit=False):
    """
    -> Para analisar notas e situação de varios alunos
    :param nota: uma ou mais notas dos alunos (aceita varias)
    :param sit: Valor opcional indica se deve ou nao indicar a situação
    :return: dicionario com varias informaçoes sobre a turma
    """
    notas_aluno = dict()
    notas_aluno['total'] = len(nota)
    notas_aluno['maior'] = max(nota)
    notas_aluno['menor'] = min(nota)
    notas_aluno['media'] = sum(nota) / len(nota)
    if sit:
        if notas_aluno['media'] < 5.0:
            notas_aluno['situação'] = "Ruim"
        elif 5.0 <= notas_aluno['media'] <= 7.0:
            notas_aluno['situação'] = "Razoavel"
        elif 7.0 < notas_aluno['media'] <= 10.0:
            notas_aluno['situação'] = "Boa"
    return notas_aluno


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
