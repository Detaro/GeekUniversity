n1 = float(input('Insira o valor da primeira nota: '))
n2 = float(input('Insira o valor da segunda nota: '))

media = (n1 + n2) / 2

if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    print(f'Média = {media}')
else:
    print("valor das notas invalidos!")
