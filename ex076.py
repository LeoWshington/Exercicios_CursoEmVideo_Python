print(f'{"-" * 40}\n'
      f'{"LISTAGEM DE PREÇOS" :^40}\n'
      f'{"-" * 40}')
lista =('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
        'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 'Regua', 3.00, 'Grampo', 1)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c] :.<31}R$', end='')
    else:
        print(f'{lista[c] :>7.2f}')
print(f'{"-" * 40}')
