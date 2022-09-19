num = int(input('Digite um valor: '))


if num % 3 == 0 and num % 5 == 0:
    print(f'valor {num} é divisivel por 3 e por 5')
elif num % 3 == 0:
    print(f'valor {num} é divisivel por 3')
elif num % 5 == 0:
    print(f'valor {num} é divisivel por 3')
elif num % 3 != 0:
    print(f'valor {num} não é divisivel por 3 nem por 5')


