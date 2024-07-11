celsius = float(input("Temperatura em celsius atual: "))

def conversorF(x):
    farenheit = (x * 9 / 5) + 32
    return farenheit

print(f'Fahrenheit: {conversorF(celsius)}')