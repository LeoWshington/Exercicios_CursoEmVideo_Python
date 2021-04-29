dis = float(input('Uma distancia em metros: '))
print(f'{dis / 1000 :<7}km\n{dis / 100 :<7}hm\n{dis / 10 :<6}dam\n{dis * 10 :<7.0f}dm\n{dis * 100 :<7.0f}cm\n{dis * 1000 :<7.0f}mm')
