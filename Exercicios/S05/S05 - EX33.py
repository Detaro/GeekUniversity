pa = float(input('Insira o preço antigo: '))
pn = 0

if pa < 50:
    print(f'PREÇO ATUALIZADO: {pa + pa * 0.05} (BARATO!)')
elif 50 <= pa <= 100:
    pn = pa + pa * 0.1
    if pn < 80:
        print(f'PREÇO ATUALIZADO: {pn} (BARATO!)')
    else:
        print(f'PREÇO ATUALIZADO: {pn} (NORMAL!)')

elif pa > 100:
    pn = pa + pa * 0.15
    if pn <= 120:
        print(f'PREÇO ATUALIZADO: {pn} (NORMAL!)')
    elif 121 < pn <= 200:
        print(f'PREÇO ATUALIZADO: {pn} (CARO!)')
    elif pn > 200:
        print(f'PREÇO ATUALIZADO: {pn} (MUITO CARO!)')
