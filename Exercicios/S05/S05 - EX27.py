i = int(input('insira a idade do nadador: '))

if i >= 5 and i <= 7:
    print('CATEGORIA: Infantil A')
elif i >= 8 and i <= 10:
    print('CATEGORIA: Infantil B')
elif i >= 11 and i <= 13:
    print('CATEGORIA: Juvenil A')
elif i >= 14 and i <= 17:
    print('CATEGORIA: Juvenil B')
elif i > 18:
    print('CATEGORIA: Senior')
else:
    print("Fora de Categoria")
