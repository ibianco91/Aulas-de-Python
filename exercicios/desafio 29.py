v = float(input('digite a velocidade do carro: '))
m = 7 *( v-80)
if v<=80:
    print('sem multas')
else:
    print('a muta sera de R${}' .format(m))