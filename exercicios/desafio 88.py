from random import randint
lista = list()
jogo = list()
jogos = int(input('Quantos jogos voce quer? '))
for j in range(0, jogos):
        for c in range(0, 6):
            n = randint(0, 60)
            if n not in lista:
                lista.append(n)
        lista.sort()
        jogo.append(lista[:])
        lista.clear()

print(jogo)