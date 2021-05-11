def area(c, la):
    print(f'A area de um terreno {c :.2f}m x {la :.2f}m é de {c * la :.2f}m².')


# Programa principal
print(f'{"Controle de Terrenos" :^30}\n'
      f'{"-" * 30}')
comp = float(input('Comprimento (m)): '))
larg = float(input('Largura (m): '))
area(comp, larg)
