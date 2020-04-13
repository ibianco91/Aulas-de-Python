import random
n = int(random.randrange(0,5))
a = int(input('Adivinhe o numero '))
if a==n:
    print('voce acertou, o numero é {}' .format(n))
else:
    print ('voce errou, o numero era {}' .format(n))