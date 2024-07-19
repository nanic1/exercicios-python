def maiorMenor(x, y, z):
    maior = x
    menor = x

    if y > maior:
        maior = y
    if z > maior:
        maior = z
    
    if y < menor:
        menor = y
    if z < menor:
        menor = z

    print(f'Maior: {maior}')
    print(f'Menor: {menor}')

num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))

maiorMenor(num1, num2, num3)