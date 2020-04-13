import random
s = 0 #este é o valor inicial
a = random.randint(0,10) #este é um valor random que vai ser somado ao s, por meio da função s+= para ser somado a um valor s final
b = random.randint(0,10)
c = random.randint(0,10)
d = random.randint(0,10)
e = random.randint(0,10)
f = random.randint(0,10)

if a % 2 == 0:
    s+=a
if b % 2 == 0:
    s+=b
if c % 2 == 0:
    s+=c
if d % 2 == 0:
    s+=d
if e % 2 == 0:
    s+=e
if f % 2 == 0:
    s+=f

print(a, b, c, d, e, f)
print('a soma dos pares será {}' .format(s))



