from random import randint
contv = 0
while True:
    s = 0
    comp = randint(0, 10)
    n = int(input('Diga um valor: '))
    op = str(input('Par ou impar? P/I ')).strip().lower()
    s = n + comp
    if s % 2 == 0 and op == 's':
        contv += 1
        print(f'Você jogou {n} e eu {comp} total {s}. É par.\n'
              f'Você venceu!!')
    elif s % 2 != 0 and op == 'i':
        contv += 1
        print(f'Você jogou {n} e eu {comp} total {s}. É impar.\n'
              f'Você venceu!!')
    elif s % 2 == 0 and op == 'i':
        print(f'Você jogou {n} e eu {comp} total {s}. É par. Você escolheu impar.\n'
              f'Você Perdeu!!')
        break
    elif s % 2 != 0 and op == 'p':
        print(f'Você jogou {n} e eu {comp} total {s}. É impar. Você escolheu par.\n'
              f'Você Perdeu!!')
        break
    print('Vamos jogar novamente...')
print(f'Voce conseguiu me vencer {contv} vezes. GAME OVER!!!!')
