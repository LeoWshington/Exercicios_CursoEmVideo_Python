def aumentar(valor=0, taxa=0):
    resposta = valor * (1 + (taxa / 100))
    return resposta


def diminuir(valor=0, taxa=0):
    return valor * (1 - (taxa / 100))


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor * 0.5




def moeda(valor):
    return f'{valor :>.2f}'.replace('.', ',')
