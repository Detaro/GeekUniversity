a = int(input('insira o valor de um lado: '))
b = int(input('insira o valor de outro lado: '))
c = int(input('insira o valor do lado restante: '))

if a >= (b + c) or b >= (a + c):
    print('os valores informados formam uma desigualdade triangular!')
elif c >= (a + b):
    print('os valores informados formam uma desigualdade triangular!')
else:
    if a == b and a == c:
        print('Triangulo equilatero')
    elif a == b != c or a == c != b:
        print('Triangulo Isóceles')
    elif b == c != a:
        print('Triangulo Isóceles')
    elif a != b != c:
        print('Triangulo Escaleno')
