from math import sqrt, pow
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))
print(f'A hipotenusa vai medir {sqrt(pow(co,2) + pow(ca,2)) :.2f}')
