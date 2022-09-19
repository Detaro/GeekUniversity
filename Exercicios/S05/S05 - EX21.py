print('Escolha uma Opção:\n1- Soma de 2 numeros.\n2- Diferença entre 2 numeros.\n3- Produto de 2 numeros.\n4- Divisao de 2 numeros.')
x = int(input())
while x != 1 and x != 2 and x != 3 and x != 4:
    print('Escolha uma Opção:\n1- Soma de 2 numeros.\n2- Diferença entre 2 numeros.\n3- Produto de 2 numeros.\n4- Divisao de 2 numeros.')
    x = int(input())


if x == 1:
    print('Soma de 2 numeros.')
    v1 = float(input('insira um valor: '))
    v2 = float(input('insira um valor: '))
    print(f'Resultado: {v1+v2}')
elif x == 2:
    print('Diferença entre 2 numeros.')
    v1 = float(input('insira um valor: '))
    v2 = float(input('insira um valor: '))
    if v1 > v2:
        print(f'Resultado: {v1 - v2}')
    else:
        print(f'Resultado: {v2 - v1}')
elif x == 3:
    print('Produto de 2 numeros.')
    v1 = float(input('insira um valor: '))
    v2 = float(input('insira um valor: '))
    print(f'Resultado: {v1 * v2}')
elif x == 4:
    print('Divisao de 2 numeros.')
    v1 = float(input('insira o numerador: '))
    v2 = float(input('insira o denominador: '))
    while v2 <= 0:
        print('denominador invalido!')
        v2 = float(input('insira o denominador: '))
        print(f'Resultado: {v1 / v2}')






