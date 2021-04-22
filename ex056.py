sidade = 0
hidade = 0
conth = 0
contm = 0
nomeh = ''
for c in range(1, 5):
    nome = str(input(f'=-=-=-=-=- DADOS {c}ª PESSOA -=-=-=-=-='
                     f'Digite o nome da pessoa: ')).lower().strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa:  ')).lower().strip()
    if sexo == "m":
        conth += 1
        if conth == 1:
            hidade = idade
            nomeh = nome
        else:
            if hidade < idade:
                hidade = idade
                nomeh = nome
    if sexo == "f" and idade < 20:
        contm += 1
    sidade += idade
print(f'A média de idade do grupo é {(sidade / 4) :.0f}.\n'
      f'O homem mais velho do grupo é {nomeh} com {hidade} anos.\n'
      f'O numero de mulheres com menos de 20 anos é {contm}.')
