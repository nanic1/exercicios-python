def vogalOuConsoante(a):
    if a in 'AEIOUaeiou':
        print('Vogal.')
    else:
        print('Consoante.')


while True:
    letra = str(input('Letra: '))
    if len(letra) > 1:
        print('Digite apenas uma letra.')
    else:
        break

vogalOuConsoante(letra)