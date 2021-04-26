from random import randint
from time import sleep
sorteados = []
ll = 0
n = int(input(f'{"-" * 45}\n'
              f'{"JOGAR NA MEGA SENA" :^30}\n'
              f'{"-" * 45}\n'
              f'Quantos jogos você quer que eu sorteie? '))
for c in range(0, n):
    for ll in range(0, 6):
        s = randint(1, 60)
        if ll != 0 and s in sorteados:
            s = randint(1, 60)
        sorteados.append(s)
    sorteados.sort()
    print(f'Jogo {c + 1 :^2}: {sorteados}')
    sorteados.clear()
    sleep(0.5)
print(f'{"< BOA SORTE! >" :=^45}')
