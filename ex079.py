valores = list()
while True:
    n = float(input('Digite um valor: '))
    if n in valores:
        print(f'O valor {n :.2f} já se encontra na lista. Não pode ser adicionado')
        n = float(input('Digite outro valor: '))
    valores.append(n)
    op = str(input('Deseja continuar [S/N]? ')).strip()[0]
    if op in 'Nn':
        break
    print(f'{"~" * 30}')
valores.sort()
print(f'Os valores digitados foram:')
for p, v in enumerate(valores):
    if (p + 1) == len(valores):
        print(v)
    else:
        print(v, end=' - ')
