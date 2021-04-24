pessoas = list()
temporario = list()
pesados = list()
leves = list()
cont = 0
maior = menor = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    pessoas.append(temporario[:])
    if cont == 0:
        maior = menor = temporario[1]
    if temporario[1] >= maior:
        if maior < temporario[1]:
            pesados.pop()
        maior = temporario[1]
        pesados.append(temporario[0].title()    )
    if temporario[1] <= menor:
        if menor < temporario[1]:
            leves.pop()
        menor = temporario[1]
        leves.append(temporario[0].title())
    temporario.clear()
    cont += 1
    op = str(input('Quer continuar[S/N]: ')).strip()[0]
    print(f'{"~" * 30}')
    if op in 'Nn':
        break
print(f'Foram cadastradas {cont} pessoas.\n'
      f'O maior peso foi {maior :.2f} de: {pesados}\n'
      f'O menor peso foi {menor :.2f} de: {leves}')
