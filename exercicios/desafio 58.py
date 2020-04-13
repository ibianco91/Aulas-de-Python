tentativas = 0
import random
n = int(random.randrange(0,5))
a = int(input('Adivinhe o numero '))
while a != n:
    a = int(input('Adivinhe o numero novamente '))
    tentativas +=1
print('Voce acertou, o numero pensado era {} e voce fez {} tentativas'.format(n,tentativas))
