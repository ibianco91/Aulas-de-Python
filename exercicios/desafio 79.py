lista =[]
while True:
    n = int(input('Digite um valor para adicionar na lista: '))
    if n not in lista:
            lista.append(n)
    else:
        print('Valor duplicado')
    resp = str(input('Deseja continuar? [S/N]')).lower()
    if resp == 'n':
            break

lista.sort()
print(lista)