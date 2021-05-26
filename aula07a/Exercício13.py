salario = float(input('Informe o salário.: '))
p = int(input('Qual o porcento de aumento: '))

nS = salario+(salario /100 * p)
aumento = (salario /100 * p)

print(f'Novo salário é {nS} com {p}% ({aumento}) de aumento')
