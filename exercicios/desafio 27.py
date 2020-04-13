n = str(input('digite seu nome completo')).strip()
n1 = n.split()
print('seu primeiro nome é {}'.format(n1[0]))
print('seu ultimo nome é {}' .format(n1[len(n1)-1]))