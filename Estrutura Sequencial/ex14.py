peso = float(input('Peso (kg): '))
excesso = peso - 50

if peso > 50:
    print(f'Foi cobrado uma multa de R${excesso * 4:.2f} pois o peso do quilo do peixe passou de 50 quilos')
else:
    print(f'Gravado no sistema os {peso} quilos de peixe.')