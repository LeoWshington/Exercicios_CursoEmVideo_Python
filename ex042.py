a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    if a == b == c:
        print('Os seguimentos passados podem formar um triangulo, e ele é equilatero.')
    elif (b == c) and c != a or (a == c) and b != a or (b == a) and c != b:
        print('Os seguimentos passados podem formar um triangulo, e ele é isosceles.')
    elif a != b and b != c and c != a:
        print('Os seguimentos passados podem formar um triangulo, e ele é escaleno.')
else:
    print('Os seguimentos passados não podem formar um triangulo.')
