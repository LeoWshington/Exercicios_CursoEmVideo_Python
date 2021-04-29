nome = input('Digite seu nome completo: ').strip()
nomes = nome.split()
print(f'Analisando seu nome...\n'
      f'Seu nome em maiusculas é "{nome.upper()}"\n'
      f'Seu nome em minusculas é "{nome.lower()}"\n'
      f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras.\n'
      f'E seu primeiro nome é "{nomes[0]}" e tem {len(nomes[0])} letras.')
