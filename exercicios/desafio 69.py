c=1
maior = masc = fem = 0
i = int(input('Digite a idade'))
s = str(input('Digite o sexo [M/F]')).upper().strip()
if i > 18:
    maior += 1
if s == 'M':
    masc += 1
if i >20 and s == 'F':
    fem += 1
while True:
    i = int (input ('Digite a idade'))
    s = str (input ('Digite o sexo [M/F]')).upper ().strip ()
    c +=1
    if i > 18:
        maior += 1
    if s == 'M':
        masc += 1
    if i > 20 and s == 'F':
        fem += 1
    cont= str(input('Deseja continuar? [S/N]')).upper ().strip ()
    if cont == 'N':
        break
print(f'{maior} pessoas tem mais de 18 anos')
print(f'{masc} são homens')
print(f'{fem} são mulheres com mais de 20 anos')
