def fatorial(n, show=False):
    """
    Calcula o fatorial de um numero com a opção de se exibir ou não o processo
    :param n: numero a ser calculado o fatorial
    :param show: True para exibir o processo
    :return: f
    """
    f = 1
    if show:
        for valor in range(n, 0, -1):
            print(f'{valor} ', end='')
            f *= valor
        print('= ', end='')
    else:
        for valor in range(n, 0, -1):
            f *= valor
    return f


print(fatorial(5, ))
