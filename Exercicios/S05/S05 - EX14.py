n1 = float(input('Insira o valor da nota do Trabalho de Laboratorio: '))
n2 = float(input('Insira o valor da Avaliação Semestral: '))
n3 = float(input('Insira o valor do Exame Final: '))

TL = n1 * 2
AS = n2 * 3
EF = n3 * 5

media = (TL + AS + EF) / 10

if media >= 5:
    print(f'Aprovado com média {media}')
elif media < 5 and media >= 3:
    print(f'Em recuperação com média {media}')
else:
    print(f'Reprovado com média {media}')
