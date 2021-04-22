from random import randint
from time import sleep
print(f'\033[1:36m{"-=-" * 20}\033[m\n'
      f'\033[1:35:40m{"JOKENPÔ":^60}\033[m\n'
      f'\033[1:36m{"-=-" * 20}\033[m')
op = int(input(f'\033[1:36m{"-=-" * 10}\033[m\n'
               f'\033[1:37m{"Ecolha:":^30}\033[m\n'
               f'\033[1:36m{"-=-" * 10}\033[m\n'
               f'1 - \033[:37mPedra\033[m\n'
               f'2 - \033[:34mPapel\033[m\n'
               f'3 - \033[:33mTesoura\033[m\n'
               f'Qual sua jogada? '))
computador = randint(1, 3)
jokenpo = [" ", "\033[:37mPedra\033[m", "\033[:34mPapel\033[m", "\033[:33mTesoura\033[m"]
if 1 <= op <= 3:
    if op == computador:
        print('\033[1:35mJO\033[m', end="")
        sleep(1)
        print('\033[1:35mKEN\033[m', end="")
        sleep(1)
        print('\033[1:35mPÔ!\033[m')
        sleep(0.2)
        print(f'Você escolheu {jokenpo[op]} eu escolhi {jokenpo[computador]},\033[:36mTEMOS UM EMPATE!\033[m')
    elif computador == 1 and op == 3 or computador == 2 and op == 1 or computador == 3 and op == 2:
        print('\033[1:35mJO\033[m', end="")
        sleep(1)
        print('\033[1:35mKEN\033[m', end="")
        sleep(1)
        print('\033[1:35mPÔ!\033[m')
        sleep(0.2)
        print(f'Você escolheu {jokenpo[op]} eu escolhi {jokenpo[computador]},\033[:31mVOCÊ PERDEU!\033[m')
    else:
        print('\033[1:35mJO\033[m', end="")
        sleep(1)
        print('\033[1:35mKEN\033[m', end="")
        sleep(1)
        print('\033[1:35mPÔ!\033[m')
        sleep(0.2)
        print(f'Você escolheu {jokenpo[op]} eu escolhi {jokenpo[computador]},\033[:32mVOCÊ GANHOU!')
else:
    print('\033[1:31:40mOPÇÃO INVALIDA!\033[m')
