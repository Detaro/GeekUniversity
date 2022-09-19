v  = float(input('Digite o valor do produto: '))
uf = str(input("Digite o estado (RJ, MG, SP, MS): "))

while uf != 'RJ' and uf != 'MG' and uf != 'SP' and uf != 'MS':
    uf = str(input("Digite o estado dentre as opções (RJ, MG, SP, MS): "))

if uf == 'RJ':
    print(f'Valor total com imposto estadual(15%): R$:{v + (v * 0.15)}')
elif uf == 'MG':
    print(f'Valor total com imposto estadual(7%): R$:{v + (v * 0.07)}')
elif uf == 'SP':
    print(f'Valor total com imposto estadual(12%): R$:{v + (v * 0.12)}')
elif uf == 'MS':
    print(f'Valor total com imposto estadual(8%): R$:{v + (v * 0.08)}')
