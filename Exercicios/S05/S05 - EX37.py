from math import ceil
entrada = str(input('Insira a hora de entrada: ')).split()
saida = str(input('Insira a hora de de saida: ')).split()
ttotal = 0

# converter tempo em horas
if int(entrada[0]) < int(saida[0]):
    tentrada = (int(entrada[0]) * 60 + int(entrada[1]))
    tsaida = (int(saida[0]) * 60 + int(saida[1]))
    ttotal = ceil(int(tsaida - tentrada)/60)
    print(f'TEMPO TOTAL: {ttotal}hs')

# pernoite
elif int(entrada[0]) > int(saida[0]):
    ttotal1 = ((24 - int(entrada[0])) * 60 + int(entrada[1])) + int(saida[0]) * 60 + int(saida[1])
    ttotal = ceil(ttotal1 / 60)
    print(f'TEMPO TOTAL: {ttotal}hs')


if ttotal == 1 or ttotal == 2:
    print(f'Valor Total: {ttotal:.2f}')
elif ttotal == 3 or ttotal == 4:
    print(f'Valor Total: {(ttotal -2) * 1.40 + 2 :.2f}')
elif ttotal >= 5:
    print(f'Valor Total: {(ttotal - 4) * 2 + 4.80 :.2f}')
