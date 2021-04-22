valores = list()
cont = 0
while True:
    n = float(input('Digite um valor: '))
    valores.append(n)
    op = str(input('Deseja continuar [S/N]? ')).strip()[0]
    cont += 1
    if op in 'Nn':
        break
    print(f'{"~" * 30}')
valores.sort(reverse=True)
print(f'Foram digitados {cont} numeros.\n'
      f'Em ordem decrecente a lista fica: ', end='')
for p, v in enumerate(valores):
    if (p + 1) == len(valores):
        print(v)
    else:
        print(v, end=' - ')
print('O numero 5 aparece na(s) ', end='')
for pos, v in enumerate(valores):
    if v == 5:
        print(f'{pos + 1}ª ', end='')

print(' posição(es).')
