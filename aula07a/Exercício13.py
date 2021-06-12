# Programa que vai ler o salário inicial de um funcionário e calcular o aumento de tantos %

salario = float(input('Informe o salário? R$ '))
p = int(input('Qual a taxa de aumento? '))

ns = salario+(salario * p /100)
aumento = (salario /100 * p)

print(f'Um funcionário que ganha R${salario}, com {p}% de aumento, passa a receber R${ns:.2f}')
print(f'Com aumento de R${aumento:.2f}')
