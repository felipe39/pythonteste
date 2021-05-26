preco = float(input('Digite o preço do produto: '))
desconto = int(input('Qual o desconto do produto ? '))

novoPreco = preco-(preco / 100 * desconto)
descont = (preco / 100 * desconto)

print(f'O novo preço do produto é {novoPreco} com desconto de {desconto}% ({descont})')
