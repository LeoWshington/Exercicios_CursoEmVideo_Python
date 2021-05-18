def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero Inteiro valido:\033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuario preferiu nao digitar o numero!\033[m ')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero Real valido:\033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuario preferiu nao digitar o numero!\033[m ')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro foi {n1} e o real foi {n2}')
