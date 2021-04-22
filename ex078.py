valores = list()
for c in range(1, 6):
    valores.append(input(f'Digite o {c}º valor: '))
print('Você digitou os valores: ', end='')
for pos, v in enumerate(valores):
    print(v, end=' ')
print(f'\nO maior numero digitado foi {max(valores)} nas ', end='')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos + 1}ª', end='')
    print('' if v == max(valores) else ' - ', end='')
print(' posição(es).')
print(f'O menor numero digitado foi {min(valores)} nas', end='')
for pos, v in enumerate(valores):
    if v == min(valores):
        if pos + 1 == len(valores):
            print(f'{pos + 1}ª')
        else:
            print(f'{pos + 1}ª', end=' - ')

print(' posição(es).')
