principal = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        principal[0].append(n)
    else:
        principal[1].append(n)
print(f'{"^~^" * 20}')
principal[0].sort()
principal[1].sort()
print(f'Os valores pares digitados foram: {principal[0]}\n'
      f'Os valores impares digitados foram: {principal[1]}')
