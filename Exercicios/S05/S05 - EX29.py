from random import randint

acertos = 0
a = randint(1, 100)
b = randint(1, 100)
r1 = int(input(f'Qual a soma de {a} + {b}: '))
if r1 == a + b:
    print("Resposta Correta!")
    acertos = acertos + 1
else:
    print("Resposta errada ")

a = randint(1, 100)
b = randint(1, 100)
r2 = int(input(f'Qual a soma de {a} + {b}: '))
if r2 == a + b:
    print("Resposta Correta!")
    acertos = acertos+1
else:
    print("Resposta errada ")

a = randint(1, 100)
b = randint(1, 100)
r3 = int(input(f'Qual a soma de {a} + {b}: '))
if r3 == a + b:
    print("Resposta Correta!")
    acertos = acertos +1
else:
    print("Resposta errada ")

a = randint(1, 100)
b = randint(1, 100)
r4 = int(input(f'Qual a soma de {a} + {b}: '))
if r4 == a + b:
    print("Resposta Correta!")
    acertos = acertos +1
else:
    print("Resposta errada ")

a = randint(1, 100)
b = randint(1, 100)
r5 = int(input(f'Qual a soma de {a} + {b}: '))
if r5 == a + b:
    print("Resposta Correta!")
    acertos = acertos +1
else:
    print("Resposta errada ")

print(f'Quantidade de acertos: {acertos}')