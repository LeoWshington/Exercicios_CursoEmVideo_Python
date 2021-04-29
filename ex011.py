l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
print(f'Sua parede tem a dimensão de {l :.2f}x{a :.2f} e sua área é de {l * a :.2f}m².\n'
      f'Para pintar essa parede, você precisará de {(l * a) / 2 :.2f}l de tinta.')
