cont = 's'
c=1
n = int(input('Digite um numero: '))
soma = maior = menor = n
while cont == 's':
    n = int(input('Digite um numero: '))
    cont = str(input('Quer continuar? [S/N]')).lower().strip()
    c +=1
    soma +=n
    if c ==1:
        maior=menor=n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
m=soma/c
print(f'a média é {m}')
print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')

