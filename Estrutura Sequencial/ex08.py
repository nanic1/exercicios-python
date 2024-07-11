valorHora = float(input("Valor ganho por hora: R$"))
horasTrabalhadas = int(input("Horas trabalhadas no mes: "))

def salario (x, y):
    return x * y

print(f'Salario: {salario(valorHora, horasTrabalhadas)}')