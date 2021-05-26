n1 = int(input('Um valor: '))
n2 = int(input('Um outro valor: '))
soma = n1 + n2
multi = n1 * n2
div = n1 / n2
divInt = n1 // n2
exp = n1 ** n2
print(f'A soma vale {soma}, o produto é {multi} e a divisão é {div:.2f}', end='__')
print(f'Divisão intira {divInt} e potência {exp}')
