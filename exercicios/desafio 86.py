matriz = [[], [], []]
for i in range(1,4):
    for j in range(1,4):
        matriz[i-1].append(int(input(f'Digite o valor para a posição {i,j}: ')))
print('=='*20)
for a in range(len(matriz)):
    for b in range(len(matriz)):
        print(f'[{matriz[a][b]}]', end=' ')
    print()﻿