def decrescente(x, y, z):
    if x >= y and x >= z:
        maior = x
        if y >= z:
            medio = y
            menor = z
        else:
            medio = z
            menor = y

    elif y >= x and y >= z:
        maior = y
        if x >= z:
            medio = x
            menor = z
        else:
            medio = z
            menor = x

    else:
        maior = z
        if x >= y:
            medio = x
            menor = y
        else:
            medio = y
            menor = x

    print(f'{maior}, {medio} e {menor}')

num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))

decrescente(num1, num2, num3)