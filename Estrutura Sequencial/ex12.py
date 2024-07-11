altura = int(input('Digite sua altura em cm: '))
alturaM = altura / 100

def pesoIdeal(x):
    calculo = (72.7 * x) - 58
    return calculo

print(f'Seu peso ideal seria {pesoIdeal(alturaM):.2f}')