def barato(x, y, z):
    baratoz = x

    if y < baratoz:
        baratoz = y
    if z < baratoz:
        baratoz = z

    print(f'Produto mais barato: {baratoz:.2f}')

prod1 = float(input('Produto 1: '))
prod2 = float(input('Produto 2: '))
prod3 = float(input('Produto 3: '))

barato(prod1, prod2, prod3)