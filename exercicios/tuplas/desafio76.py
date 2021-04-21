p = ('PC', 2500, 'TV LED 50pol LG', 3000, 'SOFÁ', 1200, 'CADEIRA', 70, 'GELADEIRA FROST-FREE', 1800, 'FOGÃO BRASTEMP', 1950, 'FREEZER', 950)
print('-='*25)
print('                TABELA DE PREÇOS')
print('-='*25)
for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<30}', end='')
    if pos % 2 != 0:
        print(f'R$  {p[pos]:>3}')