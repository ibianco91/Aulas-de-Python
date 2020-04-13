s = str(input('Digite o seu sexo [M/F]')).upper()[0]
while s not in 'MF':
    s= str(input('dado invalido, informe o seu sexo [M/F]')).upper()
print('sexo {}'.format(s))