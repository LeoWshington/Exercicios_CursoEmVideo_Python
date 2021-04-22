lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado na ultima posição.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na {pos + 1}ª posição.')
                break
            pos += 1
print(f'Os valores digitados foram\n'
      f'{"~" * 30}')
for p, v in enumerate(lista):
    if (p + 1) == len(lista):
        print(v)
    else:
        print(v, end=' - ')
