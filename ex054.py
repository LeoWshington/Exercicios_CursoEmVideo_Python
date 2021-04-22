from datetime import date
ano = date.today().year
contmenor = 0
contmaior = 0
for c in range(1, 8):
    anonasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if 1880 < anonasc <= ano:
        if ano - anonasc < 18:
            contmenor += 1
        else:
            contmaior += 1
print(f'Das 7 pessoas digitadas:\n'
      f'{contmaior} é/são maior(es) de idade.\n'
      f'{contmenor} é/são menor(es) de idade.')
