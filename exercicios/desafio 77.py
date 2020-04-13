palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','MUITO','DIVERTIDO','PRATICAR','EXERCICIOS','AJUDA','COMPREENDER','MELHOR','MATERIA','FUTURO')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end =' ')