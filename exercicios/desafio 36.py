v = float(input('Qual é o valor da casa? \n'))
s = float(input('Qual é o seu salário? \n'))
a = float(input('Vai pagar em quantos anos? \n'))
p = v/(a*12)
if p < (s+s*.3):
    print('a prestação será de R${:.2f}' .format(p))
else:
    print('Emprestimo negado')