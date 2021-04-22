a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
pa = a1
for c in range(1, 11):
    print(pa, end=" -> ")
    pa += r
print('Fim.')
