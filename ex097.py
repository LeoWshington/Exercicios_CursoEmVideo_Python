def escreva(texto):
    print(f'{"-" * (len(texto) + 4)}\n'
          f'{texto:^{len(texto) + 4}}\n'
          f'{"-" * (len(texto) + 4)}')


# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
