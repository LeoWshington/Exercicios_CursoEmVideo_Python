from random import randint
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Os numeros sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior numero é {max(numeros)}\n'
      f'O menor numero é {min(numeros)}')
