porcento = float(input('Digite o número de percento: '))
valor = int(input('Digite o valor a ser descontado: '))

result = (valor /100) * porcento

print(f'\n{porcento:.1f}% de {valor} = {result:.2f}')

