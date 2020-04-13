dado = list()
lista = list()
resp = 0
quant=0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append(dado[:])
    dado.clear()
    resp=str(input('Quer adicionar outra pessoa?')).lower()
    quant+=1
    if resp == 'n':
        break

print(f'Foram cadastradas {quant} pessoas')
print(f'o mais leve pesa {min(lista)}')
print(f'o mais pesado pesa {max(lista)}')