aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] <7:
    aluno['situação'] = 'Reprovado'
else:
        aluno['situação'] = 'Aprovado'


for k, v in aluno.items():
    print(f'{k} é {v}')
