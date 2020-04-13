n = int(input('Digite um número: '))
c=1
s=n
while True:
    n = int (input ('Digite um número ou 999 para parar: '))
    if n ==999:
        break
    c+=1
    s+=n

print(f'foram digitados {c} números e a soma deles é {s}')
