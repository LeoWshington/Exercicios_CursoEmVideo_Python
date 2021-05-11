from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim < inicio:
        for c in range(inicio, fim - 1, -passo):
            print(f'{c} ', end='')
            sleep(0.5)
        print(f'Fim!\n{"=" * 30}')
    else:
        for c in range(inicio, fim, passo):
            print(f'{c} ', end='')
            sleep(0.5)
        print(f'Fim!\n{"=" * 30}')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
