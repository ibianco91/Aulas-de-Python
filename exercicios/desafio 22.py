n = str(input('digite o nome: ')).strip() #.strip corta espaços antes e depois
print('o nome um letras maiusculas é: {}' .format(n.upper()))
print('o nome um letras minusculas é: {}' .format(n.lower()))
print('o nome tem {} letras' .format(len(n) - n.count(' ')))
print('o primeiro nome tem {} letras'.format(n.find('')))