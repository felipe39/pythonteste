# Programa que ler um número inteiro e exibe sua tabuada

numero = int(input('Digite um número para ver sua tabuada: '))

t1 = numero * 1
t2 = numero * 2
t3 = numero * 3
t4 = numero * 4
t5 = numero * 5
t6 = numero * 6
t7 = numero * 7
t8 = numero * 8
t9 = numero * 9
t10 =numero * 10

print('-' * 11)
print(f'{numero} x {1:2} = {t1}\n{numero} x {2:2} = {t2}\n{numero} x {3:2} = {t3}')
print(f'{numero} x {4:2} = {t4}\n{numero} x {5:2} = {t5}\n{numero} x {6:2} = {t6}')
print(f'{numero} x {7:2} = {t7}\n{numero} x {8:2} = {t8}\n{numero} x {9:2} = {t9}')
print(f'{numero} x {10:2} = {t10}')
print('-' * 11)

