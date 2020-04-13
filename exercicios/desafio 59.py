v1 = float(input('Digite o primeiro valor'))
v2 = float(input('Digite o segundo valor'))

o = int(input('Digite a operação desejada: \n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros \n[5] sair do programa'))

while o != 5:
    if o == 1:
        print('o valor da soma é {:.2}'.format(v1+v2))
    if o == 2:
        print('a multiplicação é igual a {:.2}'.format(v1*v2))
    if o == 3:
        if v1>v2:
            print('O maior valor é {}'.format(v1))
        if v1<v2:
            print ('O maior valor é {}'.format (v2))
        else:
            print('valores iguais')
    if o == 4:
        print('Digite novos valores:')
        v1 = float (input ('Digite o primeiro valor'))
        v2 = float (input ('Digite o segundo valor'))
print('programa terminado')
