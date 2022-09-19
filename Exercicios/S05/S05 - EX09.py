casa = float(input('\033[4;33mInsira o valor da casa: '))
sal = float(input('\033[4;33mInsira o valor do Salario: '))
ano = int(input('\033[4;33mInsira o tempo do financiamneto em anos: '))

x = sal * 0.3
mes = ano * 12
pm = casa / mes

if pm <= x:
    print(f'Valor da Prestação: {pm}')
else:
    print('\033[35mEmprestimo Negado!')