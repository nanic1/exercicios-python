def fOuM(a):
    if a in 'Ff':
        print('Feminino')
    elif a in 'Mm':
        print('Masculino')
    elif a not in 'FfMm':
        print('Sexo invalido')

sexo = str(input('Sexo: '))
fOuM(sexo)