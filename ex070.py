op = pbarato = 'Ss'
c = 1
total = contmil = barato = 0
while op not in 'Nn':
    produto = int(input(f'{"=" * 40}\n'
                        f'{"LISTANDO AS COMPRAS" :^40}\n'
                        f'{"=" * 40}\n'
                        f'Qual o {c}º produto: '))
    preco = float(input(f'Valor do {c}º produto: R$'))
    barato = preco
    if preco > 1000.00:
        contmil += 1
    total += preco
    if barato > preco:
        barato = preco
        pbarato = produto
    c += 1
    op = str(input(f'{"~" * 40}\n'
                   f'Quer cadastrar mais alguma coisa [S/N]? '))
print(f'O total a ser pago é R${total :.2f}\n'
      f'{contmil} produtos custam mais de R$1000,00.\n'
      f'O produto mais barato listado é {pbarato} custando R${barato :.2f}')
