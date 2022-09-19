h = float(input('Insira a alura em m: '))
p = float(input('Insira o peso em Kg: '))

if h < 1.20 and p < 60:
    print('CLASSIFICAÇÃO: A')
elif 1.20 <= h < 1.70 and p < 60:
    print('CLASSIFICAÇÃO: B')
elif h > 1.70 and p < 60:
    print('CLASSIFICAÇÃO: C')
elif h < 1.20 and 60 <= p < 90:
    print('CLASSIFICAÇÃO: D')
elif 1.20 <= h < 1.70 and 60 <= p < 90:
    print('CLASSIFICAÇÃO: E')
elif h > 1.70 and 60 <= p < 90:
    print('CLASSIFICAÇÃO: F')
elif h < 1.20 and p > 90:
    print('CLASSIFICAÇÃO: G')
elif 1.20 <= h < 1.70 and p > 90:
    print('CLASSIFICAÇÃO: H')
elif h > 1.70 and p > 90:
    print('CLASSIFICAÇÃO: I')
else:
    print("ERRO!")
