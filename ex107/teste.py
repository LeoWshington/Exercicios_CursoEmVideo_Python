import moeda
preco = float(input('Digite um preço: R$'))
print(f'A metade de R${preco :.2f} é R${moeda.metade(preco) :.2f}\n'
      f'O dobro de R${preco :.2f} é R${moeda.dobro(preco) :.2f}\n'
      f'Aumentando 30%, temos R${moeda.aumentar(preco, 30) :.2f}')
