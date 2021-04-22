expressao = str(input('Digite a expressão: ')).strip().lower()
conta = expressao.count('(')
contf = expressao.count(')')
if conta == contf:
    print('A expressão está correta.')
else:
    print('A expressão está errada.')
