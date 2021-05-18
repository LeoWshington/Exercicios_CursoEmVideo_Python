def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31;0mERRO! Digite um numero inteiro valido: \033[m.')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
