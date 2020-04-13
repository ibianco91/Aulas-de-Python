import random

maior = 0
menor = 0

for pess in range (1, 6):
    peso = float(random.randint(1, 200))
    print ('a pessoa {} pesa {} kg' .format(pess, peso))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('o maior peso é {} e o menor é {}' .format(maior, menor))
