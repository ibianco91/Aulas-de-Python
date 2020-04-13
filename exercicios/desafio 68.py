import random
b=0
pc = random.randint(0,6)
e = int(input('Digite [1] para impar ou [2] para par'))
n = int(input('Digite um valor de 0 a 5'))
v=n+pc
print(pc)

while True:
    if e == 1:
        if v % 2 != 0:
            print('Você ganhou')
            pc = random.randint (0, 6)
            e = int (input ('Digite [1] para impar ou [2] para par'))
            n = int (input ('Digite um valor de 0 a 5'))
            v = n + pc
            print (pc)
        else:
            print('Você perdeu')
            b = 1

    if e == 2:
        if v % 2 == 0:
            print('Você ganhou')
            pc = random.randint (0, 6)
            e = int (input ('Digite [1] para impar ou [2] para par'))
            n = int (input ('Digite um valor de 0 a 5'))
            v = n + pc
            print (pc)
        else:
            print('Você perdeu')
            b = 1
    if b == 1:
        break
