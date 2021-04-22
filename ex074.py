from random import randint
c = n0 = n1 = n2 = n3 = n4 = 0
for c in range(0, 5):
    if c == 0:
        n0 = randint(0, 100)
    if c == 1:
        n1 = randint(0, 100)
    if c == 2:
        n2 = randint(0, 100)
    if c == 3:
        n3 = randint(0, 100)
    if c == 4:
        n4 = randint(0, 100)
    c += 1
lista = (n0, n1, n2, n3, n4)
print(f'Os numeros gerados foram {lista}.\n'
      f'O maior numero é {max(lista)}.\n'
      f'O menor numero é {min(lista)}.')
