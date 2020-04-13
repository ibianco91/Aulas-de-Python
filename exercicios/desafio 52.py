num = int(input('Digite um numero: '))
tot = 0
print('{} é divisivel por: ' .format(num))
for c in range(1, num):
    if num % c == 0:
                print('{}' .format(c, num), end=', ')
                tot += 1
if tot > 2:
    print('numero não é primo')
else:
    print('O numero escolhido é primo')