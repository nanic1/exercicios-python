inteiro1 = int(input('Digite um numero inteiro: '))
inteiro2 = int(input('Digite outro numero inteiro: '))
real = float(input('Digite um numero real: '))

def exA(x, y, z):
    a = (x * 2) * (y / 2)
    return a

def exB(x, y, z):
    b = (x * 3) + z
    return b

def exC(x, y, z):
    c = z ** 3
    return c

print(f'a) {exA(inteiro1, inteiro2, real)}\nb) {exB(inteiro1, inteiro2, real)}\nc) {exC(inteiro1, inteiro2, real)}')