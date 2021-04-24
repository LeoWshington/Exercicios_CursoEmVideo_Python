temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Qauer continuar [S/N]: '))
    if resp in 'Nn':
        break
    print(f'{"~" * 30}')
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior :.2f}Kg. De: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor :.2f}Kg')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
