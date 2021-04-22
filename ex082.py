valores = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    op = str(input('Deseja continuar [S/N]? ')).strip()[0]
    if op in 'Nn':
        break
    print(f'{"~" * 30}')
print(f'A lista digitada foi: {valores}\n'
      f'A lista de numeros pares da lista a cima é: {par}\n'
      f'E a lista de numeros impares é: {impar}')
