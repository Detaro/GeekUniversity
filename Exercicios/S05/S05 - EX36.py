venda = float(input('Insira a Venca Mensal: '))

if venda >= 100.000:
    comissao = 700 + venda * 0.16
elif 80.000 >= venda < 100.000:
    comissao = 650 + venda * 0.14
elif 60.000 >= venda < 80.000:
    comissao = 600 + venda * 0.14
elif 40.000 >= venda < 60.000:
    comissao = 550 + venda * 0.14
elif 20.000 >= venda < 40.000:
    comissao = 5000 + venda * 0.14
elif venda < 20.000:
    comissao = 400 + venda * 0.14
else:
    print("ERRO")
print(f'Comissão: {comissao:.2f}')