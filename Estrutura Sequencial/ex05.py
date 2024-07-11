def conversor (x):
    cm = x * 100
    return cm

metros = float(input("Digite um valor em metros: "))
print(f'O valor em centimetros é {conversor(metros)}cm')