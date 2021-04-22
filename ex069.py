op = 'Ss'
c = 1
conth = contma = contmu =0
while op not in 'Nn':
    idade = int(input(f'{"=" * 40}\n'
                      f'{"CADASTRO DE PESSOAS" :^40}\n'
                      f'{"=" * 40}\n'
                      f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}ª pessoa [M/F]: ')).strip()[0]
    if idade >= 18:
        contma += 1
    elif sexo in 'Ff' and idade < 20:
        contmu += 1
    elif sexo in 'Hh':
        conth += 1
    c += 1
    op = str(input(f'{"~" * 40}\n'
                   f'Quer cadastrar mais pessoas[S/N]? '))
print(f'Foram cadastradas {contma} passoas com mais de 18 anos.\n'
      f'Foram cadastrados {conth} Homem(ens).\n'
      f'E {contmu} mulher têm menos de 20 anos.')
