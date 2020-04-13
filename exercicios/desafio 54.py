import datetime
import random

ano = int(datetime.datetime.now().year)

for pess in range (1, 8):
    nasc = random.randint(1990, ano)
    idade = ano - nasc
    print('A pessoa {} nasceu em {}, tem {} anos e é de '.format(pess, nasc, idade) ,end= '')
    if idade <=18:
        print('de menor')
    else:
        print('de maior')

