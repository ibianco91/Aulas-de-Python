lista = []

for cont in range(0, 5):
    lista.append(int(input(f'digite um valor para a posição {cont}')))
print(f'A lista digitada foi {lista}')
print(f'O maior valor é {max(lista)} e esta na posição',end=' ')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f'{pos}')
print(f'O menor valor é {min(lista)} e esta na posição', end=' ')
for p, v in enumerate(lista):
    if v == min(lista):
        print(f'{pos}')


