p = float(input('digite o preço normal'))
o = int(input('Digite\n [1] para dinheiro ou cheque\n [2] para a vista\n [3] em 2x\n [4] em 3x '))

if o == 1:
    print('o preço com desconto será de R${:.2f}' .format(p-p*.1))
elif o == 2:
    print ('o preço com desconto será de R${:.2f}' .format (pp*.05))
elif o == 3:
    print ('o preço  será de R${:.2f}' .format (p))
elif o == 4:
    print ('o preço com desconto será de R${:.2f}' .format (p+p*.2))
else:
    print('forma de pagamento invalida')
