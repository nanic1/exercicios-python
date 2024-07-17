def boletim(x, y):
    media = (x + y) / 2
    if media == 100:
        print('Aprovado com distinção.')
    elif media >= 70:
        print('Aprovado.')
    else:
        print('Reprovado.')

print('Digite sua notas abaixo. (0 a 100)')
while True:
    nota1 = int(input('Nota 1: '))
    if nota1 < 0 or nota1 > 100:
        print('Digite uma nota válida!')
    else:
        break

while True:
    nota2 = int(input('Nota 2: '))
    if nota2 < 0 or nota2 > 100:
        print('Digite uma nota válida!')
    else:
        break

boletim(nota1, nota2)