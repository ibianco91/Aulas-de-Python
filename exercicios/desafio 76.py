lista = ('Caderno', 25.60, 'Lápis', 0.50, 'Caneta', 1.50, 'Borracha', 2.40,
            'Tesoura', 3.50, 'Cola', 2.50, 'Corretivo', 4.20,
            'Apontador', 1.50, 'Bolsa', 135.90)
for pos in range(0, len(lista)):
    if pos %2==0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
