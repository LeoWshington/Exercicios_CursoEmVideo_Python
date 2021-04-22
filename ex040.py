n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota: '))
if ((n1 + n2) / 2) < 5:
    print(f'Sua média é {((n1 + n2) / 2)}.\nREPROVADO!')
elif 5 <= ((n1 + n2) / 2) <= 7:
    print(f'Sua média é {((n1 + n2) / 2) :.2f}\nRECUPERAÇÂO!')
elif ((n1 + n2) / 2) > 7:
    print(f'Sua média é {((n1 + n2) / 2) :.2f}\nAPROVADO!')
