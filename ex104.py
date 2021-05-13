def leiaInt(txt):
    while True:
        n = input(txt)
        if int(n.isnumeric()):
            v = n
            break
        else:
            print('\033[0;31mERRO! Digite um numero valido:\033[m ')
    return v


numero = leiaInt('Digite um numero: ')
print(f'Vocẽ acabou de digitar o valor {numero}')
