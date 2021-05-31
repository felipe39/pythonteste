# Programa que ler um valor em metros e o exibe convertido em centímetro e
# milímetros.

medida = float(input('Uma distância em metros: '))

cm = medida * 100
mm = medida * 1000

print(f'A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')
