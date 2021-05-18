def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um numero valido:\033[m ')
            continue
        return n


def leiafloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Digite um numero valido:\033[m ')
            continue
        return n


numero = leiaint('Digite um Inteiro: ')
numero2 = leiafloat('Digite um Real: ')
print(f'O valor inteiro foi {numero} e o real foi {numero2}')
