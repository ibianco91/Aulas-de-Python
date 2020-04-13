l1 = float(input('digite o primeiro lado: '))
l2 = float(input('digite o segundo lado: '))
l3 = float(input('digite o terceiro lado: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print ('é possível fazer um triangulo', end=' ')
    if l1 == l2 == l3:
        print ('equilatero')
    elif l1 != l2 != l3:
        print ('escaleno')
    else:
        print ('isosceles')
else:
    print('nao é possivel fazer um triangulo')


