v1 = int(input("insira um valor:"))

if v1 > 0 :
    print(f'A raiz quadrada de {v1} é: {v1 ** (1/2):.1f}')
elif v1 <= 0:
    print('Valor Negativo')
else:
    print("ERRO!")