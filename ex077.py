lista = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
         'Mercado', 'Programador', 'Futuro', 'Número')
for c in range(0, len(lista)):
    print(f'Na palavra "{lista[c]}" temos: ', end='')
    for c1 in range(0, len(lista[c])):
        if lista[c][c1] in 'AÁaáEÉeéIÍiíOÓoóUÚuú':
            print(f'{lista[c][c1]}', end=' ')
    print('')
