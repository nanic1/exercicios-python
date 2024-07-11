valorHora = float(input("Valor ganho por hora: R$"))
horasTrabalhadas = int(input("Horas trabalhadas no mes: "))

def salarioBruto(x, y):
    return x * y

inss = salarioBruto(valorHora, horasTrabalhadas) * 0.08
sindicato = salarioBruto(valorHora, horasTrabalhadas) * 0.05
impostoRenda = salarioBruto(valorHora, horasTrabalhadas) * 0.11
salarioLiquido = salarioBruto(valorHora, horasTrabalhadas) - impostoRenda - sindicato - inss

print(f'Salário bruto: {salarioBruto(valorHora, horasTrabalhadas)}\nIR: {impostoRenda}\nSindicato: {sindicato}\nINSS: {inss}\nSalário Líquido: {salarioLiquido}')