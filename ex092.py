from datetime import date
dados = {'nome': str(input('Nome: ')).strip(),
         'idade': int(input('Ano de nascimento: ')),
         'ctps': int(input('Carteira de trabalho (0 não tem): '))}
print('=' * 35)
dados['idade'] = date.today().year - dados['idade']
if dados['ctps'] == 0:
    print(f'  - nome tem o valor {dados["nome"]}\n  - idade tem o valor {dados["idade"]}\n'
          f'  - ctps tem o valor {dados["ctps"]}')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salario: R$'))
dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
for v, c in dados.items():
    print(f'  - {v} tem o valor {c}')
