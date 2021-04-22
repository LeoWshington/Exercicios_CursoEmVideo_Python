peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
if (peso / altura ** 2) < 18.5:
    print(f'Seu IMC atual é {(peso / altura ** 2) :.2f}.\n'
          f'Você esta abaixo do peso! REDOBRE A ATENÇÃO!')
elif 18.5 <= (peso / altura ** 2) <= 25:
    print(f'Seu IMC atual é {(peso / altura ** 2) :.2f}.\n'
          f'Você esta na faixa de peso ideal!')
elif 25 < (peso / altura ** 2) <= 30:
    print(f'Seu IMC atual é {(peso / altura ** 2) :.2f}.\n'
          f'Você esta na faixa de sobre peso. TENTE MELHORAR SUA ALIMENTAÇÃO!')
elif 30 < (peso / altura ** 2) <= 40:
    print(f'Seum IMC atual é {(peso / altura ** 2) :.2f}.\n'
          f'Você esta na faixa de obesidade. MUITO CUIDADO!')
elif (peso / altura ** 2) > 40:
    print(f'Seu IMC atual é {(peso / altura ** 2) :.2f}.\n'
          f'Você esta na faixa de obesidade morbida. PROCURE AJUDA MÉDICA IMEDIATAMENTE!')
