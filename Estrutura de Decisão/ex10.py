while True:
    turno = str(input('Digite o turno que estuda (M/T/N): '))
    if turno in "MmTtNn":
        break
    elif len(turno) > 1:
        print('Digite uma resposta válida')
    else:
        print("Resposta inválida.")

if turno in 'Mm':
    print('Bom dia!')
elif turno in 'Tt':
    print('Boa tarde!')
elif turno in 'Nn':
    print('Boa noite!')

