def leiaDinheiro(valor):
    valor = input(f'{valor}').strip()
    while True:
        if valor.isnumeric():
            valor = float(valor)
            break
        elif len(valor) >= 4 and (valor[(len(valor) - 2)] in ',.' or valor[(len(valor) - 3)] in ',.'):
            mudado = str(valor).replace(',', '.')
            valor = float(mudado)
            break
        else:
            valor = input(f'\033[1;31mERRO! "{valor}" não é um preço validado!\033[m\nDigite o preço: ').strip()
    return valor
