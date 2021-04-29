from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo desejado: '))
print(f'O ângulo de {angulo} tem SENO de {sin(radians(angulo)) :.2f}\n'
      f'O ângulo de {angulo} tem COSENO de {cos(radians(angulo)) :.2f}\n'
      f'O ângulo de {angulo} tem TANGENTE de {tan(radians(angulo)) :.2f}')
