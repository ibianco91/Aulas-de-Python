import random
import time

print ('\033[34m-=' * 10)
print ('\033[31mJOKENPÔ')
print ('\033[34m-=\033[m' * 10)
print ('\033[35mOlá caro desafiante. Bem vindo ao JOKENPÔ!')
print ('''As regras são as seguintes:
\033[30mEscolha entre pedra, papel e tesoura e tente me vencer\033[m!
\033[33mLEMBRE-SE:\033[m papel vence pedra, pedra vence tesoura, e tesoura vence papel!
\033[32mBOA SORTE\033[m!!''')
a = int (input ('\033[30mEscolha entre pedra(0), papel(1) ou tesoura(2)\033[m: '))
y = ('pedra', 'papel', 'tesoura')
x = random.randint (0, 2)
print ('\033[33mOK, vamos jogar\033[m!')
time.sleep (2)
print ('\033[36mJO')
time.sleep (1)
print ('\033[35mKEN')
time.sleep (1)
print ('\033[34mPÔ')
print ('\033[31mEu escolhi {} e você escolheu {}\033[m'.format (y[x], y[a]))
time.sleep (2)
if x == 0:
    if a == 1:
        print ('Droga, você ganhou!')
    if a == 2:
        print ('HAHA\nEu ganhei!')
if x == 1:
    if a == 2:
        print ('Droga, você ganhou!')
    if a == 0:
        print ('HAHA\nEu ganhei!')
if x == 2:
    if a == 0:
        print ('Droga, você ganhou!')
    if a == 1:
        print ('HAHA\nEu ganhei!')
if x == a:
    print ('Nossa! \n Nós empatamos!')﻿