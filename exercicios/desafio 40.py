n1 = float(input('digite a primeira nota'))
n2 = float(input('digite a segunda nota'))
m = (n1+n2)/2
if m < 5:
    print('sua média foi {:.1f} e voce esta reprovado'.format(m))
elif m >= 7:
        print('sua média foi {:.1f} e voce esta aprovado'.format(m))
else:
            print('sua média foi {:.1f} e voce esta de recuperação'.format(m))