from datetime import date
h = date.today().year
n = int(input('Em que ano nasceu?'))
i = h - n

if i < 18:
    print('voce deve se alistar em {} anos' .format(18-i))
elif i > 18:
    print('ja passou {} anos para ter se alistado' .format(i-18))
else:
    print('é hora de se alistar')
