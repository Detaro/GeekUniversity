"""
Faça um programa que receba a altura e o sexo de uma pessoa,
e calcule e mostre seu peso ideal, utilizando as seguintes
fórmulas (onde h corresponde à altura):
- Homens: (72.7 * h) - 58
- Mulheres: (62.1 * h) - 44,7
"""

h = float(input('Digite a altura (m): '))
s = str(input('Digite o sexo (M ou F):'))

if s == 'm' or s == 'M':
    print(f'peso ideal: {72.7*h-58}')
elif s == 'F' or s == 'f':
    print(f'Peso ideal: {62.1*h-44.7}')
else:
    print('sexo não renconhecido')

