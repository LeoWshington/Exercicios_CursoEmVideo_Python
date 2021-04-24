matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somat = maior = 0

for li in range(0, 3):
    for c in range(0, 3):
        matrix[li][c] = int(input(f'Insira um valor para posição [{li}, {c}]: '))
        if matrix[li][c] % 2 == 0:
            soma += matrix[li][c]
        if c == 2:
            somat += matrix[li][2]
        if li == 1 and c == 0:
            maior = matrix[2][c]
        if matrix[1][c] > maior:
            maior = matrix[1][c]
print('A matriz gerada é: ')
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[li][c] :^4}]', end=' ')
    print()
print(f'A soma de todos os valores pares é {soma}.\n'
      f'A soma de todos os valores da 3ª coluna é {somat}.\n'
      f'O maior valor da segunda coluna é {maior}.')
