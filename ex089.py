nomes = []
geral = []
notas = []
alunos = [[" ", [0.0, 0.0]]]
resposta = 'Ss'
while True:
    nomes.append(str(input('Nome: ')).strip())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos[0][0] = nomes[:]
    alunos[0][1][0] = notas[:][0]
    alunos[0][1][1] = notas[:][1]
    geral.append(alunos)
    alunos.clear()
    nomes.clear()
    notas.clear()
    alunos.clear()
    resposta = str(input('Quer continuar[S/N]? ')).strip()[0]
    if resposta in 'Nn':
        break
print(geral)
