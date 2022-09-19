sal = float(input('Insira o salario atual: '))
tempo = float(input('Insira o numero de anos na empresa: '))
reajuste = 0

if sal <= 500 and tempo <= 1:
    reajuste = sal + sal * 0.25
elif sal <= 500 and 1 < tempo <= 3:
    reajuste = (sal + sal * 0.25) + 100
elif sal <= 500 and 4 < tempo <= 6:
    reajuste = (sal + sal * 0.25) + 200
elif sal <= 500 and 7 < tempo <= 10:
    reajuste = (sal + sal * 0.25) + 300
elif sal <= 500 and tempo > 10:
    reajuste = (sal + sal * 0.25) + 500
elif sal <= 1000 and tempo < 1:
    reajuste = sal + sal * 0.20
elif sal <= 1000 and 1 < tempo <= 3:
    reajuste = (sal + sal * 0.20) + 100
elif sal <= 1000 and 4 < tempo <= 6:
    reajuste = (sal + sal * 0.20) + 200
elif sal <= 1000 and 7 < tempo <= 10:
    reajuste = (sal + sal * 0.20) + 300
elif sal <= 1000 and tempo > 10:
    reajuste = (sal + sal * 0.20) + 500
elif sal <= 1500 and tempo > 1:
    reajuste = sal + sal * 0.15
elif sal <= 1500 and 1 < tempo <= 3:
    reajuste = (sal + sal * 0.15) + 100
elif sal <= 1500 and 4 < tempo <= 6:
    reajuste = (sal + sal * 0.15) + 200
elif sal <= 1500 and 7 < tempo <= 10:
    reajuste = (sal + sal * 0.15) + 300
elif sal <= 2000 and tempo < 1:
    reajuste = sal + sal * 0.10
elif sal <= 2000 and 1 < tempo <= 3:
    reajuste = (sal + sal * 0.10) + 100
elif sal <= 2000 and 4 < tempo <= 6:
    reajuste = (sal + sal * 0.10) + 200
elif sal <= 2000 and 7 < tempo <= 10:
    reajuste = (sal + sal * 0.10) + 300
elif sal <= 2000 and  tempo > 10:
    reajuste = (sal + sal * 0.10) + 500
elif sal > 2000 and tempo < 1:
    reajuste = sal
elif sal > 2000 and 1 < tempo <= 3:
    reajuste = sal + 100
elif sal > 2000 and 4 < tempo <= 6:
    reajuste = sal + 200
elif sal > 2000 and 7 < tempo <= 10:
    reajuste = sal + 200
elif sal > 2000 and tempo > 3:
    reajuste = sal + 500
else:
    print('Error')
print(f'O Salario passou a ser: {reajuste}')
