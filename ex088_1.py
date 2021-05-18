from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGAR NA MEGA SENA')
print('-' * 30)
quant = int(input('Quantos jogos voce quer? '))
tot = 0
while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=' * 5, f'SORTEANDO {quant} Jogos', '=' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(2)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)