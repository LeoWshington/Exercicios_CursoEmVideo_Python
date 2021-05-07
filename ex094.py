dados = dict()
lista_pessoas = list()
lista_mulheres = list()
idade_maior = list()
op = 's'
soma_idade = 0
while op in 'Ss':
    dados['nome'] = str(input('Nome: ')).strip()
    dados['idade'] = int(input('Idade: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().lower()[0]
    while dados['sexo'] not in 'FfMm':
        dados['sexo'] = str(input('ERRO! Por favor digite apenas M ou F\nSexo [M/F]: ')).strip().lower()[0]
    lista_pessoas.append(dados.copy())
    soma_idade += dados['idade']
    if dados['sexo'] in 'Ff':
        lista_mulheres.append(dados.copy())
    op = str(input('Quer continuar [S/N]? ')).strip()[0]
    while op not in 'NnSs':
        op = str(input('ERRO! Por favor digite apenas S ou N\nQuer continuar [S/N]? ')).strip()[0]
    print('-' * 40)
print(f'A) Ao todo foram cadastradas {len(lista_pessoas)} pessoas.\n'
      f'B) A média da idade das pessoas cadastradas é {soma_idade / len(lista_pessoas) :.1f}\n'
      f'C) A lista de mulheres cadastradas é: ', end='')
for c in range(0, len(lista_mulheres)):
    print(f'{lista_mulheres[c]["nome"]} ', end='')
for c in range(0, len(lista_pessoas)):
    if lista_pessoas[c]['idade'] > (soma_idade / len(lista_pessoas)):
        idade_maior.append(lista_pessoas[c].copy())
print(f'\nD) A lista de pessoas a cima da média de idade que é {soma_idade / len(lista_pessoas) :.1f}:')
for c in range(0, len(idade_maior)):
    print(f'{idade_maior[c]["nome"]} com {idade_maior[c]["idade"]} anos')
print('<< ENCERRADO >>')
