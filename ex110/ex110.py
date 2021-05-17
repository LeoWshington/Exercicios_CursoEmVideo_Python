def resumo(valor, aumento=0, deducao=0):
    print(f'{"-" * 35}\n'
          f'{"RESUMO DO VALOR" :^35}\n'
          f'{"-" * 35}\n')
    print(f'Preço analisado:\t{moeda(valor)}\n'
          f'Dobro do preço: \t{moeda(dobro(valor))}\n'
          f'Metade do preço:\t{moeda(metade(valor))}\n'
          f'80% de aumento: \t{moeda(aumentar(valor, aumento))}\n'
          f'35% de aumento: \t{moeda(diminuir(valor, deducao))}')


def moeda(valor):
    return f'R${valor :>.2f}'.replace('.', ',')


def aumentar(valor, taxa=0, formato=False):
    resposta = valor * (1 + (taxa / 100))
    return resposta if formato is False else moeda(resposta)


def diminuir(valor, taxa=0, formato=False):
    resposta = valor * (1 - (taxa / 100))
    return resposta if formato is False else moeda(resposta)


def dobro(valor, formato=False):
    resposta = valor * 2
    return resposta if formato is False else moeda(resposta)


def metade(valor, formato=False):
    resposta = valor * 0.5
    return resposta if not formato else moeda(resposta)
