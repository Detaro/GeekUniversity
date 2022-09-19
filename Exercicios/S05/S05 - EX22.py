i = int(input("insira a Idade: "))
a = int(input("insira o tempo de serviço em anos: "))

if i >= 65 or a >= 30 or i >= 60 and a >= 25:
    print('Esta apto a se aposentar')
else:
    print('Não esta apto a se aposentar')
