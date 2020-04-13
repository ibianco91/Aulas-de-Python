lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N]')).lower()
    if resp == 'n':
        break
print(f'foram digitados {len(lista)} números na lista')
lista.sort()
print(f'A lista em ordem crescente: {lista}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 esta na lista')
else:
    print('O número 5 nao esta na lista')

