f = str(input('digite uma frase: ')).lower()
print('a letra A aparece {} vez na frase' .format(f.count('a')))
print('a letra A aparece na posição {}'.format(f.find('a')+1))