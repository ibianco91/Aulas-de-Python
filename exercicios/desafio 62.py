a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1

while c <= 10:
    a +=r
    c +=1
    print('{} -> ' .format(a-r), end='')

while c !=0:
    c = int(input(('\nDeseja continuar com quantos termos mais? ')))
    a += r
    c += 1
    print('{} -> '.format(a - r), end='')
