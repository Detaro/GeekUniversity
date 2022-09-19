from math import log

n = int(input('Insira um número positivo: '))

if n < 0:
    print('Néumero invalido')
else:
    print(f'log de {n} equivale a {log(n)}')