from datetime import date
anonasc = int(input('Qual o ano de nascimento? '))
if (int(date.today().year) - anonasc) <= 9:
    print(f'O atleta tem {(int(date.today().year) - anonasc)} anos de idade, por tanto sua classificação é MIRIM!')
elif 9 < (int(date.today().year) - anonasc) <= 14:
    print(f'O atleta tem {(int(date.today().year) - anonasc)} anos de idade, por tanto sua classificação é INFANTIL!')
elif 14 < (int(date.today().year) - anonasc) <= 19:
    print(f'O atleta tem {(int(date.today().year) - anonasc)} anos de idade , por tanto sua classificação é JÚNIOR!')
elif 19 < (int(date.today().year) - anonasc) <= 25:
    print(f'O atleta tem {(int(date.today().year) - anonasc)} anos de idade, por tanto sua classificação é SÊNIOR!')
elif (int(date.today().year) - anonasc) > 25:
    print(f'O atleta tem {(int(date.today().year) - anonasc)} anos de idade, por tanto sua classificação é MASTER!')
