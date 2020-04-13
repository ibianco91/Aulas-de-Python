from datetime import date
h = date.today().year
n = int(input('Em que ano nasceu?'))
i = h-n

if i <= 9:
    print('Sua categoria é mirim')
elif i <= 14:
    print('Sua categoria é junior')
elif i <= 20:
    print('Sua categoria é senior')
else:
    print('Sua categoria é master')