import math

a = float(input("informe o valor de a : "))
b = float(input("informe o valor de b : "))
c = float(input("informe o valor de c : "))

delta = b ** 2 - 4 * a * c
print(delta)
if delta < 0:
    print("Não Existe Raiz")
elif delta == 0:
    raizdelta = (-1 * b + (math.sqrt(delta)) / (2 * a))
    print(delta)
elif delta > 0:
    x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    x2 = (-1 * b - math.sqrt((delta)) / (2 * a))
    print(f"a raizes são {x1},{x2}")