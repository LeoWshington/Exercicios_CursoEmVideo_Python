def fatorial(n, show=False):
    """
    => Calcula o fatorial de um numero
    :param n: numero a ser calculado
    :param show: mostrar ou não o calculo
    :return: o valor do fatorial do numero passado
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
print(fatorial(5))
help(fatorial)
