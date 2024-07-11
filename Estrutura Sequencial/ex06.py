PI = 3.14

def area(x):
    global PI
    a = PI * (x ** 2)
    return a

raio = float(input("Digite o raio do circulo: "))
print(f'A area do circulo de raio {raio} é {area(raio)}')