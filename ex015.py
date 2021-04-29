dias = int(input('Quantos dias  ficou alugado? '))
km = float(input('Quantos quilometros rodou? '))
print(f'Tendo ficado alugado por {dias} dias e percorrido {km}km, O preço a se pagar é de'
      f'R${(dias * 60) + (km * 0.15) :.2f}.')
