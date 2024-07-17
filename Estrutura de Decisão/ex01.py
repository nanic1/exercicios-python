def maior(x, y):
    if x > y:
        print(f'{x} é maior do que {y}')
    elif y > x:
        print(f'{y} é maior do que {x}')
    else:
        print(f'{x} é igual a {y}')


num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
maior(num1, num2)