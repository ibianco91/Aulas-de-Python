q = int(input('quantos elementos quer da sequencia de fibonacci? '))
t1 = 0
t2 = 1
t3=t2
c = 0
while c <= q:
    print('{} -> '.format(t3),end='')
    c +=1
    t3 = t2 +t1
    t1 = t2
    t2 = t3
print('FIM')