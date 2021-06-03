# Algoritmo que ler o preço de um produto e mostra seu
# novo preço, com tanto porcento de desconto e se novo preço.

p = float(input('Qual é o preço do produto? R$'))
porcento = int(input('Qual o desconto do produto? %'))

nP = p-(p / 100 * porcento)
d = (p / 100 * porcento)

print(f'O produto que custava {p}, na promoção com desconto de {porcento}% vai custar R${nP:.2f}')
