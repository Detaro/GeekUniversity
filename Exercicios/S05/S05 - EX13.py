n1 = float(input('Insira o valor da primeira nota: '))
n2 = float(input('Insira o valor da segunda nota: '))
n3 = float(input('Insira o valor da terceira nota: '))
n4 = n3 *2
media = (n1 + n2 + n4) / 4

if media >= 6:
    print(f'Aprovado(a) com média {media}')
else:
    print(f'Reprovado com média {media}')

