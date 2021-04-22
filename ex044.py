preco = float(input('Qual o preço do produto? R$ '))
op = int(input('''Qual Forma de Pagamento Você Prefere:
1 - À vista dinheiro ou cheque.
2 - À vista no cartão.
3 - Em até 2x no cartão.
4 - 3x ou mais no cartão.\n'''))
if op == 1:
    print(f'O valor a ser pago é R${(preco * 0.9) :.2f}')
elif op == 2:
    print(f'O valor a ser pago é R${(preco * 0.95) :.2f}')
elif op == 3:
    print(f'O valor a ser pago são duas parcelas de R${(preco / 2) :.2f}')
elif op == 4:
    x = int(input('Em quantas vezes gostaria de pagar (3 - 10x)? '))
    if x == 3:
        print(f'O valor a ser pago são 3 parcelas de R${(preco * 1.2) / 3 :.2f} num total de R${preco * 1.2 :.2f}')
    elif 3 < x <= 10:
        print(f'O valor a ser pago serão {x} parcelas de R${(preco * 1.2) / x :.2f} num total de R${preco * 1.2 :.2f}')
    else:
        print('\033[1:31mOpção invalida!')
else:
    print('\033[1:31mOpção invalida!\033[m')
