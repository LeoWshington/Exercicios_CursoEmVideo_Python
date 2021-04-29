num = int(input('Digite um numero: '))
print(f'Analisado o numero {num}\n'
      f'Unidades: {num // 1 % 10}\n'
      f'Dezenas: {num // 10 % 10}\n'
      f'Centenas: {num // 100 % 10}\n'
      f'Milhar: {num // 1000 % 10}')
