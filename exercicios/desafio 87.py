matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l}, {c}: '))
print('-=' *10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end = '')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*10)
print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
if spar > 0:
    print(f'A soma dos pares é {spar}')
else:
    print(f'Não tem números pares nesta matriz.')
print(f'O maior valor da segunda linha é {max(matriz[1])}')﻿