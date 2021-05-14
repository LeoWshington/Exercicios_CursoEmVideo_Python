from time import sleep


def texto(msg, cor_fonte=0, cor_fundo=0):
    print(f'\033[0;{cor_fonte};{cor_fundo}m{"-"}\033[m' * (len(msg) + 4))
    print(f'\033[0;{cor_fonte};{cor_fundo}m{msg :^{(len(msg) + 4)}}\033[m')
    print(f'\033[0;{cor_fonte};{cor_fundo}m{"-"}\033[m' * (len(msg) + 4))


def pyhelp(tex):
    texto(f'Acessando o manual do comando "{text}"', 97, 44)
    sleep(0.5)
    print('\033[7;97;40m')
    help(tex)
    print('\033[m', end='')


while True:
    sleep(0.5)
    texto('SISTEMA DE AJUDA PyHELP', 97, 43)
    sleep(0.5)
    text = str(input('Função ou bibliotéca? ')).strip().lower()
    if text == 'Fim':
        break
    pyhelp(text)
len