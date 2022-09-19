print('AREA DO TRAPÉZIO')
bm = int(input('Insira o valor da base menor: '))
while bm <= 0:
    print('Valor invalido! insira um valor maior que 0: ')
    bm = int(input('Insira o valor da base menor: '))

bM = int(input('Insira o valor da base maior: '))
while bM <= 0:
    print('Valor invalido! insira um valor maior que 0: ')
    bM = int(input('Insira o valor da base maior: '))

h = int(input('Insira o valor da altura:'))
while h < 0:
    print('Valor invalido! A altura não pode ser um valor negativo!: ')
    h = int(input('Insira o valor da altura: '))

a = (bm + bM) * h / 2
print(f'O A area do trapézio equivale a: {a}')
