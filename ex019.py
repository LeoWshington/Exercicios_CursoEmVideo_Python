from random import choice
pri = input('Digite o nome do primeiro aluno: ')
seg = input('Digite o nome do segundo aluno: ')
ter = input('Digite o nome do terceiro aluno: ')
qua = input('Digite o nome do quarto aluno: ')
lista = [pri, seg, ter, qua]
print(f'O aluno sortiado foi: "{choice(lista)}"')
