jogador = dict()
jogo = list()
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Número de partidas'] = int(input('Número de partidas jogadas: '))
for c in range(0, jogador['Número de partidas']):
    jogo.append(int(input(f'Gols na partida {c+1}: ')))
jogador['gols'] = jogo[:]
jogador['total'] = sum(jogo)

for i, v in enumerate(jogador['gols']):
    print(f'na partida {i+1}, fez {v} gols')
print(f'total de {jogador["total"]} gols')