pessoa = dict()
galera = list()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('erro')
    pessoa['idade']=int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?')).upper()[0]
        if resp in 'SN':
            break
    print('erro')
    if resp == 'N':
        break
print(f'tem {len(galera)} pessoas cadastradas')
media = soma/len(galera)
print(f'a media é de {media: 5.2f} anos')
print(f'as mulheres cadastradas foram ', end ='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print('pessoas acima da media: ', end='')
for p in galera:
    if p['idade']>=media:
        print('')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()