ficha = list()

while True:
    n = str(input('Digite o nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input ('Nota 2: '))
    media=(n1+n2)/2
    ficha.append([n, [n1, n2], media])
    resp = str(input('Deseja adicionar outro aluno? [S/N]')).lower()
    if resp =='n':
        break
for i, a in enumerate(ficha):
    opc = int(input('nota de qual aluno?'))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')



