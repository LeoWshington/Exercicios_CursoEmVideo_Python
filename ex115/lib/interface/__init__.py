def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um código valido:\033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuario preferiu nao digitar o numero!\033[m ')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menuprincipal(lista):
    cabecalho('MENU PRINCIPAL v1.0')
    c = 1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    print(linha())
    resp = leiaInt('\033[0;32mSua opção:\033[m ')
    return resp
