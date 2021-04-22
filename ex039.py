from datetime import date
anonasc = int(input('Qual o ano de seu nascimento? '))
int(date.today().year)
idade = (int(date.today().year) - anonasc)
if idade > 30 or (anonasc > int(date.today().year)):
    print('ANO INVALIDO!')
else:
    if idade < 18:
        print(f'Você ainda tem {idade} anos de idade, falta(m) {18 - idade} ano(s) para vocẽ se alistar.\n'
              f'E seu alistamento sera em {int(date.today().year) + (18 - idade)}.')
    elif idade > 18:
        print(f'Vocẽ tem {idade} anos de idade, e deveria ter se alistado a {idade - 18} ano(s) atras.')
    elif idade == 18:
        print(f'Você tem exatamente {idade} anos, e deve se alistar imediatamente!')
