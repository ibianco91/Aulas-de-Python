d = float(input('Qual a distancia da viagem? \n'))
if d<=200:
    p = 0.5*d
else:
    p = 0.45*d
print('a passagem custara R${:.2f}' .format(p))