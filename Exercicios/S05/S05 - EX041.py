peso = float(input('Inisira o peso em Kg: '))
h = float(input('Inisira a altura em m: '))

imc = peso / (h**2)
print(imc)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc <= 25:
    print('Peso ideal')
elif 25.1 < imc <= 30:
    print('Sobrepeso')
elif 30.1 < imc <= 40:
    print('Obesidade')
elif imc > 30.1:
    print('Obesidade Morbida')