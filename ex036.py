vcasa = float(input('Qual o valor da casa? R$'))
tempo = float(input('Em quanto anos você pretende pagar? '))
salario = float(input('Qual seu salario? R$'))
print(f'Para uma casa no valor de R${vcasa :.2f} as parcelas serão de R${(vcasa/ (tempo * 12)) :.2f}.')
if (vcasa / (tempo * 12)) <= (salario * 0.3):
    print('Emprestimo "Aprovado"!')
else:
    print('Emprestimo "Negado"!')
