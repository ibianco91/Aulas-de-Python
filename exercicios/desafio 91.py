from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
rank = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]}')
