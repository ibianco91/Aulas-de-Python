lista = []
for cont in range (1, 6):
    lista.append(int(input(f'Digite o {cont}º para adicionar na lista')))
lista.sort()
print(lista)