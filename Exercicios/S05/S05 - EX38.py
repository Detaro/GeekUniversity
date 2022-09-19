dia = int(input('Insira o dia: '))
mes = int(input('Insira o mes: '))
ano = int(input('Insira o ano: '))

# VAALIDAÇÃO DE ANO BISEXTO
if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
    print(f"{ano} - Ano bisexto")
    bisexto = bool(True)
else:
    print(f'{ano} - Não é um ano bisexto')
    bisexto = bool(False)

if 1 <= dia <= 31 and mes == 1 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 29 and mes == 2 and 1 <= ano <= 2022 and bisexto is True:
    print("Data Valida")
elif 1 <= dia <= 28 and mes == 2 and 1 <= ano <= 2022 and bisexto is False:
    print("Data Valida")
elif 1 <= dia <= 31 and mes == 3 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 30 and mes == 4 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 31 and mes == 5 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 30 and mes == 6 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 31 and mes == 7 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 31 and mes == 8 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 30 and mes == 9 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 31 and mes == 10 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 30 and mes == 11 and 1 <= ano <= 2022:
    print("Data Valida")
elif 1 <= dia <= 31 and mes == 12 and 1 <= ano <= 2022:
    print("Data Valida")
else:
    print("Data Invalida")
