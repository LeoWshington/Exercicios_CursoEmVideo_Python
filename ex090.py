situacao_aluno = {'nome': str(input('Nome do aluno: ')).strip()}
while True:
    situacao_aluno['media'] = float(input(f'Media de {situacao_aluno["nome"].title()}: '))
    if situacao_aluno['media'] < 0.0 or situacao_aluno['media'] > 10.0:
        print('Opção invalida!\nDigite a ', end='')
    else:
        break
print('≃' * 30)
print(f'    - nome = {situacao_aluno["nome"].title()}\n'
      f'    - média = {situacao_aluno["media"]}\n'
      f'    - situação = ', end='')
if 7.0 <= situacao_aluno['media'] <= 10.0:
    print('Aprovado!')
elif 0 <= situacao_aluno['media'] <= 5.0:
    print('Reprovado!')
elif 5 < situacao_aluno['media'] < 7:
    print('Em Recuperação!')
