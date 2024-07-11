import math
areaPinto = float(input('Area a ser pintada: '))

litrosTinta = math.ceil(areaPinto / 3)
latasTinta = math.ceil(litrosTinta / 18)
precoTotal = latasTinta * 80

print(f'Latas necessárias: {latasTinta}')
print(f'Preço total: R${precoTotal}')