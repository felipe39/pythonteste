# Programa que mede a largura e a altura de uma parede
# e diz quanto de tinta precisa para pintar.

l = float(input('Largura da parade: '))
a = float(input('Altura da parede: '))

area = l * a
litros =  area /2

print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {litros}l de tinta')