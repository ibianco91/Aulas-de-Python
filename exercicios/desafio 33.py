a = float(input('digite o primeiro numero: '))
b = float(input('digite o segundo numero: '))
c = float(input('digite o terceiro numero: '))

if a > b and a > c:
    ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c
print('o maior numero é {}' .format(ma))
if a < b and a < c:
    me = a
if b < a and b < c:
    me = b
if c < a and c < b:
    me = c
print('o menor numero é {}' .format(me))