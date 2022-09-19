# Faça um programa que receba 2 numeros e mostre qual é o maior

v1 = int(input('insira um número:'))
v2 = int(input('insira outro número'))
print(v1, v2)

if v1 > v2:
    print(v1)
elif v1 == v2:
    print('Os números são iguais ')
else:
    print(v2)
