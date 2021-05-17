import ex108
preco = float(input('Digite um preço: R$'))
print(f'A metade de R${ex108.moeda(preco)} é R${ex108.moeda(ex108.metade(preco))}\n'
      f'O dobro de R${ex108.moeda(preco)} é R${ex108.moeda(ex108.dobro(preco))}\n'
      f'Aumentando 30%, temos R${ex108.moeda(ex108.aumentar(preco, 30))}')
