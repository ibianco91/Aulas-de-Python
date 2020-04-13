n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
n4 = int(input('Digite outro valor: '))
t=(n1,n2,n3,n4)

print(f'Voce digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes ')
if 3 in t:
    print(f'O primeiro valor 3 apareceu na posição {t.index(3)+1}')
else:
    print('o valor 3 não foi digitado')
print('Os valores pares são:')
for n in t:
    if n%2==0:
        print(n)
print(n)