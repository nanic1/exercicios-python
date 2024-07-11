def pesoIdealH(x):
    calculo = (72.7 * x) - 58
    return calculo

def pesoIdealM(y):
    calculo = (62.1 * y) - 44.7
    return calculo

altura = int(input('Digite sua altura em cm: '))
alturaM = altura / 100
while True:
    opcao = str(input('Voce é homem ou mulher? (H/M): '))
    if opcao in 'HhMm':
        break
    else:
        print('ERRO. Opção invalida.')

if opcao in 'Hh':
    print(f'Peso ideal: {pesoIdealH(alturaM):.2f}')
if opcao in 'Mm':
    print(f'Peso ideal: {pesoIdealM(alturaM):.2f}')