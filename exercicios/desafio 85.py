cont = 1
pares=list()
impares = list()
for c in range(0,7):
    n = int(input(f'numero {cont}: '))
    cont+=1
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'os numeros pares sao: {pares}')
print(f'os numeros impares sao: {impares}')

