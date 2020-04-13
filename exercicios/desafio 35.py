l1 = float(input('digite o primeiro lado: '))
l2 = float(input('digite o segundo lado: '))
l3 = float(input('digite o terceiro lado: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('é possível fazer um triangulo')
else:
    print('nao é possivel fazer um triangulo')

