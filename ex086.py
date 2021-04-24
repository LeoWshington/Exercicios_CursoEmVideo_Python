matrix = [[], [], []]
c = li = 0
while True:
    while li <= 2:
        c = 0
        while c <= 2:
            matrix[li].append(input(f'Digite um valor para posição [{li}, {c}]: '))
            c += 1
        li += 1
    if li > 2:
        break
print('A matrix gerada é: ')
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[li][c] :^4}]', end=' ')
    print()
