lista = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o ultimo valor: ')))
print(f'Você digitou os valores {lista}.\n'
      f'O valor 9 aparece {lista.count(9)}.\n')
if 3 in lista:
    print(f'O primeiro valor 3 aparece na posiçao {lista.index(3) + 1}.')
else:
    print('Valor 3 não encontrado.')
print(f'Os valores pares digitados foram: ', end='')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
