d=int(input('quantos dias alugados?'))
km=float(input('Kms rodados?'))
pago = (d*60)+(km*.15)
print('o total a pagar é de R${:.2f}' .format(pago))