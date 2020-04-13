u=str(input('qual é a unidade?'))
t=float(input('qual é a temperatura?'))
if u=='c':
    print('a temperatura de {}C é igual a {:.3} F' .format(t, 9*t/5+32))
elif u=='f':
    print('a temperatura de {}F é igual a {:.2}C' .format(t, ((t-32)*5)/9))
else:
    print('digite c para celsius ou f para fahrenheit')