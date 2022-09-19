ano =  int(input('Insira o ano: '))

if ano % 400 == 0 or ano % 4 == 0 and not ano % 100 == 0:
    print(f"{ano} - Ano bisexto")
else:
    print(f'{ano} - Não é um ano bisexto')
