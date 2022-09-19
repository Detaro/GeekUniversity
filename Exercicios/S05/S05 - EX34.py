nota = float(input('Insira o valor da nota: '))
falt = int(input('Insira a qtd de faltas: '))

if 9 <= nota <= 10 and falt <= 20:
    print("CONCEITO A!")
elif 9 <= nota <= 10 and falt > 20:
    print("CONCEITO B!")
elif 7.5 <= nota <= 8.9 and falt <= 20:
    print("CONCEITO B!")
elif 7.5 <= nota <= 8.9 and falt > 20:
    print("CONCEITO C!")
elif 5 <= nota <= 7.4 and falt <= 20:
    print("CONCEITO C!")
elif 5 <= nota <= 7.4 and falt > 20:
    print("CONCEITO D!")
elif 4 <= nota <= 4.9 and falt <= 20:
    print("CONCEITO D!")
elif 4 <= nota <= 4.9 and falt > 20:
    print("CONCEITO E!")
elif 0 <= nota <= 3.9:
    print("CONCEITO E!")
