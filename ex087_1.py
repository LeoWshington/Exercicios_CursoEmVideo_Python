matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for li in range(0, 3):
    for c in range(0, 3):
        matriz[li][c] = int(input(f'Digite um valor [{li},{c}]: '))
print('~' * 30)
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[li][c]:^5}] ', end='')
        if matriz[li][c] % 2 == 0:
            spar += matriz[li][c]
    print()
print(f'A soma de todos valores pares é {spar}.')
for li in range(0, 3):
    scol += matriz[li][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
