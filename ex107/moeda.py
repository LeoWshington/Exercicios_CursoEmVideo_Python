def aumentar(valor, taxa=0):
    resposta = valor * (1 + (taxa / 100))
    return resposta


def diminuir(valor, taxa=0):
    return valor * (1 - (taxa / 100))


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor * 0.5
