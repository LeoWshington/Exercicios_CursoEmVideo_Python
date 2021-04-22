n = c = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    c = 1
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c :2} = {n * c :2}')
        c += 1
print('Obrigado por usar nossa tabuada!')
