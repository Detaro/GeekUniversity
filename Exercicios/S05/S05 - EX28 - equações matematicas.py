x = int(input('Digite um valor positivo para x: '))
y = int(input('Digite um valor positivo para y: '))
z = int(input('Digite um valor positivo para z: '))
if x > 0 and y > 0 and z > 0:
    print('''ESCOLHA A FORMA DO CALCULO:
     [1] - GEOMÉTRICA 
     [2] - PONDERADA
     [3] - HARMÔNICA
     [4] - GEOMÉTRICA ''')
    choice = int(input())

    if choice == 1:
        print(f"A média geométrica é: {(x * y * z) ** (1 / 3):.2f} ")
    elif choice == 2:
        print(f"A média ponderada é: {(x + 2 * y + 3 * z) / 6:.2f} ")
    elif choice == 3:
        print(f"A média harmônica é: {1 / ((1 / x) + (1 / y) + (1 / z)):.2f} ")
    elif choice == 4:
        print(f"A média aritmética é: {(x + y + z) / 3}:.2f ")

else:
    print('Um dos números não é positivo')

