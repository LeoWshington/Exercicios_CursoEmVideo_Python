frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes na frase.\n'
      f'A primeira letra "A" aparece na posição {frase.find("A") + 1}.\n'
      f'E a ultima letra "A" aparece na posição {frase.rfind("A") + 1}.')
