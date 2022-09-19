car = float(input('Inisra o valor do carro: '))

if car <= 12000:
    car = car + car * 0.05
elif 12000 <= car <= 25000:
    car = car + (car * 0.10) + (car * 0.15)
elif car > 25000:
    car = car + (car * 0.15) + (car * 0.20)

print(f'O valor do carro com tributos é: {car:.2f}')
