print('''            CARDAPIO
COD 100 | CACHORRO-QUENTE | VALOR: 1.20 
COD 101 | BAURU SIMPLES   | VALOR: 1.30
COD 102 | BAURU COM OVO   | VALOR: 1.50  
COD 103 | HAMBURGUER      | VALOR: 1.20 
COD 104 | CHEESEBURGER    | VALOR: 1.70 
COD 105 | SUCO            | VALOR: 2.20 
COD 106 | REFRIGERANTE    | VALOR: 1.00
''')

pre = {100: 1.20,
       101: 1.30,
       102: 1.50,
       103: 1.20,
       104: 1.70,
       105: 2.20,
       106: 1.20}

prod = {100: 'Cachorro quente',
        101: 'Bauru Simples',
        102: 'Bauru com Ovo',
        103: 'Hamburguer',
        104: 'Cheeseburguer',
        105: 'Suco',
        106: 'Refrigerante'}

cod = int(input("Digite o código do produto: "))
qtd = int(input(f"Digite a quantidade de {prod[cod]}: "))
vlpg = qtd * pre[cod]
more = input('Gostaria de mais algo(S | N)? ').upper()
if more == 'S':
    cod = int(input("Digite o código do produto:  "))
    qtd = int(input(f"Digite a quantidade de {prod[cod]}: "))
    vlpg = vlpg + (qtd * pre[cod])
    print(f"O valor a ser pago é R${vlpg:.2f}")
else:
    print(f"O valor a ser pago é R${vlpg:.2f}")


