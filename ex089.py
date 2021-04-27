provisorio = []
provisorio_medio = []
alunos = []
aluno_media = []
cont = 0
while True:
    provisorio.append(str(input('Nome: ')))
    provisorio.append(float(input('Nota 1: ')))
    provisorio.append(float(input('Nota 2: ')))
    provisorio_medio.append(provisorio[:][0])
    provisorio_medio.append((provisorio[:][1] + provisorio[:][2]) / 2)
    op = str(input('Quer continuar[N/S]? ')).strip()[0]
    alunos.append(provisorio[:])
    aluno_media.append(provisorio_medio[:])
    provisorio.clear()
    provisorio_medio.clear()
    cont += 1
    print('~' * 30)
    if op in 'Nn':
        break
print(f'Nº   Nome      Média\n'
      f'{"_" * 30}')
for c in range(0, cont):
    print(c, end='   ')
    for co in range(0, 2):
        if aluno_media[c][co] == aluno_media[c][1]:
            print(f'{aluno_media[c][co] :>8.1f}')
        else:
            print(f'{aluno_media[c][co] :^7}', end='')
while True:
    op2 = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if op == 999:
        break
    print(f'As notas de {alunos[op2][0].title()} são [{alunos[op2][1]}, {alunos[op2][2]}]')
