co = 0
s = 0
for c in range(0, 6):
    n = int(input('Digite o numero: '))
    if n % 2 == 0:
        s += n
        co += 1
print(f'A soma dos {co} numeros pares digitados é {s}')
