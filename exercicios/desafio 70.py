p = q = caro = barato = total = 0
barato = ''
while True:
    n = str(input('Digite o nome do produto: ')).upper().strip()
    p = int(input('Digite o preço: R$'))
    total += p
    barato = n
    if p > 1000:
        caro += 1
    z = str(input('Deseja continuar? [S/N]')).upper().strip()
    if q == 1:
        barato = n
    if z == 'N':
        break
print(f'o total gasto na compra foi de R${total}')
print(f'{caro} produtos custam mais que R$ 1000.00')
print(f'o produto mais barato é {barato}')
