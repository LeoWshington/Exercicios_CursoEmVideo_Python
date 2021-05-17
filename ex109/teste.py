from ex109 import moeda, metade, dobro, aumentar
preco = float(input('Digite um preço: R$'))
print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}\n'
      f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}\n'
      f'Aumentando 10%, temos {moeda(aumentar(preco))}')
