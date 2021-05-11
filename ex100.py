from random import randint
from time import sleep
numeros = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(f'{numeros[c]} ', end='')
        sleep(0.5)
    print('Pronto!')


def somaPar():
    soma = 0
    print(f'Somando os valores pares de {numeros}, temos um total igual a ', end='')
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'{soma}.')


sorteia()
somaPar()
