from time import sleep

valores = list()


def maior(* num):
    if len(num) > 0:
        print('Analisando os valores passados...')
        for valor in num:
            print(f'{valor} ', end='')
            valores.append(valor)
            sleep(0.5)
        print(f'Foram informados {len(valores)} valores.\n'
              f'O maior valor informado foi {max(valores)}.')
        print('==' * 30)
        valores.clear()
    else:
        print(f'Foram digitados {len(valores)} valores ao todo.\n'
              f'E o maior valor digitado não existe.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
