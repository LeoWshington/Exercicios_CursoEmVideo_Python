frase = str(input('Digite a frase: ')).strip().upper()
frase2 = ''.join(frase.split())
frase3 = frase2[len(frase2)::-1]
if frase2 == frase3:
    print(f'A frase "{frase.title()}" é um palindromo.')
else:
    print(f'A frase "{frase.title()}" não é um palindromo.')
