op = 'sS'
while op not in 'Nn':
    valor = int(input(f'{"=" * 40}\n'
                        f'{"CAIXA ELETRONICO - BANCO TABAJARA" :^40}\n'
                        f'{"=" * 40}\n'
                        f'Qual valor você deseja sacar: R$'))
    if valor >= 50:
        print(f'{valor // 50} nota(s) de R$50,00')
        valor = (valor - (valor // 50 * 50))
    if valor >= 20:
        print(f'{valor // 20} nota(s) de R$20,00')
        valor = valor - (valor // 20 * 20)
    if valor >=10:
        print(f'{valor // 10} nota(s) de R$10,00')
        valor = valor - (valor // 10 * 10)
    if valor >= 1:
        print(f'{valor // 1} nota(s) de R$1,00')
    op = str(input(f'{"~" * 40}\n'
                   f'Deseja sacar novamente? [S/N]? '))
print('Obrigado por usar nossos serviços!')
