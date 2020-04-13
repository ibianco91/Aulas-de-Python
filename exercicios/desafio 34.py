s = float(input('qual o seu salario? \nR$'))
if s> 1250:
    print('o seu salario passara a ser R${:.2f}'.format(s+(s*10/100)))
else:
    print('o seu salario passara a ser R${:.2f}'.format(s + (s * 15 / 100)))
