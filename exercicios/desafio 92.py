import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['nasc'] = int(input('Digite o ano de nascimento: '))
pessoa['idade'] = datetime.datetime.now().year - pessoa['nasc']
pessoa['ctps'] = int(input('Carteira de trabalho (0 para não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['aposenta'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - datetime.datetime.now().year)
for k, v in pessoa.items():
    print(f'{k} tem o valor de {v}')
