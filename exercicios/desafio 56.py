soma = 0
velho = 0
novo = 0
for p in range (1, 3):
    print('pessoa {}' .format(p))
    n = str(input('Digite o nome: ')).strip()
    i = int(input('Digite a idade: '))
    s = str(input('Digite [M] para masculino e [F] para feminino')).strip()
    soma+=i
    media = soma/2
    if p == 1:
        velho = i
        nvelho = n
        novo = i
    if i > velho:
            velho = i
    if i < novo:
            novo = i

print('A média das idades é de {}' .format(media))
print('O homem mais velho tem {} ano(s) e se chama {}'.format(i,n))