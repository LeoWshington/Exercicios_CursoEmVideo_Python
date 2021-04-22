nome = str(input('Digite seu nome: ')).strip().split()
print(f'Muito prazer em te conhecer!\n'
      f'Seu primeiro nome é {nome[0]}.\n'
      f'Seu ultimo nome é {nome[len(nome) - 1]}.')
