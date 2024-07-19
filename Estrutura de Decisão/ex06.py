def maior(x, y, z):
    if x > y and x > z:
        print(f'Maior: {x}')
    elif y > x and y > z:
        print(f'Maior: {y}')
    elif z > x and z > y:
        print(f'Maior: {z}')
    else:
        print('Todos são iguais.')
    
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))

maior(num1, num2, num3)
