from random import shuffle
pri = input('Digite o nome do primeiro aluno: ')
seg = input('Digite o nome do segundo aluno: ')
ter = input('Digite o nome do terceiro aluno: ')
qua = input('Digite o nome do quarto aluno: ')
lista = [pri, seg, ter, qua]
shuffle(lista)
print(f'A ordem de apresentação será:\n{lista}')
