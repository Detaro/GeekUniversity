print('Calculadora')

# VALIDAÇÃO DO OPERANDO 1

oper1 = float(input('Digite o primeiro Operando: '))
while not oper1 is type(float):
    print('Operando Invalido!')
    oper1 = float(input('Digite o primeiro Operando: '))

# ENTRADA DO OPERADOR

sinal = input('Digite o Operador Matemático: (+, -, *, / ): ')

# VALIDAÇÃO DO OPERADOR
while sinal != '+' and sinal != '-' and sinal != '*' and sinal != '/':
    print('Operador invalido! Digite novamente:')
    print('+, -, *, / ')
    sinal = input()

# VALIDAÇÃO DO OPERANDO 2

oper2 = float(input('Digite o segundo Operando: '))
while oper2 == 0 and sinal == "/":
    print('Tentativa de divisão por zero!')
    oper2 = (float(input('Digite o segundo Operando: ')))

# PROCESSAMENTO

res = 0.0
if sinal == '+':
    res = oper1 + oper2
elif sinal == '-':
    res = oper1 - oper2
elif sinal == '*':
    res = oper1 * oper2
elif sinal == '/':
    res = oper1 / oper2

# Resultado
print(f'Resultado: {res}')
