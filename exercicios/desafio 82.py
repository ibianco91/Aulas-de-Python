lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um número para por na lista: '))
    if n % 2 ==0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    resp = str(input('Deseja continuar? [S/N]')).lower()
    if resp == 'n':
            break

print(f'Os numeros pares são: {listapar}')
print(f'Os numeros impares são: {listaimpar}')
