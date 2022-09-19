km = float(input('Insira a quantidade de Km: '))
l = float(input('Insira a quantidade de litros: '))
media = km / l

if media < 8:
    print('Venda o carro!')
elif media >= 8 and media <= 12:
    print('Economico!')
elif media > 12:
    print('Super economico!')