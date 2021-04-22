n = int(input('Digite o numero: '))
contador = 0
for c in range(n, 0, -1):
    if n % c == 0:
        contador += 1
if contador == 2:
    print(f'O número {n} é um número primo.')
else:
    print(f'O número {n} não é um número primo.')
