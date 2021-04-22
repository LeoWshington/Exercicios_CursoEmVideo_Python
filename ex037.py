n = int(input(f'Digite um numero para ser convertido: '))
o = int(input(f'1 - para binário.\n'
              f'2 - para octal.\n'
              f'3 - para hexadecimal.\n'
              f'Sua opção: '))
if o == 1:
    print(f'O numero {n} em binário é igual a : {str(bin(n))[2:]}!')
elif o == 2:
    print(f'O numero {n} em octal é igual a: {str(oct(n))[2:]}!')
elif o == 3:
    print(f'O numero {n} em hexadecimal é igual a: {str(hex(n))[2:]}!')
else:
    print('Opção INVALIDA!')
