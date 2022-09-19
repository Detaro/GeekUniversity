"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus
algarismos. Por exemplo, o número 251 corresponderá ao valor 8 (2 + 5 + 1). Se o número lido não for maior
do que zero, o programa terminará com a mensagem "Número inválido".
"""


n1 = int(input('Digite um numero maior que 0:'))
n2 = str(n1)
soma = 0

if n1 < 1:
    print('número inválido')
else:
    for carctere in n2:
        soma += int(carctere)
    print(f'A soma dos algarismos de {n1} é {soma}')