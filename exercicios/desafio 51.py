a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for c in range (a, a+10*r, r):
    print('{}'.format(c), end='->')
print('fim')

